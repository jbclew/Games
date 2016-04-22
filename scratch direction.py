import random
import os
import sys
import platform
import time

class Monster:
    def __init__(self,name,ac,hp,lowdam,highdam,level,xp):
        self.name=name
        self.ac=ac
        self.hp=hp
        self.currenhp=hp
        self.lowdam=lowdam
        self.highdam=highdam
        self.level=level
        self.xp=xp
    def deal_damage(self,lowdam,highdam,dammod):
        dam_done=random.randint(lowdam,highdam)*dammod
        if dammod >= 0:
            print"Monster did %d damage to you!"%dam_done
            if dammod > 0 and dam_done < 1:
                dam_done = 1
        if dammod < 0:
            if dammod < 0 and dam_done < 1:
                dam_done = 1
            print"Monster did %d damage to itself" % abs(dam_done)
        return dam_done
    def take_damage(self,damage):
        self.currenthp=self.currenthp-damage
class Player:
    def __init__(self,name,ac,hp,lowdam,highdam,strength,dex,constitution):
        self.name=name
        self.ac=ac
        self.maxhp=hp
        self.currenthp=hp
        self.lowdam=lowdam
        self.highdam=highdam
        self.level=1
        self.strength=strength
        self.dexterity=dex
        self.constitution=constitution
        self.xp = 0
        self.gold = 0
        self.weaponname = "Fists"
        self.armorname = 'Linens'
    def take_damage(self,damage):
        self.currenthp=self.currenthp-damage
    def deal_damage(self,lowdam,highdam,dammod):
        dam_done=(random.randint(lowdam,highdam)*dammod)+(0.25*self.strength)
        if dammod >= 0:
            print"You did %d damage!"%dam_done
            if dammod > 0 and dam_done < 1:
                dam_done = 1
        if dammod < 0:
            if dammod < 0 and dam_done < 1:
                dam_done = 1
            print"You did %d damage to yourself!" % abs(dam_done)
        return dam_done
    def check_level(self,xp):
        self.xp=self.xp+xp
        levelbefore = self.level
        if self.xp >= 0 and self.xp < 100:
            level = 1
        if self.xp > 99 and self.xp < 300:
            level = 2
        if self.xp > 299 and self.xp < 750:
            level = 3
        if self.xp > 749 and self.xp < 1500:
            level = 4
        if self.xp > 1499 and self.xp < 3000:
            level = 5
        if self.xp > 2999 and self.xp < 5000:
            level = 6
        if self.xp > 4999 and self.xp < 10000:
            level = 7
        if self.xp > 9999 and self.xp < 15000:
            level = 8
        if self.xp > 14999 and self.xp < 20000:
            level = 9
        if self.xp > 19999:
            level = 10
        if level > levelbefore:
            print"Congratulations, you leveled up!!!  Your new level is: %d" % level
            newhp = (random.randint(1, 3)+self.constitution) * (level - levelbefore)
            self.maxhp = self.maxhp + newhp
            self.currenthp = self.maxhp
            self.level = level
            print"You gained %d hp!" % newhp
        return
    def equip_weapon(self,Weapon):
        self.weaponname=Weapon.name
        self.lowdam=Weapon.lowdam
        self.highdam=Weapon.highdam
    def equip_armor(self,Armor):
        self.armorname=Armor.name
        self.ac=Armor.ac

class Room:
    def __init__(self,width,length,havetrap,secret,noofmonsters,maxmonsterlevel,northexit,eastexit,southexit,westexit,description):
        self.width=width
        self.length=length
        self.havetrap=havetrap
        self.secret=secret
        self.noofmonsters=noofmonsters
        self.maxmonsterlevel=maxmonsterlevel
        self.description=description
        self.cleared=False
        self.disarmed=False
        self.northexit=northexit
        self.eastexit=eastexit
        self.southexit=southexit
        self.westexit=westexit
        self.trapname=""
    def clear(self):
        self.cleared=True
    def notclear(self):
        self.cleared=False
    def choose_direction(self):
        print "There are exits to the ",
        if northexit == "True":
            print"(N)orth ",
        if eastexit == "True":
            print"(E)ast ",
        if southexit == "True":
            print"(S)outh ",
        if westexit == "True":
            print"(W)est "
        direction = raw_input("Which way do you want to go: ")
        return direction
    def choose_trap(self,traplist):
        setroomtrap=random.choice(traplist)
        self.trapname=setroomtrap

class Trap:
    def __init__(self, describetrap, traplodam, traphighdam):
        self.describe = describetrap
        self.traplodam = traplodam
        self.traphighdam = traphighdam
        self.disarmed = False
    def disarm_trap(self):
        self.disarmed == "True"

class Weapon:
    def __init__(self,name,minlevel,lowdam,highdam):
        self.name=name
        self.minlevel=minlevel
        self.lowdam=lowdam
        self.highdam=highdam

class Armor:
    def __init__(self, name, ac, minlevel):
        self.name=name
        self.ac=ac
        self.minlevel=minlevel

#weapons
shortsword=Weapon('Short Sword',1,2,4)
longsword=Weapon('Long Sword',1,4,6)
dagger=Weapon('Dagger',1,1,3)
spear=Weapon('Spear',1,3,5)
trident=Weapon('Trident',2,4,8)
staff=Weapon('Staff',2,5,9)
sabre=Weapon('Sabre',3,5,10)
flamedagger=Weapon('Flaming Dagger',4,6,8)
icesword=Weapon('Ice Sword',4,6,11)
twohandedsword=Weapon('Two Handed Sword',5,8,12)
flamedragonstaff=Weapon('Flaming Dragon Staff',5,9,12)
inigosabre=Weapon("Inigos' Sabre",6,10,14)
orbofimpunity=Weapon('Orb of Impunity',6,12,15)
staffofbadass=Weapon('Staff of Bad Assness',7,15,20)
wtf=Weapon('WTF is this?',8,20,25)

#armor
linens=Armor('Linens',1,1)
leather=Armor('Leather',2,1)
robe=Armor('Robe',2,1)
chain=Armor('Chain',4,2)
mail=Armor('Mail',5,2)
paddedmail=Armor('Padded Mail',6,3)
blackgreenrobe=Armor('Black or Green Robe',5,3)
hornedhelm=Armor('Horned Helmet',7,4)
plate=Armor('Plate Mail',8,4)
etherium=Armor('Etherium Armor',10,5)
mailofforce=Armor('Mail of Force',12,5)
fezzikleggings=Armor('Fezzik Leggings',14,6)
tomeofdefense=Armor('Tome of Defense',15,6)
teelabrowncharm=Armor("Teela Browns' Lucky Charm",18,7)
opfield=Armor('OP Forcefield',22,8)

#monsters name,ac,hp,lowdam,highdam,level,xp
kobold=Monster('Kobold',1,2,1,3,1,50)
troll=Monster('Troll',2,3,2,3,1,100)
ooze=Monster('Ooze',4,2,1,4,2,110)
orc=Monster('Orc',3,4,2,5,3,155)
mous=Monster('M.O.U.S',4,3,2,4,3,145)
siciliangnome=Monster('Sicilian Gnome',6,3,1,5,4,200)
giant=Monster('Giant',2,8,4,6,5,275)
humdinkguard=Monster('Humdink Guard',4,6,2,6,5,250)
goblin=Monster('Goblin',3,8,4,7,6,300)
pirate=Monster('Pirate Goon',5,8,5,8,6,310)
skeleton=Monster('Animated Skeleton',6,6,6,9,7,400)
harpy=Monster('Harpy',4,8,4,10,7,450)
goblindealer=Monster('Goblin Salesman',6,12,6,12,8,590)
tiger=Monster('Morphed Tiger',10,10,6,12,8,670)
piraterobert=Monster('Pirate Robert Dread',14,25,10,15,10,1000)


weaponlist = [shortsword,longsword,dagger,spear,trident,staff,sabre,flamedagger,icesword,twohandedsword,flamedagger,inigosabre,orbofimpunity,staffofbadass,wtf]
armorlist = [linens,leather,robe,chain,mail,paddedmail,blackgreenrobe,hornedhelm,plate,etherium,mailofforce,fezzikleggings,tomeofdefense,teelabrowncharm,opfield]
monsterlist = [kobold,troll,ooze,orc,mous,siciliangnome,giant,humdinkguard,goblin,pirate,skeleton,harpy,goblindealer,tiger,piraterobert]

def select_weapon(weaponlist, Player):
    levellist = []
    for item in weaponlist:
        if item.minlevel <= Player.level:
            levellist.append(item)
        if item.minlevel > Player.level:
            pass
    weapon_choice=random.choice(levellist)
    return weapon_choice

def select_armor(armorlist, Player):
    levellist = []
    for item in armorlist:
        if item.minlevel <= Player.level:
            levellist.append(item)
        if item.minlevel > Player.level:
            pass
    armor_choice=random.choice(levellist)
    return armor_choice

def select_monster(monsterlist,Player):
    levellist = []
    for item in monsterlist:
        if item.minlevel <= (Player.level)+2:
            levellist.append(item)
        if item.minlevel > (Player.level)+2:
            pass
    monster_choice=random.choice(levellist)
    return monster_choice

def roll():
    i = 0
    while i < 30:
        rolled = random.randint(1, 20)
        if rolled < 10:
            print "Roll (1d20): %d" % rolled,
            time.sleep(0.1)
            print "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b",
        if rolled > 9:
            print "Roll (1d20): %d" % rolled,
            time.sleep(0.1)
            print "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b",
        i = i + 1
    return rolled

def player_to_hit(Player,Monster):
    base = Player.level/(Monster.level*(0.25*Monster.ac))
    rolled = roll()
    hit = int(round(base*rolled))
    if hit <= 1:
        print("Fumbled!!")
        dammod = -0.25
    if hit > 1 and hit < 5:
        print("Miss!")
        dammod = 0
    if hit > 4 and hit < 10:
        print("Glancing Blow!")
        dammod = 0.5
    if hit > 9 and hit < 17:
        print("A Hit!")
        dammod = 1
    if hit > 16 and hit < 20:
        print("A Crit!")
        dammod = 1.5
    if hit > 19:
        print("An Ultra Crit!")
        dammod = 2.0
    print" Roll: ",roll
    print" Base: ",base
    print" Hit Value :",hit
    return (dammod)

def monster_to_hit(Player,Monster):
    base = Monster.level / (Player.level * (0.5 * Player.ac) * (0.25 * Player.dexterity))
    rolled=roll()
    hit = int(round(base*rolled))
    if hit <= 1:
        print("Fumbled!!")
        dammod = -0.25
    if hit > 1 and hit < 5:
        print("Miss!")
        dammod = 0
    if hit > 4 and hit < 10:
        print("Glancing Blow!")
        dammod = 0.5
    if hit > 9 and hit < 17:
        print("A Hit!")
        dammod = 1
    if hit > 16 and hit < 20:
        print("A Crit!")
        dammod = 1.5
    if hit > 19:
        print("An Ultra Crit!")
        dammod = 2.0
    print" Roll: ",roll
    print" Base: ",base
    print" Hit Value :",hit
    return (dammod)

def Battle(Player,Monster):
    print"You are fighting a %s. Monster Level: %d   Monster Armor: %d   Damage: %d-%d   Monster hp: %d" %(Monster.name,Monster.level,Monster.ac,Monster.lowdam,Monster.highdam,Monster.hp)
    print"Your Stats: Level: %d   AC: %d   Damage: %d-%d   hp: %d "%(Player.level, Player.ac, Player.lowdam, Player.highdam, Player.maxhp)
    while (Player.currenthp > 0) and (Monster.currenthp > 0):
        dammod = player_to_hit(Player,Monster)
        if dammod >= 0:
            player_dam_done = Player.deal_damage(Player.lowdam,Player.highdam,dammod)
            Monster.take_damage(player_dam_done)
        if dammod < 0:
            player_dam_done = Player.deal_damage(Player.lowdam,Player.highdam,dammod)
            Player.take_damage(player_dam_done)
        if (Player.currenthp > 0) and (Monster.currenthp > 0):
            print "%s HP: %d        %s HP: %d"%(Player.name,Player.currenthp,Monster.name,Monster.currenthp)
            dammod = monster_to_hit(Player,Monster)
            print"Current Monster dammd: ",dammod
            if dammod >= 0:
                monster_dam_done = Monster.deal_damage(Monster.lowdam,Monster.highdam,dammod)
                Player.take_damage(monster_dam_done)
                print "%s HP: %d        %s HP: %d"%(Player.name,Player.currenthp,Monster.name,Monster.currenthp)
            if dammod < 0:
                monster_dam_done = Monster.deal_damage(Monster.lowdam,Monster.highdam,dammod)
                Monster.take_damage(monster_dam_done)
                print "%s HP: %d        %s HP: %d"%(Player.name,Player.currenthp,Monster.name,Monster.currenthp)
        if Monster.currenthp < 1:
            print "You killed %s!"%Monster.name
            Player.check_level(Monster.xp)
        if Player.currenthp < 1:
            print"You have been defeated.  A sad day indeed."
            sys.exit()

def leave_or_pick(Player,weapon_choice,armor_choice,rollweapon,rollarmor):
    if rollweapon > 12:
        print"Enemy had %s | damage:%d-%d ."%(weapon_choice.name,weapon_choice.lowdam,weapon_choice.highdam)
        equipit=raw_input("Would you like to (L)eave it alone. (P)ick up %s: "%weapon_choice.name)
        if equipit == 'P' or equipit == 'p':
            Player.equip_weapon(weapon_choice)
        if equipit == 'L' or equipit == 'l':
            return
        if equipit != 'L' and equipit !='l' and equipit !='P' and equipit != 'p':
            print"Not a valid choice please choose (L)eave or (P)ick up"
            leave_or_pick(Player,weapon_choice,armor_choice)
    if rollweapon < 13:
        print "The enemy had no weapons."
    if rollarmor > 12:
        print"Enemy had %s | AC:%d ."%(armor_choice.name,armor_choice.ac)
        equipit=raw_input("Would you like to (L)eave it alone. (P)ick up %s: "%armor_choice.name)
        if equipit == 'P' or equipit == 'p':
            Player.equip_armor(armor_choice)
            return
        if equipit == 'L' or equipit == 'l':
            return
        if equipit != 'L' and equipit !='l' and equipit !='P' and equipit != 'p':
            print"Not a valid choice"
            leave_or_pick(Player,weapon_choice,armor_choice)
    if rollarmor < 13:
        print "The enemy had no armor."
    return

def loot(weaponlist,armorlist,Player):
    rollweapon = random.randint(1,20)
    rollarmor = random.randint(1,20)
    rollgold = random.randint(5,15)*Player.level
    Player.gold = Player.gold + rollgold
    print"Enemy had %d gold!"%rollgold
    weapon_choice=select_weapon(weaponlist, Player)
    armor_choice=select_armor(armorlist, Player)
    leave_or_pick(Player,weapon_choice,armor_choice,rollweapon,rollarmor)
    return


#rooms
#width,length,trap,secret,noofmonsters,maxmonsterlevel,northexit,eastexit,southexit,westexit,description
hallway = Room(6,40,False,False,1,1,True,False,True,False,"You enter the long dimly lit hallway.  It smells damp and undisturbed. A dark tension fills the air.")
#traps
arrowtrap= Trap("Arrows shoot out of the wall at you!",1,3)
traplist=[arrowtrap]

def try_disarm_trap(Player,traplist,Room):
    print "You attempt to disarm the trap"
    rolled=roll()
    if rolled < 4:
        disarm_dam=random.randint(1,3)
        print "Disarming the trap backfires for %d damage!"%disarm_dam
        Player.currenthp = Player.currenthp - disarm_dam
        if Player.currenthp < 1:
            print"You have died trying to disarm a trap.  Game over"
            sys.exit()
    if rolled > 3 and rolled < 17:
        print "You were unable to disarm the trap"
    if rolled > 16:
        print "You successfully disarmed the trap! You gain 50xp"
        Room.disarmed = True
        Player.check_level(50)
    return
        
        
def choose_room(Player,Room,traplist):
        choice = Room.choose_direction()
        if choice == 'D' or choice == 'd':
            pick ='D'
        if Room.northexit == True and (choice == 'N' or choice == 'n'):
            pick = 'N'
        if Room.eastexit == True and (choice == 'E' or choice == 'e'):
            pick = 'E'
        if Room.southexit == True and (choice == 'S' or choice == 's'):
            pick = 'S'
        if Room.westexit == True and (choice == 'W' or choice == 'w'):
            pick = 'W'
        else
            print"Not a valid choice"
            pick ='notvalid'
        return pick
        
def enter_room(Player,Room,traplist):
    print Room.description,
    print "The room is %d x %d",%(Room.width,Room.length)
    if Room.trap == True and Room.disarmed == False:
        trap_choice=Room.choose_Trap(traplist)
        print trap_choice.describe
        savings=roll()
        savings = savings + Player.dexterity
        trapdam = random.randint(trap_choice.lowdam,trap_choice.highdam)
        if savings <4:
            trapdam = trapdam * 2
            print"The trap crits you for %d damage!"%trapdam
            Player.currenthp = Player.currenthp - trapdam
            if Player.currenthp < 1:
                print"You have died from a trap.  Game over"
                sys.exit()
        if savings > 3 and savings < 10:
            print"The trap hits you for %d damage!"%trapdam
            Player.currenthp = Player.currenthp - trapdam
            if Player.currenthp < 1:
                print"You have died from a trap.  Game over"
                sys.exit()
        if savings >9 and savings < 16:
            trapdam = int(trapdam * 0.5)
            print"The trap barely grazes you for %d damage!"%trapdam
            Player.currenthp = Player.currenthp - trapdam
            if Player.currenthp < 1:
                print"You have died from a trap.  Game over"
                sys.exit()
        if savings < 15:
            print"You successfully dodge the trap!"
        pick = choose_room(Player, Room, traplist)
        while pick == 'notvalid':
            pick = choose_room(Player, Room, traplist)
        while pick == 'D':
            try_disarm_trap(Player,traplist,Room)

