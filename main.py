from colorama import Fore, Back, Style
import random, time
#For those of you on GitHub, this was made on replit.com. (formerly repl.it)
print(Style.BRIGHT + Fore.CYAN + Back.YELLOW + "Kinda Sus\n")
print(Fore.YELLOW + Back.CYAN + "The code is by Daniel Hsieh. He started working on this at age 10 and finished at age .")
username = input("What is your username? ")
start_or_not = input(f"Ok {username}! Would you like to start the game? (y/n): ")
if start_or_not == "n":
  print(f"Bye {username}!")
  exit()
if start_or_not == "y":
  color = input(f"What is your color, {username}? (blue/red/yellow\n/orange/cyan/purple/lime/black/white/brown): ")
  print(f"Ok {username}! You are now {color}.")
  hat_1 = ["police hat", "santa hat"]
  hat_2 = ["dum sticker", "bird mask"]
  hat_3 = ["top hat", "knife in the head"]
  hat_one = random.choice(hat_1)
  hat_two = random.choice(hat_2)
  hat_three = random.choice(hat_3)
  hat = input(f"What hat do you want? ({hat_one}/{hat_two}/{hat_three}): ")
  print(f"You have equipped the {hat}.")
  player_1 = ["squishy", "Imiss2019"] 
  player_2 = ["composer", "trust me"]
  player_3 = ["told you", "fhjdf"]
  player_4 = ["AmongSus", "pumba"]
  player_5 = ["KillerChef", "URMOM"]
  player_6 = ["hacker", "Agatha"]
  player_7 = ["teehee", "sire sirol"]
  player_8 = ["not sus", "Tiktok"]
  player_9 = ["OuterSloth", "Crispy"]
  player_one = random.choice(player_1)
  player_two = random.choice(player_2)
  player_three = random.choice(player_3)
  player_four = random.choice(player_4)
  player_five = random.choice(player_5)
  player_six = random.choice(player_6)
  player_seven = random.choice(player_7)
  player_eight = random.choice(player_8)
  player_nine = random.choice(player_9)
  all_players = [f"{player_one}", f"{player_two}", f"{player_three}", f"{player_four}", f"{player_five}", f"{player_six}", f"{player_seven}", f"{player_eight}", f"{player_nine}", f"{username}"]
  print(f"You are in a room with {player_one}, {player_two}, {player_three}, {player_four}, {player_five}, {player_six}, {player_seven}, {player_eight}, and {player_nine}.")
  print("The game will start in 5 seconds.")
  time.sleep(1)
  print("4")
  time.sleep(1)
  print("3")
  time.sleep(1)
  print("2")
  time.sleep(1)
  print("1")
  places = ["Cafeteria", "Weapons", "Navigation", "O2", "Shields", "Communications", "Storage", "Admin", "Electrical", "Lower Engine", "Security", "Reactor", "Upper Engine", "Medbay"]
  maps = ["The Skeld", "Mira HQ", "Polus", "The Airship"]
  map = random.choice(maps)
  print(f"The map is {map}.")
  if map == maps[0]:
    impostors = ["1", "2", "3"]
    impostor_count = random.choice(impostors)
    if impostor_count == impostors[0]:
      impostor_1_1 = 1
      crewmates_1_1 = 9
    secret_impostor = random.choice(all_players)
    if username == secret_impostor:
      print("Shh! You are the impostor.")
    if impostor_1_1 >= crewmates_1_1:
      print("The impostor won the game!")
      exit()
    if impostor_1_1 == 0:
      print("You lost the game.")
      exit()
      while True:
        where_impostor_1_1 = input("Where would you like to go? (Cafeteria/Weapons/Navigation/O2/Shields/Communications/Storage/Admin/Electrical/Lower Engine/Security/Reactor/Upper Engine/Medbay): ")
      if where_impostor_1_1 == "Cafeteria":
        cafe_people_1_1 = ["There are 2 people in the cafe.", "There is only one person in the cafe."]
        cafe_people_random_1_1 = random.choice(cafe_people_1_1)
        print(f"{cafe_people_random_1_1}")
        kill_or_not_1_1 = input("Would you like to kill? (y/n): ")
        if cafe_people_random_1_1 == cafe_people_1_1[0]:
          if kill_or_not_1_1 == "y":
            crewmates_1_1 -= 1
            print("The other person in the cafe reports the body and blames you. You get voted out.")
            impostor_1_1 -= 1
            exit()
          if kill_or_not_1_1 == "n":
            vent_cafe_1_1 = input("You did not kill. Would you like to vent? (y/n): ")
            if vent_cafe_1_1 == "y":
              where_to_vent_cafe_1_1 = input("Where would you like to vent? (Weapons): ")
              if where_to_vent_cafe_1_1 == "Weapons":
                print("There aren't any people in weapons.")
                task_bar_weapons_high_1_1 = ["The task bar is getting higher. You lose the game.", "Suddenly, many people leave the game. You spot a crewmate walking out of O2."]
                choice_weapons_1_1 = random.choice(task_bar_weapons_high_1_1)
                print(f"{choice_weapons_1_1}")
                if choice_weapons_1_1 == task_bar_weapons_high_1_1[0]:
                  print("You lose the game.")
                  exit()
                if choice_weapons_1_1 == task_bar_weapons_high_1_1[1]:
                  kill_or_not_weapons_1_1 = input("Would you like to kill the crewmate? (y/n): ")
                  if kill_or_not_weapons_1_1 == "y":
                    print("You killed the crewmate.")
                    crewmates_1_1 -= 1
                  if kill_or_not_weapons_1_1 == "n":
                    where_to_go_weapons_1_1 = input("You did not kill. Where would you like to go? (Admin/Security): ")
                    if where_to_go_weapons_1_1 == "Admin":
                      print("You see no one in Admin. You return to the cafe.")
                    if where_to_go_weapons_1_1 == "Security":
                      kill_or_not_security_1_1 = input("You see two people in Security. Would you like to kill? (y/n): ")
                      if kill_or_not_security_1_1 == "y":
                        report_or_not_1_1 = ["You kill the crewmate. The other one reports it and you get voted out.", "You kill the crewmate. The other player seems to be afk and stands over the body. You vent and see another crewmate walk in. They report the body and blame the afk crewmate. You walk back to the cafe."]
                        security_dead_or_not_1_1 = random.choice(report_or_not_1_1)
                        print(f"{security_dead_or_not_1_1}")
                        if security_dead_or_not_1_1 == report_or_not_1_1[0]:
                          crewmates_1_1 -= 1
                          impostor_1_1 -= 1
                        if security_dead_or_not_1_1 == report_or_not_1_1[1]:
                          crewmates_1_1 -= 2
      if where_impostor_1_1 == "Weapons":
        weapons_crewmates_1_1 = ["There are two crewmates in weapons.", "There are no people in weapons."]
        weapons_kill_or_not_variables = random.choice(weapons_crewmates_1_1)
        if weapons_kill_or_not_variables == weapons_crewmates_1_1[0]:
          kill_or_not_weapons_first_1_1 = input("Would you like to kill the crewmate? (y/n): ")
          if kill_or_not_weapons_first_1_1 == "y":
            print("The other crewmate reports the body and blames you.")
            crewmates_1_1 -= 1
            impostor_1_1 -= 1
          if kill_or_not_weapons_first_1_1 == "n":
            where_to_go_weapons_first_1_1 = input("Where do you want to go? (Medbay/Shields): ")
            if where_to_go_weapons_first_1_1 == "Medbay":
              weapons_kill_variables_1_1 = ["There are no people in Medbay. You return to the cafe.", "There are two people in Medbay.  One seems to be afk, and the other one seems to be inspecting samples."]
              weapons_kill_variables_random_1_1 = random.choice(weapons_kill_variables_1_1)
              if weapons_kill_variables_random_1_1 == weapons_kill_variables_1_1[1]:
                kill_or_not_medbay_1_1 = input("Would you like to kill the crewmate that is inspecting sample? (y/n): ")
                if kill_or_not_medbay_1_1 == "y":
                  print("You killed the crewmate. The other crewmate is afk, as expected. You report the body and blame the afk person. They get voted out.")
                  crewmates_1_1 -= 2
                if kill_or_not_medbay_1_1 == "n":
                  print("The crewmate who was inspecting samples calls a meeting and susses you for just standing there. You get voted out.")
                  impostor_1_1 -= 1
        if weapons_kill_or_not_variables == weapons_crewmates_1_1[1]:
          vent_weapons_1_1 = input("Would you like to vent? (y/n): ")
          if vent_weapons_1_1 == "y":
            where_to_vent_weapons_1_1 = input("Where would you like to vent? (Void/Upper Engine): ")
            if where_to_vent_weapons_1_1 == "Void":
              print("You vent to the void. You get sucked into a black hole.")
              impostor_1_1 -= 1
            if where_to_vent_weapons_1_1 == "Upper Engine":
              upper_engine_kill_variables_1_1 = ["There are 2 players in Upper Engine.", "There are no players in Upper Engine."]
              upper_engine_kill_variables_random_1_1 = random.choice(upper_engine_kill_variables_1_1)
              if upper_engine_kill_variables_random_1_1 == upper_engine_kill_variables_1_1[0]:
                upper_engine_kill_variables_1_1_1 = input("Whould you like to kill (y/n): ")
                if upper_engine_kill_variables_1_1_1 == "y":
                  print("You kill and the other crewmate reports it. You get voted out.")
                  impostor_1_1 -= 1
                if upper_engine_kill_variables_1_1_1 == "n":
                  print("You don't kill. You head to the cafe.")
              if upper_engine_kill_variables_random_1_1 == upper_engine_kill_variables_1_1[1]:
                print("You head back to the cafe.")
          if vent_weapons_1_1 == "n":
            print("You head back to the cafe.")
      if where_impostor_1_1 == "Navigation":
        nav_kill_variables_1_1 = ["There is one person in Navigation.", "There are no people in Navigation."]
        nav_kill_variables_random__1_1 = random.choice(nav_kill_variables_1_1)
        print(f"{nav_kill_variables_random__1_1}")
        if nav_kill_variables_random__1_1 == nav_kill_variables_1_1[0]:
          kill_or_not_nav_1_1 = input("Would you like to kill the crewmate? (y/n): ")
          if kill_or_not_nav_1_1 == "y":
            print("You kill the crewmate and another one walks in and reports the body. You get voted out.")
            crewmates_1_1 -= 1
            impostor_1_1 -= 1
          if kill_or_not_nav_1_1 == "n":
            print("You didn't kill the crewmate.")
            where_to_go_imp_nav_1_1 = input("Where do you want to go? (Electrical/Storage): ")
            if where_to_go_imp_nav_1_1 == "Electrical":
              print("There are no people in Electrical.")
              where_elec_1_1 = input("Where do you want to go? (Reactor/Communications): ")
              if where_elec_1_1 == "Reactor":
                reactor_kill_variables_1_1 = ["There is no one in the Reactor.", "There are 3 people in the Reactor."]
                reactor_kill_variables_random_1_1 = random.choice(reactor_kill_variables_1_1)
                print(f"{reactor_kill_variables_random_1_1}")
                if reactor_kill_variables_random_1_1 == reactor_kill_variables_1_1[0]:
                  print("You head back to the cafe.")
                if reactor_kill_variables_random_1_1 == reactor_kill_variables_1_1[1]:
                  kill_or_not_reactor_1_1 = input("Would you like to kill? (y/n): ")
                  if kill_or_not_reactor_1_1 == "y":
                    print("One crewmate reports the body and gets you voted out.")
                    crewmates_1_1 -= 1
                    impostor_1_1 -= 1
                  if kill_or_not_reactor_1_1 == "n":
                    print("You do not kill. You head to the cafe.")
              if where_elec_1_1 == "Communications":
                comms_kill_variables_1_1 = ["There are two people in Comms.", "There are no crewmates in Comms."]
                comms_kill_variables_random_1_1 = random.choice(comms_kill_variables_1_1)
                if comms_kill_variables_random_1_1 == comms_kill_variables_1_1[0]:
                  print(f"{comms_kill_variables_random_1_1}")
                  kill_or_not_comms_1_1 = input("would you like to kill? (y/n): ")
                  if kill_or_not_comms_1_1 == "y":
                    print("You kill, and the other crewmate reports the body. You get voted out.")
                    crewmates_1_1 -= 1
                    impostor_1_1 -= 1
                  if kill_or_not_comms_1_1 == "n":
                    print("You head back to the cafe.")
                if comms_kill_variables_random_1_1 == comms_kill_variables_1_1[1]:
                  print(f"{comms_kill_variables_random_1_1}")
                  print("You head back to the cafe.")
        if nav_kill_variables_random__1_1 == nav_kill_variables_1_1[1]:
          if crewmates_1_1 <= 9:
            print(f"{nav_kill_variables_random__1_1}")
            print("Suddenly, someone reports a body!")
          print("Red says that they saw you kill on cams. They said that they were on their way to the body when another crewmate reported it.")
          defend_body_accusation_1_1 = input("What do you reply? (1) Do nothing. (2) Accuse them of lying. (3) Blame red. (1/2/3): ")
          if defend_body_accusation_1_1 == "1":
            print("Everyone votes you out.")
            impostor_1_1 -= 1
          if defend_body_accusation_1_1 == "2":
            print("Everyone decides to skip. They think that you are both sus and decide to vote only with solid evidence. You return to the cafe.")
          if defend_body_accusation_1_1 == "3":
            print("Everyone decides to skip. They think that you are both sus and decide to vote only with solid evidence. You return to the cafe.")
          if where_to_go_imp_nav_1_1 == "Storage":
            stor_kill_variables_1_1  = ["There is one person in Storage.", "There are two crewmates in Storage."]
            stor_kill_variables_random_1_1 = random.choice(stor_kill_variables_1_1)
            print(stor_kill_variables_random_1_1)
            if stor_kill_variables_random_1_1 == stor_kill_variables_1_1[1]:
              kill_or_not_stor_1_1_1 = input("Would you like to kill? (y/n): ")
              if kill_or_not_stor_1_1_1 == "y":
                print("Just before you are about to kill, some one calls an Emergency Meeting. They say you are sus, walking around without doing any tasks you get voted out.")
                impostor_1_1 -= 1
              if kill_or_not_stor_1_1_1 == "n":
                print("you head back to the cafe.")
            if stor_kill_variables_random_1_1 == stor_kill_variables_1_1[0]:
              print("You head back to the cafe.")
      if where_impostor_1_1 == "O2":
        O2_kill_variables_1_1 = ["There is one person in O2.", "There are 2 people in O2."]
        O2_kill_variables_random_1_1 = random.choice(O2_kill_variables_1_1)
        print(O2_kill_variables_random_1_1)
        if O2_kill_variables_random_1_1 == O2_kill_variables_1_1[0]:
          sabotage_O2_1_1 = input("Would you like to sabotage? (y/n): ")
          if sabotage_O2_1_1 == "y":
            O2_sabotage_what_1_1 = input("What would you like to sabotage? (Reactor/O2/Lights/Doors): ")
            if O2_sabotage_what_1_1 == "Reactor":
              print("Everyone runs to the Reactor and eventually fixes it. Someone calls an Emergency Meeting later, saying that you were staying still the whole time. You get voted out.")
              impostor_1_1 -= 1
            if O2_sabotage_what_1_1 == "O2":
              print("Everyone runs to O2, but no one goes to Admin. The oxygen runs out.")
              crewmates_1_1 -= 1
            if O2_sabotage_what_1_1 == "Lights":
              print("Everyone runs to Electrical. You see someone coming out from Navigation.")
              kill_or_not_O2_with_lights = input("Would you like to kill the crewmate? (y/n): ")
              if kill_or_not_O2_with_lights == "y":
                print("Suddenly, the lights turn back on. A crewmate is revealed to be standing rights next to you. They report the body.")
                crewmates_1_1 -= 1
                impostor_1_1 -= 1
              if kill_or_not_O2_with_lights == "n":
                print("You don't kill. You return to the cafe.")
            if O2_sabotage_what_1_1 == "Doors":
              doors_kill_variables_1_1 = ["There is one person standing next to you.", "There is no one next to you."]
              doors_kill_variables_random_1_1 = random.choice(doors_kill_variables_1_1)
              print(doors_kill_variables_random_1_1)
              if doors_kill_variables_random_1_1 == doors_kill_variables_1_1[0]:
                kill_or_not_O2_with_doors = input("Would you like to kill? (y/n): ")
                if kill_or_not_O2_with_doors == "y":
                  print("You kill and no one reports the body.")
                  vent_where_from_O2_1_1 = input("Where would you like to vent? (Navigation/Weapons): ")
                  if vent_where_from_O2_1_1 == "Navigation":
                    nav_kill_variables_1_1_1 = ["There is one person in Navigation.", "There are no people in Navigation."]
                    nav_kill_variables_random_1_1_1 = random.choice(nav_kill_variables_1_1_1)
                    print(nav_kill_variables_random_1_1_1)
                    if nav_kill_variables_random_1_1_1 == nav_kill_variables_1_1_1[0]:
                      kill_or_not_nav_1_1_1 = input("Would you like to kill? (y/n): ")
                      if kill_or_not_nav_1_1_1 == "y":
                        print("You kill.")
                        where_to_vent_nav_1_1 = input("Where would you like to vent? (Security/Admin): ")
                        if where_to_vent_nav_1_1 == "Security":
                          security_kill_variables_1_1  = ["There are two people in Security.", "There is one crewmate in Security."]
                          security_kill_variables_random_1_1 = random.choice(security_kill_variables_1_1)
                          print(security_kill_variables_random_1_1)
                          if security_kill_variables_random_1_1 == security_kill_variables_1_1[0]:
                            kill_or_not_security_1_1_1 = input("Would you like to kill? (y/n): ")
                            if kill_or_not_security_1_1_1 == "y":
                              crewmates_1_1 -= 1
                              report_ot_not_security_1_1_variables = ["The other crewmate reports the body.", "The other crewmate, seemingly afk, does nothing."]
                              report_ot_not_security_1_1_variables_random = random.choice(report_ot_not_security_1_1_variables)
                              print(report_ot_not_security_1_1_variables_random)
                              if report_ot_not_security_1_1_variables_random == report_ot_not_security_1_1_variables[0]:
                                print("You get voted out.")
                                impostor_1_1 -= 1
                              if report_ot_not_security_1_1_variables_random == report_ot_not_security_1_1_variables[1]:
                                vent_or_not_security_1_1 = input("Would you like to vent? (y/n): ")
                                if vent_or_not_security_1_1 == "y":
                                  where_to_vent_security_1_1 = input("Where would you like to vent? (Lower Engine/Electrical): ")
                                  if where_to_vent_security_1_1 == "Lower Engine":
                                    lower_engine_kill_variables_1_1 = ["There is one person in Lower Engine.", "There are no crewmates in Lower Engine."]
                                    lower_engine_kill_variables_random_1_1 = random.choice(lower_engine_kill_variables_1_1)
                                    print(lower_engine_kill_variables_random_1_1)
                                    if lower_engine_kill_variables_random_1_1 == lower_engine_kill_variables_1_1[0]:
                                      kill_or_not_lower_engine_1_1 = input("Would you like to kill? (y/n): ")
                                      if kill_or_not_lower_engine_1_1 == "y":
                                        print("You kill. You return to the cafe.")
                                      if kill_or_not_lower_engine_1_1 == "n":
                                        where_to_go_from_lower_engine_1_1 = input("Where would you like to go? (Medbay/Cafeteria): ")
                                        if where_to_go_from_lower_engine_1_1 == "Medbay":
                                          medbay_kill_variables_1_1 = ["There is one person in Medbay.", "There are two people in Medbay."]
                                          medbay_kill_variables_random_1_1 = random.choice(medbay_kill_variables_1_1)
                                          print(medbay_kill_variables_random_1_1)
                                          if medbay_kill_variables_random_1_1 == medbay_kill_variables_1_1[0]:
                                            kill_or_not_medbay_1_1_1 = input("Would you like to kill? (y/n): ")
                                            if kill_or_not_medbay_1_1_1 == "y":
                                              print("You kill, then return the the cafe.")
                                            if kill_or_not_medbay_1_1_1 == "n":
                                              print("You return to the cafe.")
                                          if medbay_kill_variables_random_1_1 == medbay_kill_variables_1_1[1]:
                                            kill_or_not_medbay_1_1_1_1 = input("Would you like to kill? (y/n): ")
                                            if kill_or_not_medbay_1_1_1_1 == "y":
                                              crewmates_1_1 -= 1
                                              print("The other crewmate reports the body. They say that you killed the crewmate.")
                                              report_body_defense_medbay_1_1 = input("What do you say in defense? ((1) No! It was a self report!/(2) No!/(3) It's me.)")
                                              if report_body_defense_medbay_1_1 == "1":
                                                print("Everyone agrees that is sus and votes you out.")
                                                impostor_1_1 -= 1
                                              if report_body_defense_medbay_1_1 == "2":
                                                print("Everyone agrees that is sus and votes you out.")
                                                impostor_1_1 -= 1
                                              if report_body_defense_medbay_1_1 == "3":
                                                print("Everyone thinks that you are a troll. They let you live.")
                                            if kill_or_not_medbay_1_1_1_1 == "n":
                                              print("You head back to the cafe.")
                                    if lower_engine_kill_variables_random_1_1 == lower_engine_kill_variables_1_1[1]:
                                      print("You head back to the cafe.")
                                  if where_to_vent_security_1_1 == "Electrical":
                                    if crewmates_1_1 == 10:
                                      print("There are no people in Electrical. You return to the cafe.")
                                    if crewmates_1_1 <= 9:
                                      print("Someone calls a meeting. They say you are sus, randomly walking everywhere.")
                                      voted_out_or_not_1_1 = ["You get voted out.", "They decide that they're not sure if you are the impostor, so you survive.", "They decide that they're not sure if you are the impostor, so you survive."]
                                      voted_out_or_not_random_1_1 = random.choice(voted_out_or_not_1_1)
                                      print(voted_out_or_not_random_1_1)
                                      if voted_out_or_not_random_1_1 == voted_out_or_not_1_1[0]:
                                        impostor_1_1 -= 1
                                      if voted_out_or_not_random_1_1 == voted_out_or_not_1_1[1] or voted_out_or_not_1_1[2]:
                                        print("...")
                                if vent_or_not_security_1_1 == "n":
                                  where_to_go_security_1_1 = input("Where would you like to go? (Storage/O2): ")
                                  if where_to_go_security_1_1 == "Storage":
                                    storage_kill_vars_1_1 = ["There is no one in Storage.", "There are two people in Storage."]
                                    storage_kill_vars_random_1_1 = random.choice(storage_kill_vars_1_1)
                                    print(storage_kill_vars_random_1_1)
                                    if storage_kill_vars_random_1_1 == storage_kill_vars_1_1[0]:
                                      vent_or_not_stor_1_1 = input("Would you like to vent? (y/n): ")
                                      if vent_or_not_stor_1_1 == "y":
                                        where_to_vent_stor_1_1 = input("Where would you like to vent? (Admin/Reactor): ")
                                        if where_to_vent_stor_1_1 == "Admin":
                                          admin_kill_vars_1_1 = ["There are 2 players in Admin", "There are no players in Admin."]
                                          admin_kill_vars_random_1_1 = random.choice(admin_kill_vars_1_1)
                                          print(admin_kill_vars_random_1_1)
                                          if admin_kill_vars_random_1_1 == admin_kill_vars_1_1[0]:
                                            kill_or_not_Admin_1_1 = input("Would you like to kill? (y/n): ")
                                            if kill_or_not_Admin_1_1 == "y":
                                              crewmates_1_1 -= 1
                                              print("The other person reports the body. They say you killed.")
                                              body_report_defense_admin_1_1 = input("What is your defense? ((1) No!/(2) No! It was a self-report!/(3) It's me.)")
                                              if body_report_defense_admin_1_1 == "1" or "2":
                                                print("The crew decides to vote only when they are sure.")
                                              if body_report_defense_admin_1_1 == "3":
                                                print("The crew votes you out.")
                                                impostor_1_1 -= 1
                                            if kill_or_not_Admin_1_1 == "n":
                                              where_to_go_admin_1_1 = input("Where would you like to go? (Shields/Navigation): ")
                                              print("There is no one there. You return to the cafe.")
                                          if admin_kill_vars_random_1_1 == admin_kill_vars_1_1[1]:
                                            where_to_go_admin_1_1_1 = input("Where would you like to go? (Upper Engine/Weapons): ")
                                            if where_to_go_admin_1_1_1 == "Upper Engine":
                                              upper_engine_kill_vars_1_1 = ["There is one human in Upper Engine.", "There are no humans in Upper Engine."]
                                              upper_engine_kill_vars_random_1_1 = random.choice(upper_engine_kill_vars_1_1)
                                              print(upper_engine_kill_vars_random_1_1)
                                              if upper_engine_kill_vars_random_1_1 == upper_engine_kill_vars_1_1[0]:
                                                kill_or_not_up_1_1 = input("Would you like to kill? (y/n): ")
                                                if kill_or_not_up_1_1 == "y":
                                                  crewmates_1_1 -= 1
                                                  print("You kill. Suddenly, a crewmate walks in and reports the body! They say that you killed.")
                                                  up_report_body_defense_1_1 = input("What is your defense? ((1) LIAR! IT WAS A SELF REPORT!!!/(2) I think they are a troll./(3) It's me.): ")
                                                  if up_report_body_defense_1_1 == "2":
                                                    print('One of them says, "But I think you are the impostor." You get voted out.')
                                                    impostor_1_1 -= 1
                                                  if up_report_body_defense_1_1 == "3":
                                                    impostor_1_1 -= 1
                                                  if up_report_body_defense_1_1 == "1":
                                                    print("The crew decides not to vote anyone out.")
                                                if kill_or_not_up_1_1 == "n":
                                                  to_go_from_up_1_1 = input("Where would you like to go? (Storage/Electrical): ")
                                                  print("There is no one there. You return to the cafe.")
                                              if upper_engine_kill_vars_random_1_1 == upper_engine_kill_vars_1_1[1]:
                                                print("You return to the cafe.")
                                            if where_to_go_admin_1_1_1 == "Weapons":
                                              wps_kill_vars_1_1 = ["There are 2 earthlings in Weapons.", "There are no earthlings in Weapons."]
                                              wps_kill_vars_random_1_1 = random.choice(wps_kill_vars_1_1)
                                              print(wps_kill_vars_random_1_1)
                                              if wps_kill_vars_random_1_1 == wps_kill_vars_1_1[0]:
                                                kill_or_not_wps_1_1 = input("Would you like to kill? (y/n): ")
                                                if kill_or_not_wps_1_1 == "y":
                                                  crewmates_1_1 -= 1
                                                  print("The other crewmate reports the body. You die.")
                                                  impostor_1_1 -= 1
                                                if kill_or_not_wps_1_1 == "n":
                                                  print("You return to the cafe.")
                                              if wps_kill_vars_random_1_1 == wps_kill_vars_1_1[1]:
                                                print("You go back to the cafe.")
                                        if where_to_vent_stor_1_1 == "Reactor":
                                          rctr_kill_vars_1_1 = ["There are 2 people in Reactor.", "There are no earthlings in Reactor."]
                                          rctr_kill_vars_random_1_1 = random.choice(rctr_kill_vars_1_1)
                                          print(rctr_kill_vars_random_1_1)
                                          if rctr_kill_vars_random_1_1 == rctr_kill_vars_1_1[0]:
                                            rctr_k_o_n_1_1 = input("Would you like to kill? (y/n): ")
                                            if rctr_k_o_n_1_1 == "y":
                                              crewmates_1_1 -= 1
                                              print("You kill, and the other personage reports it. They say that you killed the other earthling.")
                                              def_bod_acc_rctr_1_1 = input("What is you defense? ((1) No./(2) It was a self report!(3) It's me.)")
                                              if def_bod_acc_rctr_1_1 == "1" or "3":
                                                print("The mortals think that you are sus and vote you out.")
                                                impostor_1_1 -= 1
                                              if def_bod_acc_rctr_1_1 == "2":
                                                print("The crew doesn't vote anyone out.")
                                            if rctr_k_o_n_1_1 == "n":
                                              where_to_go_rctr_1_1 = input("Where would you like to go? (Security/Admin): ")
                                              if where_to_go_rctr_1_1 == "Security":
                                                scty_kill_vars_1_1 = ["There are no humans in Security.", "There are two people in Security."]
                                                scty_kill_vars_random_1_1  = random.choice(scty_kill_vars_1_1)
                                                print(scty_kill_vars_random_1_1)
                                                if scty_kill_vars_random_1_1 == scty_kill_vars_1_1[0]:
                                                  where_to_go_from_scty_1_1 = input("Where would you like to go? You can choose anywhere! ")
                                                  print(f"There is no one in {where_to_go_from_scty_1_1}.")
                                                if scty_kill_vars_random_1_1 == scty_kill_vars_1_1[1]:
                                                  k_o_n_scty_1_1 = input("Would you like to kill? (y/n): ")
                                                  if k_o_n_scty_1_1 == "y":
                                                    crewmates_1_1 -= 1
                                                    print("The other earthling reports the body. They say you killed the crewmate.")
                                                    impostor_1_1 -= 1
                                                  if k_o_n_scty_1_1 == "n":
                                                    w_t_g_f_scty_1_1 = input("Where would you like to go? (Reactor/Communications): ")
                                                    if w_t_g_f_scty_1_1 == "Reactor":
                                                      rctr_k_v_1_1_1 = ["There are no personages in Reactor.", "There is one person in Reactor."]
                                                      rctr_k_v_random_1_1_1 = random.choice(rctr_k_v_1_1_1)
                                                      print(rctr_k_v_random_1_1_1)
                                                      if rctr_k_v_random_1_1_1 == rctr_k_v_1_1_1[0]:
                                                        w_t_g_rctr_1_1 = input("Where yould you like to go? (Shields/Weapons): ")
                                                        if w_t_g_rctr_1_1 == "Shields":
                                                          shlds_k_v_1_1 = ["There are 2 people in Shields.", "There is one person in Shields."]
                                                          shlds_k_v_rdm_1_1 = random.choice(shlds_k_v_1_1)
                                                          print(shlds_k_v_rdm_1_1)
                                                          if shlds_k_v_rdm_1_1 == shlds_k_v_1_1[0]:
                                                            k_o_n_shlds_1_1 = input("Would you like to kill? (y/n): ")
                                                            if k_o_n_shlds_1_1 == "y":
                                                              crewmates_1_1 -= 1
                                                              print("You kill, and someone reports the body.")
                                                              impostor_1_1 -= 1
                                                            if k_o_n_shlds_1_1 == "n":
                                                              print("You go back to the cafe.")
                                                          if shlds_k_v_rdm_1_1 == shlds_k_v_1_1[1]:
                                                            k_o_n_shlds_1_1_1 = input("Would you like to kill? (y/n): ")
                                                            if k_o_n_shlds_1_1_1 == "y":
                                                              print("You kill, and somebody walks in and reports the body. They say that you killed the crewmate.")
                                                              d_b_a_s_1_1 = input("What is your defense? ((1)No! (2)No! It was a self report! (3)Ok. It's me.): ")
                                                              if d_b_a_s_1_1 == "1" or "2":
                                                                print("They vote out the reporter.")
                                                                crewmates_1_1 -= 1
                                                              if d_b_a_s_1_1 == "3":
                                                                print("You are voted out.")
                                                                impostor_1_1 -= 1
                                                            if k_o_n_shlds_1_1_1 == "n":
                                                              print("Congrats! You have found an easter egg! You automatically win the game.")
                                                              exit()
                                                        if w_t_g_rctr_1_1 == "Weapons":
                                                          wpns_k_v_1_1 = ["There is one earthling in Weapons.", "There are no people in Weapons."]
                                                          wpns_k_v_random_1_1 = random.choice(wpns_k_v_1_1)
                                                          print(wpns_k_v_random_1_1)
                                                          if wpns_k_v_random_1_1 == wpns_k_v_1_1[0]:
                                                            k_o_n_wpns_1_1 = input("Would you like to kill? (y/n):")
                                                            if k_o_n_wpns_1_1 == "y":
                                                              print("You kill. Suddenly, someone walks in and reports the body and blames you!")
                                                              r_b_d_wpns_1_1 = input("What is your defense? ((1)I think it was a self-report. (2)I think they are a troll.): ")
                                                              print("They vote the reporter out.")
                                                              crewmates_1_1 -= 1
                                                            if k_o_n_wpns_1_1 == "n":
                                                              print("You head back to the cafe.")
                                                          if wpns_k_v_random_1_1 == wpns_k_v_1_1[1]:
                                                            w_t_g_wpns_1_1 = input("Where would you like to go? You can go anywhere. (Admin/Security/etc.): ")
                                                            print(f"There are no people in {w_t_g_wpns_1_1}.")
                                                      if rctr_k_v_random_1_1_1 == rctr_k_v_1_1_1[1]:
                                                        k_o_n_rctr_1_1 = input("Would you like to kill? (y/n): ")
                                                        if k_o_n_rctr_1_1 == "y":
                                                          crewmates_1_1 -= 1
                                                          print("You kill, and someone walks in and reports the body. They say you killed!")
                                                          d_f_r_b_rctr_1_1 = input("What is your defense? ((1)No! Liar! (2)No! It was a self-report! (3)It's me. ): ")
                                                          if d_f_r_b_rctr_1_1 == "1" or "2":
                                                            print("They vote the reporter out.")
                                                            crewmates_1_1 -= 1
                                                          if d_f_r_b_rctr_1_1 == "3":
                                                            print("The crewmates vote you out.")
                                                            impostor_1_1 -= 1
                                                        if k_o_n_rctr_1_1 == "n":
                                                          w_t_v_rctr_1_1 = input("Where would you like to vent? (Random/Security): ")
                                                          print("There isn't anyone there. You head back to the cafe.")
                                          if rctr_kill_vars_random_1_1 == rctr_kill_vars_1_1[1]:
                                            print("There is no one there. You return to the cafe.")
                                      if vent_or_not_stor_1_1 == "n":
                                        print("You head back to the cafe.")
                                    if storage_kill_vars_random_1_1 == storage_kill_vars_1_1[1]:
                                      k_o_n_stre_1_1 = input("Would you like to kill? (y/n): ")
                                      if k_o_n_stre_1_1 == "y":
                                        crewmates_1_1 -= 1
                                        print("You kill, and the other crewmate reports the body. They blame you.")
                                        d_e_f_r_b_stre_1_1 = input("What is your defense? ((1)No! (2)It was a self report! (3)They are a troll.): ")
                                        if d_e_f_r_b_stre_1_1 == "2" or "3":
                                          print("The reporter get voted out.")
                                          crewmates_1_1 -= 1
                                        if d_e_f_r_b_stre_1_1 == "1":
                                          print("The crew votes you out.")
                                          impostor_1_1 -= 1
                                      if k_o_n_stre_1_1 == "n":
                                          print("You head back to the cafe.")
                                  if where_to_go_security_1_1 == "O2":
                                    print("There are no people in O2. You go back to the cafe.")
                            if kill_or_not_security_1_1_1 == "n":
                              print("You head back to the cafe.")
                          if security_kill_variables_random_1_1 == security_kill_variables_1_1[1]:
                            k_o_n_scty_1_1_1 = input("Would you like to kill? (y/n): ")
                            if k_o_n_scty_1_1_1 == "y":
                              print("The crewmate runs away before you can kill. You head back to the cafe.")
                            if k_o_n_scty_1_1_1 == "n":
                              print("You return to the cafe.")
                        if where_to_vent_nav_1_1 == "Admin":
                          print("There aren't any people in Admin. You return to the cafe.")
                      if kill_or_not_nav_1_1_1 == "n":
                        print("You return to the cafe.")
                    if nav_kill_variables_random_1_1_1 == nav_kill_variables_1_1_1[1]:
                      print("You return to the cafe.")
                  if vent_where_from_O2_1_1 == "Weapons":
                    print("There are no people in Weapons. You return to the cafe.")
                if kill_or_not_O2_with_doors == "n":
                  print("You return to the cafe.")
              if doors_kill_variables_random_1_1 == doors_kill_variables_1_1[1]:
                print("You vent back to the cafe. ")
          if sabotage_O2_1_1 == "n":
            print("You head back to the cafe.")
        if O2_kill_variables_random_1_1 == O2_kill_variables_1_1[1]:
          kon_O2_1_1 = input("Would you like to kill? (y/n): ")
          if kon_O2_1_1 == "y":
            crewmates_1_1 -= 1
            print("You kill the crewmate, then return to the cafe.")
          if kon_O2_1_1 == "n":
            print("You head back to the cafe.")
      if where_impostor_1_1 == "Shields":
        shld_k_v_1_1 = ["There are no people in Shields.", "There are two people in Shields."]
        shld_k_v_rdm_1_1 = random.choice(shld_k_v_1_1)
        print(shld_k_v_rdm_1_1)
        if shld_k_v_rdm_1_1 == shld_k_v_1_1[0]:
          wtg_shld_1_1 = input("Where would you like to go? (Admin/Reactor): ")
          if wtg_shld_1_1 == "Admin":
            adm_k_v_1_1 = ["There is one person in Admin.", "There are two people in Admin."]
            adm_k_v_rdm_1_1 = random.choice(adm_k_v_1_1)
            print(adm_k_v_rdm_1_1)
            if adm_k_v_rdm_1_1 == adm_k_v_1_1[0]:
              k_o_n_adm_1_1 = input("Would you like to kill? (y/n): ")
              if k_o_n_adm_1_1 == "y":
                crewmates_1_1 -= 1
                r_o_n_adm_1_1 = input("Would you like to report the body? (y/n): ")
                print("Suddenly, someone walks in and reports the body for you. They blame you.")
                def_r_b_adm_1_1 = input("What is your defense? ((1)No! (2)It's me.): ")
                print("Someone says tan vented, even though there is no tan. The crew decides to vote out the troll, and forgets about you.")
              if k_o_n_adm_1_1 == "n":
                wtg_adm_1_1 = input("Where would you like to go? (Admin/Security): ")
                if wtg_adm_1_1 == "Admin":
                  adm_k_v_1_1_1 = ["There is one person in Admin.", "There are two crewmates in Admin."]
                  adm_k_v_rdm_1_1 = random.choice(adm_k_v_1_1_1)
                  print(adm_k_v_rdm_1_1)
                  if adm_k_v_rdm_1_1 == adm_k_v_1_1_1[0]:
                    kon_adm_1_1 = input("Would you like to kill? (y/n): ")
                    crewmates_1_1 -= 1
                    if kon_adm_1_1 == "y":
                      print("You kill.")
                      wtg_adm_1_1_1 = input("Where would you like to go? (Electrical/Shields): ")
                      if wtg_adm_1_1_1 == "Electrical":
                        ecrcl_k_v_1_1 = ["There are two people in Electrical.", "There is one person in Electrical."]
                        ecrcl_k_v_rdm_1_1 = random.choice(ecrcl_k_v_1_1)
                        print(ecrcl_k_v_rdm_1_1)
                        if ecrcl_k_v_rdm_1_1 == ecrcl_k_v_1_1[0]:
                          kon_admm_1_1 = input("Would you like to kill? (y/n): ")
                          if kon_admm_1_1 == "y":
                            crewmates_1_1 -= 1
                            print("You kill, and an earthling reports the body. They blame you. the crew votes you out.")
                            impostor_1_1 -= 1
                          if kom_admm_1_1 == "n":
                            w_admm_t_1_g_1 = input("Where would you like to go? (Reactor/Weapons): ")
                            if w_admm_t_1_g_1 == "Reactor":