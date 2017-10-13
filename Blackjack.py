#Code by Kevin Good
import random
print ("Welcome to Kevin's Casino!")
name = input("please enter your name: ")
#randomly generate a card. 11 is Ace, code to change to a 1 below
def deal_card():
    
    #pick card out of 52
    card = random.randint(1,52)
    
    #translate into an actual card
    if  card < 5:
        card = 11
    elif card > 4 and card < 9:
        card = 2
    elif card > 8 and card < 13:
        card = 3
    elif card > 12 and card < 17:
        card = 4
    elif card > 16 and card < 21:
        card = 5
    elif card > 20 and card < 25:
        card = 6
    elif card > 24 and card < 29:
        card = 7
    elif card > 28 and card < 33:
        card = 8
    elif card > 32 and card < 37:
        card = 9
    elif card > 36:
        card = 10
    return card

def player():
    #array holding the cards, 10 is maximum possible number without going over 21
    cards = [0,0,0,0,0,0,0,0,0,0]
    
    #first two cards
    cards[0] = deal_card()
    cards[1] = deal_card()
    #total when cards are added up
    total = cards[0] + cards[1]
    
    print(name,"'s two cards are ", cards[0], " and ", cards[1], " their total is ", total, sep="")
    while True:
        choice = input("do you want to 'hit' or 'stand'?")
        i = 1
        if choice == "hit":
            cards[i] = deal_card()
            if cards[i] == 11:
                print(name,"hits. The card is an ace")
            else:
                print(name,"hits. The card is", cards[i])
            total += cards[i]
            i = i + 1
            if total > 21:
                for card in cards:
                    if card == 11:
                        card = 1
                        total -= 10
            print ("your total is now", total)
            
            if total > 21:
                print (name, "BUSTED!")
                return total
        elif choice == "stand":
            print ("your total is ", total)
            return total
def dealer(total):
    cputotal = 0
    cards = [0,0,0,0,0,0,0,0,0,0]
    cards[0] = random.randint(2,11)
    cputotal += cards[0]
    if total == 21:
        print (name,"won!")
        return cputotal
    elif total > 21:
        return cputotal
    i = 1
    while cputotal < 21:
        cards[i] = random.randint(2,11)
        if cards[i] == 11:
            print ("Dealer hits. The card is an ace")
        else:
            print ("Dealer hits. The card is", cards[i])
        cputotal += cards[i]
        i = i + 1
        if cputotal > 21:
                for card in cards:
                    if card == 11:
                        card = 1
                        total -= 10
                if cputotal > 21:
                    print ("Dealer BUSTED! Player Wins.")
                    return cputotal
        if cputotal == 21:
            print ("Dealer wins!")
            return cputotal
dealer(player())

while True:
    choice = input("would you like to play again? [yes/no] ")
    if choice == "yes":
        dealer(player())
    elif choice == "no":
        break
    else:
        print ("err")
