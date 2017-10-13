# Simple Sim Railroad by Kevin Good
def printline ():
    return print (" A     B     C      D\n",train_line[0]+train_line[1]+train_line[2]+train_line[3]+train_line[4]+train_line[5]+train_line[6]+train_line[7]+train_line[8]+train_line[9]+train_line[10]+train_line[11]+train_line[12]+train_line[13]+train_line[14]+train_line[15]+train_line[16]+train_line[17]+train_line[18]+train_line[19])

    
train_count = -1
my_trains = []
my_stations = {"A":0, "B":6, "C":12, "D":19}
train_line = ['=',"=","=","=","=","=","=","=","=","=","=","=","=","=","=","=","=","=","=","=",]
train_visuals  = ["E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
combined_dictionary = {}
position_count = {"E" : 0, "F": 0, "G": 0, "H" : 0}

while True:
    print ("Welcome to Kevin Good's Railroad Simulator!")
    
    while True:
        print("\nRailroad Status:")
        for item in combined_dictionary:
            print ("Train ",item, " is ", combined_dictionary[item])
        
        printline()
        user = input ("\nAvailable Commands\n1.Create a Train\n2.Move a Train\n3.Exit Program\nSelect a command: ")
        
        if user == "1":
            train_count = train_count + 1
            train_name = input("Name your train: ")
            train_assignment = input("Will the train start at station A, B, C, or D? ")
            my_trains.append ( train_name )
            combined_dictionary[train_visuals[train_count]] = my_trains[train_count]
            if train_assignment == "A":
                if train_line[0] == "=":
                    train_line[0] = train_visuals[train_count]
                else:
                    print ("\nERROR: Station A's track is full!\n")
            elif train_assignment == "B":
                if train_line[6] == "=":
                    train_line[6] = train_visuals[train_count]
                    position_count[train_visuals[train_count]] = 6 
                else:
                    print ("Station B's track is full!")
            elif train_assignment == "C":
                if train_line [12] == "=":
                    train_line[12] = train_visuals[train_count]
                    position_count[train_visuals[train_count]] = 12
                else:
                    print("Station C's track is full!")
            elif train_assignment == "D":
                if train_line[19] == "=":
                    train_line[19] = train_visuals[train_count]
                    position_count[train_visuals[train_count]] = 19
                else:
                    print("Station D's track is full!")
            else:
                print ("ERROR")
        if user == "2":
            train_movement = input("Which train are you moving?(use letter symbol): ")
            train_direction = input("Towards which station are you moving? (Capital letter please): ")
            if train_count == -1:
                print ("\nERROR: There aren't any trains to move!")
                
            elif position_count[train_movement] == my_stations[train_direction]:
                train_line[position_count[train_movement]] = "="
                position_count[train_movement] = 0
                del combined_dictionary[train_movement]
                print ("Train ", train_movement, " has been removed from the railroad.")
                
            elif position_count[train_movement] > my_stations[train_direction]:
                if train_line[position_count[train_movement]-1] is not "=":
                    print ("\nERROR: There's a train in the way!")
                else:
                    train_line[position_count[train_movement]-1] = train_line[position_count[train_movement]]
                    train_line[position_count[train_movement]] = "="
                    position_count[train_movement] = position_count[train_movement] - 1
                    
            elif position_count[train_movement] < my_stations[train_direction]:
                if train_line[position_count[train_movement]+1] is not "=":
                    print ("\nERROR: There's a train in the way!")
                else:
                    train_line[position_count[train_movement]+1] = train_line[position_count[train_movement]]
                    train_line[position_count[train_movement]] = "="
                    position_count[train_movement] = position_count[train_movement] + 1

            else:
                print("ERROR")

        
        if user == "3":
            break
        if user != "1" and user != "2" and user != "3":
            print ("\nERROR: invalid command.")
    print ("Goodbye!")
    break
