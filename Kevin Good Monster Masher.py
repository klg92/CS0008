import random

print ("Welcome to Monster Masher by Kevin Good!")


while True:
    random.seed()
    start = input("Do you want to play? [yes/no]")
    if start == "yes":
        while True:
            player_health = random.randint(20, 40)
            player_attack = random.randint(30, 50)
            victory_count = 5
            the_round = 0
            while True:
                if the_round < 6:
                    monster_health = random.randint(25, 45)
                    monster_attack = random.randint(15, 30)
                elif the_round > 5 and the_round < 11:
                    monster_health = random.randint(30, 50)
                    monster_attack = random.randint(25, 40)
                elif the_round > 10:
                    monster_health = random.randint(35, 55)
                    monster_attack = random.randint(35, 50)
                droproll = random.random()
                
                the_round = the_round + 1
                print("-------------------------------------------------------------------\nROUND ", the_round, "!!!")
                print("You need to defeat ", victory_count, " more monsters to win!")
                print("Your health is ", player_health, " and your attack is ", player_attack)
                print("\nOh no! A monster approaches! it's health is ", monster_health, " and it's attack is ", monster_attack, "!\n")
                while True:
                    choice = input(" Do you want to fight or retreat?")
                    if choice == "fight":
                        break
                    elif choice == "retreat":
                        break
                    else:
                        print("INVALID SYNTAX.")
                if choice == "fight" and monster_health - player_attack <= 0 and player_health - monster_attack > 0:
                    victory_count = victory_count - 1
                    print ("\nYou won the round! the monster is dead!")
                    if droproll >= 0.75:
                        print ("Wow! The monster dropped a health and attack upgrade!")
                        player_health = player_health + 3
                        player_attack = player_attack + 3
                    elif droproll < 0.75 and droproll >= .50 :
                        print("The monster dropped health upgrade!")
                        player_health = player_health + 3
                    elif droproll < .50 and droproll >= .25 :
                        print("The monster dropped an attack upgrade!")
                        player_attack =  player_attack + 3
                    else:
                        print("The monster didn't drop anything.")
                elif choice == "fight" and player_health - monster_attack <= 0 :
                    print ("You died. The kingdom is doomed. \nYOU LOST\n")
                    break
                elif choice == "fight" and player_health - monster_attack > 0 and monster_health - player_attack > 0 :
                    print ("You both fought hard, but neither died. The Monster lives to fight another day. ")
                elif choice == "retreat":
                    print ("You retreated.")
                if victory_count == 0:
                    print("\nYOU WON!!!!! CONGRATULATIONS!!!!!\n")
                    break
                elif the_round == 15 and victory_count != 0:
                    print("You ran out of time.\nYOU LOSE\n")
                    break
            break        
                    
    elif start == "no":
        print("Goodbye!")
        break
    else:
        print("INVALID SYNTAX.")
    
    


