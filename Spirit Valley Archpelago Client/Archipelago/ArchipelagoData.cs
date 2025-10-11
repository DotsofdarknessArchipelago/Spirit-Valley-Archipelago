using Newtonsoft.Json;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System.Collections.Generic;
using System.Linq;
using System.Xml.Linq;

namespace SpiritValleyArchipelagoClient.Archipelago;

public class ArchipelagoData
{
    public string Uri;
    public string SlotName;
    public string Password;
    public int Index;

    public List<long> CheckedLocations;

    /// <summary>
    /// seed for this archipelago data. Can be used when loading a file to verify the session the player is trying to
    /// load is valid to the room it's connecting to.
    /// </summary>
    private string seed;

    public Dictionary<string, object> slotData;

    public List<Spirit> spiritdata = new List<Spirit>();
    public List<Trainer> trainerdata = new List<Trainer>();
    public Dictionary<string, string[]> waterdata = new Dictionary<string, string[]>();
    public Dictionary<string, string[]> grassdata = new Dictionary<string, string[]>();
    public Dictionary<string, Dictionary<string, int>> typedata = new Dictionary<string, Dictionary<string, int>>();

    public Dictionary<string, string> mapdata = new Dictionary<string, string>();

    public bool NeedSlotData => slotData == null;

    public ArchipelagoData()
    {
        Uri = "localhost";
        SlotName = "Player1";
        CheckedLocations = new();
    }

    public ArchipelagoData(string uri, string slotName, string password)
    {
        Uri = uri;
        SlotName = slotName;
        Password = password;
        CheckedLocations = new();
    }

    /// <summary>
    /// assigns the slot data and seed to our data handler. any necessary setup using this data can be done here.
    /// </summary>
    /// <param name="roomSlotData">slot data of your slot from the room</param>
    /// <param name="roomSeed">seed name of this session</param>
    public void SetupSession(Dictionary<string, object> roomSlotData, string roomSeed)
    {
        slotData = roomSlotData;
        seed = roomSeed;
    }

    /// <summary>
    /// returns the object as a json string to be written to a file which you can then load
    /// </summary>
    /// <returns></returns>
    public override string ToString()
    {
        return JsonConvert.SerializeObject(this);
    }

    public MonsterBaseStats[] grassspawn(string area)
    {
        string[] data = ArchipelagoClient.ServerData.grassdata[area];
        List<MonsterBaseStats> mons = new List<MonsterBaseStats>();
        foreach (string m in data)
        {
            mons.Add(MonsterManager.instance.GetBaseStatsByName(namehelper2(m)));
        }
        return mons.ToArray();
    }

    public MonsterBaseStats[] waterspawn(string area)
    {
        string[] water_location_list = ["Trail10", "Trail11", "Trail12", "Trail13", "Trail14", "ColdHarbor", "Trail16", "AbandonedMine", "Trail17", "Trail18", "Trail21"];
        if (!water_location_list.Contains(area)) { return null; }
        string[] data = ArchipelagoClient.ServerData.waterdata[area];
        List<MonsterBaseStats> mons = new List<MonsterBaseStats>();
        foreach (string m in data)
        {
                mons.Add(MonsterManager.instance.GetBaseStatsByName(namehelper2(m)));
        }
        return mons.ToArray();
    }

    public MonsterBaseStats[] mapspawn(MapLocationID id)
    {
        MonsterBaseStats[] waterdata = waterspawn(HelperSpirits.mapidTostring(id));
        if (waterdata == null && id != MapLocationID.Trail22) { return grassspawn(HelperSpirits.mapidTostring(id)); }
        MonsterBaseStats[] grassdata = grassspawn(HelperSpirits.mapidTostring(id));
        List<MonsterBaseStats> mapdata = new List<MonsterBaseStats>();

        foreach (var g in grassdata)
        {
            mapdata.Add(g);
        }
        foreach (var w in waterdata)
        {
            bool add = true;
            foreach (var m in mapdata)
            {
                if (m.name == w.name)
                {
                    add = false;
                    break;
                }
            }
            if (add)
            {
                mapdata.Add(w);
            }
        }

        if (id == MapLocationID.Trail16)
        {
            MonsterBaseStats[] cavedata = grassspawn("Trail16_Cave");
            foreach (var w in cavedata)
            {
                bool add = true;
                foreach (var m in mapdata)
                {
                    if (m.name == w.name)
                    {
                        add = false;
                        break;
                    }
                }
                if (add)
                {
                    mapdata.Add(w);
                }
            }
        }
        else if (id == MapLocationID.Trail22)
        {
            MonsterBaseStats[] cavedata = grassspawn("Trail22_Cave");
            foreach (var w in cavedata)
            {
                bool add = true;
                foreach (var m in mapdata)
                {
                    if (m.name == w.name)
                    {
                        add = false;
                        break;
                    }
                }
                if (add)
                {
                    mapdata.Add(w);
                }
            }
        }

        return mapdata.ToArray();
    }

    public MonsterTeamMemberBlueprint[] trainerteam(string guid)
    {
        List<MonsterTeamMemberBlueprint> team = new List<MonsterTeamMemberBlueprint>();

        foreach (Trainer t in trainerdata)
        {
            if (t.GUID == guid)
            {
                foreach (var i in t.PARTY)
                {
                    MonsterTeamMemberBlueprint mon = new MonsterTeamMemberBlueprint();
                    mon.monster = MonsterManager.instance.GetBaseStatsByName(namehelper2(i.spirit));
                    
                    mon.level = i.lv;
                    mon.isRare = i.shiny==1;
                    mon.isActiveSkillCountUnlimited = false;
                    team.Add(mon);
                }
                break;
            }
        }
        return team.ToArray();
    }

    public MonsterBaseStats getspirit(string name)
    {
        string dataname = namehelper(name);

        MonsterBaseStats spirit = null;
        foreach (MonsterBaseStats monsterBaseStats in MonsterManager.instance.monstersBaseStats)
        {
            if (monsterBaseStats.name == name)
            {
                spirit = monsterBaseStats;
                break;
            }
        }
        if (spirit == null) { ArchipelagoConsole.LogMessage($"ERROR OVERRIDING {name}'s STATS NO SPIRIT FOUND IN GAME"); }

        Spirit o = null;
        foreach (Spirit s in spiritdata)
        {
            if (s.name == dataname)
            {
                o = s;
                break;
            }
        }
        if (o == null) { ArchipelagoConsole.LogMessage($"ERROR OVERRIDING {dataname}'s STATS NO SPIRIT FOUND IN SLOTDATA"); }

        spirit.hp = o.stats["HP"];
        spirit.stamina = o.stats["STA"];
        spirit.attack = o.stats["ATT"];
        spirit.defence = o.stats["DEF"];
        spirit.speed = o.stats["SPE"];

        switch (o.type)
        {
            case "Furry":
                spirit.elementalStat = MonsterManager.instance.GetElementalStatByType(ElementalType.Furry);
                break;
            case "Lust":
                spirit.elementalStat = MonsterManager.instance.GetElementalStatByType(ElementalType.Lust);
                break;
            case "Plant":
                spirit.elementalStat = MonsterManager.instance.GetElementalStatByType(ElementalType.Plant);
                break;
            case "Demon":
                spirit.elementalStat = MonsterManager.instance.GetElementalStatByType(ElementalType.Demon);
                break;
            case "Scalie":
                spirit.elementalStat = MonsterManager.instance.GetElementalStatByType(ElementalType.Scalie);
                break;
            case "Slime":
                spirit.elementalStat = MonsterManager.instance.GetElementalStatByType(ElementalType.Slime);
                break;
            case "Oppai":
                spirit.elementalStat = MonsterManager.instance.GetElementalStatByType(ElementalType.Oppai);
                break;
            case "Avian":
                spirit.elementalStat = MonsterManager.instance.GetElementalStatByType(ElementalType.Avian);
                break;
            case "Aquatic":
                spirit.elementalStat = MonsterManager.instance.GetElementalStatByType(ElementalType.Aquatic);
                break;
            default:
                break;
        }

        if (o.evolution != null)
        {
            foreach (var i in o.evolution)
            {
                spirit.evolutionLevelBreakpoint = i.Value;
                foreach (MonsterBaseStats monsterBaseStats in MonsterManager.instance.monstersBaseStats)
                {
                    if (monsterBaseStats.name == namehelper(i.Key))
                    {
                        spirit.nextEvolutionBaseStats = monsterBaseStats;
                        break;
                    }
                }

            }
        }

        List<SkillConfiguration> mov = new List<SkillConfiguration>();
        foreach (var m in o.moves)
        {
            SkillConfiguration mo = new SkillConfiguration();
            mo.skill = HelperSpirits.skilllist[m.Key];
            mo.unlockedAtLevel = m.Value;
            mov.Add(mo);
        }
        spirit.skills = mov.ToArray();

        return spirit;
    }

    public void overidebasestats()
    {
        for (int i = 0; i < MonsterManager.instance.monstersBaseStats.Count(); i++)
        {
            MonsterManager.instance.monstersBaseStats[i] = ArchipelagoClient.ServerData.getspirit(MonsterManager.instance.monstersBaseStats[i].name);
        }
    }

    public void overidetypes()
    {
        for (int i = 0; i < MonsterManager.instance.elementalStats.Count() ; i++)
        {
            List<ElementalStat> inc = new List<ElementalStat>();
            List<ElementalStat> dec = new List<ElementalStat>();
            foreach (var s in typedata[stattostring(MonsterManager.instance.elementalStats[i].type)])
            {
                if (s.Value == 1)
                {
                    foreach (var t in MonsterManager.instance.elementalStats)
                    {
                        if (t.type == stringtostat(s.Key))
                        {
                            inc.Add(t);
                        }
                    }
                }
                else if (s.Value == -1)
                {
                    foreach (var t in MonsterManager.instance.elementalStats)
                    {
                        if (t.type == stringtostat(s.Key))
                        {
                            dec.Add(t);
                        }
                    }
                }
            }
            MonsterManager.instance.elementalStats[i].decreasedDamageTo = dec.ToArray();
            MonsterManager.instance.elementalStats[i].increasedDamageTo = inc.ToArray();
        }
    }

    public static string namehelper(string name)
    {
        if (name == "Centiboob_Normal")
        {
            return "Centiboob";
        }
        else if (name == "Centiboob")
        {
            return "Centiboob_Boss";
        }
        else if (name == "Valkyrie_Normal")
        {
            return "Valkyrie";
        }
        else if (name == "Valkyrie")
        {
            return "Valkyrie_Boss";
        }
        else
        {
            return name;
        }
    }

    public static string namehelper2(string name)
    {
        if (name == "Centiboob")
        {
            return "Centiboob_Normal";
        }
        else if (name == "Centiboob_Boss")
        {
            return "Centiboob";
        }
        else if (name == "Valkyrie")
        {
            return "Valkyrie_Normal";
        }
        else if (name == "Valkyrie_Boss")
        {
            return "Valkyrie";
        }
        else
        {
            return name;
        }
    }

    public static string stattostring(ElementalType type)
    {
        switch (type)
        {
            case ElementalType.Slime:
                return "Slime";
            case ElementalType.Furry:
                return "Furry";
            case ElementalType.Plant:
                return "Plant";
            case ElementalType.Scalie:
                return "Scalie";
            case ElementalType.Lust:
                return "Lust";
            case ElementalType.Oppai:
                return "Oppai";
            case ElementalType.Demon:
                return "Demon";
            case ElementalType.Avian:
                return "Avian";
            case ElementalType.Aquatic:
                return "Aquatic";
            default:
                break;
        }
        return null;
    }

    public static ElementalType stringtostat(string type)
    {
        switch (type)
        {
            case "Slime":
                return ElementalType.Slime;
            case "Furry":
                return ElementalType.Furry;
            case "Plant":
                return ElementalType.Plant;
            case "Scalie":
                return ElementalType.Scalie;
            case "Lust":
                return ElementalType.Lust;
            case "Oppai":
                return ElementalType.Oppai;
            case "Demon":
                return ElementalType.Demon;
            case "Avian":
                return ElementalType.Avian;
            case "Aquatic":
                return ElementalType.Aquatic;
            default:
                break;
        }
        return ElementalType.Normal;
    }

    public static string getquestspirit(string questid)
    {
        switch (questid)
        {
            case "main_quest_19_total_domination":
                return namehelper2(ArchipelagoClient.ServerData.slotData["MAIN_QUEST_TOTAL_DOMINATION"].ToString());
            case "side_quest_perky_petunia":
                return namehelper2(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_PERKY_PETUNIA_SPIRIT"].ToString());
            case "side_quest_slithering_menace":
                return namehelper2(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_SLITHERING_MENACE_SPIRIT"].ToString());
            case "side_quest_deadly_waters":
                return namehelper2(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_DEADLY_WATERS_SPIRIT"].ToString());
            case "side_quest_starry_eyed_surprise":
                return namehelper2(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_STARRY_EYED_SURPRISE_SPIRIT"].ToString());
            case "side_quest_arctic_menace":
                return namehelper2(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_ARCTIC_MENACE_SPIRIT"].ToString());
            case "side_quest_hunt_for_the_centiboob_part1":
                return namehelper2(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_CENTIBOOB_1_SPIRIT"].ToString());
            case "side_quest_hunt_for_the_centiboob_part2":
                return namehelper2(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_CENTIBOOB_2_SPIRIT"].ToString());
            case "side_quest_hunt_for_the_centiboob_part3":
                return namehelper2(ArchipelagoClient.ServerData.slotData["SIDE_QUEST_CENTIBOOB_3_SPIRIT"].ToString());
            default:
                ArchipelagoConsole.LogMessage($"ERROR IN ArchipelagoData/getsidequestspirit WITH QUESTID {questid}");
                return null;
        }
    }
}