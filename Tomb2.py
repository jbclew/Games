import random
import os
import sys
import platform
import time

#Should Run Now
ver=platform.system()
if ver=='Windows':
    os.system("cls")
    os.system("mode con cols=150 lines=80")
else:
    os.system('clear')
    os.system("stty columns 150,60")

#Set inital values for the character
print"\n"
name=raw_input("Enter the name of your Adventurer: ")
print"\n"
#inital values
hp=random.randint(5,12)
maxhp=hp
gold=1
level=1
xp=0

#weapon is [0-name,1-lowdamage,2-highdamage]
weaponlist=[['Short Sword',2,4],['Long Sword',4,6],['Blackbeards Saber',5,8],['Pointed Mace',4,8],['2 Handed Sword',7,12],['Gordons Trident',6,10],['Flaming Dragon Dagger',4,7]]
initweapon=['Fists',1,1]
#armor is [0-'name',1-AC]
armorlist=[['Leather Armor',2],['Chain Armor',4],['Mail Armor',6],['Plate Armor',8],['Etherium Armor',10],['Padded Mail',5],['Black or Green Robe',3],['Horned Helmet',2]]
initarmor=['Linens',1]
#monster is [0-'Name',1-monster hp,2-level,3-lowdamage,4-highdamage,5-monster ac,6-monsterxp]
monsterlist=[['Orc',5,1,1,2,3,100],['Troll',7,2,3,5,6,200],['Sicilian Gnome',8,2,2,8,1,250],['M.O.U.S',10,2,4,6,5,400],['Giant',12,3,5,10,3,750],['Ooze',5,3,2,5,10,800]]

class PlayerClass:
    maxhp=hp
    currenthp=maxhp
    gold=1
    level=1
    weapon=initweapon[0]
    lowdamage=initweapon[1]
    highdamage=initweapon[2]
    armor=initarmor[0]
    ac=initarmor[1]
    xp=0
    name=name
    
class MonsterClass:
    name="name"
    maxhp=1
    currenthp=1
    level=1
    lowdamage=1
    highdamage=1
    ac=1
    xp=1
    
  
class RoomsClear:
    hallway=False
    room1=False
    room2=False
    room3=False
    room4chest=False
    room4pass=False
    room5=False
    room6=False
    room6pass=False
    room7=False
    room8=False

def SelectMonster(monsterlist,goblin,boss):
    monster=monsterlist[random.randint(1,(len(monsterlist)-1))]
    if boss == True:
        MonsterClass.name='Pirate Robert Dread'
        MonsterClass.maxhp=100
        MonsterClass.currenthp=50
        MonsterClass.level=8
        MonsterClass.lowdamage=10
        MonsterClass.highdamage=30
        MonsterClass.ac=9
        MonsterClass.xp=5000
    if goblin == True:
        MonsterClass.name='Goblin Salesman'
        MonsterClass.maxhp=16
        MonsterClass.currenthp=16
        MonsterClass.level=6
        MonsterClass.lowdamage=6
        MonsterClass.highdamage=10
        MonsterClass.ac=8
        MonsterClass.xp=3000
    if goblin ==False:
        MonsterClass.name=monster[0]
        MonsterClass.maxhp=monster[1]
        MonsterClass.currenthp=MonsterClass.maxhp
        MonsterClass.level=monster[2]
        MonsterClass.lowdamage=monster[3]
        MonsterClass.highdamage=monster[4]
        MonsterClass.ac=monster[5]
        MonsterClass.xp=monster[6]
        
def SelectWeapon(weaponlist):
    weapon=weaponlist[random.randint(0,(len(weaponlist)-1))]
    return weapon
    
def SelectArmor(armorlist):
    armor=armorlist[random.randint(0,(len(weaponlist)-1))]
    return armor

def GoblinBuying():
    print"I gots all the weapons and armors you can wants!"
    print"WARNING: Purchasing an item will equip it and destroy existing item"
    vendorweapon=[['Rusted Sword',1,2,10],['Shiny Dagger',3,6,20],['Andres Fist',4,8,25],['Inigos Sword',5,10,35],['Magic Sword',12,20,150]]
    vendorarmor=[['Diced Leather',1,10],['Chain Mail',4,30],['Polished Plate',10,100],['Magic Armor',20,200]]
    inbuying=True
    while inbuying==True:
        buymenu=raw_input("(W)eapons, (A)rmor, (E)xit: ")
        if buymenu=='W' or buymenu=='w':
            inweapon=True
            while inweapon==True:
                x=len(vendorweapon)
                for y in range(0,x):
                    print "(%d) Item: %s   Damage: %d-%d   Cost: %d gold"%((y+1),vendorweapon[y][0],vendorweapon[y][1],vendorweapon[y][2],vendorweapon[y][3])
                choice=raw_input("Gold:%d           Choose 1-%d: or 0 to go back: "%(PlayerClass.gold,x))
                choice=int(choice)-1
                if choice<0:
                    inweapon=False
                weapon=vendorweapon[choice]
                if vendorweapon[choice][3]>PlayerClass.gold and choice >-1:
                    print"You do not have enough gold to purchase this weapon"
                    inweapon=False
                if vendorweapon[choice][3]<=PlayerClass.gold and choice >-1:
                    PlayerClass.gold=PlayerClass.gold-vendorweapon[choice][3]
                    PlayerClass.weapon=weapon[0]
                    PlayerClass.lowdamage=weapon[1]
                    PlayerClass.highdamage=weapon[2]
                    vendorweapon.remove(weapon)
                    print"\nYou purchased %s   damage:%d-%d"%(weapon[0],weapon[1],weapon[2])
                    print"\n"
                if len(vendorweapon)<1:
                    print"you bought everything"
                    inweapon=False
        if buymenu=='A' or buymenu=='a':
            inarmor=True
            while inarmor==True:
                x=len(vendorarmor)
                for y in range(0,x):
                    print "(%d) Item: %s   Armor: %d   Cost: %d gold"%((y+1),vendorarmor[y][0],vendorarmor[y][1],vendorarmor[y][2])
                choice=raw_input("Gold:%d           Choose 1-%d: or 0 to go back: "%(PlayerClass.gold,x))
                choice=int(choice)-1
                if choice<0:
                    inarmor=False
                armor=vendorarmor[choice]
                if vendorarmor[choice][2]>PlayerClass.gold and choice >-1:
                    print"You do not have enough gold to purchase this weapon"
                    inarmor=False
                if vendorarmor[choice][2] <= PlayerClass.gold and choice >-1:
                    PlayerClass.gold=PlayerClass.gold-vendorarmor[choice][2]
                    PlayerClass.armor=armor[0]
                    PlayerClass.ac=armor[1]
                    vendorarmor.remove(armor)
                    print"You purchased %s   AC:%d"%(weapon[0],weapon[1])
                if len(vendorarmor)<1:
                    print"you bought everything"
                    inarmor=False
        if buymenu=='E' or buymenu=='e':
            inbuying=False 
    return
                
rolllist=[]

def PrintDashboard():
    print"\n\n\n\n\n\n\n\n\n"
    '''print 'gold',PlayerClass.gold
    print'armor',PlayerClass.armor
    print'ac',PlayerClass.ac
    print'weapon',PlayerClass.weapon
    print'lowdam',PlayerClass.lowdamage
    print'highdam',PlayerClass.highdamage
    print'level',PlayerClass.level
    print'name',PlayerClass.name
    
    print"-----------------------------------------------------------------------------------------------------------------------------------"
    print"  _____          _           __   _   _          ___ _          _         ___     _             _     ___                  _  "
    print" |_   _|__ _ __ | |__   ___ / _| | |_| |_  ___  | _ (_)_ _ __ _| |_ ___  | _ \___| |__  ___ _ _| |_  |   \ _ _ ___ __ _ __| | "
    print"   | |/ _ \ '  \| '_ \ / _ \  _| |  _| ' \/ -_) |  _/ | '_/ _` |  _/ -_) |   / _ \ '_ \/ -_) '_|  _| |  ) | '_/ -_) _` / _` | "
    print"   |_|\___/_|_|_|_.__/ \___/_|    \__|_||_\___| |_| |_|_| \__,_|\__\___| |_|_\___/_.__/\___|_|  \__/ |___/|_| \___\__,_\__,_| "
    print"                                                                                                                                  "
    '''
    print"-----------------------------------------------------------------------------------------------------------------------------------"
    print"-----------------------------------------------------DASHBOARD --------------------------------------------------------------------"
    print"-----------------------------------------------------------------------------------------------------------------------------------"
    print"\n \n"
    print"   HP: %d/%d     XP: %d      Gold: %d      Armor: %s   AC:%d     Damage: %s(%d-%d)     Level: %d     Name: %s "% (PlayerClass.currenthp,PlayerClass.maxhp,PlayerClass.xp,PlayerClass.gold,PlayerClass.armor,PlayerClass.ac,PlayerClass.weapon,PlayerClass.lowdamage,PlayerClass.highdamage,PlayerClass.level,PlayerClass.name)
    print"\n \n"
    print "Hall: %s |Rm1: %s |Rm2: %s |Rm3: %s |Rm4 chest: %s |Rm4 pass: %s |Rm5: %s |Rm6: %s |Rm6 pass: %s|Rm7: %s |Rm8: %s"%(RoomsClear.hallway,RoomsClear.room1, RoomsClear.room2, RoomsClear.room3,RoomsClear.room4chest,RoomsClear.room4pass,RoomsClear.room5,RoomsClear.room6,RoomsClear.room6pass,RoomsClear.room7,RoomsClear.room8)
    print"-----------------------------------------------------------------------------------------------------------------------------------"

def WelcomeCharacter():
    if PlayerClass.maxhp==5 or PlayerClass.maxhp==6:
        welcometext='''  All your life %s you have been picked on and pushed around.  Your puny size has made you an outcast in your own village.  
The final straw came when a stiff breeze blew through the village and knocked you on your back.  Your father disgraced, has
kicked you out. With nowhere to go you stumble through the forest searching for food only to find the entrance of a dark
tomb. It will at least provide you shelter for the night.''' % PlayerClass.name
    if PlayerClass.maxhp>6 and PlayerClass.maxhp<11:
        welcometext='''  You are a very average person %s.  All your life you have never exceled at anything or have been noticed by anyone.
Lost in thought about what to do next in life, you walk through the forest and stumble across the entrance of a dark tomb.
"This could be the way to make a name for myself", you think as you enter in.''' % PlayerClass.name 
    if PlayerClass.maxhp>10:
        welcometext='''  You are quite the fierce warrior %s. You have bested many in the arenas and continue to impress everyone with your skill and
ability to defeat even the most ubiquitous of enemies.  Off to prove you are the elitess of the elite you travel through the
forest to the hidden tomb of which few have ever returned from.  The entrance is dark and you step inside.''' % PlayerClass.name
    return(welcometext)    

def Roll():
    i=0
    while i<40:
        num=random.randint(1,20)
        if num<10:
            print "Roll (1d20): %d"% num,
            time.sleep(0.1)
            print "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b",
        if num>9:
            print "Roll (1d20): %d"% num,
            time.sleep(0.1)
            print "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b",       
        i=i+1
    return num

def ChangeName(rolllist):
    if len(rolllist) <3:
        return
    else:
        lastthree=rolllist[-3:]
        if lastthree[0]==1 and lastthree[1]==1 and lastthree[2]==1:
            newname='%s the Fortunate'% PlayerClass.name
            PlayerClass.name=newname
        if lastthree[0]==20 and lastthree[1]==20 and lastthree[2]==20:
            newname='%s the Fortunate'% PlayerClass.name
            PlayerClass.name=newname
        return
        
def PlayerToHit(rolllist):
    d20=Roll()
    print"--------------------Your Attack------------------------------"
    print"You Rolled :",d20
    rolllist.append(d20)
    ChangeName(rolllist)
    #basehit=(PlayerClass.level/((MonsterClass.level* (0.05*(MonsterClass.ac)))))
    basehit=1
    hit=int(round(basehit*d20))
    if hit <=1:
        print("Fumbled!!")
        dammod=-0.25
    if hit >1 and hit <5:
        print("Miss!")
        dammod=0
    if hit >4 and hit <10:
        print("Glancing Blow!")
        dammod=0.5
    if hit >9 and hit <17:
        print("A Hit!")
        dammod=1
    if hit > 16 and hit < 20:
        print("A Crit!")
        dammod=1.5
    if hit >19:
        print("An Ultra Crit!")
        dammod=2.0
    return(dammod,rolllist)

def PlayerDamage(dammod):
    if dammod <0:
        selfdamage=int(round(random.randint(float(PlayerClass.lowdamage),float(PlayerClass.highdamage))*.25))
        damage=0
    if dammod ==0:
        selfdamage=0
        damage=0
    if dammod >0:
        selfdamage=0
        damage=int(round(float(PlayerClass.level)/float(MonsterClass.level))*(random.randint(PlayerClass.lowdamage,PlayerClass.highdamage)*dammod))
        if damage==0:
            damage=1
    if dammod <0:
        print"You are attacking %s" %MonsterClass.name
        print"You did %d damage to yourself!" %selfdamage
    if dammod > -1:
        print"You are attacking %s" %MonsterClass.name
        print"You did %d damage to %s!"%(damage,MonsterClass.name)
    return (damage,selfdamage)

def MonsterHit():
    print"--------------------Enemy Attacks------------------------------"
    print"%s attacks you!"% MonsterClass.name
    d20=Roll()
    #basehit=(MonsterClass.level/(PlayerClass.level*(PlayerClass.ac)))
    basehit=1
    hit=int(round(basehit*d20))
    print"\b"
    if hit <=2:
        print("%s Fumbled!!"% MonsterClass.name)
        dammod=-0.25
    if hit >2 and hit <7:
        print("%s Misses!"% MonsterClass.name)
        dammod=0
    if hit >6 and hit <12:
        print("%s landed a Glancing Blow!"% MonsterClass.name)
        dammod=0.5
    if hit >11 and hit <19:
        print("%s Hits you!"% MonsterClass.name)
        dammod=1
    if hit > 18:
        print("%s lands A Crit!"% MonsterClass.name)
        dammod=1.5
    return(dammod)

def MonsterDamage(dammod):
    monsterdamage=int(round(((float(PlayerClass.level)/float(MonsterClass.level))*(random.randint(MonsterClass.lowdamage,MonsterClass.highdamage)*dammod))))
    if dammod <0:
        monsterselfdamage=int(round(random.randint(MonsterClass.lowdamage,MonsterClass.highdamage)*.25))
        monsterdamage=0
        print"%s did %d damage to itself!"% (MonsterClass.name,monsterselfdamage)
    if dammod >=0:
        print"%s did %d damage to you!"% (MonsterClass.name,monsterdamage)
        monsterselfdamage=0
    return (monsterdamage,monsterselfdamage)
       

def PickUpWeapon(input,weapon):
    i=0
    j=0
    while input !='P'and input !='p' and input !='l'and input !='L':
        if i>1 and i <4:
            print"What are you daft? Type (P) or (L) this isn't Advanced Ethereal Conjuring"
        if i>3 and i <6:
            print"Look, if you don't want to play you don't have to, just go outside and play in traffic or something!"
        if i>5 and i <9:
            print"Quit it, stop poking me!"
        if i>8:
            print"Well two can play at this game"
            time.sleep(2)
            while j < 30:
                print"(P) or (L)!!!!!!"
                j=j+1
                i=0
        print" That is not a valid selection.  Please choose (P) to pickup or (L)to leave alone"
        input=raw_input("Enter your choice: ")
        i=i+1
    if input=='p' or input=='P':
        PlayerClass.weapon=weapon[0]
        PlayerClass.lowdamage=weapon[1]
        PlayerClass.highdamage=weapon[2]
        ChoiceTaken() 
        return
    if input=='l' or input=='L':
        return

def PickUpArmor(input,armorloot):
    i=0
    j=0
    while input !='P'and input !='p' and input !='l'and input !='L':
        if i>2 and i <5:
            print"Sigh....."
        if i>4 and i <7:
            print"Huff..........."
        if i>6 and i <10:
            print"Look, even my four year old neice can do this."
        if i>9:
            print"You have unleashed teh fury!!!"
            time.sleep(2)
            while j < 50:
                print"<Unleashed Fury Here>"
                j=j+1
                i=0
        print" That is not a valid selection.  Please choose (P) to pickup or (L)to leave alone"
        input=raw_input("Enter your choice: ")
        i=i+1
    if input=='p' or input=='P':
        PlayerClass.armor=armorloot[0]
        PlayerClass.ac=armorloot[1]
        ChoiceTaken() 
        return
    if input=='l' or input=='L':
        return
    
def ChoiceTaken():
    print"\n"
    print"                      ------------------------Choice Accepted!---------------------------"
    print"\n"
       
def CalculateXP():
    PlayerClass.xp=PlayerClass.xp+(MonsterClass.xp*(float(MonsterClass.level)/float(PlayerClass.level)))
    return

def CheckLevel():
    levelbefore=PlayerClass.level
    if PlayerClass.xp>=0 and PlayerClass.xp<100:
        level=1
    if PlayerClass.xp>99 and PlayerClass.xp<300:
        level=2
    if PlayerClass.xp>299 and PlayerClass.xp<750:
        level=3
    if PlayerClass.xp>749 and PlayerClass.xp<1500:
        level=4
    if PlayerClass.xp>1499 and PlayerClass.xp<3000:
        level=5
    if PlayerClass.xp>2999 and PlayerClass.xp<5000:
        level=6
    if PlayerClass.xp>4999 and PlayerClass.xp<10000:
        level=7
    if PlayerClass.xp>9999 and PlayerClass.xp<15000:
        level=8
    if PlayerClass.xp>14999 and PlayerClass.xp<20000:
        level=9
    if PlayerClass.xp>19999:
        level=10
    if level>levelbefore:
        print"Congratulations, you leveled up!!!  Your new level is: %d" %level
        newhp=(random.randint(5,10))*(level-levelbefore)
        PlayerClass.currenthp=PlayerClass.maxhp+newhp
        PlayerClass.maxhp=PlayerClass.currenthp
        PlayerClass.level=level
        print"You gained %d hp!"%newhp
    return 
    
def Battle(rolllist):
    print"\n"
    print"You are fighting a %s.  Monster Level: %d   Monster Armor: %d   Damage: %d-%d   Monster hp: %d"% (MonsterClass.name,MonsterClass.level,MonsterClass.ac,MonsterClass.lowdamage,MonsterClass.highdamage,MonsterClass.maxhp)
    while (PlayerClass.currenthp>0) and (MonsterClass.currenthp>0):
        dammod,rolllist=PlayerToHit(rolllist)
        damage,selfdamage=PlayerDamage(dammod)
        MonsterClass.currenthp=MonsterClass.currenthp-damage
        PlayerClass.currenthp=PlayerClass.currenthp-selfdamage
        if (PlayerClass.currenthp>0) and (MonsterClass.currenthp>0):
            print "%s HP:%d        %s HP:%d" %(PlayerClass.name,PlayerClass.currenthp,MonsterClass.name,MonsterClass.currenthp)
            dammod=MonsterHit()
            damage,monsterselfdamage=MonsterDamage(dammod)
            MonsterClass.currenthp=MonsterClass.currenthp-monsterselfdamage
            PlayerClass.currenthp=PlayerClass.currenthp-damage
            print "%s HP:%d        %s HP:%d" %(PlayerClass.name,PlayerClass.currenthp,MonsterClass.name,MonsterClass.currenthp)
        else:
            print "%s HP:%d        %s HP:%d" %(PlayerClass.name,PlayerClass.currenthp,MonsterClass.name,MonsterClass.currenthp)
    if PlayerClass.currenthp<1:
        print"you died!"
        sys.exit()
    if MonsterClass.currenthp<1:
        print"you killed the %s"%MonsterClass.name
        CalculateXP()
        CheckLevel()
        goldloot=Loot(weaponlist,armorlist)
        PlayerClass.gold=PlayerClass.gold+goldloot
    return rolllist
    
def Loot(weaponlist,armorlist):
    rollweapon=random.randint(1,20)
    rollarmor=random.randint(1,20)
    rollgold=(random.randint(1,10))*PlayerClass.level
    if rollweapon>1:
        weaponloot=SelectWeapon(weaponlist)
    else:
        weaponloot='No Weapons'
    if rollarmor>1:
        armorloot=SelectArmor(armorlist)
        print "Armor loot is now: ",armorlist
    else:
        armorloot="No Armor"
    goldloot=rollgold    
    print"Looting Enemy......  Enemy had %d Gold"%goldloot
    if weaponloot =='No Weapons':
        print"Looting Enemy......  Enemy had no Weapons"
    if weaponloot !='No Weapons':
        print"Looting Enemy......  Enemy had Weapon: %s  Damage:%d-%d"%(weaponloot[0],weaponloot[1],weaponloot[2])
    if armorloot =='No Armor':
        print"Looting Enemy......  Enemy had no Armor"
    if armorloot !='No Armor':
        print"Looting Enemy......  Enemy had Armor: %s  Armor:%d"%(armorloot[0],armorloot[1])
    if weaponloot !='No Weapons':     
        winput=raw_input("(P)ick up %s  (L)eave the %s alone: "%(weaponloot[0],weaponloot[0]))
        PickUpWeapon(winput,weaponloot)
    if armorloot !='No Armor':
        winput=raw_input("(P)ick up %s  (L)eave the %s alone: "%(armorloot[0],armorloot[0]))
        PickUpArmor(winput,armorloot)
    return goldloot
   
#Entrance Room
welcometext=WelcomeCharacter()
print welcometext

#First Hallway
def Hallway(monsterlist,rolllist):
    PrintDashboard()
    if RoomsClear.hallway==False:
        print "\n\n"
        print" As you walk into the tomb from the north you trip over a skeleton.  Falling to the ground you come face to face with a small sword. "
        input=raw_input("(P)ick up the sword.  (L)eave the sword alone, I'd rather bloody my knuckles fighting with my fists : ")
        PickUpWeapon(input,weaponlist[1])
        if input == 'l' or input == 'L':
            pickupsword=False
        if input =='P' or input =='p':
            pickupsword=True
        PrintDashboard()
        RoomsClear.hallway==True
        print"Just set hallway to true"
        print "Hallway: ",RoomsClear.hallway
        print"From here you there is a door to your south or you can leave the dungeon."
        leaveorgo=raw_input("Open the (D)oor or (L)eave dungeon: ")
        if leaveorgo=='D' or leaveorgo=='d':
            Room1(monsterlist,rolllist)
            return
        if leaveorgo=='L' or leaveorgo=='l':
            print"\n"
            print"You go back to town and are laughed at by everyone from the pee stains on your linens."
            sys.exit()
    if RoomsClear.hallway==True and pickupsword==True:
        print"So you ran away from your first real fight.  Bravo (slow clap).  At this point you have two options.  (G)o back into the room and face the scary monster. Or (L)eave the dungeon a coward and a complete failure."
        leaveorgo=raw_input("(G)o back in or (L)eave the dungeon a coward: ")
        if leaveorgo =='G' or leaveorgo=='g':
            Room1(monsterlist,rolllist)
        if leaveorgo =='L' or leaveorgo=='l':
            print"You go back to town and are laughed at by everyone from the pee stains on your linens."
            sys.exit()
    if RoomsClear.hallway==False and pickupsword==False:
        print"I am just going to assume you ran back to the hallway to retrieve the sword that you did not pick up before and not because you are a wimpering scared little coward."
        input=raw_input("(P)ick up the sword.  (L)eave the sword alone, I'd rather bloody my knuckles fighting with my fists : ")
        PickUpWeapon(input,weaponlist[1])
        if input == 'l' or input == 'L':
            pickupsword=False
        if input =='P' or input =='p':
            pickupsword=True
        PrintDashboard()
        RoomsClear.hallway==True
        return   

#Room #1
def Room1(monsterlist,rolllist):
    PrintDashboard()
    if RoomsClear.room1 ==True:
        print"You enter the room, it looks familiar, there is a dead corpse on the ground"
        print"There is a door to the south, and a hallway to the east."
        southoreast=raw_input("(S)outh or (E)ast: ")
        if southoreast=='S' or southoreast=='s':
            print"You head south and open the door"
            Room7(monsterlist,rolllist)
            return 
        if southoreast=='E' or southoreast=='e':
            print"You head east down the hallway, after 30 feet it turns south. After 30 more feet it heads east again"
            Room2Instersect(monsterlist,rolllist)
        
    if RoomsClear.room1 ==False:
        print "There is a door in front of you, as you open it, it emits a loud creaking noise.  The noise alerts a creature in the dimly lit room."
        print "It charges towards you."
        attackorrun=raw_input("Do you want to (A)ttack or (R)un away?: ")
        if attackorrun=='A' or attackorrun=='a':
            SelectMonster(monsterlist,False,False)
            Battle(rolllist)
            PrintDashboard()
            RoomsClear.room1==True
            print"There is a door to the south, and a hallway to the east."
            southoreast=raw_input("(S)outh or (E)ast: ")
        if southoreast=='S' or southoreast=='s':
            print"You head south and open the door"
            Room7(monsterlist,rolllist)
            return 
        if southoreast=='E' or southoreast=='e':
            print"You head east down the hallway, after 30 feet it turns south. After 30 more feet it heads east again"
            Room2Instersect(monsterlist,rolllist)
            return 
        if attackorrunn=='R' or attackorrun=='r':
            print "You run back into the hallway, closing the door behind you."
            RoomsClear.room1==False
            Hallway(monsterlist,rolllist)
    if (RoomsClear.room1,RoomsClear.room2,RoomsClear.room3,RoomsClear.room4pass,RoomsClear.room5,RoomsClear.room6,RoomsClear.room7,RoomsClear.room8):
        print"As you go to leave the dungeon a figure appears from smoke in the middle of the room"
        print"He says I am the Pirate Robert Dread.  You have defiled my tomb and looted my wares.  Prepare to meet your doom."
        SelectMonster(monsterlist,False,True)
        Battle(rolllist)
        PrintDashboard()
        print"You have defeated the mighty Pirate Robert Dread.  You have looted his tomb and cleared it of monsters."
        print"Today is a glorious day! You head back to town to start your new life"
        print"The End"
        sys.exit()
        
def Room2Instersect(monsterlist,rolllist):
    PrintDashboard()
    print"There is a door here, the hallway also heads north and south."
    doororhall=raw_input("open (D)oor, (N)orth up hallway, (S)outh down hallway: ")
    if doororhall=='D' or doororhall=='d':
        Room2(monsterlist,rolllist)
    if doororhall=='N' or doororhall=='n':
        print"You travel north up the hallway for 30 feet and it turns west.  After 30 feet it opens into a room."
        Room1(monsterlist,rolllist)     
    if doororhall=='S' or doororhall=='s':
        print"You travel south down the hallway for 50 feet and it opens into a room"
        Room3(monsterlist,rolllist)
            
 #Room #2
def Room2(monsterlist,rolllist):
    PrintDashboard()
    if RoomsClear.room2 ==True:
        print"You enter the room, it looks familiar, there is a dead corpse on the ground"
    if RoomsClear.room2 ==False:
        print "You open the door.  The noise alerts a creature in the dimly lit room.  It charges towards you."
        attackorrun=raw_input("Do you want to (A)ttack or (R)un away?")
        if attackorrun=='A' or attackorrun=='a':
            SelectMonster(monsterlist,False,False)
            Battle(rolllist)
            PrintDashboard()
            RoomsClear.room2=True
            print"Rooms Clear====================================",RoomsClear.room2
            print"The room appears empty except for the dead corpse.  Your only option is to head back out the room"
            Room2Instersect(monsterlist,rolllist)
            return
        if attackorrun=='R' or attackorrun=='r':
            print "You run back into the hallway, closing the door behind you."
            RoomsClear.room2==False
            Room2Instersect(monsterlist,rolllist)

def Room3(monsterlist,rolllist):
    PrintDashboard()
    if RoomsClear.room3 ==True:
        print"You enter the room, it looks familiar, there is a dead corpse covered by a trenchcoat on the ground.  It smells like honey and leather, the commonly known smell of decaying goblin."
    if RoomsClear.room3 ==False:
        print "As you enter the room you see a short goblin wearing a trenchcoat.  He does not appear to be hostile. Upon seeing you, he says, 'psst hey there, you want to buy some weapons?'"
        buyfromgoblin=raw_input("Do you want to (B)uy from the Goblin, (I)gnore the Goblin, (A)ttack the Goblin?")
        if buyfromgoblin=='A' or buyfromgoblin=='a':
            SelectMonster(monsterlist,True,False)
            Battle(rolllist)
            PrintDashboard()
            RoomsClear.room3==True
            print"You can head back north or there is a door to the south."
            pickdirection=raw_input("Head back (N)orth, Open (D)oor to the south.")
            if pickdirection=='N' or pickdirection=='n':
                print"You head north up the hallway"
                Room2Instersect(monsterlist,rolllist)
                return
            if pickdirection =='D' or pickdirection=='d':
                Room5(monsterlist,rolllist)
            return
        if buyfromgoblin=='I' or buyfromgoblin=='i':
            print"The goblin says to you, 'No matter, i'll be gathering your things once you are off'd'"
            pickdirection=raw_input("Head back (N)orth, Open (D)oor to the south.")
            if pickdirection=='N' or pickdirection=='n':
                print"You head north up the hallway"
                Room2Instersect(monsterlist,rolllist)
                return
            if pickdirection =='D' or pickdirection=='d':
                Room5(monsterlist,rolllist)
            return
        if buyfromgoblin=='B' or buyfromgoblin=='b':
            GoblinBuying()
            Room3(monsterlist,rolllist)
            

def Room4Trap(rolllist):
    print"As you open the chest, a flame shoots at you. Make a savings roll"
    result=Roll()
    ChangeName(rolllist)
    print"You rolled a %d"%result
    if result <4:
        flamedam=random.randint(2,5)*2
        print"The flame crits you for %d damage!"%flamedam
        PlayerClass.currenthp=PlayerClass.currenthp-flamedam
        if PlayerClass.currenthp<1:
            print"You have died!"
            sys.exit()
    if result >3 and result <10:
        flamedam=random.randint(2,5)
        print"The flame hits you for %d damage!!"%flamedam
        PlayerClass.currenthp=PlayerClass.currenthp-flamedam
        if PlayerClass.currenthp<1:
            print"You have died!"
            sys.exit()   
    if result >9 and result <16:
        flamedam=(random.randint(2,5))/2
        print"The flame barely singes you for %d damage!"%flamedam
        PlayerClass.currenthp=PlayerClass.currenthp-flamedam
        if PlayerClass.currenthp<1:
            print"You have died!"
            sys.exit()       
    if result > 15:
        print"You successfully dodged the flame!"
    return           
            
def Room4(monsterlist,rolllist):
    PrintDashboard()
    if RoomsClear.room4chest==False and RoomsClear.room4pass==False:
        print"This 40x50 foot room is well lit by torches. In the back of the room there is a throne. Next to the throne is a chest. "
        print"There is a door headed West in the north corner.  The room looks otherwise empty."
        print"What do you want to do?  Go through door to the West?  Open the Chest? Sit in the Throne?"
        room4choice=raw_input("Door to the(W)est.  (O)pen Chest. (S)it in throne?: ")
        if room4choice=='W' or room4choice=='w':
            Room5(monsterlist,rolllist)
        if room4choice=='O' or room4choice=='o':
            Room4Trap(rolllist)
            goldsack=random.randint(300,1200)
            print"Inside the chest is a sack.  As you pick up the sack it is very light."
            print"Inside you can see what appears to be hundreds of gold coins"
            print"You receive %d gold"%goldsack
            PlayerClass.gold=PlayerClass.gold+goldsack
            RoomsClear.room4chest=True
        if room4choice=='S' or room4choice=='s':
            print"You sit down in the throne. It is magnificent.  You could see yourself as ruler one day, sitting in one of these."
            print"As you revel in the throne's glory, you notice a button on the right side of the armrest."
            room4button=raw_input("(P)ress the button. (D)on't press the button, get off throne: ")
            if room4button=='P' or room4button=='p':
                print"You press the button and a secret door opens on the west wall"
                RoomsClear.room4pass=True
                RoomsClear.room6pass
            if room4button=='D' or room4button=='d':
                print"You get up off the throne."
        Room4(monsterlist,rolllist)
    if RoomsClear.room4chest==False and RoomsClear.room4pass==True:
        print"This 40x50 foot room is well lit by torches. In the back of the room there is a throne. Next to the throne is a chest. "
        print"There is a door headed West in the north corner and the Secret passage near the south headed west."
        print"The room looks otherwise empty."
        print"What do you want to do?  Go through door to the West?  Open the Chest? Go through Secret Passage"
        room4choice=raw_input("Door to the(W)est.  (O)pen Chest. (S)ecret Passage:  ")
        if room4choice=='W' or room4choice=='w':
            Room5(monsterlist,rolllist)
        if room4choice=='O' or room4choice=='o':
            Room4Trap(rolllist)
            goldsack=random.randint(300,1200)
            print"Inside the chest is a sack.  As you pick up the sack it is very light."
            print"Inside you can see what appears to be hundreds of gold coins"
            print"You receive %d gold"%goldsack
            PlayerClass.gold=PlayerClass.gold+goldsack
            RoomsClear.room4chest=True
            Room4(monsterlist,rolllist)
        if room4choice=='S' or room4choice=='s':        
            Room6(monsterlist,rolllist)
    if RoomsClear.room4chest==True and RoomsClear.room4pass==False:    
        print"This 40x50 foot room is well lit by torches. In the back of the room there is a throne. "
        print"There is a door headed West in the north corner.  The room looks otherwise empty."
        print"What do you want to do?  Go through door to the West?  Sit in the Throne?"
        room4choice=raw_input("Door to the(W)est. (S)it in throne?: ")
        if room4choice=='W' or room4choice=='w':
            Room5(monsterlist,rolllist)
        if room4choice=='S' or room4choice=='s':
            print"You sit down in the throne. It is magnificent.  You could see yourself as ruler one day, sitting in one of these."
            print"As you revel in the throne's glory, you notice a button on the right side of the armrest."
            room4button=raw_input("(P)ress the button. (D)on't press the button, get off throne: ")
            if room4button=='P' or room4button=='p':
                print"You press the button and a secret door opens on the west wall"
                RoomsClear.room4pass=True
                RoomsClear.room6pass=True
            if room4button=='D' or room4button=='d':
                print"You get up off the throne."
            Room4(monsterlist,rolllist)
    if RoomsClear.room4chest==True and RoomsClear.room4pass==True:
        print"This 40x50 foot room is well lit by torches. In the back of the room there is a throne. "
        print"There is a door headed West in the north corner and the Secret passage near the south headed west."
        print"The room looks otherwise empty."
        print"What do you want to do?  Go through door to the West?  Go through Secret Passage"
        room4choice=raw_input("Door to the(W)est. (S)ecret Passage:  ")
        if room4choice=='W' or room4choice=='w':
            Room5(monsterlist,rolllist)
        if room4choice=='S' or room4choice=='s':        
            Room6(monsterlist,rolllist)    
    return    
       
def Room5Trap(rolllist):
    print"As you open the door, arrows shoot out of the wall towards you. Make a savings roll"
    result=Roll()
    ChangeName(rolllist)
    print"You rolled a %d"%result
    if result <4:
        arrowdam=random.randint(2,10)*2
        print"The arrow crits you for %d damage!"%arrowdam
        PlayerClass.currenthp=PlayerClass.currenthp-arrowdam
        if PlayerClass.currenthp<1:
            print"You have died!"
            sys.exit()
    if result >3 and result <10:
        arrowdam=random.randint(2,10)
        print"The arrow hits you for %d damage!"%arrowdam
        PlayerClass.currenthp=PlayerClass.currenthp-arrowdam
        if PlayerClass.currenthp<1:
            print"You have died!"
            sys.exit()   
    if result >9 and result <16:
        arrowdam=(random.randint(2,10))/2
        print"The arrow grazes you for %d damage!"%arrowdam
        PlayerClass.currenthp=PlayerClass.currenthp-arrowdam
        if PlayerClass.currenthp<1:
            print"You have died!"
            sys.exit()       
    if result > 15:
        print"You successfully dodged the arrow!"
    return
    
def Room5(monsterlist,rolllist):
    PrintDashboard()
    if RoomsClear.room5==False:
        Room5Trap(rolllist)
        print"The room is small, 10 feet long by 20 feet wide.  The room is almost empty except for the dozens of bloodied broken arrows laying on the floor next to gnawed bones."
        print"Would you like to open the door to the North, Open the door to the East, try to disarm the arrow trap?"
        room5choice=raw_input("Door to the (N)orth, Door to the (E)ast, (D)isarm arrows?: ")
        if room5choice=='N' or room5choice=='n':
            if RoomsClear.room5==True:
                print"You open the door to the North"
                Room3(monsterlist,rolllist)
            if RoomsClear.room5==False:
                Room5Trap(rolllist)
                Room3(monsterlist,rolllist)
        if room5choice=='E' or room5choice=='e':
            print"You open the door to the East"
            if RoomsClear.room5==True:
                Room4(monsterlist,rolllist)
            if RoomsClear.room5==False:
                Room5Trap(rolllist)
                Room4(monsterlist,rolllist)
        if room5choice=='D' or room5choice=='d':
            room5choice2='D'
            while room5choice2=='D' or room5choice2=='d':
                print"You attempt to disarm the trap"
                disarmtrap=Roll()
                print"You rolled a %d"%disarmtrap
                if disarmtrap<2:
                    disarmdamage=random.randint(2,6)
                    print"Attempting to disarm the trap backfired! You take %d damage and were unable to disarm the trap! "%disarmdamage
                    PlayerClass.currenthp=PlayerClass.currenthp-disarmdamage
                    if PlayerClass.currenthp<1:
                        print"You have died"
                        sys.exit()                     
                if disarmtrap>1 and disarmtrap<20:
                    print"You could not figure out how to disarm the trap!"
                if disarmtrap>19:
                    print"You successfully disarmed the trap!"
                    print"You gain 20xp"
                    PlayerClass.xp=PlayerClass.xp+20
                    RoomsClear.room5=True
                    room5choice2=raw_input("Door to the (N)orth, Door to the (E)ast?: ")
                    if room5choice2=='N' or room5choice=='n':
                        Room3(monsterlist,rolllist)
                    if room5choice2=='E' or room5choice=='e':
                        Room4(monsterlist,rolllist)
                room5choice2=raw_input("Door to the (N)orth, Door to the (E)ast, Disarm (A)rrows?: ")      
                if room5choice2=='N' or room5choice=='n':
                    Room3(monsterlist,rolllist)
                if room5choice2=='E' or room5choice=='e':
                    Room4(monsterlist,rolllist)
def Room6(monsterlist,rolllist):
    PrintDashboard()
    if RoomsClear.room6 ==True and RoomsClear.room6pass==True:
        print"You enter the room, it looks familiar, there is two dead corpses on the ground."
        print"There is a painting on the east wall that is rotated 45 degrees and a secret passage heading East"
        print"There is a hallway headed North."
        room6choice=raw_input("(S)ecret passage East, (H)allway North: ")
        if room6choice=='S' or room6choice=='s':
            Room4(monsterlist,rolllist)
        if room6choice=='H' or room6choice=='h':
            Room7(monsterlist,rolllist)
    if RoomsClear.room6 ==True and RoomsClear.room6pass==False:
        print"You enter the room, it looks familiar, there is two dead corpses on the ground."
        print"There is a painting on the east wall and a hallway headed North."
        room6choice=raw_input("(H)allway North or (T)ake Painting: ")
        if room6choice=='T' or room6choice=='t':
            print"You walk over to the painting and try to remove it."
            print"The painting rotates 45 degrees and a secret passage opens up next to it headed east."
            RoomsClear.room6pass=True
            RoomsClear.room4pass=True
            Room6(monsterlist,rolllist)
        if room6choice=='H' or room6choice=='h':
            Room7(monsterlist,rolllist)
    if RoomsClear.room6 ==False and RoomsClear.room6pass ==False:
        print"As you enter the room, two creatures attack you!"
        attackorrun=raw_input("Do you want to (A)ttack or (R)un away?")
        if attackorrun=='A' or attackorrun=='a':
            SelectMonster(monsterlist,False,False)
            Battle(rolllist)
            SelectMonster(monsterlist,False,False)
            Battle(rolllist)
            RoomsClear.room6=True
            Room6(monsterlist,rolllist)
            return
        if attackorrunn=='R' or attackorrun=='r':
            print "You run back into the hallway"
            RoomsClear.room6=False
            Room7(monsterlist,rolllist)
    if RoomsClear.room6 ==False and RoomsClear.room6pass ==True:
        print"As you enter the room, two creatures attack you!"
        attackorrun=raw_input("Do you want to (A)ttack or (R)un away?")
        if attackorrun=='A' or attackorrun=='a':
            SelectMonster(monsterlist,False,False)
            Battle(rolllist)
            SelectMonster(monsterlist,False,False)
            Battle(rolllist)
            RoomsClear.room6=True
            Room6(monsterlist,rolllist)
            return
        if attackorrunn=='R' or attackorrun=='r':
            print "You run back through the secret passage"
            RoomsClear.room6=False
            Room4(monsterlist,rolllist)
            
def Room7(monsterlist,rolllist):
    PrintDashboard()
    if RoomsClear.room7 ==True:
        print"This is a 60x60 foot room.  There is a dead corpse on the ground. "
        print"There is a door to the North and a hallway to the south"
        room7choice=raw_input("Open door to (N)orth.  Hallway to (S)outh? :")
        if room7choice=='N' or room7choice=='n':
            Room8(monsterlist,rolllist)
        if room7choice=='S' or room7choice=='s':
            Room6(monsterlist,rolllist)
    if RoomsClear.room7 ==False:
        print"A creature spots you!"
        attackorrun=raw_input("Do you want to (A)ttack or (R)un away?")
        if attackorrun=='A' or attackorrun=='a':
            SelectMonster(monsterlist,False,False)
            Battle(rolllist)            
            RoomsClear.room7=True
            Room7(monsterlist,rolllist)
        if attackorrun=='R' or attackorrun=='r':
            if RoomsClear.room6==True:
                print "You run back down the hallway"
                Room7(monsterlist,rolllist)
            if RoomsClear.room8==True:
                print "You run back through the door, closing it behind you"
                Room8(monsterlist,rolllist)

def Room8(monsterlist,rolllist):
    print"As you close the door behind you, you step into a small 10x10 foot room."
    print"There is a large pit in the center of the room full of bones"
    print"The bones are covered in a powdery substance.  It's Iocane powder, you're sure of it."
    print"There is a door to the North and a door to the South."
    room8choice=raw_input("(N)orth door. (S)outh Door.")
    if room8choice=='N' or room8choice=='n':
        RoomsClear.room8=True
        Room1(monsterlist,rolllist) 
    if room8choice=='S' or room8choice=='s':
        RoomsClear.room8=True
        Room7(monsterlist,rolllist)

        
Hallway(monsterlist,rolllist)









