using Archipelago.MultiClient.Net.Models;
using System.Collections.Generic;

namespace SpiritValleyArchipelagoClient.Archipelago
{
    public class ArchipelagoItem
    {
        public long Id;
        public string ItemName;
        public string PlayerName;
        public long LocationId;
        public bool processed = false;
        public bool putinshop = false;

        public ArchipelagoItem(ItemInfo item) 
        {
            this.Id = item.ItemId;
            this.ItemName = item.ItemName;
            this.PlayerName = item.Player.Name;
            this.LocationId = item.LocationId;
        }

        public ArchipelagoItem()
        {
            this.Id = -1;
            this.ItemName = "";
            this.PlayerName = "";
            this.LocationId = -1;
        }

    }

    public class ArchipelageItemList
    {
        public List<ArchipelagoItem> list = new List<ArchipelagoItem>();
        public string seed = "";
        public int listversion = 1;

        public void add(ItemInfo netitem)
        {
            if (netitem.LocationId <= 0)
            {
                ArchipelagoItem t = new ArchipelagoItem(netitem);
                list.Add(t);
                return;
            }
            for (int i = 0; i < list.Count; i++)
            {
                if (list[i].Id == netitem.ItemId && list[i].PlayerName == netitem.Player.Name && list[i].LocationId == netitem.LocationId)
                {
                    return;
                }
            }
            ArchipelagoItem item = new ArchipelagoItem(netitem);
            list.Add(item);
        }
        public void add(ArchipelagoItem netitem)
        {
            for (int i = 0; i < list.Count; i++)
            {
                if (list[i].Id == netitem.Id && list[i].PlayerName == netitem.PlayerName && list[i].LocationId == netitem.LocationId)
                {
                    list[i].processed = netitem.processed;
                    list[i].putinshop = netitem.putinshop;
                    return;
                }
            }
            list.Add(netitem);
        }

        public void merge(List<ArchipelagoItem> oldlist)
        {
            foreach (ArchipelagoItem item in oldlist)
            {
                if (item.LocationId <= 0) { continue; }
                add(item);
            }

            foreach (ArchipelagoItem i in list)
            {
                if (i.LocationId <= 0) { i.processed = true; }
            }
        }

        public bool hasitem(int flag)
        {
            for (int i = 0; i < list.Count; i++)
            {
                if (list[i].Id == flag)
                {
                    return true;
                }
            }
            return false;
        }

        public string listprint()
        {
            string output = "";
            output += "-------------\n";
            for (int i = 0; i < list.Count; i++)
            {
                output += $"I:{i}";
                output += $"ID:{list[i].Id} PLAYER:{list[i].PlayerName} LOC:{list[i].LocationId}\n";
                output += $"PROCESSED:{list[i].processed} PUTINSHOP:{list[i].putinshop}\n";
            }
            return output;
        }

        public bool needprocessing()
        {
            for (int i = 0; i < list.Count; i++)
            {
                if (!list[i].processed) { return true; }
            }
            return false;
        }
    }
}
