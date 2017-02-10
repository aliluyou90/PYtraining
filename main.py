import random
import time
from gamemap import *
from initialization import *
from battle import *
from event import event


def death():
    print_info("You are dead ! Game Over")
    exit()

def show_manu():
    print("=========================================\n"
          "Name: {}                                 \n"
          "HP: {}        AT: {}        DE:{}        \n"
          "Armor:{}                                 \n"
          "Infantry: {}                             \n"
          "=========================================\n".format(playerA.name, playerA.health, playerA.attack, playerA.defense,"None","None")
        )


def require_cmd(info):
    print(info + "\n")
    cmd = input().lower().split()
    return cmd


def fail_condition(gamer, nonsense):
    if gamer.health <= 0 and gamer.isplayer == True:
        death()
    elif gamer.health <= 0 and gamer.isplayer == False:
        print_info("You WIN!!!")
        return

    if nonsense >= 5:
        nonsense_check = input("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" +
                               "Can you be serious and don't say those crap's to me?(y/n)\n" +
                               "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        if "y" in nonsense_check.split():
            gamer.nonsense = 0
        else:
            print_info("All right, then I will kill you....")
            death()


def execute_event(args):
    this_event = event[args]
    if this_event["active"]:
        print_info(this_event["description"][0])
        if this_event["creeps"]:
            defend = enemy(creeps[this_event["creeps"]])
            battle(playerA, defend)
            return
        elif this_event["status_change"]:
            change = this_event["status_change"]
            playerA.health -= change[0]
            playerA.defense -= change[1]
            playerA.health -= change[2]
        else:
            pass
        this_event["active"] = False

    else:
        print_info(this_event["description"][1])


def info_exit(current_location):
    exits = gamemap[current_location]["exits"]
    go = list(exits.keys())

    for i in go:
        print_info("Go " + i.upper() + " to " + exits[i].upper())
    while True:

        cmd_e = require_cmd("what is your decision?")

        player_decision = list(map(exits.get, cmd_e))
        temp_decisionlen = len(player_decision)
        if not temp_decisionlen:
            print_info("I don't understand")
            continue

        if temp_decisionlen == 1 and player_decision[0] != None:  # temperory solution there was a weird bug about type(None)
            new_location = player_decision[0]
            return new_location
        else:
            print_info("Can you split and go different ways at once?")

if __name__ == "__main__":
    nonsense = 0
    playerA = introduction()

    try:
        print_info("Now you are in " + playerA.location)
        while True:
            fail_condition(playerA, nonsense)
            cmd = require_cmd("Now what's your move?\n"
                              "[search/s, manu/m or Leave/L]")

            if "search" in cmd or "s" in cmd:
                print_info(gamemap[playerA.location]["description"])
                search_res = gamemap[playerA.location]["key_eve"]
                keyword = list(search_res.keys())
                eve_name = list(search_res.values())
                while True:
                    print("Now you want to : \n")
                    [print_info(i) for i in gamemap[playerA.location]["action_info"]]
                    cmd_s = require_cmd("")
                    player_decision = []

                    [player_decision.append(eve_name[i]) for i in range(len(keyword)) if keyword[i].lower() in cmd_s]
                    temp_decisionlen = len(player_decision)
                    if not temp_decisionlen:
                        print("I don't understand, do it again")
                        continue
                    if temp_decisionlen == 1:
                        execute_event(player_decision[0])
                        break
                    else:
                        print("Slow down, do one thing at a time")

            elif "leave" in cmd or "l" in cmd:
                playerA.location = info_exit(playerA.location)
            elif "manu" in cmd or "m" in cmd:
                show_manu()

    except KeyboardInterrupt:
        print_info("Why don't try harder")
        exit()
    except SystemExit:
        exit()
