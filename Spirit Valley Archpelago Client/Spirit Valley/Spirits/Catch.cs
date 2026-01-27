using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;
using System.Linq;
using UnityEngine.Localization;
using UnityEngine.Localization.Settings;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Spirits
{
    [HarmonyPatch]
    public class Catch
    {
        [HarmonyPatch(typeof(GameEventManager), "OnMonsterCaptured")]
        [HarmonyPrefix]
        public static void moncaught(MonsterState monsterState)
        {
            if (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Single_Catch"]) == 1 && HelperItems.save.currentSceneName != "OakwoodVillage_Clinic")
            {
                ArchipelagoClient.archlist.caughtmaps.Add(HelperItems.save.currentSceneName);
            }

            int startid = 0;
            int rarestartid = 0;
            if (monsterState.isRare)
            {
                rarestartid = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Spirit_Rare_Start"]);
            }
            startid = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Spirit_Id_Start"]);
            
            for (int i = 0; i < GameDataManager.instance.databaseEntries.Length; i++)
            {
                if (GameDataManager.instance.databaseEntries[i].name == monsterState.baseStatsName)
                {
                    if (rarestartid != 0){ArchipelagoClient.sendloc(rarestartid + i + 1);}
                    ArchipelagoClient.sendloc(startid + i + 1);
                    return;
                }
            }
        }


        [HarmonyPatch(typeof(ItemManager), "GetGuaranteedCatchBelowLevelForCatchPotency")]
        [HarmonyPrefix]
        public static bool guarenteedcatch(ref int __result)
        {
            if (Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Catch_Cheat"]))
            {
                __result = 200;
                return false;
            }
            return true;
        }



        public static LocalizedString limitcapture;

        [HarmonyPatch(typeof(CrystalsTab), "OnItemClicked")]
        [HarmonyPrefix]
        public static bool guarenteedcatch(CrystalsTab __instance)
        {
            if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Single_Catch"])) { return true; }

            if (limitcapture == null)
            {
                var t = LocalizationSettings.Instance.GetStringDatabase().GetTable(__instance.itemsNotUsableMessage.TableReference).AddEntry("limitcapture", "You have already captured a spirit from this location");
                limitcapture = new LocalizedString(__instance.itemsNotUsableMessage.TableReference, "limitcapture");
            }

            if (HelperItems.save.isFightOn && HelperItems.save.isWildEncounter && ArchipelagoClient.archlist.caughtmaps.Contains(HelperItems.save.currentSceneName))
            {
                GlobalHUD.instance.EnqueueToast(limitcapture);
                return false;
            }
            return true;
        }

    }
}
