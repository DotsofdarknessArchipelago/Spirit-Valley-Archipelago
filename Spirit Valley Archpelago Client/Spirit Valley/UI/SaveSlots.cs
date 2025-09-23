using HarmonyLib;
using System;
using System.Collections.Generic;
using System.Text;
using UnityEngine.Tilemaps;
using UnityEngine;
using UnityEngine.Localization.Pseudo;
using System.Reflection;
using TMPro;
using SpiritValleyArchipelagoClient.Archipelago;
using UnityEngine.UI;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.UI
{
    [HarmonyPatch]
    public class SaveSlots
    {

        [HarmonyPatch(typeof(SaveSlotsWindow), "RegainFocus")]
        [HarmonyPrefix]
        public static void disablewindow()
        {
            Plugin.BepinLogger.LogMessage("SAVE SLOT WINDOW UPDATE");
            GameObject.Find("TitleScreenMenu/SaveSlotsWindow/Fade/Bg/SlotContainer").SetActive(false);
            GameObject.Find("TitleScreenMenu/SaveSlotsWindow/Fade/Bg/TitleLabel").SetActive(false);

            //if (GameObject.Find("TitleScreenMenu/SaveSlotsWindow/Fade/Bg/ArchContainer") == null)
            //{
            //    var window = new GameObject("ArchContainer", typeof(VerticalLayoutGroup), typeof(ContentSizeFitter));
            //
            //    window.transform.SetParent(GameObject.Find("TitleScreenMenu/SaveSlotsWindow/Fade/Bg").transform);
            //
            //    window.GetComponent<VerticalLayoutGroup>().childControlWidth = false;
            //    window.GetComponent<VerticalLayoutGroup>().childControlHeight = false;
            //    window.GetComponent<ContentSizeFitter>().horizontalFit = ContentSizeFitter.FitMode.PreferredSize;
            //    window.GetComponent<ContentSizeFitter>().verticalFit = ContentSizeFitter.FitMode.PreferredSize;
            //
            //    var host = new GameObject("ArchHost", typeof(TMP_InputField), typeof(Image));
            //    var user = new GameObject("ArchUser", typeof(TMP_InputField), typeof(Image));
            //    var pass = new GameObject("ArchPass", typeof(TMP_InputField), typeof(Image));
            //
            //
            //    host.transform.SetParent(window.transform);
            //    user.transform.SetParent(window.transform);
            //    pass.transform.SetParent(window.transform);
            //
            //    host.GetComponent<Image>().color = Color.white;
            //    user.GetComponent<Image>().color = Color.red;
            //    pass.GetComponent<Image>().color = Color.blue;
            //}
            //else
            //{
            //
            //}
        }


        [HarmonyPatch(typeof(GameManager), "InitCoroutine")]
        [HarmonyPostfix]
        public static void archslot(GameManager __instance)
        {
            ArchipelagoConsole.LogDebug("game manager init");
            if (__instance.gameStates.Length == 4)
            {
                SystemData<GameState>[] t = new SystemData<GameState>[5];
                t[0] = __instance.gameStates[0];
                t[1] = __instance.gameStates[1];
                t[2] = __instance.gameStates[2];
                t[3] = __instance.gameStates[3];
                t[4] = new SystemData<GameState>(Application.persistentDataPath + "/archipelago", "archipelago", "json");
                __instance.gameStates = t;
                //__instance.gameStates[4].Delete(SaveType.Manual);
                //__instance.gameStates[4].Delete(SaveType.Auto);
            }
        }
    }
}
