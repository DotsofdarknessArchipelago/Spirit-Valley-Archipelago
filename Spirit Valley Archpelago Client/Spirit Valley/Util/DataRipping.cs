using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Util
{
    public static class DataRipping
    {
        public static void outputalldata()
        {
            ArchipelagoConsole.LogMessage("SPIRIT DATA");
            OutputSpiritData();
            ArchipelagoConsole.LogMessage("\nQUEST DATA");
            QuestData();
            ArchipelagoConsole.LogMessage("\nITEM DATA");
            ItemData();
            ArchipelagoConsole.LogMessage("\nMOVE DATA");
            moveData();
        }

        public static void OutputSpiritData()
        {
            MonsterManager man = MonsterManager.instance;
            foreach (MonsterBaseStats mon in man.monstersBaseStats)
            {
                //string output = $"Spirit(\"{mon.name}\",{{";
                string output = $"\"{mon.name}\":SpiritData({{";
                foreach (SkillConfiguration s in mon.skills)
                {
                    output = output + $"\"{s.skill.name}\":{s.unlockedAtLevel},";
                }
                if (mon.nextEvolutionBaseStats != null)
                {
                    output = output + $"}},{{\"{mon.nextEvolutionBaseStats.name}\":{mon.evolutionLevelBreakpoint}}},\"{mon.elementalStat.name}\",{{\"HP\":{mon.hp},\"STA\":{mon.stamina},\"ATT\":{mon.attack},\"DEF\":{mon.defence},\"SPE\":{mon.speed}}})";
                }
                else
                {
                    output = output + $"}},None,\"{mon.elementalStat.name}\",{{\"HP\":{mon.hp},\"STA\":{mon.stamina},\"ATT\":{mon.attack},\"DEF\":{mon.defence},\"SPE\":{mon.speed}}})";
                }
                ArchipelagoConsole.LogMessage(output);
            }
        }

        public static void QuestData()
        {
            QuestManager quests = QuestManager.instance;
            for (int i = 0; i < quests.mainQuest.Length; i++)
            {
                //ArchipelagoConsole.LogMessage($"MAIN QUEST #{i}: {quests.mainQuest[i].title.GetLocalizedString()}");
                ArchipelagoConsole.LogMessage($"MAIN QUEST #{i}: {quests.mainQuest[i].id}");
            }
            for (int i = 0; i < quests.sideQuests.Length; i++)
            {
                //ArchipelagoConsole.LogMessage($"SIDE QUEST #{i}: {quests.sideQuests[i].title.GetLocalizedString()}");
                ArchipelagoConsole.LogMessage($"SIDE QUEST #{i}: {quests.sideQuests[i].id}");
            }
        }

        public static void ItemData()
        {
            foreach (Item i in ItemManager.instance.items)
            {
                ArchipelagoConsole.LogMessage($"name: {i.name}\nlocalised name: {i.title.GetLocalizedString()}\nMenu Catergory: {i.menuCategory}\n");
            }
        }

        public static void moveData()
        {
            MonsterManager man = MonsterManager.instance;
            //MonsterSkill[] skillout = new MonsterSkill[0];
            List<string> skillout = new List<string>();
            List<string> pskillout = new List<string>();
            foreach (MonsterBaseStats mon in man.monstersBaseStats)
            {
                foreach (SkillConfiguration s in mon.skills)
                {
                    //ArchipelagoConsole.LogMessage($"SKILL:{s.skill.skillName.GetLocalizedString()}, POWER:{s.skill.power}");
                    if (s.skill.power == 0)
                    {
                        if (!pskillout.Contains(s.skill.name))
                        {
                            pskillout.Add(s.skill.name);
                        }
                    }
                    else
                    {
                        if (!skillout.Contains(s.skill.name))
                        {
                            skillout.Add(s.skill.name);
                        }
                    }
                }
            }

            ArchipelagoConsole.LogMessage("ATTACKING MOVES");
            foreach (String s in skillout)
            {
                ArchipelagoConsole.LogMessage(s);
            }
            ArchipelagoConsole.LogMessage("");
            ArchipelagoConsole.LogMessage("NON ATTACKING MOVES");
            foreach (String s in pskillout)
            {
                ArchipelagoConsole.LogMessage(s);
            }
        }
    }
}
