using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System;
using UnityEngine.SceneManagement;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class MapRando
    {
        [HarmonyPatch(typeof(MapManager), "Start")]
        [HarmonyPrefix]
        public static void maprando1(MapManager __instance)
        {
            if (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["randomise_map"]) == 0) { return; }

            string mapid = SceneManager.GetActiveScene().name;

            //ArchipelagoConsole.LogMessage($"MAPID: {mapid}");
            foreach (TransitionArea a in __instance.transitionObjects.GetComponentsInChildren<TransitionArea>())
            {
                string newdata = "";
                if (ArchipelagoClient.ServerData.mapdata.TryGetValue($"{mapid} {a.id}", out newdata))
                {
                    //ArchipelagoConsole.LogMessage($"OLD TRANSITIONAREA: ID={a.id}, NEXTAREA={a.nextSceneName}, NEXTID={a.nextTransitionAreaID}");
                    a.nextSceneName = newdata.Split(' ')[0];
                    a.nextTransitionAreaID = newdata.Split(' ')[1];
                    //ArchipelagoConsole.LogMessage($"NEW TRANSITIONAREA: ID={a.id}, NEXTAREA={a.nextSceneName}, NEXTID={a.nextTransitionAreaID}");
                }
                else
                {
                    if (mapid == "EvergreenOutpost" && a.id == "Right")
                    {
                        newdata = ArchipelagoClient.ServerData.mapdata[$"EvergreenOutpost_East Right"];
                        //ArchipelagoConsole.LogMessage($"OLD TRANSITIONAREA: ID={a.id}, NEXTAREA={a.nextSceneName}, NEXTID={a.nextTransitionAreaID}");
                        a.nextSceneName = newdata.Split(' ')[0];
                        a.nextTransitionAreaID = newdata.Split(' ')[1];
                        //ArchipelagoConsole.LogMessage($"NEW TRANSITIONAREA: ID={a.id}, NEXTAREA={a.nextSceneName}, NEXTID={a.nextTransitionAreaID}");
                    }
                    else if (mapid == "Trail16" && a.id == "Cave")
                    {
                        newdata = ArchipelagoClient.ServerData.mapdata[$"Trail16_Top Cave"];
                        //ArchipelagoConsole.LogMessage($"OLD TRANSITIONAREA: ID={a.id}, NEXTAREA={a.nextSceneName}, NEXTID={a.nextTransitionAreaID}");
                        a.nextSceneName = newdata.Split(' ')[0];
                        a.nextTransitionAreaID = newdata.Split(' ')[1];
                        //ArchipelagoConsole.LogMessage($"NEW TRANSITIONAREA: ID={a.id}, NEXTAREA={a.nextSceneName}, NEXTID={a.nextTransitionAreaID}");
                    }
                    else if (mapid == "Trail20" && a.id == "Right")
                    {
                        newdata = ArchipelagoClient.ServerData.mapdata[$"Trail20_Right Right"];
                        //ArchipelagoConsole.LogMessage($"OLD TRANSITIONAREA: ID={a.id}, NEXTAREA={a.nextSceneName}, NEXTID={a.nextTransitionAreaID}");
                        a.nextSceneName = newdata.Split(' ')[0];
                        a.nextTransitionAreaID = newdata.Split(' ')[1];
                        //ArchipelagoConsole.LogMessage($"NEW TRANSITIONAREA: ID={a.id}, NEXTAREA={a.nextSceneName}, NEXTID={a.nextTransitionAreaID}");
                    }
                    else
                    {
                        ArchipelagoConsole.LogDebug($"{mapid} {a.id}: NOT IN DICT");
                    }
                }
            }
        }
    }
}
