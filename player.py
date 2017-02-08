class player:
    inventory = []
    location = "Main Hall"
    isplayer = True
    nonsense = 0
    attack = 10
    defense = 0
    health = 100
    name = ""
    skillname = {"a": "cat_1", "b": "snake_1"}
    attack_description = ["You use your left fist to punch the enemy's face",
                          "You jumped high and kick the enemy's head",
                          "you use your elbow to kick the enemy's belly"]
    battle_cmd = ["attack", "run", "use item", "use skills"]

    def __init__(self, name):
        self.name = name


PLAYER = {
    "inventory": [],
    # Start game at the reception
    "location": "dragon room",
    "isplayer": True,
    "nonsense": 0,
    "attack": 10,
    "defense": 0,
    "health": 100,
    "name": "",
    "skills_id": (),
    "attack_description": ["You use your left fist to punch the enimy's face",
                           "You jumped high and kick the enimy's head",
                           "you use your elbow to kick the enimy's belly"],

    "battle_cmd": ["attack", "run", "use item", "use skills"]
}
