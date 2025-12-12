using Archipelago.MultiClient.Net.Enums;
using HarmonyLib;
using Newtonsoft.Json;
using SpiritValleyArchipelagoClient.Archipelago;
using System.IO;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class Save
    {

        [HarmonyPatch(typeof(SystemData<GameState>), "SaveAsync")]
        [HarmonyPrefix]
        public static void savedata(SystemData<GameState> __instance, SaveType type, ref string ___manualSavePath)
        {
            if (GameManager.instance.GetActiveGameState() == null) { return; }
            if (__instance.ToString() != "SystemData`1[GameState]") { return; }

            ArchipelagoConsole.LogDebug("SAVING GAME");
            if (type == SaveType.Manual) { ArchipelagoConsole.LogDebug("MANUAL SAVE"); } else { ArchipelagoConsole.LogDebug("AUTO SAVE"); }

            bool goal = __instance.data.GetActiveMainQuestState().id == "main_quest_55_life_as_a_spirit_warden";
            if (!goal)
            {
                ArchipelagoConsole.LogDebug("GOAL NOT ACHIEVED YET");

                if (ArchipelagoClient.archlist.host != ArchipelagoClient.ServerData.Uri) { ArchipelagoClient.archlist.host = ArchipelagoClient.ServerData.Uri; }
                if (ArchipelagoClient.archlist.user != ArchipelagoClient.ServerData.SlotName) { ArchipelagoClient.archlist.user = ArchipelagoClient.ServerData.SlotName; }
                if (ArchipelagoClient.archlist.pass != ArchipelagoClient.ServerData.Password) { ArchipelagoClient.archlist.pass = ArchipelagoClient.ServerData.Password; }

                using (StreamWriter archfile = File.CreateText(___manualSavePath.Substring(0, ___manualSavePath.Length - 22) + "/archdata.json"))
                {
                    JsonSerializer serializer = new JsonSerializer();
                    serializer.Serialize(archfile, ArchipelagoClient.archlist);
                }
            }
            else if (File.Exists(___manualSavePath.Substring(0, ___manualSavePath.Length - 22) + "/archdata.json")) 
            {
                ArchipelagoConsole.LogMessage("Goal Achieved setting save file for deletion upon restart");
                File.Delete(___manualSavePath.Substring(0, ___manualSavePath.Length - 22) + "/archdata.json"); 
            }


            bool setup = ArchipelagoClient.session.DataStorage[Scope.Slot, "slotsetup"];
            if (!setup) { ArchipelagoClient.session.DataStorage[Scope.Slot, "slotsetup"] = true; }
        }
    }
}
