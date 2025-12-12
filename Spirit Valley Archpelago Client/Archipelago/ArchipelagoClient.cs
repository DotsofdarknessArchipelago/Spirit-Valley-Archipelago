using Archipelago.MultiClient.Net;
using Archipelago.MultiClient.Net.BounceFeatures.DeathLink;
using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Helpers;
using Archipelago.MultiClient.Net.MessageLog.Messages;
using Archipelago.MultiClient.Net.Models;
using Archipelago.MultiClient.Net.Packets;
using BepInEx;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using Newtonsoft.Json.Serialization;
using SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Sockets;
using System.Runtime.CompilerServices;
using System.Threading;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace SpiritValleyArchipelagoClient.Archipelago;

public class ArchipelagoClient
{
    public const string APVersion = "0.5.0";
    private const string Game = "Spirit Valley";

    public static bool Authenticated;
    private bool attemptingConnection;

    public static bool slotstate = false;
    public static int totalloc = 0;
    public static int totalitem = 0;

    public static int servermajor = 0;
    public static int serverminor = 5;
    public static int serverbuild = 0;


    public static ArchipelageItemList archlist = new ArchipelageItemList();

    public static ArchipelagoData ServerData = new();
    private DeathLinkHandler DeathLinkHandler;
    public static ArchipelagoSession session;

    /// <summary>
    /// call to connect to an Archipelago session. Connection info should already be set up on ServerData
    /// </summary>
    /// <returns></returns>
    public void Connect()
    {
        if (Authenticated || attemptingConnection) return;

        try
        {
            session = ArchipelagoSessionFactory.CreateSession(ServerData.Uri);
            SetupSession();
        }
        catch (Exception e)
        {
            SpiritValleyArchipelago.BepinLogger.LogError(e);
        }

        TryConnect();
    }

    /// <summary>
    /// add handlers for Archipelago events
    /// </summary>
    private void SetupSession()
    {
        session.MessageLog.OnMessageReceived += message => ArchipelagoConsole.LogMessage(message.ToString());
        session.Items.ItemReceived += OnItemReceived;
        session.Socket.ErrorReceived += OnSessionErrorReceived;
        session.Socket.SocketClosed += OnSessionSocketClosed;
    }

    /// <summary>
    /// attempt to connect to the server with our connection info
    /// </summary>
    private void TryConnect()
    {
        try
        {
            // it's safe to thread this function call but unity notoriously hates threading so do not use excessively
            ThreadPool.QueueUserWorkItem(
                _ => HandleConnectResult(
                    session.TryConnectAndLogin(
                        Game,
                        ServerData.SlotName,
                        ItemsHandlingFlags.AllItems,
                        new Version(APVersion),
                        password: ServerData.Password,
                        requestSlotData: ServerData.NeedSlotData
                    )));
        }
        catch (Exception e)
        {
            SpiritValleyArchipelago.BepinLogger.LogError(e);
            HandleConnectResult(new LoginFailure(e.ToString()));
            attemptingConnection = false;
        }
    }

    /// <summary>
    /// handle the connection result and do things
    /// </summary>
    /// <param name="result"></param>
    private void HandleConnectResult(LoginResult result)
    {
        string outText;
        if (result.Successful)
        {
            var success = (LoginSuccessful)result;

            ServerData.SetupSession(success.SlotData, session.RoomState.Seed);
            Authenticated = true;

            HelperSpirits.genskilllist();

            DeathLinkHandler = new(session.CreateDeathLinkService(), ServerData.SlotName);
            session.Locations.CompleteLocationChecksAsync(ServerData.CheckedLocations.ToArray());
            outText = $"Successfully connected to {ServerData.Uri} as {ServerData.SlotName}!";

            totalitem = Convert.ToInt32(ServerData.slotData["total_items"]);
            totalloc = Convert.ToInt32(ServerData.slotData["total_locations"]);
            slotstate = session.DataStorage[Scope.Slot, "slotsetup"];

            ArchipelagoConsole.LogMessage(outText);

            ServerData.grassdata = JsonConvert.DeserializeObject<Dictionary<string, string[]>>(ArchipelagoClient.ServerData.slotData["Grass_spawn"].ToString());
            ServerData.waterdata = JsonConvert.DeserializeObject<Dictionary<string, string[]>>(ArchipelagoClient.ServerData.slotData["Water_spawn"].ToString());
            ServerData.typedata = JsonConvert.DeserializeObject<Dictionary<string, Dictionary<string, int>>>(ArchipelagoClient.ServerData.slotData["TYPES"].ToString());

            if (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["randomise_map"]) == 1)
            {
                List<List<string>> tempdata = JsonConvert.DeserializeObject<List<List<string>>>(ArchipelagoClient.ServerData.slotData["RANDO"].ToString());
                foreach (var item in tempdata)
                {
                    ServerData.mapdata.Add(item[0], item[1]);
                }
            }

            ServerData.overidetypes();

            if (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Randomise_Move_Data"]) == 1)
            {
                HelperSpirits.modskilllist(ArchipelagoClient.ServerData.slotData["MOVES"].ToString());
            }

            List<string> s2 = JsonConvert.DeserializeObject<List<string>>(ArchipelagoClient.ServerData.slotData["SPIRITS"].ToString());
            foreach (string item in s2)
            {
                ServerData.spiritdata.Add(JsonConvert.DeserializeObject<Spirit>(item));
            }

            ServerData.overidebasestats();

            List<string> t2 = JsonConvert.DeserializeObject<List<string>>(ArchipelagoClient.ServerData.slotData["ENEMIES"].ToString());
            foreach (var item in t2)
            {
                ServerData.trainerdata.Add(JsonConvert.DeserializeObject<Trainer>(item));
            }




            if (File.Exists(Application.persistentDataPath + $"/archipelagoslot{SpiritValleyArchipelago.slot + 1}/archdata.json"))
            {
                using (StreamReader file = File.OpenText(Application.persistentDataPath + $"/archipelagoslot{SpiritValleyArchipelago.slot + 1}/archdata.json"))
                {
                    JsonSerializer serializer = new JsonSerializer();
                    ArchipelageItemList savedlist = (ArchipelageItemList)serializer.Deserialize(file, typeof(ArchipelageItemList));
                    if (session.RoomState.Seed == savedlist.seed)
                    {
                        ArchipelagoConsole.LogDebug("archdata file found restoring session");
                        archlist.merge(savedlist.list);
                    }
                    else
                    {
                        ArchipelagoConsole.LogDebug("ARCHDATA found but an error occoured just going to use new archdata");
                    }
                }
            }
            else
            {
                ArchipelagoConsole.LogDebug("archdata file not found creating new session");
                archlist.seed = session.RoomState.Seed;
                archlist.host = ServerData.Uri;
                archlist.user = ServerData.SlotName;
                archlist.pass = ServerData.Password;
            }


            if (servermajor != Convert.ToInt32(ServerData.slotData["world_version_major"]) || serverminor != Convert.ToInt32(ServerData.slotData["world_version_minor"]) || serverbuild != Convert.ToInt32(ServerData.slotData["world_version_build"]))
            {
                ArchipelagoConsole.LogMessage("WARNING EXPECTED APWORLD VERSION MISSMATCH");
                ArchipelagoConsole.LogError($"EXPECTED V{servermajor}:{serverminor}:{serverbuild} GOT V{ServerData.slotData["world_version_major"]}:{ServerData.slotData["world_version_minor"]}:{ServerData.slotData["world_version_build"]}");
            }

        }
        else
        {
            var failure = (LoginFailure)result;
            outText = $"Failed to connect to {ServerData.Uri} as {ServerData.SlotName}.";
            outText = failure.Errors.Aggregate(outText, (current, error) => current + $"\n    {error}");

            SpiritValleyArchipelago.BepinLogger.LogError(outText);

            Authenticated = false;
            Disconnect();
        }

        attemptingConnection = false;
    }

    /// <summary>
    /// something went wrong, or we need to properly disconnect from the server. cleanup and re null our session
    /// </summary>
    private void Disconnect()
    {
        SpiritValleyArchipelago.BepinLogger.LogDebug("disconnecting from server...");
        session?.Socket.DisconnectAsync();
        session = null;
        Authenticated = false;
    }

    public void SendMessage(string message)
    {
        if (message.StartsWith("$"))
        {
            Codes.processcode(message);
        }
        else
        {
            session.Socket.SendPacketAsync(new SayPacket { Text = message });
        }
    }

    public static void sendloc(int loc)
    {
        ArchipelagoConsole.LogDebug($"SENDING LOCATION ID: {loc}");
        session.Locations.CompleteLocationChecks(loc);
    }

    /// <summary>
    /// we received an item so reward it here
    /// </summary>
    /// <param name="helper">item helper which we can grab our item from</param>
    private void OnItemReceived(ReceivedItemsHelper helper)
    {
        var receivedItem = helper.DequeueItem();

        archlist.add(receivedItem);

        if (helper.Index < ServerData.Index) return;

        ServerData.Index++;
    }

    /// <summary>
    /// something went wrong with our socket connection
    /// </summary>
    /// <param name="e">thrown exception from our socket</param>
    /// <param name="message">message received from the server</param>
    private void OnSessionErrorReceived(Exception e, string message)
    {
        SpiritValleyArchipelago.BepinLogger.LogError(e);
        ArchipelagoConsole.LogMessage(message);
    }

    /// <summary>
    /// something went wrong closing our connection. disconnect and clean up
    /// </summary>
    /// <param name="reason"></param>
    private void OnSessionSocketClosed(string reason)
    {
        SpiritValleyArchipelago.BepinLogger.LogError($"Connection to Archipelago lost: {reason}");
        Disconnect();
    }

    public static void complete()
    {
        var statusUpdatePacket = new StatusUpdatePacket();
        statusUpdatePacket.Status = ArchipelagoClientState.ClientGoal;
        session.Socket.SendPacket(statusUpdatePacket);
    }

    public static void resetlist()
    {
        ArchipelagoConsole.LogMessage("RESETING RECIEVED ITEMS");
        ArchipelageItemList newlist = new ArchipelageItemList();
        newlist.host = archlist.host;
        newlist.user = archlist.user;
        newlist.pass = archlist.pass;
        int i = 0;

        foreach (ItemInfo item in session.Items.AllItemsReceived)
        {
            ArchipelagoConsole.LogMessage($"NAME:{item.ItemName} ID:{item.ItemId} RECIEVED");
            newlist.add(item);
            i++;
        }
        archlist = newlist;
        ArchipelagoConsole.LogMessage("ITEM RESET COMPLETE, RESET " + i.ToString() + " ITEMS");
    }

    
}