using Archipelago.MultiClient.Net.Enums;
using BepInEx;
using BepInEx.Logging;
using HarmonyLib;
using Newtonsoft.Json;
using SpiritValleyArchipelagoClient.Archipelago;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;
using TMPro;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace SpiritValleyArchipelagoClient;

[BepInPlugin(PluginGUID, PluginName, PluginVersion)]
public class Plugin : BaseUnityPlugin
{
    public const string PluginGUID = "com.yourName.projectName";
    public const string PluginName = "Spirit Valley Archipelago Client";
    public const int PluginVersionMajor = 0;
    public const int PluginVersionMinor = 1;
    public const int PluginVersionBuild = 0;
    public const string PluginVersion = "0.1.0";//TODO MAKE SURE THESE MATCH

    public const string ModDisplayInfo = $"{PluginName} v{PluginVersion}";
    private const string APDisplayInfo = $"Archipelago v{ArchipelagoClient.APVersion}";
    public static ManualLogSource BepinLogger;
    public static ArchipelagoClient ArchipelagoClient;
    public static bool start = false;
    public static bool fixerror = false;

    public ArchipelagoData data = ArchipelagoClient.ServerData;

    public Rect archwindow = new Rect(Screen.width / 2 - (560 / 2), Screen.height / 2 - (400 / 2), 560, 400);
    public static GUIStyle mlabel;
    public static GUIStyle mlabel2;
    public static GUIStyle mlabel3;
    public static GUIStyle mbutton;
    public static GUIStyle mtext;

    public Dictionary<string, MonsterSkill> skilllist => HelperSpirits.skilllist;
    public static ArchipelageItemList test = null;


    private void Awake()
    {
        // Plugin startup logic
        BepinLogger = Logger;
        ArchipelagoClient = new ArchipelagoClient();
        ArchipelagoConsole.Awake();

        new Harmony(PluginGUID).PatchAll();

        ArchipelagoConsole.LogMessage($"{ModDisplayInfo} loaded!");
    }



    void Update()
    {
        if (Input.GetKeyDown(KeyCode.F8))
        {
            ArchipelagoConsole.toggleConsole();
        }
        if (Input.GetKeyDown(KeyCode.F7))
        {
            Cheats.wallhaks();
        }
        if (Input.GetKeyDown(KeyCode.F9))
        {
        }
        if (Input.GetMouseButtonDown(0))
        {
        }

        if (SceneManager.GetActiveScene().name == "TitleScreen")
        {
            GameObject.Find("TitleScreenMenu/ButtonContainer/StartGameButton/Label").GetComponent<TextMeshProUGUI>().SetText("Start Archipelago Game");
            if (GameObject.Find("TitleScreenMenu/SaveSlotsWindow") != null)
            {
                start = true;
            }
            else
            {
                start= false;
            }
        }
        else
        {
            start = false;
        }

    }

    private void OnGUI()
    {
        if (mlabel == null)
        {
            mlabel = new GUIStyle(GUI.skin.label.name);
            mlabel2 = new GUIStyle(GUI.skin.label.name);
            mlabel3 = new GUIStyle(GUI.skin.label.name);
            mbutton = new GUIStyle(GUI.skin.button.name);
            mtext = new GUIStyle(GUI.skin.textField.name);
            mlabel.fontSize = 34;
            mlabel2.fontSize = 28;
            mlabel3.fontSize = 24;
            mtext.fontSize = 20;
            mbutton.fontSize = 20;
            mtext.alignment = TextAnchor.MiddleLeft;
            mlabel.alignment = TextAnchor.MiddleRight;
            mlabel2.alignment = TextAnchor.MiddleCenter;
            mlabel3.alignment = TextAnchor.MiddleCenter;
        }

        // show the mod is currently loaded in the corner
        ArchipelagoConsole.OnGUI();
        GUI.Window(60, new Rect(10, 10, 320, 40), versionWindow, "");
        if (start)
        {
            GUI.color = new Color(0, 0, 0, 0);
            GUI.Window(61, archwindow, archWindow, "");
        }
    }

    public void versionWindow(int id)
    {
        GUI.depth = 0;
        GUI.backgroundColor = Color.clear;
        // show the Archipelago Version and whether we're connected or not
        if (ArchipelagoClient.Authenticated)
        {
            if ((PluginVersionMajor == Convert.ToInt32(ArchipelagoClient.ServerData.slotData["world_version_major"]))&& (PluginVersionMinor == Convert.ToInt32(ArchipelagoClient.ServerData.slotData["world_version_minor"]))&& (PluginVersionBuild == Convert.ToInt32(ArchipelagoClient.ServerData.slotData["world_version_build"])))
            {
                GUI.Label(new Rect(16, 16, 300, 20), "Client/World V(" + PluginVersion + ") : Status: Connected");
            }
            else
            {
                GUI.Label(new Rect(16, 16, 300, 20), $"Client V({PluginVersion}), World V({ArchipelagoClient.ServerData.slotData["world_version_major"]}.{ArchipelagoClient.ServerData.slotData["world_version_minor"]}.{ArchipelagoClient.ServerData.slotData["world_version_build"]}): Status: Connected");
            }
        }
        else
        {
            GUI.Label(new Rect(16, 16, 300, 20), "Client V(" + PluginVersion + "): Status: NOT Connected");
        }
    }

    public void archWindow(int id)
    {
        if (ArchipelagoClient.Authenticated)
        {

            string state = "";
            string button = "";
            float loc = 0;
            float item = 0;
            if (ArchipelagoClient.slotstate)
            {
                state = "GAME STARTED";
                button = "CONTINUE";
            }
            else
            {
                state = "NEW GAME";
                button = "START GAME";
            }
            if (ArchipelagoClient.session.Locations.AllLocationsChecked.Count() > 0)
            {
                loc = ArchipelagoClient.session.Locations.AllLocationsChecked.Count() / ArchipelagoClient.totalloc * 100;
            }
            else
            {
                loc = 0;
            }
            if (ArchipelagoClient.archlist.list.Count() > 0)
            {
                item = ArchipelagoClient.archlist.list.Count() / ArchipelagoClient.totalitem * 100;
            }
            else
            {
                item = 0;
            }
            //((ArchipelagoClient.session.Locations.AllLocationsChecked.Count()/ ArchipelagoClient.totalloc)*100)
            GUI.Label(new Rect(20, 100, 540, 40), $"SERVER STATE: {state}", mlabel3);
            GUI.Label(new Rect(20, 150, 540, 40), $"LOCATIONS CHECKED: {ArchipelagoClient.session.Locations.AllLocationsChecked.Count()} OF {ArchipelagoClient.totalloc} ({loc:G4}%)", mlabel3);
            GUI.Label(new Rect(20, 200, 540, 40), $"ITEMS RECIEVED: {ArchipelagoClient.archlist.list.Count()}  OF  {ArchipelagoClient.totalitem} ({item:G4}%)", mlabel3);
            if (GUI.Button(new Rect(140, 250, 280, 60), button, mbutton))
            {
                startarch();
            }
        }
        else
        {
            GUI.Label(new Rect(10, 20, 540, 60), "Client V(" + PluginVersion + "): Status: NOT Connected", mlabel2);
            GUI.Label(new Rect(10, 120, 270, 40), "Host: ", mlabel);
            GUI.Label(new Rect(10, 160, 270, 40), "Player Name: ", mlabel);
            GUI.Label(new Rect(10, 200, 270, 40), "Password: ", mlabel);

            ArchipelagoClient.ServerData.Uri = GUI.TextField(new Rect(archwindow.width / 2, 120, 270, 40), ArchipelagoClient.ServerData.Uri, mtext);
            ArchipelagoClient.ServerData.SlotName = GUI.TextField(new Rect(archwindow.width / 2, 160, 270, 40), ArchipelagoClient.ServerData.SlotName, mtext);
            ArchipelagoClient.ServerData.Password = GUI.TextField(new Rect(archwindow.width / 2, 200, 270, 40), ArchipelagoClient.ServerData.Password, mtext);

            if (GUI.Button(new Rect(archwindow.width / 2 - 50, 280, 100, 40), "Connect", mbutton) &&
                !ArchipelagoClient.ServerData.SlotName.IsNullOrWhiteSpace())
            {
                ArchipelagoClient.Connect();
            }

        }
    }

    public void startarch()
    {
        
        HelperSpirits.genskilllist();
        bool setup = ArchipelagoClient.session.DataStorage[Scope.Slot, "slotsetup"];
        ArchipelagoClient.ServerData.overidetypes();
        ArchipelagoClient.ServerData.overidebasestats();
        ArchipelagoConsole.LogDebug($"SETUP VALUE: {setup}");
        setup = setup && (File.Exists(Application.persistentDataPath + "/archipelago/archipelago.json") || File.Exists(Application.persistentDataPath + "/archipelago/archipelago_auto.json"));
        if (setup)
        {
            ArchipelagoConsole.LogDebug("Archipelago Game Started");
            //GameManager.instance.gameStates[4].data = JsonConvert.DeserializeObject<GameState>(Crypt.Decrypt(ArchipelagoClient.session.DataStorage[Scope.Slot, "save"]));
            //ArchipelagoConsole.LogDebug($"SAVE VALUE: \n{ArchipelagoClient.session.DataStorage[Scope.Slot, "save"]}");
            //GameManager.instance.gameStates[4].SaveAsync(SaveType.Auto).GetAwaiter().OnCompleted(loadgame);
            //File.WriteAllText(Application.persistentDataPath + "/archipelago/archipelago_auto.json", ArchipelagoClient.session.DataStorage[Scope.Slot, "save"].ToString());
            loadgame(File.GetLastWriteTimeUtc(Application.persistentDataPath + "/archipelago/archipelago.json") < File.GetLastWriteTimeUtc(Application.persistentDataPath + "/archipelago/archipelago_auto.json"));
        }
        else
        {
            ArchipelagoClient.session.DataStorage[Scope.Slot, "save"].Initialize("");
            ArchipelagoClient.session.DataStorage[Scope.Slot, "archdata"].Initialize("");

            ArchipelagoConsole.LogDebug("Archipelago Game Not Started");
            SystemData<GameState> systemData = GameManager.instance.gameStates[4];
            systemData.InitNew();
            systemData.data.migrationIndex = MigrationManager.instance.GetCurrentMigrationIndex();
            systemData.data.heroName = ArchipelagoClient.ServerData.SlotName;
            systemData.data.skinTonePresetIndex = 0;
            systemData.data.hairStylePresetIndex = 0;
            systemData.data.hairColorPresetIndex = 0;
            systemData.data.costumePresetIndex = 0;

            systemData.SaveAsync(SaveType.Auto).GetAwaiter().OnCompleted(delegate { loadgame(true); });
        }
    }

    public static void loadgame(bool auto)
    {
        if (auto)
        {
            GameManager.instance.LoadAndSetActiveGameState(4, SaveType.Auto);
        }
        else
        {
            GameManager.instance.LoadAndSetActiveGameState(4, SaveType.Manual);
        }
        AudioManager.instance.StopMusic();
        SceneTransitionManager.instance.screenFade.FadeOut(1f, delegate
        {
            string currentSceneName = GameManager.instance.GetActiveGameState().data.currentSceneName;
            if (string.IsNullOrEmpty(currentSceneName))
            {
                currentSceneName = "IntroScene";
            }
            ArchipelagoConsole.LogDebug("Continue save from " + currentSceneName);
            SceneManager.LoadScene(currentSceneName, LoadSceneMode.Single);
        });
    }
}