import random

from worlds.spirit_valley.Data_Spirits import spirit_list


class Trainer:
    name:str
    party:[[str,int, bool]]
    guid:str

    def __init__(self, name, party, guid):
        self.name=name
        self.party=party
        self.guid=guid

    def __str__(self):
        s= f'{{"NAME":"{self.name}", "PARTY":['
        for i in range(len(self.party)):
            if i != 0:
                s=s+','
            if(len(self.party[i]) ==2):
                s = s + f'{{"spirit":"{self.party[i][0]}","lv":{self.party[i][1]},"shiny":0}}'
            else:
                s = s + f'{{"spirit":"{self.party[i][0]}","lv":{self.party[i][1]},"shiny":{self.party[i][2]}}}'
        return s+ f'], "GUID":"{self.guid}"}}'

Default_Trainers = [
    #"Oakwood Village"
    Trainer("Robbie",[["Wolfy",3]],"61822611-267a-4366-b99c-fadc5a23ad01"),# SCRIPTED FIGHT "61822611-267a-4366-b99c-fadc5a23ad01"
    #"Evergreen Outpost"
    Trainer("Elise",[["Beebee",3]],"19c75671-2314-414f-b500-ef28c011d8d2"),
    #"Trail 02"
    Trainer("Billy",[["Gloria",3], ["Petunia",2]],"0a40a301-741a-4843-8008-799f4ba37287"),
    Trainer("Macy",[["Ursie",4]],"bf261ea7-7b93-4c0b-89a8-da7c93550808"),
    Trainer("Skyler",[["Slimee",3], ["Beebee",3]],"a79a0909-43a5-47ff-b990-a1632a224e83"),
    Trainer("Crimson Agent",[["Wolfy",4], ["Petunia",3]],"Trail 02: Crimson Agent"),#SCRIPTED FIGHT "53af4c29-1d1b-4655-a1db-9ed89c32a981"
    #"Trail 03"
    Trainer("Cheese",[["Oakie",6], ["Beebee",5]],"b40b0778-da74-4660-b0a1-fba6d1d16bdd"),
    Trainer("Miriam",[["Petunia",7], ["Wolfy",6]],"c029e36a-14ec-4d07-a45b-b7b57f406575"),
    Trainer("Jenna",[["Ursie",6]],"6778b3a1-97d4-457d-adc1-c324dbad017e"),
    #"Evergreen Caverns"
    Trainer("Stu",[["Serpentia",7], ["Gloria",6]],"e6929a89-5dc3-4118-bcf9-ff20df7ed4af"),
    Trainer("Nicole",[["Octopussy",8], ["Slimee",6]],"364ef3fd-dfe9-41bb-aa8c-9583af54d8f8"),
    Trainer("Rawry",[["Rawry",15]],"72e0b641-b787-46cb-8fe8-eb17f93073fa"),
    #"Ancient temple entrense"
    Trainer("1st crimson cloak near entrense",[["Spinnie",8]],"5efd2110-61ad-4bea-9551-2bffee802492"),
    Trainer("2nd crimson cloak near pillars",[["Trissy",8], ["chubbie",7]],"27d2018d-9706-4b17-981d-e408d42e1041"),
    Trainer("3rd crimson cloak near chest",[["Serpentia",9], ["Belle",6]],"cae4d216-6d69-470b-a721-3d83290c0de6"),
    Trainer("4th crimson cloak right after first fork",[["Wolfy",8], ["Beebee",7]],"2174dd35-f25f-4d1a-86a3-c1f46f576ff9"),
    Trainer("5th crimson cloak",[["Trissy",9]],"677f47ac-c833-42c8-a19a-4d99d5985fdd"),
    Trainer("6th crimson cloak blocking chest",[["Ursie",8], ["Oakie",6]],"7c73c737-4fd5-4266-92ea-caf02f8c9320"),
    #"Ancient temple room 1"
    Trainer("1st L-S-L-S-R",[["Octopussy",8], ["Serpentia",6], ["Spinnie",7]],"122ab3e7-c278-402b-a741-c83633c93626"),
    #"Ancient temple room 2"
    Trainer("Valkrie",[["Valkrie",11]], "Boss_Valkrie"),#SCRIPTED FIGHT
    #"Trail 05"
    Trainer("Mila",[["Pusseen",9], ["Slimee",7]],"83b06037-1fe2-47d9-8887-479a7b0104d6"),
    Trainer("Roy",[["Rawry",10]],"e6cda171-22b9-43fb-9ca0-f2411e2e4226"),
    Trainer("Lulu",[["Boobae",10], ["Beebee",7]],"72a096dd-0fe8-4146-9bf0-c7d5e5234b98"),
    #"Sandy tunnels"
    Trainer("Chad",[["Octopussy",10]],"666003ef-c69e-4279-809a-e757e8cb60b2"),
    Trainer("Destiny",[["Oakie",9], ["Serpentina",7]],"265abaf4-18eb-45fd-8aba-6bc4f8844f81"),
    #"Trail 06"
    Trainer("Kelsie",[["Serpentax",10], ["Wolfy",8]],"acd2e86c-2cdd-48e9-aaed-ba84a84d70a3"),
    Trainer("Hayden",[["Beebee",9]],"8cad5228-7db2-49cd-9fcc-e625029e6817"),
    Trainer("Juliet",[["Spinnie",10], ["Tinky",7]],"4cc138d0-8b3d-4ea6-8dd4-e593ae0d9aef"),
    #"Trail 07"
    Trainer("Sally McTits",[["Dripsy",14], ["Gloreen",13], ["Kittypus",13], ["Boobae",11]],"6db1fd7b-c78b-4de1-967c-ce67e656236e"),
    Trainer("Bella",[["Serpentax",13], ["cactee",10], ["Bovina",11]],"56c3e787-d36a-4e11-aead-ea47f500e261"),
    Trainer("Dakota",[["Birdy",12], ["Flora",11]],"ab480291-fa67-4ec2-a724-c048b4537914"),
    Trainer("Cassidy",[["Twerky",11], ["Buzzeena",13], ["Tinky",10], ["Octopussy",11]],"0f05b20d-99cf-4cee-852e-7e5edac5a456"),
    #"Tumbleweed Town"
    Trainer("Willy Wanker",[["Bearboo",17], ["Kittypus",17], ["Bunni",16]],"Tumbleweed Town: Willy Wanker"),#MODIFY SASSY NPC ??? 2aefb292-7d0d-4674-a0bd-eb5e487b1272
    Trainer("Dick Cummings",[["Lacteena",18], ["Megaboob",20], ["Triboobe",17], ["Bovina",17]],"Tumbleweed Town: Dick Cummings"),#MODIFY SASSY NPC ??? 2aefb292-7d0d-4674-a0bd-eb5e487b1272
    Trainer("Dick Louie",[["Buzzeena",19], ["Flora",18], ["Gloreen",19], ["Thiccsie",18], ["Spinnie",17]],"Tumbleweed Town: Dick Louie"),#MODIFY SASSY NPC ??? 2aefb292-7d0d-4674-a0bd-eb5e487b1272
    #"Trail 08"
    Trainer("Marisa",[["Lacteena",13], ["Hornie",13]],"e07a91ad-6fd5-4d54-8b05-36c3f9d090c1"),
    Trainer("Jenni",[["Gloreen",14], ["Birdy",12]],"bd2e9de2-30db-42f2-aa44-678cf71649ea"),
    Trainer("Alanna",[["Buzzeena",14], ["Serpentax",13], ["Flora",13]],"163d96da-8b46-4b1e-baf6-e46708072abe"),
    #"Dusty Grotto"
    Trainer("Arnie",[["Chubbie",14], ["Bunni",12], ["Hornie",15]],"af5b25fb-7066-4fca-b1fa-c94fb7e5f330"),
    Trainer("Crystal",[["Buzzeena",15], ["Cactee",12]],"cf1d4fc7-2757-41ea-8198-322dda687398"),
    Trainer("Skye",[["Lacteena",13], ["Serpentax",14], ["Rawry",13]],"176d7645-f963-47ca-9af5-344d1c2e8dc0"),
    #"Trail 09"
    Trainer("Mike", [["Birdy",16], ["Buzzeena",15]],"f792e755-6771-4f50-8dca-8d3cf8b6017a"),
    Trainer("Clementine", [["Bovina",14], ["Gloreen",16]],"00c525ca-41d2-40ba-a68e-c40f8990652c"),
    Trainer("Bonnie", [["Octocunt",17], ["Buxzzeena",16], ["Growleen",16]],"b4d3fec1-9f7f-4b2e-a3de-cf25bc3fe399"),
    #"stone temple entrence"
    Trainer("1st crismon cloak", [["Domina",19], ["Growleen",18]],"48a6856e-4dbd-4ca9-b6d5-066b5a55d783"),
    Trainer("2nd crismon cloak", [["Buzzeena",17]],"7b40e4f2-990b-4a2c-8ccc-aa283653436a"),
    Trainer("3rd crismon cloak", [["Kittypus",16], ["Flora",17], ["Dripsy",15]],"b3ab8b9c-5260-47a6-befc-d99487a2a53f"),
    Trainer("4th crismon cloak near chest", [["Harlie",18]],"bf8484cc-5889-45ce-8b18-c35b96e0d0e7"),
    Trainer("5th crismon cloak ", [["Lacteena",20], ["Octocunt",18]],"02067b08-1777-4713-af0d-123bb86102fe"),
    Trainer("6th crismon cloak west of 5th", [["Megaboob",18]],"a0268c7e-1417-41cb-aa2a-109240ff2eac"),
    #"stone temple room 1"
    Trainer("Domino", [["Octocunt",18], ["Serpentax",19], ["Harlie",18], ["Hornie",17], ["Bearboo",17]], "Stone Temple: Domino"),#SCRIPTED FIGHT
    #"Crash Site"
    Trainer("Athena", [["Pinchie",18], ["Dracoomer",17], ["Cactee",15]],"ae458556-c336-43a7-a7c3-be76c84f0a48"),
    Trainer("Janet", [["Mamaoak",21], ["Bearboo",16]],"ef863488-65f8-4827-9e80-0e1c6a42b681"),
    #"Trail 10"
    Trainer("Bailee", [["Amazona",20], ["Octocunt",17]],"b15889a3-63eb-490f-8f7b-e14555ac9d97"),
    Trainer("Eve", [["Domina",17], ["Sexybun",21]],"6ee5a399-6614-482d-8e07-00abcf34d10e"),
    #"Trail 11"
    Trainer("Alice", [["Marinel",21], ["Pinchie",20], ["Sharky",22]],"ceba2e6b-5cd3-40ae-8696-f9ef461c7b14"),#SCRIPED FIGHT GUID"ceba2e6b-5cd3-40ae-8696-f9ef461c7b14"
    Trainer("Emilia", [["Hornie",17], ["Marinel",19]],"cc69f7aa-a078-448c-ab25-00c8f774926f"),
    Trainer("Sydney", [["Octocunt",16], ["Mamaoak",20], ["Serpentax",17]],"2bf2f7ed-e375-4747-875c-3bd1b2048e46"),
    #"Trail 12"
    Trainer("Sophie", [["Harlie",17], ["Faerie",21]],"ddc0cee9-5a37-431b-baf8-8653a97f13a0"),
    Trainer("Ciara", [["Grewleen",17], ["Dracoomer",17], ["Sharky",20]],"961a23f5-023b-4d31-ab65-b8d227a52ded"),
    #"Fishing Hut"
    Trainer("Bonnie Baiter", [["chocostar",21], ["Mamaoak",20], ["Marinel",20]],"05ba33a6-2693-49ba-b570-543c25feeeb2"),#SCRIPTED FIGHT "05ba33a6-2693-49ba-b570-543c25feeeb2"
    #"Trail 13"
    Trainer("1st cultist", [["Gloreen",23], ["Mamaoak",21], ["Sharky",20]],"a4a13dee-d151-407c-8ed1-8db2d45efdf2"),
    Trainer("2nd cultist", [["Triboobe",21], ["Dripsy",23]],"b4a8bd50-ab01-4e3c-8aba-0469ada1c52f"),
    #"Trail 14"
    Trainer("1st cultist", [["Kittypus",18], ["Thiccsie",20], ["Jellygal",22]],"38dd508c-5633-47c3-b142-846c3915716d"),
    Trainer("2nd cultist", [["Buzzeena",18], ["Sexybun",22], ["Twerqueen",24], ["Chocostar",20]],"9b009cf3-5fad-4076-88d2-3e43e004efec"),
    #"Island Cave"
    Trainer("1st cultist", [["Bovina",18], ["Mamaoak",22]],"5fbd94fe-f5dc-42bb-9f57-dbaec4d8d3c3"),
    Trainer("2nd cultist", [["Harpie",23], ["Twerqueen",23], ["Amazona",20]],"1ad60dfe-2454-431e-8f8a-8f512003aa1d"),
    Trainer("3rd cultist", [["Lacteena",22], ["Jellygal",24]],"46a60f99-3cb9-42cf-860f-9e471707e263"),
    Trainer("4th cultist", [["Succubae",25], ["Udderella",22]],"5f53e18a-e6b1-473a-8252-f0d68286ca57"),
    #"Island Cave lv2"
    Trainer("Centiboob", [["Centiboob",26]],"Island Cave: Centiboob"),#SCRIPTED FIGHT
    #"Cold Harbor"
    Trainer("Vanessa", [["Harpie",25], ["Gangfang",26]],"323cbfec-0db2-43c2-a538-e3b4cf02d260"),
    Trainer("Iris", [["Amazona",22], ["Polaria",26], ["Snowbae",23]],"c34254a6-6f54-4643-8319-75636a798542"),
    #"Frostville"
    Trainer("Mother Evilyn", [["Hornie",29], ["Arachna",32], ["Octomommy",31]],"aa1ce20e-a988-48c9-8a4b-e246fb163402"),#SCRIPTED FIGHT "aa1ce20e-a988-48c9-8a4b-e246fb163402"
    #"Trail 15"
    Trainer("Mia", [["Deardeer",25], ["Chocostar",25]],"705f45eb-9221-4c47-b339-e8d2b2f6d862"),
    Trainer("Olga", [["Pinchie",24], ["Polaria",27], ["Harpie",26]],"9f573d72-be6e-48dc-9ffd-50044176a86c"),
    #"Trail 16"
    Trainer("Karin", [["Mamaoak",21], ["Gangfang",26]],"911604b8-a719-4eb6-af17-42bd8dc35a9b"),
    Trainer("Dahlia", [["Snowbae",25], ["Chocostar",23], ["Polaria",28]],"1e4eb581-53ee-4f87-b021-ff0ebc931798"),
    #"Trail 17"
    Trainer("Clara", [["Slithereen",27], ["Arachna",28]],"5d964c9f-f399-4a24-98f6-def8af276d4c"),
    Trainer("Liv", [["Jellybish",29], ["Jawsy",27], ["Harpie",23]],"38419b1d-9908-4ef4-a962-1406aa2a4352"),
    Trainer("Karly", [["Slushie",25], ["Gangfang",30]],"d09da17a-d5b6-415f-986f-9dc216400385"),
    #"Trail 18"
    Trainer("Stacy", [["Polaria",30], ["Harpie",28]],"0a2fe22c-e43e-457f-85af-29ed94e9f57d"),
    Trainer("Anabelle", [["Jellybish",31], ["Slithereen",29]],"4492eac4-575d-46c8-8d4f-4418e4ab1065"),
    Trainer("Ingrid", [["Slithereen",28], ["Queenbee",31], ["Slushie",25]],"5676a70d-5a1c-4868-906f-a269dffc5f2f"),
    #"artic temple entrence"
    Trainer("1st Crismon Cloak", [["Octomommy",32], ["Harpie",26], ["Mamaoak",27]],"23aa2df5-197e-45cb-af67-dfc97e83dd3b"),
    Trainer("2nd Crismon Cloak", [["Arachna",28], ["Boobarella",31]],"1452eb18-e64d-4fb6-93b3-84574ee29396"),
    Trainer("3rd Crismon Cloak", [["Jellybish",30], ["Polaria",29]],"4bd72a1d-cdf9-49b4-ba2b-245dabf60035"),
    Trainer("4th Crismon Cloak", [["Slithereen",31], ["Deardeer",32]],"60f3aad3-3f2d-4ce1-ab4a-f6833957b8ab"),
    Trainer("5th Crismon Cloak", [["Gangfang",27], ["Queenbee",31]],"5272d410-ae2d-42b5-93a8-b06b4ba20fe2"),
    #"artic temple room1"
    Trainer("Crismon countess", [["Queenbee",32], ["Chocostar",28], ["Octomommy",30], ["Archna",31], ["Jawsy",33]],"Artic Temple: Crimson Countess"), #SCRIPTED FIGHT

    #"Trail 19"
    Trainer("1st Crimson Cloak", [["Harpie", 34], ["Slithereen", 32]], "97fab556-a752-489c-8de5-04d3449afeca"),
    Trainer("2nd Crimson Cloak", [["Fungie", 33]], "ce0b7e57-6bbd-4034-9f2b-2785f6b6f07d"),
    Trainer("3rd Crimson Cloak", [["Arachna", 32], ["Jellybish", 33]], "bbb2a608-b9f8-4701-a978-549f98628a70"),
    #"Trail 20"
    Trainer("1st Crimson Cloak", [["Chocostar", 34], ["Fungie", 32]], "4d8163f6-3e75-4112-9824-7e0247d4118f"),
    Trainer("2nd Crimson Cloak", [["Polaria", 35]], "72d37c80-d416-48b0-8e1f-ab6c9f49e40c"),
    Trainer("3rd Crimson Cloak", [["Mamaoak", 32], ["Jawsy", 34]], "149cf1b9-7344-4037-88b8-42fe6f471e64"),
    #"Trail 21"
    Trainer("1st Crimson Cloak", [["Juggsie", 36]], "ff372848-9064-45a9-9e2c-dd98e3fd1313"),#BUGGED TRAINER
    Trainer("2nd Crimson Cloak", [["Unihorn", 34], ["Octomommy", 30]], "ff372848-9064-45a9-9e2c-dd98e3fd1313"),#BUGGED TRAINER
    Trainer("Kinley", [["Queenbee", 32], ["Snowbae", 30], ["Pinchie", 35], ["Boobarella", 34]], "0ea61b92-8dcd-4adf-a070-4bc5870b2698"),
    #"Spirit Passage"
    Trainer("1st crismon cloak", [["Chocostar", 35], ["Harpie", 32]], "9eeac2b8-20b3-4d35-a7b9-bb01169dc72d"),
    Trainer("2nd crismon cloak", [["Slushie", 35]], "70e65def-a84b-4df5-873c-77d2f02fc30b"),
    Trainer("3rd crismon cloak", [["Amazona", 37]], "b8863596-1a75-481f-94ca-4178785f0554"),
    Trainer("4th crismon cloak", [["Seraphina", 38], ["Marinel", 36]], "97835a52-0d7b-4d9d-9184-8eb813faf909"),
    Trainer("5th crismon cloak", [["Twerqueen", 36], ["Faerie", 37]], "a2557c2e-85f8-4511-8d14-da72a962943c"),
    #"Trail 22"
    Trainer("1st Crimson Cloak", [["Deardeer", 36], ["Dominatrix", 35], ["Octocunt", 35]], "7f45394d-44a9-466e-b9a5-7a169ae47754"),
    Trainer("2nd Crimson Cloak", [["Seraphina", 39], ["Unihorn", 33]], "95124723-8456-47a9-91fa-1576ef841d84"),
    Trainer("3rd Crimson Cloak", [["Jawsy", 39]], "c618afc1-47b2-4de3-b09d-483d57333482"),
    #"Inner Grove"
    Trainer("Spirit Mother", [["SpiritMother", 43]], "Inner Grove: Spirit Mother"),

]

def rand_trainer(rand) -> list[str]:
    trainret = []
    if rand:
        for t in Default_Trainers:
            mon = random.sample(spirit_list, random.choice(range(1,7)))
            party = []
            for m in mon:
                mlv = t.party[0][1]-3
                if mlv <=0: mlv = 1
                party.append([m, random.choice(range(mlv,t.party[0][1]+2)), random.choice([0, 1])])
            trainret.append(Trainer(t.name, party, t.guid))
    else:
        trainret = Default_Trainers.copy()
    return [f"{t}" for t in trainret]