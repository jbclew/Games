import random
import sys

choices=['Paper','Rock','Scissors']
user_stats={'Paper':0,'Rock':0,'Scissors':0,'Wins':0,'Losses':0,'Ties':0}
comp_stats={'Paper':0,'Rock':0,'Scissors':0,'Wins':0,'Losses':0,'Ties':0}

def choose(choices):
    choice=""
    print"\n\n"
    human_choice=raw_input("(P)aper, (R)ock, or (S)cissors? : ")
    comp_choice=random.choice(choices)
    human_choice=human_choice.upper()
    if human_choice=='P':
        choice='Paper'
    if human_choice=='R':
        choice='Rock'
    if human_choice=='S':
        choice='Scissors'
    return choice,comp_choice

def pick_winner(human_choice,comp_choice,user_stats,comp_stats):
    if comp_choice=='Paper' and human_choice=='Paper':
        winner='Tied'
        user_stats['Ties'] += 1
        comp_stats['Ties'] += 1
        user_stats['Paper'] += 1
        comp_stats['Paper'] += 1
    if comp_choice=='Paper' and human_choice=='Rock':
        winner='Computer'
        user_stats['Losses'] += 1
        comp_stats['Wins'] += 1
        user_stats['Rock'] += 1
        comp_stats['Paper'] += 1
    if comp_choice=='Paper' and human_choice=='Scissors':
        winner='Player'
        user_stats['Wins'] += 1
        comp_stats['Losses'] += 1
        user_stats['Scissors'] += 1
        comp_stats['Paper'] += 1
    if comp_choice=='Rock' and human_choice=='Rock':
        winner='Tied'
        user_stats['Ties'] += 1
        comp_stats['Ties'] += 1
        user_stats['Rock'] += 1
        comp_stats['Rock'] += 1
    if comp_choice=='Rock' and human_choice=='Scissors':
        winner='Computer'
        user_stats['Losses'] += 1
        comp_stats['Wins'] += 1
        user_stats['Scissors'] += 1
        comp_stats['Rock'] += 1
    if comp_choice=='Rock' and human_choice=='Paper':
        winner='Player'
        user_stats['Wins'] += 1
        comp_stats['Losses'] += 1
        user_stats['Paper'] += 1
        comp_stats['Rock'] += 1
    if comp_choice=='Scissors' and human_choice=='Scissors':
        winner='Tied'
        user_stats['Ties'] += 1
        comp_stats['Ties'] += 1
        user_stats['Scissors'] += 1
        comp_stats['Scissors'] += 1
    if comp_choice=='Scissors' and human_choice=='Paper':
        winner='Computer'
        user_stats['Losses'] += 1
        comp_stats['Wins'] += 1
        user_stats['Scissors'] += 1
        comp_stats['Paper'] += 1
    if comp_choice=='Scissors' and human_choice=='Rock':
        winner='Player'
        user_stats['Wins'] += 1
        comp_stats['Losses'] += 1
        user_stats['Rock'] += 1
        comp_stats['Scissors'] += 1
    return winner,user_stats,comp_stats

def header(human_choice,comp_choice,user_stats,comp_stats):
    print"------------------------------------------------Paper, Rock, Scissors -------------------------------------------------------"
    print"Player:  Wins: %d   Losses: %d   Ties: %d    Times picked Paper: %d      Times picked Rock: %d     Times picked Scissors: %d"%(user_stats['Wins'],user_stats['Losses'],user_stats['Ties'],user_stats['Paper'],user_stats['Rock'],user_stats['Scissors'])
    print"Computer:  Wins: %d   Losses: %d   Ties: %d    Times picked Paper: %d      Times picked Rock: %d     Times picked Scissors: %d"%(comp_stats['Wins'],comp_stats['Losses'],comp_stats['Ties'],comp_stats['Paper'],comp_stats['Rock'],comp_stats['Scissors'])
    print"------------------------------------------------------------------------------------------------------------------------------"
    return
 
play_again='Y'
    
while play_again=='Y':
    human_choice,comp_choice=choose(choices) 
    winner,user_stats,comp_stats=pick_winner(human_choice,comp_choice,user_stats,comp_stats)
    print"\n"
    print"Computer has: %s "%comp_choice
    print"You have: %s "%human_choice
    print"\n"
    if winner =='Tied':
        print"You have tied, Go again!"
    if winner == 'Player':
        play_again=raw_input("You Win!, Play again? (Y) or (N): ")
        play_again=play_again.upper()
        if play_again=='N':
            sys.exit()
    if winner =='Computer':
        play_again=raw_input("You lose!, Play again? (Y) or (N): ")
        play_again=play_again.upper()
        if play_again=='N':
            sys.exit()
    header(human_choice,comp_choice,user_stats,comp_stats)