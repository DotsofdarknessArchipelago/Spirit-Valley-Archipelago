using Archipelago.MultiClient.Net.Enums;
using Archipelago.MultiClient.Net.Models;
using Archipelago.MultiClient.Net.Packets;
using Newtonsoft.Json;
using SpiritValleyArchipelagoClient.Archipelago;
using System;
using System.IO;
using UnityEngine;
using UnityEngine.SceneManagement;
using static System.Collections.Specialized.BitVector32;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Util
{
    public class Codes
    {
        public static void processcode(string code)
        {
            ArchipelagoConsole.LogDebug($"processing code {code}");
            if (code.StartsWith("$warp"))
            {
                processwarp(code);
                return;
            }

            switch (code)
            {
                case "$resetitems":
                    ArchipelagoConsole.LogMessage("RESETING SENT ITEM LIST ALL ITEMS WILL BE REPROCESSED");
                    ArchipelagoClient.resetlist();
                    break;


                case "$resync":
                    ArchipelagoConsole.LogMessage("Resyncing Client");
                    ArchipelagoClient.session.Socket.SendPacket(new SyncPacket());
                    break;
                case "$resync.items":
                    ArchipelagoConsole.LogMessage("Resyncing Items Recieved");
                    foreach (ItemInfo item in ArchipelagoClient.session.Items.AllItemsReceived)
                    {
                        ArchipelagoConsole.LogMessage($"RESYNCING ITEM ({item.ItemDisplayName}) FROM ({item.Player.Name} : {item.LocationDisplayName})");
                        ArchipelagoClient.archlist.add(item);
                    }
                    ArchipelagoConsole.LogMessage("Resyncing Items Recieved DONE");
                    break;


                case "$deletesave":
                    ArchipelagoConsole.LogMessage("resetting save/archdata");
                    ArchipelagoClient.session.DataStorage[Scope.Slot, "slotsetup"] = false;
                    ArchipelagoClient.resetlist();
                    break;


                case "$debugarchdata":
                    ArchipelageItemList alist;
                    using (StreamReader file = File.OpenText(Application.persistentDataPath + $"/archipelagoslot{SpiritValleyArchipelago.slot + 1}/archdata.json"))
                    {
                        JsonSerializer serializer = new JsonSerializer();
                        alist = (ArchipelageItemList)serializer.Deserialize(file, typeof(ArchipelageItemList));
                    }

                    if (alist == null) { return; }

                    ArchipelagoConsole.LogMessage($"------------ARCHDATA START -----------");
                    ArchipelagoConsole.LogMessage(alist.listprint());
                    ArchipelagoConsole.LogMessage($"------------ARCHDATA END -----------");
                    break;
                case "$debugdump":
                    ArchipelagoConsole.LogMessage($"TOTAL DOMINATION QUEST SPIRIT: {ArchipelagoClient.ServerData.slotData["MAIN_QUEST_TOTAL_DOMINATION"]}");
                    ArchipelagoConsole.LogMessage($"PERKY PETUNIA QUEST SPIRIT: {ArchipelagoClient.ServerData.slotData["SIDE_QUEST_PERKY_PETUNIA_SPIRIT"]}");
                    ArchipelagoConsole.LogMessage($"SLITHERING MENANCE QUEST SPIRIT: {ArchipelagoClient.ServerData.slotData["SIDE_QUEST_SLITHERING_MENACE_SPIRIT"]}");
                    ArchipelagoConsole.LogMessage($"DEADLY WATERS QUEST SPIRIT: {ArchipelagoClient.ServerData.slotData["SIDE_QUEST_DEADLY_WATERS_SPIRIT"]}");
                    ArchipelagoConsole.LogMessage($"STARRY EYED SURPRISE QUEST SPIRIT: {ArchipelagoClient.ServerData.slotData["SIDE_QUEST_STARRY_EYED_SURPRISE_SPIRIT"]}");
                    ArchipelagoConsole.LogMessage($"ARCTIC MENACE QUEST SPIRIT: {ArchipelagoClient.ServerData.slotData["SIDE_QUEST_ARCTIC_MENACE_SPIRIT"]}");
                    ArchipelagoConsole.LogMessage($"CENTIBOOB QUEST 1 SPIRIT: {ArchipelagoClient.ServerData.slotData["SIDE_QUEST_CENTIBOOB_1_SPIRIT"]}");
                    ArchipelagoConsole.LogMessage($"CENTIBOOB QUEST 2 SPIRIT: {ArchipelagoClient.ServerData.slotData["SIDE_QUEST_CENTIBOOB_2_SPIRIT"]}");
                    ArchipelagoConsole.LogMessage($"CENTIBOOB QUEST 3 SPIRIT: {ArchipelagoClient.ServerData.slotData["SIDE_QUEST_CENTIBOOB_3_SPIRIT"]}");
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
                case "$debugclientdata":
                    DataRipping.outputalldata();
                    break;
                case "$debugdata":
                    ArchipelagoConsole.LogMessage("OUTPUTING SERVER DATA");
                    foreach (var i in ArchipelagoClient.ServerData.slotData)
                    {
                        ArchipelagoConsole.LogMessage($"key:{i.Key} || Value:");
                        ArchipelagoConsole.LogMessage(ArchipelagoClient.ServerData.slotData[i.Key].ToString());
                    }
                    ArchipelagoConsole.LogMessage("OUTPUTING SERVER DATA COMPLETE");
                    break;
                case "$debugrando":
                    ArchipelagoConsole.LogMessage("OUTPUTING RANDO DATA");
                    if (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["randomise_map"]) == 0)
                    {
                        ArchipelagoConsole.LogMessage("MAP RANDO NOT ENABLED");
                        break;
                    }
                    foreach (var i in ArchipelagoClient.ServerData.mapdata)
                    {
                        ArchipelagoConsole.LogMessage($"{i.Key} -> {i.Value}");
                    }
                    ArchipelagoConsole.LogMessage("OUTPUTING RANDO DATA COMPLETE");
                    break;
                case "$fixsave"://might work?
                                //save.fixsave();

                    ArchipelagoClient.session.DataStorage[Scope.Slot, "save"].Initialize("");
                    break;



                //CHEATS
                case "$cheat.reset":
                    ArchipelagoConsole.LogMessage("resetting save flag");
                    ArchipelagoClient.session.DataStorage[Scope.Slot, "slotsetup"] = false;
                    break;
                case "$cheat.quest":
                    ArchipelagoConsole.LogMessage("advanceing main quest");
                    SpiritValleyArchipelago.ArchipelagoClient.SendMessage($"Activated quest dev cheat to advance main quest");
                    string quest = QuestManager.instance.mainQuest[QuestManager.instance.GetIndexForMainQuestByID(HelperItems.save.GetActiveMainQuestState().id) + 1].id;
                    HelperItems.save.AdvanceMainQuest(quest);
                    break;
                case "$cheat.crystals":
                    ArchipelagoConsole.LogMessage("Adding 10 Spirit Crystal+2 to Inventory");
                    SpiritValleyArchipelago.ArchipelagoClient.SendMessage($"Activated crystal dev cheat for extra spirit crystals");
                    HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Crystal_SpiritCrystal+2"), 10, true);
                    break;
                case "$cheat.potion":
                    ArchipelagoConsole.LogMessage("Adding 10 Greater Rejuvenation Potion and Golden Seed of Life to Inventory");
                    SpiritValleyArchipelago.ArchipelagoClient.SendMessage($"Activated potion dev cheat for extra potions/revives");
                    HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Potion_GreaterRejuvenationPotion"), 10, true);
                    HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_CleansingTonic"), 10, true);
                    HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_GoldenSeedOfLife"), 10, true);
                    break;
                case "$cheat.sex":
                    ArchipelagoConsole.LogMessage("Adding 10 ChocolateCake to Inventory");
                    SpiritValleyArchipelago.ArchipelagoClient.SendMessage($"Activated affection dev cheat giving extra affection items");
                    HelperItems.save.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Consumable_ChocolateCake"), 10, true);
                    break;
                case "$cheat.warp":
                    SpiritValleyArchipelago.ArchipelagoClient.SendMessage($"Activated warp dev cheat unlocking all warp locations");
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

                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail1)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail1); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail2)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail2); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail3)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail3); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail4)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail4); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail5)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail5); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail6)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail6); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail7)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail7); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail8)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail8); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail9)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail9); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail10)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail10); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail11)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail11); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail12)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail12); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail13)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail13); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail14)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail14); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail15)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail15); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail16)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail16); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail17)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail17); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail18)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail18); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail19)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail19); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail20)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail20); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail21)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail21); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail22)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.Trail22); }

                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.EvergreenOutpost)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.EvergreenOutpost); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.EvergreenCaverns)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.EvergreenCaverns); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.SandyTunnels)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.SandyTunnels); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.DairyFarm)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.DairyFarm); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.DustyGrotto)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.DustyGrotto); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.OldMastersHut)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.OldMastersHut); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.ColdHarbor)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.ColdHarbor); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.AbandonedMine)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.AbandonedMine); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.SpiritPassage)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.SpiritPassage); }
                    if (!HelperItems.save.visitedMapLocations.Contains(MapLocationID.CrashSite)) { HelperItems.save.visitedMapLocations.Add(MapLocationID.CrashSite); }
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

        public static void processwarp(string code)
        {

            if (SceneManager.GetActiveScene().name == "TitleScreen") { ArchipelagoConsole.LogMessage("CANNOT WARP WHEN ON TITLE SCREEN:"); return; }

                string[] warps = code.Split(' ');

            bool rando = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["randomise_map"]) == 1;

            switch (warps[1].ToLower())
            {
                case "list":
                    ArchipelagoConsole.LogMessage("Use: \"$warp <location>\"");
                    ArchipelagoConsole.LogMessage("Possibe locations:");
                    ArchipelagoConsole.LogMessage("trail1, trail2 ... trail21, trail 22, oakwood, greensvale, tumbleweedtown, coconutvillage, frostville, evergreenoutpost, evergreencaverns, sandytunnels, dairyfarm, dustygrotto, oldMastershut, coldharbor, abandonedmine, spiritpassage, crashsite");
                    break;


                case "oakwood":
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
                case "greensvale":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Greensvale))
                    {
                        HelperItems.save.transitionSceneName = "Greensvale";
                        HelperItems.save.transitionAreaID = "waystone";
                        SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                        {
                            SceneManager.LoadScene("Greensvale", LoadSceneMode.Single);
                        });
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "tumbleweedtown":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.TumbleweedTown))
                    {
                        HelperItems.save.transitionSceneName = "TumbleweedTown";
                        HelperItems.save.transitionAreaID = "waystone";
                        SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                        {
                            SceneManager.LoadScene("TumbleweedTown", LoadSceneMode.Single);
                        });
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "coconutvillage":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.CoconutVillage))
                    {
                        HelperItems.save.transitionSceneName = "CoconutVillage";
                        HelperItems.save.transitionAreaID = "waystone";
                        SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                        {
                            SceneManager.LoadScene("CoconutVillage", LoadSceneMode.Single);
                        });
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "frostville":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Frostville))
                    {
                        HelperItems.save.transitionSceneName = "Frostville1";
                        HelperItems.save.transitionAreaID = "waystone";
                        SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                        {
                            SceneManager.LoadScene("Frostville1", LoadSceneMode.Single);
                        });
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;


                case "evergreenoutpost":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.EvergreenOutpost))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["EvergreenOutpost Bottom"].Split(' ')[0])))
                            {
                                id = "Bottom";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["EvergreenOutpost Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["EvergreenOutpost_East Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "EvergreenOutpost";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("EvergreenOutpost", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "EvergreenOutpost";
                            HelperItems.save.transitionAreaID = "Bottom";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("EvergreenOutpost", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "evergreencaverns":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.EvergreenCaverns))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["EvergreenCaverns Bottom"].Split(' ')[0])))
                            {
                                id = "Bottom";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["EvergreenCaverns Top"].Split(' ')[0])))
                            {
                                id = "Top";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "EvergreenCaverns";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("EvergreenCaverns", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "EvergreenCaverns";
                            HelperItems.save.transitionAreaID = "Bottom";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("EvergreenCaverns", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "sandytunnels":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.SandyTunnels))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["SandyTunnels Bottom"].Split(' ')[0])))
                            {
                                id = "Bottom";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["SandyTunnels Top"].Split(' ')[0])))
                            {
                                id = "Top";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "SandyTunnels";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("SandyTunnels", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "SandyTunnels";
                            HelperItems.save.transitionAreaID = "Bottom";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("SandyTunnels", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "dairyfarm":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.DairyFarm))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.GetWayStoneState("DairyFarm").isActive)
                            {
                                id = "waystone";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["DairyFarm Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["DairyFarm Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "DairyFarm";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("DairyFarm", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "DairyFarm";
                            HelperItems.save.transitionAreaID = "Left";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("DairyFarm", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "dustygrotto":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.DustyGrotto))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["DustyGrotto Top"].Split(' ')[0])))
                            {
                                id = "Top";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["DustyGrotto Bottom"].Split(' ')[0])))
                            {
                                id = "Bottom";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "DustyGrotto";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("DustyGrotto", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "DustyGrotto";
                            HelperItems.save.transitionAreaID = "Top";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("DustyGrotto", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "oldmastershut":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.OldMastersHut))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["OldMastersHut Tunnel"].Split(' ')[0])))
                            {
                                id = "Tunnel";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["OldMastersHut HutOut"].Split(' ')[0])))
                            {
                                id = "HutOut";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["OldMastersHut Cave"].Split(' ')[0])))
                            {
                                id = "Cave";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "OldMastersHut";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("OldMastersHut", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "OldMastersHut";
                            HelperItems.save.transitionAreaID = "HutOut";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("OldMastersHut", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "coldharbor":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.ColdHarbor))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (QuestManager.instance.GetIsActiveMainQuestGreaterOrEqualThan("main_quest_37_the_frigid_maiden"))
                            {
                                id = "waystone";
                            }
                            else if (HelperItems.save.GetWayStoneState("ColdHarbor").isActive)
                            {
                                id = "waystone";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["ColdHarbor Top"].Split(' ')[0])))
                            {
                                id = "Top";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "ColdHarbor";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("ColdHarbor", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "ColdHarbor";
                            HelperItems.save.transitionAreaID = "waystone";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("ColdHarbor", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "abandonedmine":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.AbandonedMine))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.GetWayStoneState("AbandonedMine").isActive)
                            {
                                id = "waystone";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["AbandonedMine Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["AbandonedMine House1"].Split(' ')[0])))
                            {
                                id = "House1";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "AbandonedMine";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("AbandonedMine", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "AbandonedMine";
                            HelperItems.save.transitionAreaID = "waystone";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("AbandonedMine", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "spiritpassage":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.SpiritPassage))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["SpiritPassage Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["SpiritPassage Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "SpiritPassage";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("SpiritPassage", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "SpiritPassage";
                            HelperItems.save.transitionAreaID = "Left";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("SpiritPassage", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "crashsite":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.CrashSite))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (QuestManager.instance.GetIsActiveMainQuestGreaterOrEqualThan("main_quest_30_welcome_to_paradise"))
                            {
                                id = "waystone";
                            }
                            else if (HelperItems.save.GetWayStoneState("CrashSite").isActive)
                            {
                                id = "waystone";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["CrashSite Bottom"].Split(' ')[0])))
                            {
                                id = "Bottom";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "SpiritPassage";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("SpiritPassage", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "SpiritPassage";
                            HelperItems.save.transitionAreaID = "waystone";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("SpiritPassage", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                
                case "trail1":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail1))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail1 Bottom"].Split(' ')[0])))
                            {
                                id = "Bottom";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail1 Top"].Split(' ')[0])))
                            {
                                id = "Top";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail1";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail1", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail1";
                            HelperItems.save.transitionAreaID = "Bottom";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail1", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail2":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail2))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail2 Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail2 Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail2";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail2", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail2";
                            HelperItems.save.transitionAreaID = "Right";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail2", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail3":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail3))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail3 Bottom"].Split(' ')[0])))
                            {
                                id = "Bottom";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail3 Cave"].Split(' ')[0])))
                            {
                                id = "Cave";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail3";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail3", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail3";
                            HelperItems.save.transitionAreaID = "Bottom";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail3", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail4":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail4))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.GetWayStoneState("Trail4").isActive)
                            {
                                id = "waystone";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail4 Cave"].Split(' ')[0])))
                            {
                                id = "Cave";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail4 Temple"].Split(' ')[0])))
                            {
                                id = "Temple";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail4";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail4", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail4";
                            HelperItems.save.transitionAreaID = "Cave";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail4", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail5":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail5))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail5 Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail5 TunnelsOut"].Split(' ')[0])))
                            {
                                id = "TunnelsOut";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail5";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail5", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail5";
                            HelperItems.save.transitionAreaID = "Left";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail5", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail6":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail6))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail6 TunnelsOut"].Split(' ')[0])))
                            {
                                id = "TunnelsOut";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail6 Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail6";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail6", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail6";
                            HelperItems.save.transitionAreaID = "TunnelsOut";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail6", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail7":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail7))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail7 Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail7 Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail7";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail7", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail7";
                            HelperItems.save.transitionAreaID = "Left";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail7", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail8":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail8))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail8 Top"].Split(' ')[0])))
                            {
                                id = "Top";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail8 Tunnel"].Split(' ')[0])))
                            {
                                id = "Tunnel";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail8";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail8", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail8";
                            HelperItems.save.transitionAreaID = "Top";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail8", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail9":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail9))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail9 Bottom"].Split(' ')[0])))
                            {
                                id = "Bottom";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail9 Temple"].Split(' ')[0])))
                            {
                                id = "Temple";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail9";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail9", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail9";
                            HelperItems.save.transitionAreaID = "Bottom";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail9", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail10":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail10))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail10 Top"].Split(' ')[0])))
                            {
                                id = "Top";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail10 Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail10";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail10", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail10";
                            HelperItems.save.transitionAreaID = "Top";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail10", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail11":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail11))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail11 Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail11 Bottom"].Split(' ')[0])))
                            {
                                id = "Bottom";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail11 pier"].Split(' ')[0])))
                            {
                                id = "pier";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail11";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail11", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail11";
                            HelperItems.save.transitionAreaID = "Right";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail11", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail12":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail12))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail12 Top"].Split(' ')[0])))
                            {
                                id = "Top";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail12 Bottom"].Split(' ')[0])))
                            {
                                id = "Bottom";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail12";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail12", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail12";
                            HelperItems.save.transitionAreaID = "Top";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail12", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail13":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail13))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail13 pier"].Split(' ')[0])))
                            {
                                id = "pier";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail13 Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail13";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail13", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail13";
                            HelperItems.save.transitionAreaID = "pier";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail13", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail14":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail14))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.GetWayStoneState("Trail14").isActive)
                            {
                                id = "waystone";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail14 Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail14 CaveIn"].Split(' ')[0])))
                            {
                                id = "CaveIn";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail14";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail14", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail14";
                            HelperItems.save.transitionAreaID = "Right";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail14", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail15":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail15))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail15 Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail15 Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail15 Left2"].Split(' ')[0])))
                            {
                                id = "Left2";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail15";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail15", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail15";
                            HelperItems.save.transitionAreaID = "Right";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail15", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail16":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail16))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail16 Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail16_Top Right2"].Split(' ')[0])))
                            {
                                id = "Right2";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail16 Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail16_Top Cave"].Split(' ')[0])))
                            {
                                id = "Cave";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail16";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail16", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail16";
                            HelperItems.save.transitionAreaID = "Right";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail16", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail17":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail17))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail17 Bottom"].Split(' ')[0])))
                            {
                                id = "Bottom";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail17 Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail17";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail17", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail17";
                            HelperItems.save.transitionAreaID = "Bottom";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail17", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail18":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail18))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.GetWayStoneState("Trail18").isActive)
                            {
                                id = "waystone";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail18 Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail18 TempleIn"].Split(' ')[0])))
                            {
                                id = "TempleIn";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail18";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail18", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail18";
                            HelperItems.save.transitionAreaID = "Left";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail18", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail19":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail19))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (QuestManager.instance.GetIsActiveMainQuestGreaterOrEqualThan("main_quest_50_sanctuary_shakedown"))
                            {
                                id = "waystone";
                            }
                            else if (HelperItems.save.GetWayStoneState("Trail4").isActive)
                            {
                                id = "waystone";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail19 Top"].Split(' ')[0])))
                            {
                                id = "Top";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail19";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail19", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail19";
                            HelperItems.save.transitionAreaID = "waystone";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail19", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail20":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail20))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail20 Bottom"].Split(' ')[0])))
                            {
                                id = "Bottom";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail20 Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail20_Right Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail20";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail20", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail20";
                            HelperItems.save.transitionAreaID = "Bottom";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail20", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail21":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail21))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail21 Right"].Split(' ')[0])))
                            {
                                id = "Right";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail21";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail21", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail21";
                            HelperItems.save.transitionAreaID = "Right";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail21", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                case "trail22":
                    if (HelperItems.save.visitedMapLocations.Contains(MapLocationID.Trail22))
                    {
                        if (rando)
                        {
                            string id = null;
                            if (HelperItems.save.GetWayStoneState("Trail22").isActive)
                            {
                                id = "waystone";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail22 Left"].Split(' ')[0])))
                            {
                                id = "Left";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail22 Top"].Split(' ')[0])))
                            {
                                id = "Top";
                            }
                            else if (HelperItems.save.visitedMapLocations.Contains(HelperSpirits.mapstringToid(ArchipelagoClient.ServerData.mapdata["Trail22 Cave"].Split(' ')[0])))
                            {
                                id = "Cave";
                            }

                            if (id != null)
                            {
                                HelperItems.save.transitionSceneName = "Trail22";
                                HelperItems.save.transitionAreaID = id;
                                SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                                {
                                    SceneManager.LoadScene("Trail22", LoadSceneMode.Single);
                                });
                            }
                        }
                        else
                        {
                            HelperItems.save.transitionSceneName = "Trail22";
                            HelperItems.save.transitionAreaID = "Left";
                            SceneTransitionManager.instance.screenFade.FadeOut(0.5f, delegate
                            {
                                SceneManager.LoadScene("Trail22", LoadSceneMode.Single);
                            });
                        }
                    }
                    else
                    {
                        ArchipelagoConsole.LogMessage("Player Hasnt Visted Location Unable To Warp");
                    }
                    break;
                
                
                default:
                    ArchipelagoConsole.LogMessage($"WARP CODE ({code}) NOT RECONISED USE CODE \"$warp list\" to get list of possible warps");
                    break;
            }
        }

    }
}
