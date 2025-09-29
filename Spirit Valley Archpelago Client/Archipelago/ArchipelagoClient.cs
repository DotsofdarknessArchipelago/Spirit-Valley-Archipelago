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
using System.Linq;
using System.Runtime.CompilerServices;
using System.Threading;
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
            Plugin.BepinLogger.LogError(e);
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
            Plugin.BepinLogger.LogError(e);
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


            List<string> s2 = JsonConvert.DeserializeObject<List<string>>(ArchipelagoClient.ServerData.slotData["SPIRITS"].ToString());
            foreach (string item in s2)
            {
                ServerData.spiritdata.Add(JsonConvert.DeserializeObject<Spirit>(item));
            }

            List<string> t2 = JsonConvert.DeserializeObject<List<string>>(ArchipelagoClient.ServerData.slotData["ENEMIES"].ToString());
            foreach (var item in t2)
            {
                ServerData.trainerdata.Add(JsonConvert.DeserializeObject<Trainer>(item));
            }

            string alists = session.DataStorage[Scope.Slot, "archdata"];
            ArchipelageItemList alist2 = JsonConvert.DeserializeObject<ArchipelageItemList>(alists);
            Plugin.test = alist2;
            Plugin.BepinLogger.LogMessage("SERVER ARCHDATA:");
            Plugin.BepinLogger.LogMessage(alists);
            if (!alist2.seed.IsNullOrWhiteSpace())
            {
                ArchipelagoConsole.LogDebug("ARCHDATA FOUND ON SERVER");
                archlist = alist2;
                archlist.seed = session.RoomState.Seed;
            }
            else
            {
                archlist.seed = session.RoomState.Seed;
                ArchipelagoConsole.LogDebug("ARCHDATA NOT FOUND CREATING NEW");
            }

        }
        else
        {
            var failure = (LoginFailure)result;
            outText = $"Failed to connect to {ServerData.Uri} as {ServerData.SlotName}.";
            outText = failure.Errors.Aggregate(outText, (current, error) => current + $"\n    {error}");

            Plugin.BepinLogger.LogError(outText);

            Authenticated = false;
            Disconnect();
        }

        ArchipelagoConsole.LogMessage(outText);
        attemptingConnection = false;
    }

    /// <summary>
    /// something went wrong, or we need to properly disconnect from the server. cleanup and re null our session
    /// </summary>
    private void Disconnect()
    {
        Plugin.BepinLogger.LogDebug("disconnecting from server...");
        session?.Socket.DisconnectAsync();
        session = null;
        Authenticated = false;
    }

    public void SendMessage(string message)
    {
        if (message.StartsWith("$"))
        {
            processcode(message);
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
        Plugin.BepinLogger.LogError(e);
        ArchipelagoConsole.LogMessage(message);
    }

    /// <summary>
    /// something went wrong closing our connection. disconnect and clean up
    /// </summary>
    /// <param name="reason"></param>
    private void OnSessionSocketClosed(string reason)
    {
        Plugin.BepinLogger.LogError($"Connection to Archipelago lost: {reason}");
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

    public static void processcode(string code)
    {
        switch (code)
        {
            case "$resetitems":
                ArchipelagoConsole.LogMessage("RESETING SENT ITEM LIST ALL ITEMS WILL BE REPROCESSED");
                session.DataStorage[Scope.Slot, "archdata"] = "";
                resetlist();
                break;

            case "$deletesave":
                ArchipelagoConsole.LogMessage("resetting save/archdata");
                session.DataStorage[Scope.Slot, "save"] = "";
                session.DataStorage[Scope.Slot, "archdata"] = "";
                session.DataStorage[Scope.Slot, "slotsetup"] = false;
                resetlist();
                break;
            case "$debugsave":
                //string playerfile = Crypt.Decrypt(ArchipelagoClient.session.DataStorage[Scope.Slot, "save"]);
                //
                //ArchipelagoConsole.LogMessage($"------------PLAYER FILE START -----------");
                //ArchipelagoConsole.LogMessage($"{playerfile}");
                //ArchipelagoConsole.LogMessage($"------------PLAYER FILE END -----------");
                break;
            case "$debugarchdata":
                string adata = ArchipelagoClient.session.DataStorage[Scope.Slot, "archdata"];

                ArchipelagoConsole.LogMessage($"------------ARCHDATA START -----------");
                ArchipelagoConsole.LogMessage($"{adata}");
                ArchipelagoConsole.LogMessage($"------------ARCHDATA END -----------");
                break;


            case "$warp":
                if (HelperItems.save.currentSceneName != "OakwoodVillage")
                {
                    HelperItems.save.transitionSceneName = "OakwoodVillage";
                    HelperItems.save.transitionAreaID = "waystone";
                    SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                    {
                        SceneManager.LoadScene("OakwoodVillage", LoadSceneMode.Single);
                    });
                }
                break;
            case "$warpall":
                HelperItems.save.GetWayStoneState("OakwoodVillage").isActive = true;
                HelperItems.save.GetWayStoneState("Greensvale").isActive = true;
                HelperItems.save.GetWayStoneState("Trail4").isActive = true;
                HelperItems.save.GetWayStoneState("DairyFarm").isActive = true;
                HelperItems.save.GetWayStoneState("TumbleweedTown").isActive = true;
                HelperItems.save.GetWayStoneState("CrashSite").isActive = true;
                HelperItems.save.GetWayStoneState("CoconutVillage").isActive = true;
                HelperItems.save.GetWayStoneState("Trail14").isActive = true;
                HelperItems.save.GetWayStoneState("ColdHarbor").isActive = true;
                HelperItems.save.GetWayStoneState("Frostville1").isActive = true;
                HelperItems.save.GetWayStoneState("AbandonedMine").isActive = true;
                HelperItems.save.GetWayStoneState("Trail18").isActive = true;
                HelperItems.save.GetWayStoneState("Trail19").isActive = true;
                HelperItems.save.GetWayStoneState("Trail22").isActive = true;
                HelperItems.save.isFastTravelUnlocked = true;
                break;
            case "$debugdump":
                ArchipelagoConsole.LogMessage($"TOTAL DOMINATION QUEST SPIRIT: {ServerData.slotData["MAIN_QUEST_TOTAL_DOMINATION"]}");
                ArchipelagoConsole.LogMessage($"PERKY PETUNIA QUEST SPIRIT: {ServerData.slotData["SIDE_QUEST_PERKY_PETUNIA_SPIRIT"]}");
                ArchipelagoConsole.LogMessage($"SLITHERING MENANCE QUEST SPIRIT: {ServerData.slotData["SIDE_QUEST_SLITHERING_MENACE_SPIRIT"]}");
                ArchipelagoConsole.LogMessage($"DEADLY WATERS QUEST SPIRIT: {ServerData.slotData["SIDE_QUEST_DEADLY_WATERS_SPIRIT"]}");
                ArchipelagoConsole.LogMessage($"STARRY EYED SURPRISE QUEST SPIRIT: {ServerData.slotData["SIDE_QUEST_STARRY_EYED_SURPRISE_SPIRIT"]}");
                ArchipelagoConsole.LogMessage($"ARCTIC MENACE QUEST SPIRIT: {ServerData.slotData["SIDE_QUEST_ARCTIC_MENACE_SPIRIT"]}");
                ArchipelagoConsole.LogMessage($"CENTIBOOB QUEST 1 SPIRIT: {ServerData.slotData["SIDE_QUEST_CENTIBOOB_1_SPIRIT"]}");
                ArchipelagoConsole.LogMessage($"CENTIBOOB QUEST 2 SPIRIT: {ServerData.slotData["SIDE_QUEST_CENTIBOOB_2_SPIRIT"]}");
                ArchipelagoConsole.LogMessage($"CENTIBOOB QUEST 3 SPIRIT: {ServerData.slotData["SIDE_QUEST_CENTIBOOB_3_SPIRIT"]}");
                break;
            case "$debugslotdata":
                ArchipelagoConsole.LogMessage("OUTPUTING SLOT DATA TO LOG FILE");
                ArchipelagoConsole.LogDebug("SLOTDATA GRASS:");
                ArchipelagoConsole.LogDebug(ArchipelagoClient.ServerData.slotData["Grass_spawn"].ToString());
                ArchipelagoConsole.LogDebug("SLOTDATA WATER:");
                ArchipelagoConsole.LogDebug(ArchipelagoClient.ServerData.slotData["Water_spawn"].ToString());
                ArchipelagoConsole.LogDebug("SLOTDATA SPIRITS:");
                ArchipelagoConsole.LogDebug(ArchipelagoClient.ServerData.slotData["SPIRITS"].ToString());
                ArchipelagoConsole.LogDebug("SLOTDATA TYPECHART:");
                ArchipelagoConsole.LogDebug(ArchipelagoClient.ServerData.slotData["TYPES"].ToString());
                ArchipelagoConsole.LogDebug("SLOTDATA TRAINERS:");
                ArchipelagoConsole.LogDebug(ArchipelagoClient.ServerData.slotData["ENEMIES"].ToString());
                ArchipelagoConsole.LogMessage("SLOT DATA OUTPUT COMPLETE");
                break;
            case "$fixsave"://might work?
                save.fixsave();
                break;



            //CHEATS
            case "$cheat.reset":
                ArchipelagoConsole.LogMessage("resetting save flag");
                session.DataStorage[Scope.Slot, "slotsetup"] = false;
                break;
            case "$cheat.quest":
                ArchipelagoConsole.LogMessage("advanceing main quest");
                Plugin.ArchipelagoClient.SendMessage($"Activated quest dev cheat to advance main quest");
                string quest = QuestManager.instance.mainQuest[QuestManager.instance.GetIndexForMainQuestByID(HelperItems.save.GetActiveMainQuestState().id) + 1].id;
                HelperItems.save.AdvanceMainQuest(quest);
                break;
            case "$cheat.crystals":
                ArchipelagoConsole.LogMessage("Adding 10 Spirit Crystal+2 to Inventory");
                Plugin.ArchipelagoClient.SendMessage($"Activated crystal dev cheat for extra spirit crystals");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Crystal_SpiritCrystal+2"), 10, true);
                break;
            case "$cheat.potion":
                ArchipelagoConsole.LogMessage("Adding 10 Greater Rejuvenation Potion and Golden Seed of Life to Inventory");
                Plugin.ArchipelagoClient.SendMessage($"Activated potion dev cheat for extra potions/revives");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Potion_GreaterRejuvenationPotion"), 10, true);
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_CleansingTonic"), 10, true);
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_GoldenSeedOfLife"), 10, true);
                break;
            case "$cheat.sex":
                ArchipelagoConsole.LogMessage("Adding 10 ChocolateCake to Inventory");
                Plugin.ArchipelagoClient.SendMessage($"Activated affection dev cheat giving extra affection items");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_ChocolateCake"), 10, true);
                break;
            case "$cheat.warp":
                Plugin.ArchipelagoClient.SendMessage($"Activated warp dev cheat unlocking all warp locations");
                ArchipelagoConsole.LogMessage("MAKING ALL WARPS ACCESSIABLE");
                HelperItems.save.isFastTravelUnlocked = true;
                HelperItems.save.GetWayStoneState("OakwoodVillage").isActive = true;
                HelperItems.save.GetWayStoneState("Greensvale").isActive = true;
                HelperItems.save.GetWayStoneState("Trail4").isActive = true;
                HelperItems.save.GetWayStoneState("DairyFarm").isActive = true;
                HelperItems.save.GetWayStoneState("TumbleweedTown").isActive = true;
                HelperItems.save.GetWayStoneState("CrashSite").isActive = true;
                HelperItems.save.GetWayStoneState("CoconutVillage").isActive = true;
                HelperItems.save.GetWayStoneState("Trail14").isActive = true;
                HelperItems.save.GetWayStoneState("ColdHarbor").isActive = true;
                HelperItems.save.GetWayStoneState("Frostville1").isActive = true;
                HelperItems.save.GetWayStoneState("AbandonedMine").isActive = true;
                HelperItems.save.GetWayStoneState("Trail18").isActive = true;
                HelperItems.save.GetWayStoneState("Trail19").isActive = true;
                HelperItems.save.GetWayStoneState("Trail22").isActive = true;
                break;
            case "$cheat.1"://Ancient Temple Key
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Ancient Temple Key");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_AncientTempleKey"), 1, true);
                ArchipelagoConsole.LogMessage("Added Ancient Temple Key to Inventory");
                break;
            case "$cheat.2"://Cock Shaped Key
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Cock Shaped Key");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_CockShapedKey"), 1, true);
                ArchipelagoConsole.LogMessage("Added Cock Shaped Key to Inventory");
                break;
            case "$cheat.3"://Cracked Power Crystal
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Cracked Power Crystal");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_CrackedPowerCrystal"), 1, true);
                ArchipelagoConsole.LogMessage("Added Cracked Power Crystal to Inventory");
                break;
            case "$cheat.4"://Dynamite
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Dynamite");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_Dynamite"), 1, true);
                ArchipelagoConsole.LogMessage("Added Dynamite to Inventory");
                break;
            case "$cheat.5"://Fancy Suit
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Fancy Suit");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_FancySuit"), 1, true);
                ArchipelagoConsole.LogMessage("Added Fancy Suit to Inventory");
                break;
            case "$cheat.6"://Fishing Rod
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Fishing Rod");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_FishingRod"), 1, true);
                ArchipelagoConsole.LogMessage("Added Fishing Rod to Inventory");
                break;
            case "$cheat.7"://Power Crystal
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Power Crystal");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_PowerCrystal"), 1, true);
                ArchipelagoConsole.LogMessage("Added Power Crystal to Inventory");
                break;
            case "$cheat.8"://Raw Crystal Chunk
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Raw Crystal Chunk");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_RawCrystalChunk"), 1, true);
                ArchipelagoConsole.LogMessage("Added Raw Crystal Chunk to Inventory");
                break;
            case "$cheat.9"://Red Harmony Crystal
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Red Harmony Crystal");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_RedHarmonyCrystal"), 1, true);
                ArchipelagoConsole.LogMessage("Added Red Harmony Crystal to Inventory");
                break;
            case "$cheat.10"://Spirit Handler License
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Spirit Handler License");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_SpiritHandlerLicense"), 1, true);
                ArchipelagoConsole.LogMessage("Added Spirit Handler License to Inventory");
                break;
            case "$cheat.11"://Stone Key
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Stone Key");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_StoneKey"), 1, true);
                ArchipelagoConsole.LogMessage("Added Stone Key to Inventory");
                break;
            case "$cheat.12"://Super Secret Orders
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Super Secret Orders");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_SuperSecretOrders"), 1, true);
                ArchipelagoConsole.LogMessage("Added Super Secret Orders to Inventory");
                break;
            case "$cheat.13"://Testosterone Pills
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Testosterone Pills");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_TestosteronePills"), 1, true);
                ArchipelagoConsole.LogMessage("Added Testosterone Pills to Inventory");
                break;
            case "$cheat.14"://Video Cassette
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Video Cassette");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_VideoCasette"), 1, true);
                ArchipelagoConsole.LogMessage("Added Video Cassette to Inventory");
                break;
            case "$cheat.15"://Wedding Ring
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Wedding Ring");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_WeddingRing"), 1, true);
                ArchipelagoConsole.LogMessage("Added Wedding Ring to Inventory");
                break;
            case "$cheat.16"://Yellow Harmony Crystal
                Plugin.ArchipelagoClient.SendMessage($"Activated keyitem dev cheat giving keyitem: Yellow Harmony Crystal");
                HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("KeyItem_YellowHarmonyCrystal"), 1, true);
                ArchipelagoConsole.LogMessage("Added Yellow Harmony Crystal to Inventory");
                break;


            default:
                if (code.StartsWith("$cheat."))
                {
                    ArchipelagoConsole.LogMessage("UNKNOWN CLIENT CHEAT COMMAND: " + code);
                }
                else
                {
                    ArchipelagoConsole.LogMessage("UNKNOWN CLIENT COMMAND: " + code);
                }
                    break;
        }
    }

}