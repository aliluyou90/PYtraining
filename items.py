

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
def use_key(user):
    if user.location == "exit":
        print("You open the door and save you life...."
                       "You win the game! Thank you for playing this crapy game.")
        exit()
    else:
        print("You can's use the Key here")
def use_potion(user):
    user.health = user.health + 30 if user.health <= 70 else 100
    user.defense = 0 if user.defense < 0 else user.defense
    print("Your HP is {} now, and your Armor is fixed".format(user.health))

def use_instruction(user):
   print("Actually, I don't like this game either.\n"
                                "So, just find the key and end it please...",)

def use_wine(user):
    user.health = user.health + 10 if user.health <= 90 else 100
    user.attack += 1
    user.defense += 1
    print("Your are drunk and fear of nothing (+1AT, DE +10HP)")
def use_painkiller(user):
    user.health = user.health + 20 if user.health <= 80 else 100
    print("Your feel better (+20HP)")

item_stick = {
                "usable": True,
                "description" : "You try to swing it and found it is pretty handy",
                "use_item": use_stick,
                 }
item_painkiller = {
                "usable": True,
                "description" : "You try to swing it and found it is pretty handy",
                "use_item": use_painkiller,
                 }
item_wine = {
                "usable": True,
                "description" : "You try to swing it and found it is pretty handy",
                "use_item": use_wine,
                 }

item_coffee = {
                "usable": True,
                "description" : "It smelled pretty good, you drunk and feel really refreshing (+15 HP, +1 AT)",
                "use_item": use_coffee,
                 }

item_boots = {
                "usable": True,
                "description" : "It is made of premium leather",
                "use_item": use_boot,
                 }

item_coat = {
                "usable": True,
                "description" : "You took a try, not bad at all, maybe this coat can save your life...",
                "use_item": use_coat,
                 }

item_instruction = {
                "usable": False,
                "description" : "Congrats! You found the shortcut of the game.",
                "use_item": use_instruction,
                 }

item_key = {
                "usable": True,
                "description" : "You can's use it.",
                "use_item": use_key,
                 }

item_potion = {
                "usable": True,
                "description" : "The potion seems to be the cure to all damage the ant can do\n"
                                "Is that stupid???",
                "use_item": use_potion,
                 }

items = { "Iron Stick" : item_stick,
          "Cup of Coffee": item_coffee,
          "Pirate's Boots" : item_boots,
          "Warm Coat"  : item_coat,
          "Game Instruction": item_instruction,
          "Potion": item_potion,
          "Key": item_key,
          "Wine": item_wine,
          "Pain Killer": item_painkiller
        }