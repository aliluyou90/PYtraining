



DR01 = {"description": ["You played the broken piano and made distribing noises...\n So I desided to release a creep to kill you!",
                        "You step over the cat's body and play anoying noise on the piano"],
        
        "creeps": "ugly_cat",
        
        "status_change":[],
        
        "active": True
        }

NON = {"description": ["Nothing happened","Nothing happened"],

        "creeps": "",
        
        "status_change":[],
        
        "active": True
        }

DR02 = {"description": ["There is something covered by the blood, you try to wipe it off to see it clear.\n but you got hurt by a rat trap (-10 HP)"
                        
                        ,"You cannot find anything except the trap hurt you before"],

       "creeps": "",

        "status_change": [10, 0, 0],

        "active": True
        }
SB01 = {"description": ["What a beautiful crown and it looks perfect on you, huh?\n A snake is behind you while you are enjoying youself"

                        ,"You remember how hurt the snake-bite was......"],

        "creeps": "golden_snake",

       "status_change": [],

        "active": True
        }

SB02 = {"description": ["You pick up the sticky stink cake and start eating it, so disgusting... \n Guess what? You get "
                        "poisoned and black out for half a day, you wake up and find yourself cant feel anything (+2 Ar"
                        "mor) except for headache (-5HP)"

                        ,"You already had ate them all......"],

        "creeps": "",

       "status_change":[5, 2, 0],

        "active": True
        }

ST01 = {"description": ["You picked a handy stick, this could be a good weapon (+3 AT)"

                        ,"You cannot carry more of them....."],

        "creeps": "",

        "status_change":[5, 2, 0],

        "item": "item_stick",

        "active": True
        }

event = {"event_DR01": DR01,
         "event_DR02":DR02,
         "event_BR01": NON,
         "event_BR02":NON, 
         "event_TR01": NON,
         "event_TR02":NON,
         "event_CD01": NON,
         "event_CD02":NON,    
         "event_ST01": ST01,
         "event_EX01": NON,
         "event_EX02":NON,            
         "leave": NON,
         "event_SB01": SB01,
         "event_SB02": SB02
         }


