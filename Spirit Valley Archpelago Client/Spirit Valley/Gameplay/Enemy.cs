using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class Enemy
    {

        public static Dictionary<string, float> t = new Dictionary<string, float>();

        [HarmonyPatch(typeof(EnemyMapItem), "Update")]
        [HarmonyPrefix]
        public static void spinn(EnemyMapItem __instance, ref Hero ___hero)
        {
            if (GameManager.instance.GetIsGamePaused()) { return; }
            if (!___hero.GetIsInputEnabled()) { return; }

            if (!Convert.ToBoolean(ArchipelagoClient.ServerData.slotData["Enemy_Vision"]))
            {
                AutoInteractObject ao = __instance.GetComponentInChildren<AutoInteractObject>();
                if (ao == null)
                {
                    ArchipelagoConsole.LogDebug($"EnemyMapItem:{__instance.guid} HAS NO AutoInteractObject");
                    return;
                }

                ao.transform.localPosition = new Vector3(0.5f, 0.5f, 0);
                ao.transform.localScale = new Vector3(1, 1, 1);

                return; 
            }

            if (!t.ContainsKey(__instance.guid)) {  t[__instance.guid] = 0.0f; return; }
            else { t[__instance.guid] += Time.deltaTime; }

            if (t[__instance.guid] < new System.Random().Next(1,11)) { return; }
            t[__instance.guid] = 0.0f;

            switch (Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Enemy_Spin"]))
            {
                case 0:
                    break;
                case 1:
                    if (__instance.faceDirection == Vector3Int.up)
                    {
                        __instance.faceDirection = Vector3Int.right;
                        int w = 15;
                        for (int m = 0; m < 15; m++)
                        {
                            if (__instance.gridMovementController.TestHasOverlappingCollisionMaskCollisions(new Vector3Int(__instance.gridMovementController.GetCurrentCell().x + m + 1, __instance.gridMovementController.GetCurrentCell().y, __instance.gridMovementController.GetCurrentCell().z)))
                            {
                                w = m;
                                break;
                            }
                        }

                        AutoInteractObject ao = __instance.GetComponentInChildren<AutoInteractObject>();
                        if (ao == null)
                        {
                            ArchipelagoConsole.LogDebug($"EnemyMapItem:{__instance.guid} HAS NO AutoInteractObject");
                            break;
                        }

                        if (w == 0)
                        {
                            ao.transform.localPosition = new Vector3(0.5f, 0.5f, 0);
                            ao.transform.localScale = new Vector3(1, 1, 1);
                        }
                        else
                        {
                            ao.transform.localPosition = new Vector3(1 + (w / 2), 0.5f, 0);
                            ao.transform.localScale = new Vector3(w, 1, 1);
                        }
                    }
                    else if (__instance.faceDirection == Vector3Int.right)
                    {
                        __instance.faceDirection = Vector3Int.down;
                        int w = 15;
                        for (int m = 0; m < 15; m++)
                        {
                            if (__instance.gridMovementController.TestHasOverlappingCollisionMaskCollisions(new Vector3Int(__instance.gridMovementController.GetCurrentCell().x, __instance.gridMovementController.GetCurrentCell().y - m - 1, __instance.gridMovementController.GetCurrentCell().z)))
                            {
                                w = m;
                                break;
                            }
                        }

                        AutoInteractObject ao = __instance.GetComponentInChildren<AutoInteractObject>();
                        if (ao == null)
                        {
                            ArchipelagoConsole.LogDebug($"EnemyMapItem:{__instance.guid} HAS NO AutoInteractObject");
                            break;
                        }

                        if (w == 0)
                        {
                            ao.transform.localPosition = new Vector3(0.5f, 0.5f, 0);
                            ao.transform.localScale = new Vector3(1, 1, 1);
                        }
                        else
                        {
                            ao.transform.localPosition = new Vector3(0.5f, -(w / 2), 0);
                            ao.transform.localScale = new Vector3(1, w, 1);
                        }
                    }
                    else if (__instance.faceDirection == Vector3Int.down)
                    {
                        __instance.faceDirection = Vector3Int.left;
                        int w = 15;
                        for (int m = 0; m < 15; m++)
                        {
                            if (__instance.gridMovementController.TestHasOverlappingCollisionMaskCollisions(new Vector3Int(__instance.gridMovementController.GetCurrentCell().x - m - 1, __instance.gridMovementController.GetCurrentCell().y, __instance.gridMovementController.GetCurrentCell().z)))
                            {
                                w = m;
                                break;
                            }
                        }

                        AutoInteractObject ao = __instance.GetComponentInChildren<AutoInteractObject>();
                        if (ao == null)
                        {
                            ArchipelagoConsole.LogDebug($"EnemyMapItem:{__instance.guid} HAS NO AutoInteractObject");
                            break;
                        }

                        if (w == 0)
                        {
                            ao.transform.localPosition = new Vector3(0.5f, 0.5f, 0);
                            ao.transform.localScale = new Vector3(1, 1, 1);
                        }
                        else
                        {
                            ao.transform.localPosition = new Vector3(-(w / 2), 0.5f, 0);
                            ao.transform.localScale = new Vector3(w, 1, 1);
                        }
                    }
                    else //left
                    {
                        __instance.faceDirection = Vector3Int.up;
                        int w = 15;
                        for (int m = 1; m < 16; m++)
                        {
                            if (__instance.gridMovementController.TestHasOverlappingCollisionMaskCollisions(new Vector3Int(__instance.gridMovementController.GetCurrentCell().x, __instance.gridMovementController.GetCurrentCell().y + m + 1, __instance.gridMovementController.GetCurrentCell().z)))
                            {
                                w = m;
                                break;
                            }
                        }

                        AutoInteractObject ao = __instance.GetComponentInChildren<AutoInteractObject>();
                        if (ao == null)
                        {
                            ArchipelagoConsole.LogDebug($"EnemyMapItem:{__instance.guid} HAS NO AutoInteractObject");
                            break;
                        }

                        if (w == 0)
                        {
                            ao.transform.localPosition = new Vector3(0.5f, 0.5f, 0);
                            ao.transform.localScale = new Vector3(1, 1, 1);
                        }
                        else
                        {
                            ao.transform.localPosition = new Vector3(0.5f, 1 + (w / 2), 0);
                            ao.transform.localScale = new Vector3(1, w, 1);
                        }
                    }
                    break;
                case 2:
                    int r = new System.Random().Next(4);

                    if (r == 0)
                    {
                        __instance.faceDirection = Vector3Int.right;
                        int w = 15;
                        for (int m = 0; m < 15; m++)
                        {
                            if (__instance.gridMovementController.TestHasOverlappingCollisionMaskCollisions(new Vector3Int(__instance.gridMovementController.GetCurrentCell().x + m + 1, __instance.gridMovementController.GetCurrentCell().y, __instance.gridMovementController.GetCurrentCell().z)))
                            {
                                w = m;
                                break;
                            }
                        }

                        AutoInteractObject ao = __instance.GetComponentInChildren<AutoInteractObject>();
                        if (ao == null)
                        {
                            ArchipelagoConsole.LogDebug($"EnemyMapItem:{__instance.guid} HAS NO AutoInteractObject");
                            break;
                        }

                        if (w == 0)
                        {
                            ao.transform.localPosition = new Vector3(0.5f, 0.5f, 0);
                            ao.transform.localScale = new Vector3(1, 1, 1);
                        }
                        else
                        {
                            ao.transform.localPosition = new Vector3(1 + (w / 2), 0.5f, 0);
                            ao.transform.localScale = new Vector3(w, 1, 1);
                        }
                    }
                    else if (r == 1)
                    {
                        __instance.faceDirection = Vector3Int.down;
                        int w = 15;
                        for (int m = 0; m < 15; m++)
                        {
                            if (__instance.gridMovementController.TestHasOverlappingCollisionMaskCollisions(new Vector3Int(__instance.gridMovementController.GetCurrentCell().x, __instance.gridMovementController.GetCurrentCell().y - m - 1, __instance.gridMovementController.GetCurrentCell().z)))
                            {
                                w = m;
                                break;
                            }
                        }

                        AutoInteractObject ao = __instance.GetComponentInChildren<AutoInteractObject>();
                        if (ao == null)
                        {
                            ArchipelagoConsole.LogDebug($"EnemyMapItem:{__instance.guid} HAS NO AutoInteractObject");
                            break;
                        }

                        if (w == 0)
                        {
                            ao.transform.localPosition = new Vector3(0.5f, 0.5f, 0);
                            ao.transform.localScale = new Vector3(1, 1, 1);
                        }
                        else
                        {
                            ao.transform.localPosition = new Vector3(0.5f, -(w / 2), 0);
                            ao.transform.localScale = new Vector3(1, w, 1);
                        }
                    }
                    else if (r == 2)
                    {
                        __instance.faceDirection = Vector3Int.left;
                        int w = 15;
                        for (int m = 0; m < 15; m++)
                        {
                            if (__instance.gridMovementController.TestHasOverlappingCollisionMaskCollisions(new Vector3Int(__instance.gridMovementController.GetCurrentCell().x - m - 1, __instance.gridMovementController.GetCurrentCell().y, __instance.gridMovementController.GetCurrentCell().z)))
                            {
                                w = m;
                                break;
                            }
                        }

                        AutoInteractObject ao = __instance.GetComponentInChildren<AutoInteractObject>();
                        if (ao == null)
                        {
                            ArchipelagoConsole.LogDebug($"EnemyMapItem:{__instance.guid} HAS NO AutoInteractObject");
                            break;
                        }

                        if (w == 0)
                        {
                            ao.transform.localPosition = new Vector3(0.5f, 0.5f, 0);
                            ao.transform.localScale = new Vector3(1, 1, 1);
                        }
                        else
                        {
                            ao.transform.localPosition = new Vector3(-(w / 2), 0.5f, 0);
                            ao.transform.localScale = new Vector3(w, 1, 1);
                        }
                    }
                    else //left
                    {
                        __instance.faceDirection = Vector3Int.up;
                        int w = 15;
                        for (int m = 1; m < 16; m++)
                        {
                            if (__instance.gridMovementController.TestHasOverlappingCollisionMaskCollisions(new Vector3Int(__instance.gridMovementController.GetCurrentCell().x, __instance.gridMovementController.GetCurrentCell().y + m + 1, __instance.gridMovementController.GetCurrentCell().z)))
                            {
                                w = m;
                                break;
                            }
                        }

                        AutoInteractObject ao = __instance.GetComponentInChildren<AutoInteractObject>();
                        if (ao == null)
                        {
                            ArchipelagoConsole.LogDebug($"EnemyMapItem:{__instance.guid} HAS NO AutoInteractObject");
                            break;
                        }

                        if (w == 0)
                        {
                            ao.transform.localPosition = new Vector3(0.5f, 0.5f, 0);
                            ao.transform.localScale = new Vector3(1, 1, 1);
                        }
                        else
                        {
                            ao.transform.localPosition = new Vector3(0.5f, 1 + (w / 2), 0);
                            ao.transform.localScale = new Vector3(1, w, 1);
                        }
                    }
                    break;
                default:
                    break;
            }
        }

    }
}
