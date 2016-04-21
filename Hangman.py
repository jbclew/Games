import sys
import os
import random
import platform
IN_GAME=True
while IN_GAME==True:
    WORD_LIST=('FATHOM','MARSH','MARCH','HARMS','MAJOR','MANGOS','ISOGRAM','BEACH','FLOWER','DEATH','COURTS','FLAMES','PHONE','ORGANISM','SOARING','MINORS','DOWNSTREAM','MISTAKE','SHOCKING','DUPLICATE','HOSPITAL','TRAMPOLINE','BLACKSMITH','AFTERSHOCK','ARTICHOKE')
    ALL_LETTERS=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    avail_letters=ALL_LETTERS
    guessed_list=[]
    WORD = random.choice(WORD_LIST)
    LEN_OF_WORD = len(WORD)
    no_of_wrong = 0
    correct_guess=[]

    def set_word_place(word):
        wordplace={}
        for i in range(0,len(word)):
            wordplace.update({word[i]:i})
        return wordplace

    def ask_guess(no_of_wrong,avail_letters,word,guessed_list,correct_guess,wordplace):
        print"\n"
        print "======================================================================================"
        print"\n\n\n"
        print"Available Letters: ",
        for leng in range(0,len(avail_letters)):
            print avail_letters[leng],
        print"\n\n\n"
        guess=raw_input("Enter a letter: ")
        print"\n"
        guess=guess.upper()
        if guess in guessed_list:
            print "You already Guessed that"
            ask_guess(no_of_wrong,avail_letters,word,guessed_list,correct_guess,wordplace)
        print"You Guessed: ",guess

        guessed_list.append(guess)
        if guess in avail_letters:
            avail_letters.remove(guess)
        if guess in wordplace:
            listupdate=wordplace[guess]
        if guess not in wordplace:
            listupdate=-1
            print"There is no letter %s in the word!"%guess
            no_of_wrong=no_of_wrong+1
        print"\n\n\n\n"
        if listupdate >= 0:
            correct_guess.append(listupdate)
        for i in range(0,len(word)):
            if i in correct_guess:
                print"__%s__   "%word[i],
            if i not in correct_guess:
                print"_____   ",
        print"\n\n\n"
        if len(correct_guess)==len(word):
            print "\n\n\n\n\n"
            print "You Win!!!!!!!"
            print"\n"
            no_of_wrong=6
            return avail_letters,no_of_wrong,guessed_list
        return avail_letters,no_of_wrong,guessed_list

    def print_hangman(no_of_wrong):
        no_right=6-no_of_wrong
        print"Guesses Left:",no_right,
        print"     ",
        print"No. of Wrong Guesses:",
        print' [X] '* no_of_wrong,
        print' [ ] '* no_right,

    wordplace=set_word_place(WORD)
    ver=platform.system()
    if ver=='Windows':
        os.system("cls")

    print"--------------------------------------------------------------------------------------"
    print"|                         Welcome to Hangman                                          |"
    print"--------------------------------------------------------------------------------------"

    while no_of_wrong < 6:
        avail_letters,no_of_wrong,guessed_list=ask_guess(no_of_wrong,avail_letters,WORD,guessed_list,correct_guess,wordplace)
        print_hangman(no_of_wrong)

    if no_of_wrong >= 6:
        print"\n\n"
        print"Game Over!!   The word was %s"%WORD
        print"\n"
        play_again=raw_input("Would you like to play again: Y or N: ")
        play_again=play_again.upper()
        if play_again != 'Y':
            sys.exit()
        if play_again == 'Y':
            IN_GAME=True
            
    
