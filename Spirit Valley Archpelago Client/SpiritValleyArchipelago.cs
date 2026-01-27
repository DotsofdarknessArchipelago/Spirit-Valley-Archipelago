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
using TMPro;
using UnityEngine;
using UnityEngine.Localization.Settings;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

namespace SpiritValleyArchipelagoClient;

[BepInPlugin(PluginGUID, PluginName, PluginVersion)]
public class SpiritValleyArchipelago : BaseUnityPlugin
{
    public const string PluginGUID = "com.yourName.projectName";
    public const string PluginName = "Spirit Valley Archipelago Client";
    public const int PluginVersionMajor = 1;
    public const int PluginVersionMinor = 0;
    public const int PluginVersionBuild = 0;
    public const string PluginVersion = "1.0.0";//TODO MAKE SURE THESE MATCH

    public const string ModDisplayInfo = $"{PluginName} v{PluginVersion}";
    private const string APDisplayInfo = $"Archipelago v{ArchipelagoClient.APVersion}";
    public static ManualLogSource BepinLogger;
    public static ArchipelagoClient ArchipelagoClient;
    public static bool start = false;
    public static bool newgame = false;
    public static bool versioncheck = true;
    public static bool overritedata = false;

    //public ArchipelagoData data = ArchipelagoClient.ServerData;

    public Rect archwindow = new Rect(Screen.width / 2 - (560 / 2), Screen.height / 2 - (400 / 2), 560, 400);
    public static GUIStyle mlabel;
    public static GUIStyle mlabel2;
    public static GUIStyle mlabel3;
    public static GUIStyle mbutton;
    public static Texture trash;
    public static GUIStyle mtext;

    public static int slot = 0;

    public Dictionary<string, MonsterSkill> skilllist => HelperSpirits.skilllist;
    public static Dictionary<string, object> skilllisttest = new Dictionary<string, object>();
    public static GameState test = null;


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

        }
        if (Input.GetKeyDown(KeyCode.F9))
        {
            overritedata = true;
        }
        if (Input.GetMouseButtonDown(0))
        {
        }

        if (SceneManager.GetActiveScene().name == "TitleScreen")
        {
            GameObject.Find("TitleScreenMenu/ButtonContainer/StartGameButton/Label").GetComponent<TextMeshProUGUI>().SetText("Start Archipelago Game");
            if (trash == null)
            {
                foreach (GameObject go in Resources.FindObjectsOfTypeAll(typeof(GameObject)) as GameObject[])
                {
                    if (go.name == "DeleteButton")
                    {
                        foreach (Image i in go.GetComponentsInChildren<Image>())
                        {
                            if (i.name == "Image")
                            {
                                trash = i.mainTexture;
                                break;
                            }
                        }
                        break;
                    }
                }
            }
            if (GameObject.Find("TitleScreenMenu/SaveSlotsWindow") != null)
            {
                start = true;
            }
            else
            {
                newgame = false;
                start= false;
            }
            if (versioncheck)
            {
                versioncheck = false;
                if (GameObject.Find("TitleScreenMenu/Footer/VersionText").GetComponent<TextMeshProUGUI>().text != "V1.4.1")
                {
                    ArchipelagoConsole.LogMessage("WARNING EXPECTED GAME CLIENT VERSION MISSMATCH");
                    ArchipelagoConsole.LogError($"EXPECTED \"V1.4.1\" GOT \"{GameObject.Find("TitleScreenMenu/Footer/VersionText").GetComponent<TextMeshProUGUI>().text}\"");
                }
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
        GUI.Window(60, new Rect(10, 10, 340, 40), versionWindow, "");
        if (start)
        {
            GUI.color = new UnityEngine.Color(0, 0, 0, 0);
            GUI.Window(61, archwindow, archWindow, "");
        }
    }

    public void versionWindow(int id)
    {
        GUI.depth = 0;
        GUI.backgroundColor = UnityEngine.Color.clear;
        // show the Archipelago Version and whether we're connected or not
        if (ArchipelagoClient.Authenticated)
        {
            if ((PluginVersionMajor == Convert.ToInt32(ArchipelagoClient.ServerData.slotData["world_version_major"]))&& (PluginVersionMinor == Convert.ToInt32(ArchipelagoClient.ServerData.slotData["world_version_minor"]))&& (PluginVersionBuild == Convert.ToInt32(ArchipelagoClient.ServerData.slotData["world_version_build"])))
            {
                GUI.Label(new Rect(16, 16, 300, 20), $"Client/World V({PluginVersion}) : Status: Connected, S{slot}");
            }
            else
            {
                GUI.Label(new Rect(16, 16, 320, 20), $"Client V({PluginVersion}), World V({ArchipelagoClient.ServerData.slotData["world_version_major"]}.{ArchipelagoClient.ServerData.slotData["world_version_minor"]}.{ArchipelagoClient.ServerData.slotData["world_version_build"]}): Status: Connected, S{slot}");
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
                state = $"GAME STARTED (SLOT {slot+1})";
                button = "CONTINUE";
            }
            else
            {
                state = $"NEW GAME (SLOT {slot+1})";
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
        else if (newgame)
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
        else
        {
            if (File.Exists(Application.persistentDataPath + "/archipelagoslot1/archdata.json")) 
            {
                List<string> s1 = readarchdata(Application.persistentDataPath + "/archipelagoslot1/archdata.json");
                if (s1[1].IsNullOrWhiteSpace())
                {
                    if (GUI.Button(new Rect(20, 10, 475, 120), s1[0], mbutton))
                    {
                        slot = 0;
                        newgame = true;
                    }
                }
                else
                {
                    if (GUI.Button(new Rect(20, 10, 475, 120), s1[0], mbutton))
                    {
                        slot = 0;
                        ArchipelagoClient.ServerData.Uri = s1[1];
                        ArchipelagoClient.ServerData.SlotName = s1[2];
                        ArchipelagoClient.ServerData.Password = s1[3];
                        ArchipelagoClient.Connect();
                    }
                }
                if (GUI.Button(new Rect(500, 50, 40, 40), trash, mbutton))
                {
                    File.Delete(Application.persistentDataPath + "/archipelagoslot1/archdata.json");
                }
            }
            else 
            { 
                if (GUI.Button(new Rect(20, 10, 520, 120), "Click To Start A New Archipelago Game in Slot 1", mbutton))
                {
                    slot = 0;
                    newgame = true;
                }
            }

            if (File.Exists(Application.persistentDataPath + "/archipelagoslot2/archdata.json")) 
            {
                List<string> s2 = readarchdata(Application.persistentDataPath + "/archipelagoslot2/archdata.json");

                if (s2[1].IsNullOrWhiteSpace())
                {
                    if (GUI.Button(new Rect(20, 140, 475, 120), s2[0], mbutton))
                    {
                        slot = 1;
                        newgame = true;
                    }
                }
                else
                {
                    if (GUI.Button(new Rect(20, 140, 475, 120), s2[0], mbutton))
                    {
                        slot = 1;
                        ArchipelagoClient.ServerData.Uri = s2[1];
                        ArchipelagoClient.ServerData.SlotName = s2[2];
                        ArchipelagoClient.ServerData.Password = s2[3];
                        ArchipelagoClient.Connect();
                    }
                }
                if (GUI.Button(new Rect(500, 180, 40, 40), trash, mbutton))
                {
                    File.Delete(Application.persistentDataPath + "/archipelagoslot2/archdata.json");
                }
            }
            else 
            { 
                if (GUI.Button(new Rect(20, 140, 520, 120), "Click To Start A New Archipelago Game in Slot 2", mbutton))
                {
                    slot = 1;
                    newgame = true;
                }
            }

            if (File.Exists(Application.persistentDataPath + "/archipelagoslot3/archdata.json")) 
            {
                List<string> s3 = readarchdata(Application.persistentDataPath + "/archipelagoslot3/archdata.json");

                if (s3[1].IsNullOrWhiteSpace())
                {
                    if (GUI.Button(new Rect(20, 270, 475, 120), s3[0], mbutton))
                    {
                        slot = 2;
                        newgame = true;
                    }
                }
                else
                {
                    if (GUI.Button(new Rect(20, 270, 475, 120), s3[0], mbutton))
                    {
                        slot = 2;
                        ArchipelagoClient.ServerData.Uri = s3[1];
                        ArchipelagoClient.ServerData.SlotName = s3[2];
                        ArchipelagoClient.ServerData.Password = s3[3];
                        ArchipelagoClient.Connect();
                    }
                }
                if (GUI.Button(new Rect(500, 310, 40, 40), trash, mbutton))
                {
                    File.Delete(Application.persistentDataPath + "/archipelagoslot3/archdata.json");
                }
            }
            else 
            { 
                if (GUI.Button(new Rect(20, 270, 520, 120), "Click To Start A New Archipelago Game in Slot 3", mbutton))
                {
                    slot = 2;
                    newgame = true;
                }
            }
        }
    }

    public static List<string> readarchdata(string path)
    {
        List<string> output = new List<string>();
        using (StreamReader file = File.OpenText(path))
        {
            JsonSerializer serializer = new JsonSerializer();
            ArchipelageItemList savedlist = (ArchipelageItemList)serializer.Deserialize(file, typeof(ArchipelageItemList));
            if (savedlist.host.IsNullOrWhiteSpace())
            {
                output.Add($"ERROR RETREVING SAVED CONNECTION DATA\nCLICK TO RE-ENTER DATA\nLast Played:{File.GetLastWriteTime(path).ToString("d MMM h:m:s tt")}");
            }
            else if (overritedata)
            {
                output.Add($"OVERWRITE DATA KEY PRESSED\nCLICK TO RE-ENTER DATA\nLast Played:{File.GetLastWriteTime(path).ToString("d MMM h:m:s tt")}");
                output.Add(null);
                return output;
            }
            else
            {
                output.Add($"Host:{savedlist.host}\nUser:{savedlist.user}\nLast Played:{File.GetLastWriteTime(path).ToString("d MMM h:m:s tt")}");
            }
            output.Add(savedlist.host);
            output.Add(savedlist.user);
            output.Add(savedlist.pass);
        }
        return output;
    }

    public void startarch()
    {
        
        bool setup = ArchipelagoClient.session.DataStorage[Scope.Slot, "slotsetup"];
        ArchipelagoConsole.LogDebug($"SETUP VALUE: {setup}");
        setup = setup && (File.Exists(Application.persistentDataPath + $"/archipelagoslot{slot + 1}/archipelagoslot{slot + 1}.json") || File.Exists(Application.persistentDataPath + $"/archipelagoslot{slot + 1}/archipelagoslot{slot + 1}_auto.json") && File.Exists(Application.persistentDataPath + $"/archipelagoslot{slot+1}/archdata.json"));
        if (setup)
        {
            ArchipelagoConsole.LogDebug("Archipelago Game Started");

            loadgame(File.GetLastWriteTimeUtc(Application.persistentDataPath + $"/archipelagoslot{slot + 1}/archipelagoslot{slot + 1}.json") < File.GetLastWriteTimeUtc(Application.persistentDataPath + $"/archipelagoslot{slot + 1}/archipelagoslot{slot + 1}_auto.json"));
        }
        else
        {
            ArchipelagoConsole.LogDebug("Archipelago Game Not Started");
            SystemData<GameState> systemData = GameManager.instance.gameStates[4+slot];
            systemData.InitNew();
            systemData.data.migrationIndex = MigrationManager.instance.GetCurrentMigrationIndex();
            systemData.data.heroName = ArchipelagoClient.ServerData.SlotName;

            systemData.data.heroCharacterSettingsIndex = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Char_Gender"]);

            systemData.data.skinTonePresetIndex = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Char_Skin"]);
            systemData.data.hairStylePresetIndex = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Char_Hairstyle"]);
            systemData.data.hairColorPresetIndex = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Char_Haircolor"]);
            systemData.data.costumePresetIndex = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Char_Outfit"]);

            systemData.data.AddItemToInventory(ItemManager.instance.GetItemAssetByName("Crystal_SpiritCrystal"), 5, true);

            systemData.SaveAsync(SaveType.Auto).GetAwaiter().OnCompleted(delegate { loadgame(true); });
        }
    }

    public static void loadgame(bool auto)
    {
        if (auto)
        {
            GameManager.instance.LoadAndSetActiveGameState(4+slot, SaveType.Auto);
        }
        else
        {
            GameManager.instance.LoadAndSetActiveGameState(4 + slot, SaveType.Manual);
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