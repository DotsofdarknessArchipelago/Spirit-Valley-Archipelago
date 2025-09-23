using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Models;
using HarmonyLib;
using Newtonsoft.Json;
using SpiritValleyArchipelagoClient.Archipelago;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;
using static System.Collections.Specialized.BitVector32;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class Save
    {
        public static bool wait = false;

        [HarmonyPatch(typeof(SystemData<GameState>), "SaveAsync")]
        [HarmonyPrefix]
        public static void savedata(SystemData<GameState> __instance, SaveType type)
        {
            if (GameManager.instance.GetActiveGameState() == null) { return; }
            ArchipelagoConsole.LogDebug("SAVING GAME");
            if (type == SaveType.Manual) { ArchipelagoConsole.LogDebug("MANUAL SAVE"); } else { ArchipelagoConsole.LogDebug("AUTO SAVE"); }


            //string text = Crypt.Encrypt(JsonConvert.SerializeObject(__instance.data));
            //ArchipelagoConsole.LogDebug($"SAVING GAME");
            //ArchipelagoClient.session.DataStorage[Scope.Slot, "save"] = text;
            //ArchipelagoClient.session.DataStorage[Scope.Slot, "save"] = text + Callback.Add((oldValue, newValue, x) => { ArchipelagoConsole.LogDebug("TEST???"); }); 
            //ArchipelagoConsole.LogDebug("hello");

            if (ArchipelagoClient.archlist.seed != ArchipelagoClient.session.RoomState.Seed) { ArchipelagoClient.archlist.seed = ArchipelagoClient.session.RoomState.Seed; }
            string text2 = JsonConvert.SerializeObject(ArchipelagoClient.archlist);
            ArchipelagoConsole.LogDebug($"ARCHDATA: {text2}");
            ArchipelagoClient.session.DataStorage[Scope.Slot, "archdata"] = JsonConvert.SerializeObject(ArchipelagoClient.archlist);

            bool setup = ArchipelagoClient.session.DataStorage[Scope.Slot, "slotsetup"];
            if (!setup) { ArchipelagoClient.session.DataStorage[Scope.Slot, "slotsetup"] = true; }
        }


        [HarmonyPatch(typeof(SystemData<GameState>), "SaveAsync")]
        [HarmonyPostfix]
        public static void savedatacheck(SaveType type, Task<bool> __result)
        {
            if (GameManager.instance.GetActiveGameState() == null) { return; }
            //if (!__result.Result) { ArchipelagoConsole.LogDebug("ERROR SAVING FILE"); return; }
            //if (type == SaveType.Manual)
            //{
            //    ArchipelagoClient.session.DataStorage[Scope.Slot, "save"] = File.ReadAllText(Application.persistentDataPath + "/archipelago/archipelago.json");
            //    ArchipelagoConsole.LogDebug("GAME SAVE COMPLETE");
            //    //ArchipelagoClient.session.DataStorage[Scope.Slot, "save"] = File.ReadAllText(Application.persistentDataPath + "/archipelago/archipelago.json") + Callback.Add((x, y, z) => { ArchipelagoConsole.LogDebug("GAME SAVE COMPLETE"); });
            //}
            //else
            //{
            //    ArchipelagoClient.session.DataStorage[Scope.Slot, "save"] = File.ReadAllText(Application.persistentDataPath + "/archipelago/archipelago_auto.json");
            //    ArchipelagoConsole.LogDebug("GAME SAVE COMPLETE");
            //    //ArchipelagoClient.session.DataStorage[Scope.Slot, "save"] = File.ReadAllText(Application.persistentDataPath + "/archipelago/archipelago_auto.json") + Callback.Add((x, y, z) => { ArchipelagoConsole.LogDebug("GAME SAVE COMPLETE"); });
            //}
        }
    }
}
