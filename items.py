

def use_stick(user):
    user.attack += 3
    print("You are more powerful than ever")
def use_coffee(user):
    user.health = user.health+ 30 if user.health <=70 else 100
    print("Your HP is {} now!".format(user.health))

def use_boot(user):
    user.defense += 1
    print("Your Armor is strengthened")
def use_coat(user):
    user.defense += 3
    print("Your Armor is strengthened")
def use_coat(user):
    if user.location == "Exit":
        win_end()
    else:
        print("You can's use the Key here")
def use_potion(user):
    user.health = user.health + 30 if user.health <= 70 else 100
    user.defence = 0 if user.defense < 0 else user.defence
    print("Your HP is {} now, and your Armor is fixed".format(user.health))









item_stick = {"name":"Iron Stick",
                "usable": False,
                "description" : "You try to swing it and found it is pretty handy",
                 }

item_coffee = {"name":"A cup of coffee",
                "usable": True,
                "description" : "It smelled pretty good, you drunk and feel really refreshing (+15 HP, +1 AT)",
                "status_change":[15, -1, 0, 0],
                 }

item_boots = {"name":"Pirate's Boots",
                "usable": False,
                "description" : "It is made of premium leather",
                "status_change":[0, 0, -1, 0],
                 }

item_coat = {"name":"Warm Coat",
                "usable": False,
                "description" : "You took a try, not bad at all, maybe this coat can save your life...",
                "status_change":[0, 0, -2, 0],
                 }

item_instruction = {"name":"Game Instruction",
                "usable": True,
                "description" : "Congrats! You found the shortcut of the game.\n"
                                "Actually, I don't like this game either.\n"
                                "So, just find the key and end it please...",
                "status_change":[],
                 }

item_key = {"name":"Key",
                "usable": True,
                "description" : "You can's use it.",
                "status_change":[],
                 }

items = { "item_stick" : item_stick,
          "item_coffee": item_coffee,
          "item_boots" : item_boots,
          "item_coat"  : item_coat,
          "item_instruction": item_instruction,
          "item_key": item_key
        }