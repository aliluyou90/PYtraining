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
                "snake_2": {"description": "Head Swing",
                            "effect": [13, 0, -10]
                            },
                }

creep_uglycat = {"name": "Ugly Cat",
                 "description": "a cat that is extremely ugly",
                 "attack_description": ["The cat scratch your face", "The cat bite your arm", "The cat screamed"],
                 "status": (False, 7, 1, 50, 0),
                 "battle_cmd": ("attack", "use skills"),
                 "skillID": ("cat_1", "cat_2")
                 }

creep_pirate = {"name": "One-eye Pirate",
                "description": "a strong pirate with one eye",
                "attack_description": ["The Pirate kicked you with his wooden leg",
                                       "The Pirate smashed you with his harmer",
                                       "The pirate attacked you with black smog from his pipe "],
                "status": (False, 9, -1, 70, 0),
                "battle_cmd": ("attack", "use skills"),
                "skillID": ("pirate_1", "pirate_2")
                }

creep_giantant = {"name": "Giant Ant",
                  "description": "an ant that is more huge than you can imagine",
                  "attack_description": ["The ant spit acid to you",
                                         "The ant attacked you with it's leg",
                                         "The ant shot a stick to you"],

                  "status": (False, 4, 3, 60, 0),
                  "battle_cmd": ("attack", "use skills"),
                  "skillID": ("ant_1", "ant_2")
                  }

creep_snake = {"name": "Golden Snake",
               "description": "A big snake",
               "attack_description": ["The snake bite you shoulder",
                                      "The snake triped you down with its tail",
                                      "The snake flashed and you feel dazzled"],

               "status": (False, 11, 1, 40, 0),
               "battle_cmd": ("attack", "use skills"),
               "skillID": ("snake_1", "snake_2")
               }

creeps = {"giant_ant": creep_giantant,
          "ugly_cat": creep_uglycat,
          "oneeye_pirate": creep_pirate,
          "golden_snake": creep_snake
          }


class enemy:
    def __init__(self, creep_data):
        self.isplayer, self.attack, self.defense, self.health, self.nonsense = creep_data["status"]

        self.name, self.skillID, self.attack_description, self.battle_cmd = creep_data["name"], creep_data["skillID"], \
                                                                            creep_data["attack_description"], \
                                                                            creep_data["battle_cmd"]
        self.skillname = []
        for i in self.skillID:
            self.skillname.append(creep_skills.get(i))


room_basement = {
    "name": "basement",

    "description": "",

    "exits": {"east": "Main Hall", "south": "exit"},

    "action_info": ["A : Play the piano although you know nothing about it",
                    "B : Check the bloody desk",
                    "C : Just Leave"],

    "key_eve": {"A": "event_DR01",
                "B": "event_DR02",
                "C": "leave"},

    "items": [],

}

room_boss = {
    "name": "Boss Room",

    "description": "",

    "exits": {"south": "Basement"},

    "action_info": ["A : Take the shining crown and put it on",
                    "B : eat the cake on the floor",
                    "C : Just Leave"],

    "key_eve": {"A": "event_BR01",
                "B": "event_BR02",
                "C": "leave"},

    "items": [],
}

armoury = {
    "name": "Armoury",

    "description": "",

    "exits": {"east": "Basement"},

    "action_info": ["A : Take the shining crown and put it on",
                    "B : eat the cake on the floor",
                    "C : Just Leave"],

    "key_eve": {"A": "event_AM01",
                "B": "event_AM02",
                "C": "leave"},
    "items": [],
}

room_treasure = {

    "name": "Treasure Room",

    "description": "",

    "exits": {"southwest": "Basement"},

    "items": [],

    "action_info": ["A : Take the shining crown and put it on",
                    "B : eat the cake on the floor",
                    "C : Just Leave"],

    "key_eve": {"A": "event_TR01",
                "B": "event_TR02",
                "C": "leave"},
}

mainhall = {
    "name": "Main Hall",

    "description": "",

    "exits": {"north": "boss", "northeast": "treasure", "downstairs": "Basement", "west": "armoury"},

    "items": [],

    "action_info": ["A : Take the shining crown and put it on",
                    "B : eat the cake on the floor",
                    "C : Just Leave"],

    "key_eve": {"A": "event_CD01",
                "B": "event_CD02",
                "C": "leave"},
}

room_exit = {
    "name": "Exit",

    "description": "",

    "exits": {"north": "Main Hall"},

    "items": [],

    "action_info": ["A : Take the shining crown and put it on",
                    "B : eat the cake on the floor",
                    "C : Just Leave"],

    "key_eve": {"A": "event_EX01",
                "B": "event_EX02",
                "C": "leave"},
}

gamemap = {
    "Main Hall": mainhall,
    "boss": room_boss,
    "armoury": armoury,
    "treasure": room_treasure,
    "Basement": room_basement,
    "exit": room_exit
}