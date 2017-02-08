import random
import time
from gamemap import *
from initialization import *
from battle import *
from event import event


def death():
    print_info("You are dead ! Game Over")
    exit()


def require_cmd(info):
    print(info + "\n")
    cmd = input().lower().split()
    return cmd


def fail_condition(gamer, nonsense):
    if gamer.health <= 0 and gamer.isplayer == True:
        death()
    elif gamer.health <= 0 and gamer.isplayer == False:
        print_info("You WIN!!!")

    if nonsense >= 5:
        nonsense_check = input("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n" +
                               "Can you be serious and don't say those crap's to me?(y/n)\n" +
                               "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
        if "y" in nonsense_check.split():
            nonsense = 0
        else:
            print_info("All right, then I will kill you....")
            death()


def execute_event(args):
    this_event = event[args]
    if this_event["active"]:
        print_info(this_event["description"][0])
        if len(this_event["creeps"]) != 0:
            defend = enemy(creeps[this_event["creeps"]])
            battle(playerA, defend)
        elif len(this_event["status_change"]) != 0:
            change = this_event["status_change"]
            playerA.health -= change[0]
            playerA.defense -= change[1]
            playerA.health -= change[2]
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
        checker = len(player_decision)

        if checker == 1 and player_decision[0] != None:  # temperory solution there was a weird bug about type(None)
            new_location = player_decision[0]
            return new_location
        elif checker > 1:
            print_info("Can you split and go different ways at once?")
        else:
            print_info("I don't understand")


if __name__ == "__main__":
    nonsense = 0
    playerA = introduction()
    # creep_inbattle =enemy(random.choice(creeps))

    try:
        while True:
            fail_condition(playerA, nonsense)

            print_info("Now you are in " + playerA.location)
            cmd = require_cmd("Now what's your move?\n"
                              "[search/s or Leave/L]")

            if "search" in cmd or "s" in cmd:
                search_res = gamemap[playerA.location]["key_eve"]
                keyword = list(search_res.keys())
                eve_name = list(search_res.values())
                while True:
                    print("Now you want to : \n")
                    [print_info(i) for i in gamemap[playerA.location]["action_info"]]
                    cmd_s = require_cmd("")
                    player_decision = []

                    [player_decision.append(eve_name[i]) for i in range(len(keyword)) if keyword[i].lower() in cmd_s]
                    if len(player_decision) == 1:
                        execute_event(player_decision[0])
                        break
                    elif len(player_decision) > 1:
                        print("Slow down, do one thing at a time")

                    else:
                        print("I don't understand, do it again")

            elif "leave" in cmd or "l" in cmd:
                current_location = playerA.location
                new_location = info_exit(current_location)
                playerA.location = new_location
    except KeyboardInterrupt:
        print_info("Why don't try harder")
        exit()
    except SystemExit:
        exit()
