import random

#dictionary to convert random numbers to letters
letters = {1: 'a', 2:'b', 3:'c',4:'d',5:'e', 6:'f', 7:'g', 8:'h', 9:'i',
           10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q',
           18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y',
           26:'z'}
# dictionary to convert letters to score
scores = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8,
          'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1,
          'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}
#holds the board
board = []

#lists to detect connectivity of letters
psfl = []
psfl2 = []
positionsOfLetters = []

#opens dictionary file and adds lines to list 
file = open("dict.txt", 'r')
legalwords = file.readlines()

#holds words already guessed by player
guessedWords = []

#total score of player
score = 0

#these three functions randomly generate a 4x4 board and print it
def randomLetter():
    randomNumber = random.randint(1, 26)
    return letters[randomNumber]

def generateBoard():
    i = 0
    while i < 16:
        board.append(randomLetter())
        i = i + 1
    
def printBoard():
    print(board[0], board[1], board[2], board[3])
    print(board[4], board[5], board[6], board[7])
    print(board[8], board[9], board[10], board[11])
    print(board[12], board[13], board[14], board[15])

#see if user input is a word
def isAWord(string):
    for words in legalwords:
        if words == string and len(string) > 2:
            return True
    print ("not a word")
    return False

def isNotGuessed(string):
    for words in guessedWords:
        if string == words:
            print ("that word has been guessed already!")
            return False
    return True

#find how many times a letter shows up
def detectNumberOfOccurences(char):
    count = 0
    for letter in board:
        if letter == char:
            count = count + 1
    return count

#see if letters in user input are on board
def isOnBoard(word):
    lettersInWord = []
    count = 0
    while count < (len(word)-1):
        if detectNumberOfOccurences(word[count]) == 0:
            print (word, "is not on board")
            return False
        count = count + 1
    return True
#see if two spaces are connected
def areSpacesConnected(base, test):
    if base == 0 and (test == 1 or test == 4  or test == 5):
        return True
    elif base == 1 and (test == 0 or test == 2 or test == 4 or test == 5 or test == 6):
        return True
    elif base == 2 and (test == 1 or test == 3 or test == 5 or test == 6 or test == 7):
        return True
    elif base == 3 and (test == 2 or test == 6 or test == 7):
        return True
    elif base == 4 and (test == 0 or test == 1 or test == 5 or test == 8 or test == 9):
        return True
    elif base == 5 and (test == 0 or test == 1 or test == 2 or test == 4 or test == 6 or test == 8 or test == 9 or test == 10):
        return True
    elif base == 6 and (test == 1 or test == 2 or test == 3 or test == 5 or test == 7 or test == 9 or test == 10 or test == 11):
        return True
    elif base == 7 and (test == 2 or test == 3 or test == 6 or test == 10 or test == 11):
        return True
    elif base == 8 and (test == 4 or test == 5 or test == 9 or test == 12 or test == 13):
        return True
    elif base == 9 and (test == 4 or test == 5 or test == 6 or test == 8 or test == 10 or test == 12 or test == 13 or test == 14):
        return True
    elif base == 10 and (test == 5 or test == 6 or test == 7 or test == 9 or test == 11 or test == 13 or test == 14 or test == 15):
        return True
    elif base == 11 and (test == 6 or test == 7 or test == 10 or test == 14 or test == 15):
        return True
    elif base == 12 and (test == 8 or test == 9 or test == 13):
        return True
    elif base == 13 and (test == 8 or test == 9 or test == 10 or test == 12 or test == 14):
        return True
    elif base == 14 and (test == 9 or test == 10 or test == 11 or test == 13 or test == 15):
        return True
    elif base == 15 and (test == 10 or test == 11 or test == 14):
        return True
    return False

#first function determines all the possible places of char on board
#the second one determines if two letters are connected and if they are it adds
#the position of the first to a list that contains the positions of the word
#the third combines the two to see if the letters for the whole word are connected
def determinePossibleSpaces(char):
    i = 0
    possibleSpacesForLetter = []
    while i < 16:
        if board[i] == char:
            possibleSpacesForLetter.append(i)
        i = i + 1
    return possibleSpacesForLetter

def areLettersConnected(char1, char2, count):
    psfl = determinePossibleSpaces(char1)
    psfl2 = determinePossibleSpaces(char2)
    for pos in psfl:
        i = 0
        while i < len(psfl2):
            if areSpacesConnected(pos, psfl2[i]):
                positionsOfLetters.append(pos)
                if (count + 1) == (len(word) - 1):
                    positionsOfLetters.append(psfl2[i])
                return True
            i = i + 1
    return False

def isWordConnected(word):
    positionsOfLetters.clear()
    count = 0
    while count < (len(word) - 1):
        if areLettersConnected(word[count], word[count+1], count):
            count = count + 1
        else:
            print ("some letters aren't connected!")
            return False
    return True

#calculate score for word
def calculateScore(word):
    word = word.lower()
    total = 0
    i = 0
    for letter in word:
        total += scores[letter]
    return total

#determine if a letter on board is used more than once
def areLettersUsedOnce():
    i = 0
    j = 0
    while j < (len(positionsOfLetters) - 1):
        while i < (len(positionsOfLetters)):
            if positionsOfLetters[i] == positionsOfLetters[j] and i != j:
                return False
            i = i + 1
        j = j + 1
    return True

while True:
    print ("----------------------------------")
    print ("Welcome to Boggle hardmode by Kevin Good!")
    generateBoard()
    printBoard()
    print ("----------------------------------")
    word = input("guess a word from the board:")
    if word == "q":
        break
    #words in dictionary file have newline characters, word2 used for comparison
    word2 = word + "\n"
    #determine if the input is legal according to boggle rules
    print ("results:")
    if isAWord(word2) and isOnBoard(word) and isWordConnected(word) and isNotGuessed(word):
        if areLettersUsedOnce():
            score = score + calculateScore(word)
            print("success! your score is now",score)
        else:
            print ("INVALID GUESS")
        guessedWords.append(word)
    else:
        guessedWords.append(word)
        print ("INVALID GUESS")
#update scores
file2 = open("scores.txt", "r")
scores = file2.readlines()
file2.close()
for item in scores:
    item = item.strip()
for number in range(0, 9):
    scores[number] = int(scores[number])
    if score > scores[number]:
        print (score, "is a new high score!")
        scores[number] = score
        break
file3 = open("scores.txt", "w")
initials = input("enter your initials:")
for score3 in scores:
    print (score3)
    if int(score3) > 0:
        score3 = str(score3) + "\n"
    file3.write(score3)
file3.close()
file.close()

