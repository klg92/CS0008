print ("Welcome to Tic Tac Toe by Kevin Good!")
board = input("What file is being used as the board? ")


real_rows = []
#add the empty board to real_rows list
file = open (board, "r+")
rows = file.readlines()
file.close()
for item in rows:
    result = ""
    new = item.strip()
    result = result + new
    real_rows.append(result)
#variables to count stuff
number_of_x = 0
number_of_o = 0
gamewon = False
turn = 1

player = input("Are you going to be X or O? [use capital letter]: ")
while gamewon == False:
    #taking in current boardstate
    file = open (board, "w") 
    file.close()
    
    file2 = open(board, "r+")
    rows2 = file2.readlines()
    for item in rows2:
        result = ""
        new = item.strip()
        result = result + new
        real_rows.append(result)
    for item in real_rows:
        file2.write(item)
        file2.write("\n")
    file2.close()
    turn = turn + 1
    print ("Game Status:")
    print (real_rows[0],real_rows[1],real_rows[2], sep = "")
    print (real_rows[3],real_rows[4],real_rows[5], sep = "")
    print (real_rows[6],real_rows[7],real_rows[8], sep = "")
    
    # Entering a Move
    while True:
        check = input("is it your turn?")
        if check == "yes":
            break
    if turn > 3 and real_rows[0] == "[]":
        if real_rows[0] == real_rows[1] == real_rows[2] == real_rows[3] == real_rows[4] == real_rows[5] == real_rows[6] == real_rows[7] == real_rows[8]:
            if player == "X":
                print ("You lost. The winner is O")
            elif player == "O":
                print ("You lost. The winner is X")
            break
    count = -1
    for item in rows2:
        count = count + 1
        result = ""
        new = item.strip()
        result = result + new
        real_rows[count] = result
    print ("Game Status:")
    print (real_rows[0],real_rows[1],real_rows[2], sep = "")
    print (real_rows[3],real_rows[4],real_rows[5], sep = "")
    print (real_rows[6],real_rows[7],real_rows[8], sep = "")
    print ("X goes first. DON'T CHEAT.")
    move_row = input("Select row for move [0-2]: ")
    move_column = input ("Select column for move [0-2]: ")
    rownum = int(move_row)
    columnnum = int(move_column)

    # Win Conditions
    if real_rows[0] != "[]":
        if real_rows[0] == real_rows[1] == real_rows[2] or real_rows[0] == real_rows[4] == real_rows[8] or real_rows[0] == real_rows[3] == real_rows[6]:
            gamewon = True
    if real_rows[1] != "[]":
        if real_rows[1] == real_rows[4] == real_rows[7]:
            gamewon = True
    if real_rows[2] != "[]":
        if real_rows[2] == real_rows[5] == real_rows[8]:
            gamewon = True
        elif real_rows[2] == real_rows [4] == real_rows [6]:
            gamewon = True
    if real_rows[3] != "[]":
        if real_rows[3] == real_rows[4] == real_rows[5]:
            gamewon = True
    if real_rows[6] != "[]":
        if real_rows[6] == real_rows[7] == real_rows[8]:
            gamewon = True
            
    # Making a Move        
    if player == "X":
        if rownum == 0 and real_rows[columnnum] == "[]":
            real_rows[columnnum] = "[X]"
            number_of_x = number_of_x + 1
        elif rownum == 1 and real_rows[columnnum + 3] == "[]":
            real_rows[columnnum + 3] = "[X]"
            number_of_x = number_of_x + 1
        elif rownum == 2 and real_rows[columnnum + 6] == "[]":
            real_rows[columnnum + 6] = "[X]"
            number_of_x = number_of_x + 1
        else:
            print ("you've lost a turn! stop cheating!")
            
    elif player == "O":
        if rownum == 0 and real_rows[columnnum] == "[]":
            real_rows[columnnum] = "[O]"
            number_of_o = number_of_o + 1
        elif rownum == 1 and real_rows[columnnum + 3] == "[]":
            real_rows[columnnum + 3] = "[O]"
            number_of_o = number_of_o + 1
        elif rownum == 2 and real_rows[columnnum + 6] == "[]":
            real_rows[columnnum + 6] = "[O]"
            number_of_o = number_of_o + 1
            
    turn = turn + 1
    
    # Win conditions Again
    if real_rows[0] != "[]":
        if real_rows[0] == real_rows[1] == real_rows[2] or real_rows[0] == real_rows[4] == real_rows[8] or real_rows[0] == real_rows[3] == real_rows[6]:
            gamewon = True
    if real_rows[1] != "[]":
        if real_rows[1] == real_rows[4] == real_rows[7]:
            gamewon = True
    if real_rows[2] != "[]":
        if real_rows[2] == real_rows[5] == real_rows[8]:
            gamewon = True
        elif real_rows[2] == real_rows [4] == real_rows [6]:
            gamewon = True
    if real_rows[3] != "[]":
        if real_rows[3] == real_rows[4] == real_rows[5]:
            gamewon = True
    if real_rows[6] != "[]":
        if real_rows[6] == real_rows[7] == real_rows[8]:
            gamewon = True
    
# Display who wins
if player == "X":
    print ("The winner is ", player)
else:
    print ("The Winner is", player)
    
# Clear Board
file3 = open(board, "w")
file3.close()
#rewrite empty spaces
file4 = open (board, "r+")
count = 0
while count < 9:
    file4.write("[]")
    file4.write("\n")
    count = count + 1
file4.close()


