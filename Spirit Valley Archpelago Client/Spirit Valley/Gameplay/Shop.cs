using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class Shop
    {

        [HarmonyPatch(typeof(MerchantNPCMapItem), "Start")]
        [HarmonyPatch(typeof(MerchantNPCMapItem), "Interact")]
        [HarmonyPostfix]
        public static void test(MerchantNPCMapItem __instance)
        {
            ArchipelagoConsole.LogDebug("RESETING ITEM LIST");
            List<ItemBundle> inv  = new List<ItemBundle>();
            int start = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["items_archipelago_id_start"]);

            inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_Antidote"), true));

            if (ArchipelagoClient.archlist.hasitem(start + 1)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Crystal_SpiritCrystal"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 2)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Crystal_SpiritCrystal+1"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 3)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Crystal_SpiritCrystal+2"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 4)) 
            { 
                inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Potion_VialOfHealth"), true)); 
                inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Potion_HealingPotion"), true));
                inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Potion_GreaterHealingPotion"), true));
            }
            if (ArchipelagoClient.archlist.hasitem(start + 5)) 
            { 
                inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Potion_VialOfStamina"), true)); 
                inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Potion_StaminaPotion"), true)); 
                inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Potion_GreaterStaminaPotion"), true));
            }
            if (ArchipelagoClient.archlist.hasitem(start + 6)) 
            { 
                inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Potion_VialOfRejuvenation"), true)); 
                inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Potion_RejuvenationPotion"), true)); 
                inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Potion_GreaterRejuvenationPotion"), true));
            }
            if (ArchipelagoClient.archlist.hasitem(start + 7)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_SeedOfLife"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 8)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_GoldenSeedOfLife"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 9)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_Donut"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 10)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_Cupcake"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 11)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_Lollipop"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 12)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_CandyCane"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 13)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_StrawberryCake"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 14)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_ChocolateCake"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 15)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_GoldFish"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 16)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_ChocolateStarfish"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 17)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_ArcticCod"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 18)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_NorthernBlowfish"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 19)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_SeaCucumber"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 20)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_ElusiveScent"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 21)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_PotentScent"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 22)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_SpiritRepellent"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 23)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_XPBoosters"), true)); }
            if (ArchipelagoClient.archlist.hasitem(start + 24)) { inv.Add(HelperItems.genbundle(ItemManager.instance.GetItemAssetByName("Consumable_CleansingTonic"), true)); }

            __instance.inventory = inv.ToArray();

            __instance.state.inventoryItemStates.Clear();
            foreach (ItemBundle itemBundle in __instance.inventory)
            {
                InventoryItemState inventoryItemState = new InventoryItemState(itemBundle.item);
                inventoryItemState.count = itemBundle.Count;
                inventoryItemState.isCountInfinite = itemBundle.isCountInfinite;
                __instance.state.inventoryItemStates.Add(inventoryItemState);
            }
        }



    }
}
