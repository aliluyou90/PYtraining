import time
import random
from player import *


info_block =  ["================================================================================\n"
               "|{}|\n"
               "================================================================================"]

def print_info(info) :
 for i in info.split("\n"):
  
  print(info_block[0].format(i.center(79," ")))
  time.sleep(1)
  




 # Start game at the reception



welcome = [

                                                            
 "           _______   _         _______   _______   _______   _______ ",
 "|\     /| (  ____ \ ( \       (  ____ \ (  ___  ) (       ) (  ____ \\",
 "| )   ( | | (    \/ | (       | (    \/ | (   ) | | () () | | (    \/",
 "| | _ | | | (__     | |       | |       | |   | | | || || | | (__    ",
 "| |( )| | |  __)    | |       | |       | |   | | | |(_)| | |  __)   ",
 "| || || | | (       | |       | |       | |   | | | |   | | | (      ",
 "| () () | | (____/\ | (____/\ | (____/\ | (___) | | )   ( | | (____/\\",
 "(_______) (_______/ (_______/ (_______/ (_______) |/     \| (_______/",
 
 
                                     
 "                       _________  _______                            ",
 "                       \__   __/ (  ___  )                           ",
 "                          ) (    | (   ) |                           ",
 "                          | |    | |   | |                           ",
 "                          | |    | |   | |                           ",
 "                          | |    | |   | |                           ",
 "                          | |    | (___) |                           ",
 "                          )_(    (_______)                           ",
                                        
 "   _         _______           _______   _______   _______   _______ ",                                                           
 "  | \    /\ (  ____ \         (  ____ \ (  ___  ) (       ) (  ____ \\",
 "  |  \  / / | (    \/         | (    \/ | (   ) | | () () | | (    \/",
 "  |  (_/ /  | |        _____  | |       | (___) | | || || | | (__    ",
 "  |   _ (   | | ____  (_____) | | ____  |  ___  | | |(_)| | |  __)   ",
 "  |  ( \ \  | | \_  )         | | \_  ) | (   ) | | |   | | | (      ",
 "  |  /  \ \ | (___) |         | (___) | | )   ( | | )   ( | | (____/\\",
 "  |_/    \/ (_______)         (_______) |/     \| |/     \| (_______/",
]


intro= ["Hello, my friend! Welcome to this so-called GAME!!!",
        "I'm honored to be your narrator today.",
        "Now say Hi to me...in front of your computer. ",
        "Not funny? Tough kid huh...",
        "Anyways, let's talk about the rules before we start.",
        "First, you should play with your command window...obviously. ",
        "So you need be serious and say something makes sense, OK?" ,
        "Cause I'm a narrator with bad attitude, and I won't get paid. ",
        "Second, don's get pissed off easily.",
        "Unpredictable bugs, crashes or just stupid design. ",
        "Reason? You are so stupid to open this game, now you tell me the reason.",
        "So, just be easy.....Now, let's begin"
]


       
def introduction():
       # [print(eachline) for eachline in welcome]
        for line in welcome:
         print(line)
         time.sleep(0.1)        
        for line in intro:
                print_info(line)
                time.sleep(0.5)
        no_name = 0
        while True:

                
                player_name = input("Now inter your name :")
                player_name = player_name[0].upper() + player_name[1:].lower()
                
                no_name = no_name+1
                                               
                temp_namewordlen = len(player_name.split())
                temp_namelen = len(player_name)
                if not temp_namewordlen:
                        print_info("Should I call you Space Guy? Enter Guy? Or Mr. No Name !?")
                        continue

                elif temp_namelen<=2 :
                        
                        print_info("Come on, "+player_name+" is not a name, are you shy?")
                        continue
                elif temp_namelen >= 16 or temp_namewordlen>3:
                        print_info("You got to be kiding me, your name is so freaking long")
                else:
                        break

                if no_name>3  :
                 player_name = "Player A"
                 
                 print("All right, enough. I'll just call you " + player_name+", you happy now?")                         
                 break
                 print("Now do it again.....")
                                
        time.sleep(0.5) 
        
        print("\n Initializing", end =' ')
        time.sleep(1)
        print("...", end = ' ' )
        print("Just Kidding" )
        playerA = player(player_name)
        print("OK," +player_name+". Let's start the show.")
        return playerA
#----------------------------------------------------------------------

 

         


#def initialize_player():
        
