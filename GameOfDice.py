import random
import sys
import time
import os

in_game='Y'
money=1000
winnings=0

def Dashboard(money):
    print"\n"
    print"-------------------------------------------------------------------------------------"
    print"--------------------------------Game of Dice-----------------------------------------"
    print"Current money: $%d"%money
    print"-------------------------------------------------------------------------------------"
    print"\n"

def RollDice():
    comp_roll=random.randint(1,6)
    i=0
    j=0
    print"\n"
    while i<40:
        user_roll=random.randint(1,6)
        print "Your roll: %d"%user_roll,
        time.sleep(0.1)
        print "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b",
        i=i+1
    print"\n"
    while j<40:
        comp_roll=random.randint(1,6)
        print "Computers roll: %d"%comp_roll,
        time.sleep(0.1)
        print "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b",
        j=j+1
    print"\n"
    return user_roll,comp_roll

def PlaceBet(money):
    bet=raw_input("How much money do you want to bet? ")
    try:
        bet=int(bet)
    except ValueError:
        print"Not a valid bet"
        bet=raw_input("How much money do you want to bet? ")
        bet=int(bet)
    if bet>money:
        print"You do not have that much money!"
        PlaceBet(money)
    return bet

def WhoWon(user_roll,comp_roll,bet,money,winnings):
    if user_roll > comp_roll:
        print"what is my current bet: ",bet
        print "You won $%d!"%bet
        money=money+bet
        winnings=winnings+bet
    if user_roll == comp_roll:
        print"what is my current bet: ",bet
        print "You tied, bet returned"
        money=money
    if user_roll < comp_roll:
        print"what is my current bet: ",bet
        print "You lost $%d"%bet
        money=money-bet
        winnings=winnings-bet
    return money,winnings

print"\n\n"
print"Welcome to Game of dice!"
if os.path.isfile('saved.txt'):
    load=raw_input("Would you like to load the saved game? (Y) or (N): ")
    load=load.upper()
    if load=='Y':
        f=open('saved.txt','r')
        data=f.readlines()
        f.close()
        money=data[0]
        money=int(money)
Dashboard(money)

while in_game=='Y':
    bet=PlaceBet(money)
    user_roll,comp_roll=RollDice()
    money,winnings=WhoWon(user_roll,comp_roll,bet,money,winnings)
    Dashboard(money)
    if money < 1:
        print"Game Over.  You ran out of money! "
        in_game=raw_input("Would you like to play again? (Y) or (N): ")
        in_game=in_game.upper()
        if in_game=='N':
            sys.exit()
        if in_game=='Y':
            money=1000
            bet=PlaceBet(money)
            user_roll,comp_roll=RollDice()
            money,winnings=WhoWon(user_roll,comp_roll,bet,money,winnings)
            Dashboard(money)
    in_game=raw_input("Would you like to play again? (Y) or (N): ")
    in_game=in_game.upper()
    if in_game=='N':
        print"Your total winnings were: $%d"%winnings
        save=raw_input("Would you like to save your game? (Y) or (N): ")
        save=save.upper()
        if save=='Y':
            f=open('saved.txt','w')
            money=str(money)
            f.write(money)
            f.close()
        sys.exit()