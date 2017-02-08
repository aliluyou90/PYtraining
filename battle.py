import random
from player import *
from initialization import *
from main import *
import os


def die_end():
    print_info("You lose the battle")
    death()


def damage_gen(attack):
    damage = int(attack + random.randrange(-20, 20) / 10)
    return damage


def battle_cmd_gen(Attacker):
    if Attacker.isplayer:
        cmd = input("Now what's your move?\n"
                    "[Attack/A, Run/R or Use Skill/U]\n").lower().split()
    else:
        cmd = random.choice(Attacker.battle_cmd)
    return cmd


def battle(Attack, Defend):
    nonsense = 0
    print_info("A battle between " + Attack.name + " and " + Defend.name + " , who's the winner?")
    next_round = 0
    try:

        while True:

            # if Defend.health <=0:
            # break
            fail_condition(Defend, nonsense)
            if next_round == 1:
                Defend, Attack = Attack, Defend
                print_info("Now it's " + Attack.name + "'s turn!")
            cmd = battle_cmd_gen(Attack)

            if "attack" in cmd or "a" in cmd:

                print_info(random.choice(Attack.attack_description))
                Defend.health -= damage_gen(Attack.attack)
                next_round = 1
                # print_info(Defender.name+"'s HP is " +str(Defender.health)+" .")

            elif "run" in cmd or "r" in cmd:
                run_chance = random.randrange(9)
                if run_chance <= 10:
                    print_info("You really suck on running...... I'm so disappointed.")
                    # "So as you expected, d-o-u-b-l-e the d-e-m-a-g-e!!")
                    #  Attack.health -= damage_gen(Defend.attack)*2
                    next_round = 1
                else:

                    print_info("You escaped...... I'm impressed")
                    break
            elif "skill" in cmd:
                if Attack.isplayer:
                    print("Now you want to use: \n")
                    skill_keys = list(Attack.skillname.keys())
                    skillID = list(Attack.skillname.values())
                    [print_info(skill_keys[i] + ": " + skillID[i]) for i in range(len(skillID))]
                    while True:
                        cmd_useskill = require_cmd("")
                        player_decision = []
                        [player_decision.append(i) for i in skill_keys if i.lower() in cmd_useskill]
                        if len(player_decision) == 1:
                            skill = creep_skills[Attack.skillname[player_decision[0]]]
                            break
                        elif len(player_decision) > 1:
                            print("You can only use one skill at a time.")

                        else:
                            print("I don't understand, do it again.")
                else:
                    skill = random.choice(Attack.skillname)
                print_info(Attack.name + " use skill ----->" + skill["description"])
                Defend.health -= int(skill["effect"][0] * (10 - Defend.defense) / 10)
                Defend.defense -= skill["effect"][1]
                Attack.health -= skill["effect"][2]
            else:
                print_info("You just can't type well, can you?")
                nonsense += 1
                next_round = 0
                continue

            if Defend.health <= 0:
                print_info(Defend.name + " is dead!")
                break
            else:
                print_info(Defend.name + "'s HP is " + str(Defend.health) + ".")
    except KeyboardInterrupt:
        print_info("Why don't try harder")
        exit()
    except SystemExit:
        exit()
        #
