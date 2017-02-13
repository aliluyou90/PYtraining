# import event
creep_skills = {"cat_1": {"description": "big hit",
                          "effect": [10, 0, 0]
                          },
                "cat_2": {"description": "armor break",
                          "effect": [3, 3, 0]
                          },
                "pirate_1": {"description": "big hit",
                             "effect": [14, 0, 0]
                             },
                "pirate_2": {"description": "self healing",
                             "effect": [0, 0, -12]
                             },
                "ant_1": {"description": "big hit",
                          "effect": [14, 0, 0]
                          },
                "ant_2": {"description": "absorb your health and heal itself",
                          "effect": [8, 0, -10]
                          },
                "snake_1": {"description": "Golden Venom",
                            "effect": [4, 4, 0]
                            },
                "snake_2": {"description": "Head Swing (self-healing 10HP)",
                            "effect": [13, 0, -10]
                            },
                }

creep_uglycat = {"name": "Ugly Cat",
                 "description": "a cat that is extremely ugly",
                 "attack_description": ["The cat scratch your face", "The cat bite your arm", "The cat screamed"],
                 "status": (False, 7, 1, 50, 0),
                 "battle_cmd": ("attack", "use skills"),
                 "skillID": ("cat_1", "cat_2"),
                 "drop_item": "Potion"
                 }

creep_pirate = {"name": "One-eye Pirate",
                "description": "a strong pirate with one eye",
                "attack_description": ["The Pirate kicked you with his wooden leg",
                                       "The Pirate smashed you with his harmer",
                                       "The pirate attacked you with black smog from his pipe "],
                "status": (False, 9, -1, 70, 0),
                "battle_cmd": ("attack", "attack", "use skills"),
                "skillID": ("pirate_1", "pirate_2"),
                "drop_item": "Pirate's Boots"
                }

creep_giantant = {"name": "Giant Ant",
                  "description": "an ant that is more huge than you can imagine",
                  "attack_description": ["The ant spit acid to you",
                                         "The ant attacked you with it's leg",
                                         "The ant shot a stick to you"],

                  "status": (False, 4, 3, 60, 0),
                  "battle_cmd": ("attack", "attack", "use skills"),
                  "skillID": ("ant_1", "ant_2"),
                  "drop_item": "Potion"
                  }

creep_snake = {"name": "Golden Snake",
               "description": "A big snake",
               "attack_description": ["The snake bite you shoulder",
                                      "The snake triped you down with its tail",
                                      "The snake flashed and you feel dazzled"],

               "status": (False, 11, 1, 40, 0),
               "battle_cmd": ("attack", "use skills"),
               "skillID": ("snake_1", "snake_2"),

               "drop_item": "Key"
               }

creeps = {"giant_ant": creep_giantant,
          "ugly_cat": creep_uglycat,
          "oneeye_pirate": creep_pirate,
          "golden_snake": creep_snake
          }


class enemy:
    def __init__(self, creep_data):
        self.isplayer, self.attack, self.defense, self.health, self.nonsense = creep_data["status"]

        self.name, self.skillID, self.attack_description, self.battle_cmd, self.drop_item = creep_data["name"], creep_data["skillID"], \
                                                                            creep_data["attack_description"], \
                                                                            creep_data["battle_cmd"], creep_data["drop_item"]
        self.skillname = []
        for i in self.skillID:
            self.skillname.append(creep_skills.get(i))

room_boss = {
    "name": "Boss Room",

    "description": "房间布置得很精致，左边有个药品箱，酒柜上有很多酒\n"
                   "中间的大桌子上面摆着一个漂亮的小盒子",

    "exits": {"downstairs": "Main Hall"},

    "action_info": ["A : 试图打开盒子",
                    "B : 倒一杯酒",
                    "C : 在药品箱里找找"
                    "D : Just Leave"],

    "key_eve": {"A": "event_BR01",
                "B": "event_BR02",
                "C": "event_BR03",
                "D": "leave"},
}

room_exit = {
    "name": "Exit",

    "description": "The door is locked, you have to find the key.",

    "exits": {"north": "Main Hall"},

    "action_info": ["A . Hit the door with rocks",
                    "B . Take a look at the shoe shelf",
                     ],

    "key_eve": {"A": "leave", "B": "event_EX01"},
            }
room_burrow = {
    "name": "Suspicious Burrow",

    "description": "地洞的角落里面闪着微弱的光，你向光源走去试图一探究竟\n却踩到了一滩粘糊糊的东西，原来地上有一块发霉的蛋糕。\n你走到闪光的地方，发现了一顶金灿灿的王冠！It's better to stay away....",

    "exits": {"up": "Basement"},


    "action_info": ["A : Take the shining crown and put it on",
                    "B : eat the cake on the floor",
                    "C : Just Leave"],

    "key_eve": {"A": "event_SB01",
                "B": "event_SB02",
                "C": "leave"},
                }

room_basement = {
    "name": "basement",

    "description": "",

    "exits": {"upstairs": "Main Hall", "down": "Suspicious Burrow"},

    "action_info": ["A : Play the piano although you know nothing about it",
                    "B : Check the bloody desk",
                    "C : Just Leave"],

    "key_eve": {"A": "event_DR01",
                "B": "event_DR02",
                "C": "leave"},

}

mainhall = {
    "name": "Main Hall",

    "description": "",

    "exits": {"south": "exit", "upstairs": "boss", "downstairs": "Basement", "west": "Storage Room"},

    "action_info": ["A : Take the shining crown and put it on",
                    "B : eat the cake on the floor",
                    "C : Just Leave"],

    "key_eve": {"A": "event_MH01",
                "B": "event_MH02",
                "C": "leave"},
}

room_storage = {
    "name": "Storage",

    "description": "A big messy storage room, there is several iron sticks could be useful",

    "exits": {"east": "Main Hall"},

    "action_info": ["A : Take the a metal stick",
                    "B : Just Leave"],

    "key_eve": {"A": "event_ST01",
                "B": "leave"},
}

gamemap = {
    "boss": room_boss,
    "Basement": room_basement,
    "Main Hall": mainhall,
    "exit": room_exit,
    "Suspicious Burrow": room_burrow,
    "Storage Room": room_storage
}
