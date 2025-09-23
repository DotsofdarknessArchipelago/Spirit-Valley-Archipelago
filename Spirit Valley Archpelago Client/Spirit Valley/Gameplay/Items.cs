using HarmonyLib;
using SpiritValleyArchipelagoClient.Archipelago;
using SpiritValleyArchipelagoClient.Spirit_Valley.Util;
using System;

namespace SpiritValleyArchipelagoClient.Spirit_Valley.Gameplay
{
    [HarmonyPatch]
    public class Items
    {

        [HarmonyPatch(typeof(ChestMapItem), "Interact")]
        [HarmonyPrefix]
        public static void chestopen(ChestMapItem __instance)
        {
            __instance.itemBundles = HelperItems.centbundle();

            int chestintstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Chest_Start"]);
            switch (__instance.guid)
            {
                case "b9f52b5c-fd8d-43b8-9f5c-85a5b3686a6a": //"Oakwood Village: Chest In Uncles House"
                    ArchipelagoClient.sendloc(chestintstart + 1);
                    break;
                case "33bdf3c7-7b56-4578-b038-3d9f10a7c978": //"Trail 01: Chest Near Piper"
                    ArchipelagoClient.sendloc(chestintstart + 2);
                    break;
                case "33a2ce7f-9568-4435-ac78-a4e3660948fe": //"Trail 01: Chest North of Piper"
                    ArchipelagoClient.sendloc(chestintstart + 3);
                    break;
                case "3019ab50-bd67-4887-9865-cdc2fa604f55": //"Trail 01: Potion From Jane"
                    ArchipelagoClient.sendloc(chestintstart + 4);
                    break;
                case "7c0b0138-7aa6-49ea-a1eb-015e33731f51": //"Evergreen Outpost: Chest Near Medic"
                    ArchipelagoClient.sendloc(chestintstart + 5);
                    break;
                case "49a27369-563a-444d-9112-45ff04198979": //"Evergreen Outpost: Chest Above Grass Patch"
                    ArchipelagoClient.sendloc(chestintstart + 6);
                    break;
                case "576ccf5e-ee72-49c4-930c-a3e4acf6c1b7": //"Evergreen Outpost: Chest Behind Pushable Bolder"
                    ArchipelagoClient.sendloc(chestintstart + 7);
                    break;
                case "e129287a-733f-4761-b12d-d4f6265d3e38": //"Trail 02: Chest Near Billy"
                    ArchipelagoClient.sendloc(chestintstart + 8);
                    break;
                case "d36a4079-4dc5-4cbf-92ec-fbb4e5e5a674": //"Trail 02: Chest in Hidden Path Next to Macy"
                    ArchipelagoClient.sendloc(chestintstart + 9);
                    break;
                case "a6673de2-6794-43ee-b1c3-cc7e7468c7f9": //"Trail 02: Chest East of Macy"
                    ArchipelagoClient.sendloc(chestintstart + 10);
                    break;
                case "5c0b8d8e-e4fe-4505-871c-d2c3964b75b5": //"Trail 02: Chest Near Skyler"
                    ArchipelagoClient.sendloc(chestintstart + 11);
                    break;
                case "e5139fe4-aae0-4c8c-9591-94cd9405a8cb": //"Greensvale: Chest South of Waystone"
                    ArchipelagoClient.sendloc(chestintstart + 12);
                    break;
                case "64386704-ba0e-461c-ad5d-36327d902e9b": //"Greensvale: Chest in Red House"
                    ArchipelagoClient.sendloc(chestintstart + 13);
                    break;
                case "23d8f4fb-7284-483c-a145-ed500c426339": //"Greensvale: Chest Next To XXX Shop"
                    ArchipelagoClient.sendloc(chestintstart + 14);
                    break;
                case "c0fa6732-bee2-47c2-9853-1ffa3e6a98e0": //"Greensvale: Chest Behind Pushable Bolder In the North"
                    ArchipelagoClient.sendloc(chestintstart + 15);
                    break;
                case "e21093f1-32a4-4e08-ba6c-7090002ccdd9": //"Milly's Farm: Chest Behind Pushable Bolder"
                    ArchipelagoClient.sendloc(chestintstart + 16);
                    break;
                case "44683738-a42b-4c9c-b200-e4742152e790": //"Trail 03: Chest North of Miriam"
                    ArchipelagoClient.sendloc(chestintstart + 17);
                    break;
                case "4d2efd45-b043-46de-9a27-e75da0caec9f": //"Trail 03: Chest South of Miriam"
                    ArchipelagoClient.sendloc(chestintstart + 18);
                    break;
                case "0ab8b8d9-28b6-4bfe-9a4c-188297627ed3": //"Trail 03: Chest Chest Before Evergreen Caverns Entrance"
                    ArchipelagoClient.sendloc(chestintstart + 19);
                    break;
                case "0b29ff75-0e24-4378-9053-db03ca077e79": //"Evergreen Caverns: Chest West of Stu"
                    ArchipelagoClient.sendloc(chestintstart + 20);
                    break;
                case "9396ff11-ac75-4b7c-8999-286ff2c84f75": //"Evergreen Caverns: Chest South of Nicole"
                    ArchipelagoClient.sendloc(chestintstart + 21);
                    break;
                case "f4de6097-3346-4921-849f-b099ee698aa2": //"Evergreen Caverns: Chest 1 Behind Rawry"
                    ArchipelagoClient.sendloc(chestintstart + 22);
                    break;
                case "42de807c-00fe-4570-91ee-8ef1a1241777": //"Evergreen Caverns: Chest 2 Behind Rawry"
                    ArchipelagoClient.sendloc(chestintstart + 23);
                    break;
                case "0471dbe1-259d-4067-a0a3-ef54917278ad": //"Trail 04: Chest West of Evergreen Caverns Entrance"
                    ArchipelagoClient.sendloc(chestintstart + 24);
                    break;
                case "32d13c92-6c2f-4386-8a6c-e3d6849fbcf8": //"Trail 04: Chest West Side of Map"
                    ArchipelagoClient.sendloc(chestintstart + 25);
                    break;
                case "19a41d7a-cd3b-4e23-b71a-67f28af913e1": //"Trail 04: Chest Near Waystone"
                    ArchipelagoClient.sendloc(chestintstart + 26);
                    break;
                case "84c4ca3f-c75c-404d-a348-fb7969103347": //"Ancient Temple 1: Chest Near 3rd Crimson Cloak"
                    ArchipelagoClient.sendloc(chestintstart + 27);
                    break;
                case "d62d3ed0-99f1-4c84-9c89-cdee2fbcda22": //"Ancient Temple 1: Chest in Path Loop"
                    ArchipelagoClient.sendloc(chestintstart + 28);
                    break;
                case "36739a3e-47ec-4785-a0e7-6c71bc38f964": //"Ancient Temple 1: Chest Near 6th Crimson Cloak"
                    ArchipelagoClient.sendloc(chestintstart + 29);
                    break;
                case "0b46cb8f-5eb2-4a50-8586-07f94fa07c80": //"Ancient Temple 2: Chest West Side of Room"
                    ArchipelagoClient.sendloc(chestintstart + 30);
                    break;
                case "c6b0df02-8d68-414d-9a25-8b9dd4c854f6": //"Ancient Temple 2: Chest East side of Room"
                    ArchipelagoClient.sendloc(chestintstart + 31);
                    break;
                case "920a56c1-5bda-41ae-8935-c29d33c2c6f1": //"Ancient Temple 2: Chest in Middle Area of Room"
                    ArchipelagoClient.sendloc(chestintstart + 32);
                    break;
                case "4c8940eb-e49c-40dc-8a26-d4f60f4bc9c2": //"Trail 05: Chest Near Evergreen Outpost Entrance"
                    ArchipelagoClient.sendloc(chestintstart + 33);
                    break;
                case "816a4058-20a0-4996-9648-145ad9597850": //"Trail 05: Chest East of Mila"
                    ArchipelagoClient.sendloc(chestintstart + 34);
                    break;
                case "653e6c73-99ab-4b7b-93b3-6b94301378db": //"Trail 05: Chest West of Roy"
                    ArchipelagoClient.sendloc(chestintstart + 35);
                    break;
                case "854bb842-23cc-4f46-ae38-7be9f17a2a4b": //"Trail 05: Chest East of Lulu"
                    ArchipelagoClient.sendloc(chestintstart + 36);
                    break;
                case "ba7ef7c4-2cbe-48ef-b777-c9c279d3a8f3": //"Sandy Tunnels: Chest South of Chad"
                    ArchipelagoClient.sendloc(chestintstart + 37);
                    break;
                case "323a990d-8933-4c80-839b-1c40a3eeaaf9": //"Sandy Tunnels: Chest North of Chad"
                    ArchipelagoClient.sendloc(chestintstart + 38);
                    break;
                case "0cceeb16-b7e3-4440-916f-c08d6662a535": //"Sandy Tunnels: Chest West of Destiny"
                    ArchipelagoClient.sendloc(chestintstart + 39);
                    break;
                case "c135099c-4730-4f32-a9c8-1c79ac82945b": //"Sandy Tunnels: Healing Potion From Jessica"
                    ArchipelagoClient.sendloc(chestintstart + 40);
                    break;
                case "002d680f-44a9-4e90-8827-c57cc8f69e65": //"Trail 06: Chest West of Sandy Tunnels Entrance"
                    ArchipelagoClient.sendloc(chestintstart + 41);
                    break;
                case "be999696-f2d3-4379-adf3-7d16693a5e5f": //"Trail 06: Chest East of Kelsie"
                    ArchipelagoClient.sendloc(chestintstart + 42);
                    break;
                case "2c975ba2-b3a3-4cea-adb9-b66ddf3c42fc": //"Trail 06: Chest South of Hayden"
                    ArchipelagoClient.sendloc(chestintstart + 43);
                    break;
                case "303be291-de84-4fae-b055-822959b7cc0a": //"Dairy Farm: Chest North of Waystone"
                    ArchipelagoClient.sendloc(chestintstart + 44);
                    break;
                case "d27f5dea-d45b-4cb8-9df8-67538b55548d": //"Dairy Farm: Chest South of Waystone"
                    ArchipelagoClient.sendloc(chestintstart + 45);
                    break;
                case "f54b3d20-a63e-4f8b-ac30-4c6d8875dd61": //"Dairy Farm: Chest Next to House"
                    ArchipelagoClient.sendloc(chestintstart + 46);
                    break;
                case "d6f46d56-9a4b-4225-a4ca-a01067840674": //"Dairy Farm: Chest North-East of House"
                    ArchipelagoClient.sendloc(chestintstart + 47);
                    break;
                case "38122e15-ff3c-4777-be9f-53b2e7c8c73c": //"Trail 07: Chest Near Dairy Farm Entrance"
                    ArchipelagoClient.sendloc(chestintstart + 48);
                    break;
                case "add11e84-b206-48ba-b2dd-2ff56262eabc": //"Trail 07: Chest North of Bella"
                    ArchipelagoClient.sendloc(chestintstart + 49);
                    break;
                case "d834c481-c66d-4f5a-a3f3-376b6239c4a0": //"Trail 07: Chest South of Bella"
                    ArchipelagoClient.sendloc(chestintstart + 50);
                    break;
                case "c22c51bc-6eaf-40ed-9f4b-62a6e1268a88": //"Trail 07: Chest South of Dakota"
                    ArchipelagoClient.sendloc(chestintstart + 51);
                    break;
                case "e4d4ae3a-d411-488f-819d-a9624148a5ed": //"Tumbleweed Town: Chest South of Town"
                    ArchipelagoClient.sendloc(chestintstart + 52);
                    break;
                case "b0973844-878a-47e9-8ab2-bea68625ace0": //"Tumbleweed Town: Chest North-West of Town"
                    ArchipelagoClient.sendloc(chestintstart + 53);
                    break;
                case "71627b20-173d-4c34-8242-82806333e7b5": //"Tumbleweed Town: Chest in House Next to Shop"
                    ArchipelagoClient.sendloc(chestintstart + 54);
                    break;
                case "24c5ce52-ec0f-492f-9447-401df4f6c100": //"Trail 08: Chest West of Tumbleweed Town Entrance"
                    ArchipelagoClient.sendloc(chestintstart + 55);
                    break;
                case "baea8603-5e88-4935-95a9-ef10c47e8bad": //"Trail 08: Chest South of Marisa"
                    ArchipelagoClient.sendloc(chestintstart + 56);
                    break;
                case "54012631-5481-4e97-85b3-835e6f2128ab": //"Trail 08: Chest Near Dusty Grotto Entrance"
                    ArchipelagoClient.sendloc(chestintstart + 57);
                    break;
                case "25d61715-32da-4887-a04d-381b74e7fd70": //"Dusty Grotto: Chest Near Crystal"
                    ArchipelagoClient.sendloc(chestintstart + 58);
                    break;
                case "b859600e-fad1-486c-9879-5d0782077bc3": //"Dusty Grotto: Chest West of Skye"
                    ArchipelagoClient.sendloc(chestintstart + 59);
                    break;
                case "33323326-8c5c-448e-acac-2f50cba62286": //"Old Masters Hut: Chest North of House"
                    ArchipelagoClient.sendloc(chestintstart + 60);
                    break;
                case "7410e48c-cf0e-42da-9760-e0d756ec5856": //"Old Masters Hut: Chest Next to House"
                    ArchipelagoClient.sendloc(chestintstart + 61);
                    break;
                case "bbef9238-1d46-4d89-8f42-3f086d169e35": //"Old Masters Hut: Chest in House"
                    ArchipelagoClient.sendloc(chestintstart + 62);
                    break;
                case "0feafe23-7fc6-4175-b8b1-90d2323095ce": //"Old Masters Hut: Chest in House Basement"
                    ArchipelagoClient.sendloc(chestintstart + 63);
                    break;
                case "52ca3362-6a85-4eba-9a4e-64d29dca413e": //"Cave of Torment: Chest East Side of Cave"
                    ArchipelagoClient.sendloc(chestintstart + 64);
                    break;
                case "f6f9100f-d007-4407-8273-bb8ac9fc98a7": //"Cave of Torment: Chest North Side of Cave"
                    ArchipelagoClient.sendloc(chestintstart + 65);
                    break;
                case "e44bc915-f705-4b68-8a9d-a3527264dad8": //"Cave of Torment: Chest West Side of Cave"
                    ArchipelagoClient.sendloc(chestintstart + 66);
                    break;
                case "369c6ee5-6b6a-4433-ae92-e5f4b9e911e1": //"Trail 09: Chest near Clementine"
                    ArchipelagoClient.sendloc(chestintstart + 67);
                    break;
                case "1457c1a2-8177-4571-b438-f53cb9c6cd34": //"Trail 09: Chest North of Mike"
                    ArchipelagoClient.sendloc(chestintstart + 68);
                    break;
                case "8af95e31-a76f-4004-9ed4-d208fb94efb3": //"Trail 09: Chest Near Stone Temple Back Entrance Ledge"
                    ArchipelagoClient.sendloc(chestintstart + 69);
                    break;
                case "515e573f-cf67-473f-a241-7177098013c1": //"Stone Temple 1: Chest Near Trail 09 Entrence"
                    ArchipelagoClient.sendloc(chestintstart + 70);
                    break;
                case "1f27c663-1dce-47e0-821c-8fd1aae55a46": //"Stone Temple 1: Chest Near 6th Crimson Cloak"
                    ArchipelagoClient.sendloc(chestintstart + 71);
                    break;
                case "57db7ff2-69b0-4c98-a81b-79b30eb2dd88": //"Stone Temple 1: Chest Near Stone Temple 2 Entrance"
                    ArchipelagoClient.sendloc(chestintstart + 72);
                    break;
                case "20af0b9d-a48e-4dff-995e-53758e7d61f3": //"Crash Site: Chest East of Athena"
                    ArchipelagoClient.sendloc(chestintstart + 73);
                    break;
                case "c6f2ad98-a787-4805-9c9b-fca34bd7dee3": //"Crash Site: Chest West of Janet"
                    ArchipelagoClient.sendloc(chestintstart + 74);
                    break;
                case "2300e642-581b-43e8-bc83-c78a246fe948": //"Crash Site: Chest South of Janet"
                    ArchipelagoClient.sendloc(chestintstart + 75);
                    break;
                case "cbbdd4da-69d4-41c2-9165-ea07e647a369": //"Trail 10: Chest West of Crash Site Entrance"
                    ArchipelagoClient.sendloc(chestintstart + 76);
                    break;
                case "545492fc-2eea-4a81-b1db-12825748f4a0": //"Trail 10: Chest Near Eve"
                    ArchipelagoClient.sendloc(chestintstart + 77);
                    break;
                case "5c21066a-081c-4c75-8a0f-1694ccddbe1f": //"Trail 10: Chest South of Bailee"
                    ArchipelagoClient.sendloc(chestintstart + 78);
                    break;
                case "9b0fd14d-0aec-4790-900f-553f98af0eb1": //"Coconut Village: Chest North-East in Village"
                    ArchipelagoClient.sendloc(chestintstart + 79);
                    break;
                case "56fa7c21-327e-4f5f-8fe2-1b1d35da3dc9": //"Coconut Village: Chest East of Village"
                    ArchipelagoClient.sendloc(chestintstart + 80);
                    break;
                case "8a4cdd76-b0a6-4256-a9d4-5797167f7ae5": //"Coconut Village: Chest in House in the South-East"
                    ArchipelagoClient.sendloc(chestintstart + 81);
                    break;
                case "e68357b4-2017-4962-9935-febbb8afa19e": //"Coconut Village: Chest in Temple"
                    ArchipelagoClient.sendloc(chestintstart + 82);
                    break;
                case "11a5f5c0-f303-469e-96f0-d0df45d2e631": //"Coconut Village: Chest In Temple After Locked Door"
                    ArchipelagoClient.sendloc(chestintstart + 83);
                    break;
                case "7e5e1b32-a395-449e-8524-85100357f829": //"Trail 11: Chest Near Alice"
                    ArchipelagoClient.sendloc(chestintstart + 84);
                    break;
                case "fc2ae356-2928-4f20-b00a-882f8498ebfc": //"Trail 11: Chest Near Pier"
                    ArchipelagoClient.sendloc(chestintstart + 85);
                    break;
                case "1eb894db-663f-4ef8-8bec-9eff702f539b": //"Trail 11: Chest East of Emilia"
                    ArchipelagoClient.sendloc(chestintstart + 86);
                    break;
                case "f54d4a60-9550-4505-962d-917242c1853e": //"Trail 11: Chest South of Sydney"
                    ArchipelagoClient.sendloc(chestintstart + 87);
                    break;
                case "e2598159-fb05-4e8f-88a4-cbb55d12546f": //"Trail 12: Chest North of Sophie"
                    ArchipelagoClient.sendloc(chestintstart + 88);
                    break;
                case "df5ab9f9-17b1-4629-a683-8e1c6ff122e4": //"Trail 12: Chest North of Ciara"
                    ArchipelagoClient.sendloc(chestintstart + 89);
                    break;
                case "ed0b2740-17bd-49bb-b431-8ee30ffee485": //"Fishing Hut: Chest North-West on the Beach"
                    ArchipelagoClient.sendloc(chestintstart + 90);
                    break;
                case "570c6d8b-0f44-4611-8c16-676ea4f2dcf7": //"Fishing Hut: Chest Next to House"
                    ArchipelagoClient.sendloc(chestintstart + 91);
                    break;
                case "38a94edd-1946-4076-8ddf-c9e9bf6b3358": //"Fishing Hut: Chest East on the Beach"
                    ArchipelagoClient.sendloc(chestintstart + 92);
                    break;
                case "8fa902d2-fc53-4502-b2a4-edd4c2fcdbba": //"Fishing Hut: Chest Eastern Side of Map"
                    ArchipelagoClient.sendloc(chestintstart + 93);
                    break;
                case "2432ca26-daf4-4f91-b0f5-65094ef2f236": //"Trail 13: Chest South-West of 1st Cultist"
                    ArchipelagoClient.sendloc(chestintstart + 94);
                    break;
                case "e349a432-ea25-48fa-b78a-4f7e24a1a21e": //"Trail 13: Chest North of 1st Cultist"
                    ArchipelagoClient.sendloc(chestintstart + 95);
                    break;
                case "5fb24dfe-bb8f-4e3d-b5d2-f18331df4040": //"Trail 14: Chest North-West of 1st Cultist"
                    ArchipelagoClient.sendloc(chestintstart + 96);
                    break;
                case "4e89c1b8-d75b-4dd1-b333-c091f0683bd8": //"Trail 14: Chest East of 1st Cultist"
                    ArchipelagoClient.sendloc(chestintstart + 97);
                    break;
                case "7b172b42-b00c-4e6b-a6d2-3176cac758d3": //"Trail 14: Chest East of Waystone"
                    ArchipelagoClient.sendloc(chestintstart + 98);
                    break;
                case "be99f6ef-4289-45b9-b8ca-c6432f64c982": //"Island Cave 1: Chest North-West After 1st Cultist"
                    ArchipelagoClient.sendloc(chestintstart + 99);
                    break;
                case "1ffad415-a599-4752-a847-c093e51cbcbe": //"Island Cave 1: Chest East After 2st Cultist"
                    ArchipelagoClient.sendloc(chestintstart + 100);
                    break;
                case "78734a81-9888-4e7f-97a8-1b68f590ef43": //"Island Cave 1: Chest West After 2nd Cultist"
                    ArchipelagoClient.sendloc(chestintstart + 101);
                    break;
                case "9ad68fef-4f77-4490-9ccd-5d779083bddb": //"Island Cave 1: Chest Near 3rd Cultist"
                    ArchipelagoClient.sendloc(chestintstart + 102);
                    break;
                case "4f0e46a1-ad29-4472-a6a9-24120c07535c": //"Cold Harbour: Chest North-East of Waystone"
                    ArchipelagoClient.sendloc(chestintstart + 103);
                    break;
                case "4b5bceb4-7cff-4419-8116-cf5dd4e6dcb8": //"Cold Harbour: Chest East of Iris"
                    ArchipelagoClient.sendloc(chestintstart + 104);
                    break;
                case "dd42f2b7-841c-4726-a597-a8e197e384f4": //"Frostville: Chest North of Waystone"
                    ArchipelagoClient.sendloc(chestintstart + 105);
                    break;
                case "d4f07026-13b3-4b49-ae53-57764bed39a6": //"Frostville: Chest South of Waystone"
                    ArchipelagoClient.sendloc(chestintstart + 106);
                    break;
                case "4c13b886-9a90-4896-b235-d013e69c60e6": //"Frostville: Chest West of Town"
                    ArchipelagoClient.sendloc(chestintstart + 107);
                    break;
                case "18ec8ed3-304e-47a1-8311-b53e9e76ceee": //"Trail 15: Chest South of Frostville Entrence"
                    ArchipelagoClient.sendloc(chestintstart + 108);
                    break;
                case "c8875e05-570c-4b7c-a3a6-3939a80e373d": //"Trail 15: Chest West of Mia"
                    ArchipelagoClient.sendloc(chestintstart + 109);
                    break;
                case "334ebd4f-e47e-494a-9010-f0e431e93cd3": //"Trail 15: Chest South-West of Olga"
                    ArchipelagoClient.sendloc(chestintstart + 110);
                    break;
                case "60a5df17-adb0-46ba-ae67-e4df1e45718f": //"Trail 16: Chest Near Northern Trail 15 Entrence"
                    ArchipelagoClient.sendloc(chestintstart + 111);
                    break;
                case "f55efa41-a0da-4307-aa3b-584c1238ddaf": //"Trail 16: Chest North of Karin"
                    ArchipelagoClient.sendloc(chestintstart + 112);
                    break;
                case "97595abc-e511-4733-827e-e6180c716210": //"Trail 16: Chest North-West of Karin"
                    ArchipelagoClient.sendloc(chestintstart + 113);
                    break;
                case "e89b33c2-ef03-4abd-b216-81df8d7e0f65": //"Trail 16: Chest East of Dahlia"
                    ArchipelagoClient.sendloc(chestintstart + 114);
                    break;
                case "46cf0856-3d1c-440b-a065-b357d399964b": //"Abandoned Mine: Chest North of Trail 16 Entrence"
                    ArchipelagoClient.sendloc(chestintstart + 115);
                    break;
                case "575941ce-96f2-477f-b0bc-facec059184c": //"Abandoned Mine: Chest South-West of House"
                    ArchipelagoClient.sendloc(chestintstart + 116);
                    break;
                case "db51e404-218c-4288-8860-b5ecf2b25059": //"Trail 17: Chest North of Clara"
                    ArchipelagoClient.sendloc(chestintstart + 117);
                    break;
                case "2d01eaea-aecd-4b90-9029-6498f03c3558": //"Trail 17: Chest South-East of Liv"
                    ArchipelagoClient.sendloc(chestintstart + 118);
                    break;
                case "cef39514-d07c-4531-8fa5-52ebd56df4c9": //"Trail 17: Chest North-East of Karly"
                    ArchipelagoClient.sendloc(chestintstart + 119);
                    break;
                case "1f7ba32d-3992-42c2-ab0c-f5b7d382af55": //"Trail 18: Chest South of Anabelle"
                    ArchipelagoClient.sendloc(chestintstart + 120);
                    break;
                case "72243934-12c9-440a-a226-e9de780f25fd": //"Trail 18: Chest in North Part of Map"
                    ArchipelagoClient.sendloc(chestintstart + 121);
                    break;
                case "02d71004-c006-4b9a-a467-48396c815865": //"Trail 18: Chest North of Ingrid"
                    ArchipelagoClient.sendloc(chestintstart + 122);
                    break;
                case "f5c25d35-2be7-445d-8432-f31b58d29f81": //"Artic Temple: Chest in South-East"
                    ArchipelagoClient.sendloc(chestintstart + 123);
                    break;
                case "c1b51d5f-663e-4ca5-94a2-1611880789d7": //"Artic Temple: Chest in West"
                    ArchipelagoClient.sendloc(chestintstart + 124);
                    break;
                case "c790f2f6-78ae-4e26-b46b-82d0823a6118": //"Artic Temple: Chest in North-West"
                    ArchipelagoClient.sendloc(chestintstart + 125);
                    break;
                case "c1df6726-ecd8-4863-b1ae-d2d995d6cdf4": //"Trail 19: Chest Near Start"
                    ArchipelagoClient.sendloc(chestintstart + 126);
                    break;
                case "e8bbd1c5-3777-4a13-bcf2-b58e2d6d5d2c": //"Trail 19: Chest South of 1st Crimson Cloak"
                    ArchipelagoClient.sendloc(chestintstart + 127);
                    break;
                case "5a746032-358e-4ace-aa5e-bd614f610742": //"Trail 19: Chest East of 2nd Crimson Cloak"
                    ArchipelagoClient.sendloc(chestintstart + 128);
                    break;
                case "ac4251e7-b377-4124-814a-95601ac2e10f": //"Trail 20: Chest Near 1st Crimson Cloak"
                    ArchipelagoClient.sendloc(chestintstart + 129);
                    break;
                case "b8d3a32e-2b9a-45a9-8496-07d98d24ebe3": //"Trail 20: Chest Near 2nd Crimson Cloak"
                    ArchipelagoClient.sendloc(chestintstart + 130);
                    break;
                case "affeeef4-519b-4b7c-8bea-f6011e35c2fe": //"Trail 20: Chest Near Cave Entrance"
                    ArchipelagoClient.sendloc(chestintstart + 131);
                    break;
                case "c9bccc23-9abc-412b-a969-be4b38fe8c07": //"Trail 21: Chest Near Pushable Bolder"
                    ArchipelagoClient.sendloc(chestintstart + 132);
                    break;
                case "a0ea4f50-253d-41c3-a01e-4b2c0de0c846": //"Trail 21: Chest North of Pond"
                    ArchipelagoClient.sendloc(chestintstart + 133);
                    break;
                case "0c7e4c71-2b16-4171-a256-55820b5f41c5": //"Trail 21: Chest South area of map"
                    ArchipelagoClient.sendloc(chestintstart + 134);
                    break;
                case "35f79fc2-e0ce-4b1a-90a5-fc87436b8c51": //"Trail Spirit Passage: Chest north of first fork in path"
                    ArchipelagoClient.sendloc(chestintstart + 135);
                    break;
                case "1ae0306c-1da3-4248-b1a2-b4ecb14d40c5": //"Trail Spirit Passage: Chest in first loop area"
                    ArchipelagoClient.sendloc(chestintstart + 136);
                    break;
                case "dec67487-358b-43b6-a97e-ca892aa95d89": //"Trail Spirit Passage: Chest north of first loop area"
                    ArchipelagoClient.sendloc(chestintstart + 137);
                    break;
                case "ee7e2616-1b0d-4c92-9014-53c9fa72f424": //"Trail Spirit Passage: Chest near 5th Crimson Cloak"
                    ArchipelagoClient.sendloc(chestintstart + 138);
                    break;
                case "22527dc8-b6b1-4af2-974d-2e56b8fc96b6": //"Trail 22: Chest north west of pond"
                    ArchipelagoClient.sendloc(chestintstart + 139);
                    break;
                case "a3f235a1-bc10-4012-8203-37be87ecf06c": //"Trail 22: Chest north path before large grass patch"
                    ArchipelagoClient.sendloc(chestintstart + 140);
                    break;
                case "e88b6c20-4e22-459e-b229-50bd0edc835d": //"Trail 22: Chest north of large grass patch"
                    ArchipelagoClient.sendloc(chestintstart + 141);
                    break;
                case "f533f7ee-5852-4dc8-87c4-73e434942e3d": //"Trail 22: Chest west side of lake near waypoint"
                    ArchipelagoClient.sendloc(chestintstart + 142);
                    break;
                case "afe7ac71-80d5-45c2-b6c0-683732d1fdf4": //"Trail 22 Cave: Chest"
                    ArchipelagoClient.sendloc(chestintstart + 143);
                    break;
                default:
                    ArchipelagoConsole.LogMessage($"CHEST GUID NOT KNOWN:{__instance.guid}");
                    break;
            }
        }


        [HarmonyPatch(typeof(GenericNPCMapItem), "OnDialogExited")]
        [HarmonyPrefix]
        public static void npcitem(GenericNPCMapItem __instance)
        {
            if (__instance.firstEncounterGifts.Length != 0)
            {
                int chestintstart = Convert.ToInt32(ArchipelagoClient.ServerData.slotData["Chest_Start"]);
                __instance.firstEncounterGifts = HelperItems.centbundle();
                if (__instance.guid == "3019ab50-bd67-4887-9865-cdc2fa604f55")//jane (Trail 01)
                {
                    ArchipelagoClient.sendloc(chestintstart+4);
                }
                else if (__instance.guid == "c135099c-4730-4f32-a9c8-1c79ac82945b")//jessica (Sandy Tunnels)
                {
                    ArchipelagoClient.sendloc(chestintstart + 40);
                }
            }
        }
    }
}




























































































































