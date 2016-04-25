import random
import os
import sys
import platform
import time
import textwrap

ver=platform.system()
if ver=='Windows':
    os.system("cls")
    os.system("mode con cols=150 lines=60")
else:
    os.system('clear')
    os.system("stty columns 150,60")

class Monster:
    def __init__(self,name,ac,hp,lowdam,highdam,level,xp):
        self.name=name
        self.ac=ac
        self.hp=hp
        self.currenthp=hp
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
    def __init__(self,name,hp,strength,dex,constitution):
        self.name=name
        self.ac=1
        self.maxhp=hp
        self.currenthp=hp
        self.lowdam=1
        self.highdam=2
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
        dam_done=(random.randint(lowdam,highdam)*dammod)+(0.5*self.strength)
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
        if self.xp >= 0 and self.xp < 200:
            level = 1
        if self.xp > 199 and self.xp < 400:
            level = 2
        if self.xp > 399 and self.xp < 800:
            level = 3
        if self.xp > 799 and self.xp < 1500:
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
            print"-----------------------------------------------------------------------------------------------------------------------------------"
            print"Congratulations, you leveled up!!!  Your new level is: %d" % level
            newhp = (random.randint(1, 3)+self.constitution) * (level - levelbefore)
            self.maxhp = self.maxhp + newhp
            self.currenthp = self.maxhp
            self.level = level
            print"You gained %d hp!" % newhp
            skill_points = 3
            print"You earned 3 skill points to add to your attributes."
            print"Add a point to:"
            while skill_points > 0:
                addpoints = raw_input("(S)trength, (D)exterity, or (C)onstitution: ")
                if addpoints == 'S' or addpoints == 's':
                    self.strength=self.strength + 1
                    skill_points = skill_points - 1
                    print"1 Point added to strength.  Strength is now: %d"%self.strength
                if addpoints == 'D' or addpoints == 'd':
                    self.dexterity = self.dexterity + 1
                    skill_points = skill_points - 1
                    print"1 Point added to dexterity.  Dexterity is now: %d"%self.dexterity
                if addpoints == 'C' or addpoints == 'c':
                    self.constitution = self.constitution + 1
                    skill_points = skill_points - 1
                    print"1 Point added to constitution.  Constitution is now: %d"%self.constitution
                if addpoints != 'S' and addpoints !='s' and addpoints !='D' and addpoints != 'd' and addpoints !='C' and addpoints !='c':
                    print"Not a Valid Choice!"
                print "Skill Points Left: %d"%skill_points
        return
    def equip_weapon(self,Weapon):
        self.weaponname=Weapon.name
        self.lowdam=Weapon.lowdam
        self.highdam=Weapon.highdam
    def equip_armor(self,Armor):
        self.armorname=Armor.name
        self.ac=Armor.ac

class Room:
    def __init__(self,width,length,havetrap,secret,noofmonsters,maxmonsterlevel,northroom,southroom,eastroom,westroom,description):
        self.width=width
        self.length=length
        self.havetrap=havetrap
        self.secret=secret
        self.noofmonsters=noofmonsters
        self.maxmonsterlevel=maxmonsterlevel
        self.description=description
        self.cleared=False
        self.disarmed=False
        self.northroom=northroom
        self.eastroom=eastroom
        self.southroom=southroom
        self.westroom=westroom
        self.trapname=""
    def clear(self):
        self.cleared=True
    def notclear(self):
        self.cleared=False
    def choose_direction(self):
        roomchosen = ""
        print "There are exits to the ",
        if self.northroom != 'none':
            print"(N)orth ",
        if self.southroom != "none":
            print"(S)outh ",
        if self.eastroom != "none":
            print"(E)ast ",
        if self.westroom != "none":
            print"(W)est ",
        if self.havetrap == True and self.disarmed == False:
            print"(D)isarm Trap"
        print"\n"
        direction = raw_input("What do you want to do: ")
        if direction == 'N' or direction == 'n':
            roomchosen = self.northroom
        if direction == 'S' or direction == 's':
            roomchosen = self.southroom
        if direction == 'E' or direction == 'e':
            roomchosen = self.eastroom
        if direction == 'W' or direction == 'w':
            roomchosen = self.westroom
        if direction == 'D' or direction == 'd':
            roomchosen = 'D'
        return roomchosen

    def choose_trap(self,traplist):
        setroomtrap=random.choice(traplist)
        self.trapname=setroomtrap
        return setroomtrap

class Trap:
    def __init__(self, describetrap, traplodam, traphighdam):
        self.describe = describetrap
        self.traplodam = traplodam
        self.traphighdam = traphighdam
        self.disarmed = False
    def disarm_trap(self):
        self.disarmed = True

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

#traps
arrowtrap = Trap("Arrows shoot out of the wall at you!",1,3)
firetrap = Trap("Flames shoot from the wall towards you!",2,4)
acidtrap = Trap("Acid sprays from above!",1,3)
spiketrap = Trap("Spikes shoot up from the ground",2,4)
sonictrap = Trap("Sonic blast surrounds you",2,3)

#rooms width,length,havetrap,secret,noofmonsters,maxmonsterlevel,northroom,southroom,eastroom,westroom,description

txtwidth = 130
hallwrap = textwrap.fill("You enter the long dimly lit hallway.  It smells damp and undisturbed. A dark tension fills the air.", width=txtwidth)
room1wrap = textwrap.fill("This room smells strange, no doubt due to the weird sheets of black slime that drip from cracks in the ceiling and spread across the floor. The slime seeps from the shattered stone of the ceiling at a snails crawl, forming a mess of dangling walls of gook. As you watch, a bit of the stuff separates from a sheet and drops to the ground with a wet plop.", width=txtwidth)
room2wrap = textwrap.fill("Burning torches in iron sconces line the walls of this room, lighting it brilliantly. At the room's center lies a squat stone altar, its top covered in recently spilled blood. A channel in the altar funnels the blood down its side to the floor where it fills grooves in the floor that trace some kind of pattern or symbol around the altar. Unfortunately, you can't tell what it is from your vantage point.", width=txtwidth)
room3wrap = textwrap.fill("You open the door to a scene of carnage. Two male humans, a male elf, and a female dwarf lie in drying pools of their blood. It seems that they might once have been wearing armor, except for the elf, who remains dressed in a blue robe. Clearly they lost some battle and victors stripped them of their valuables.", width=txtwidth)
room4wrap = textwrap.fill("The manacles set into the walls of this room give you the distinct impression that it was used as a prison and torture chamber, although you can see no evidence of torture devices. One particularly large set of manacles -- big enough for an ogre -- have been broken open.", width=txtwidth)
room5wrap = textwrap.fill("This hall is choked with corpses. The bodies of orcs and ogres lie in tangled heaps where they died, and the floor is sticky with dried blood. It looks like the orcs and ogres were fighting. Some side was the victor but you're not sure which one. The bodies are largely stripped of valuables, but a few broken weapons jut from the slain or lie discarded on the floor.", width=txtwidth)
room6wrap = textwrap.fill("The door to this room swings open easily on well-oiled hinges. Beyond it you see that the chamber walls have been disguised by wood paneling, and the stone ceiling and floor are hidden by bright marble tiles. Several large and well-stuffed chairs are arranged about the room along with some small reading tables.", width=txtwidth)
room7wrap = textwrap.fill("Looking into this room, you note four pits in the floor. A wide square is nearest you, a triangular pit beyond it, and a little farther than both lie two circular pits. The room is rectangular nearest you but it widens into a larger rounded chamber starting just beyond the rectangular pit. You note that many flagstones, ceiling tiles, and wall blocks are carved with a skull emblem of some kind, whose dark openings emulate the layout of the pits", width=txtwidth)
room8wrap = textwrap.fill("The strong, sour-sweet scent of vinegar assaults your nose as you enter this room. Sundered casks and broken bottle glass line the walls of this room. Clearly this was someone's wine cellar for a time. The shards of glass are somewhat dusty, and the spilled wine is nothing more than a sticky residue in some places.", width=100)
room9wrap = textwrap.fill("You inhale a briny smell like the sea as you crack open the door to this chamber. Within you spy the source of the scent: a dark and still pool of brackish water within a low circular wall. Above it stands a strange statue of a lobster-headed and clawed woman. The statue is nearly 15 feet tall ", width=txtwidth)
room10wrap = textwrap.fill("This small room contains several pieces of well-polished wood furniture. Eight ornate, high-backed chairs surround a long oval table, and a side table stands next to the far exit. All bear delicate carvings of various shapes. One bears carvings of skulls and bones, another is carved with shields and magic circles, and a third is carved with shapes like flames and lightning strokes. ", width=txtwidth)
room11wrap = textwrap.fill("You peer into this room and spot the white orb of a skull lying on the floor. Suddenly a stone falls from the ceiling and smashes the skull to pieces. An instant later, another stone from the ceiling drops to strike the floor and shatter. You hear a low rumbling and cracking noise", width=txtwidth)
room12wrap = textwrap.fill("You pull open the door and hear the scrape of its opening echo throughout what must be a massive room. Peering inside, you see a vast cavern. Stalactites drip down from the ceiling in sharp points while flowstone makes strange shapes on the floor.", width=txtwidth)

hallway = Room(10,30,False,False,0,1,'none','room1','none','none',hallwrap)
room1 = Room(30,35,False,False,1,1,'hallway','room3','none','room2',room1wrap)
room2 = Room(20,40,False,False,2,1,'none','room3','room1','none',room2wrap)
room3 = Room(15,30,True,False,0,1,'none','room4','room1','room2',room3wrap)
room4 = Room(55,30,False,False,1,2,'room3','none','room5','none',room4wrap)
room5 = Room(25,10,True,False,1,2,'room6','room4','none','none',room5wrap)
room6 = Room(30,40,False,False,2,3,'room7','none','room8','room5',room6wrap)
room7 = Room(40,20,False,False,1,4,'room9','room6','none','none',room7wrap)
room8 = Room(20,10,True,False,1,4,'room9','room6','none','none',room8wrap)
room9 = Room(35,30,False,False,2,5,'none','room8','room10','room7',room9wrap)
room10 = Room(35,55,False,False,1,6,'none','room11','none','room9',room10wrap)
room11 = Room(20,15,True,False,1,7,'room10','room12','none','none',room11wrap)
room12 = Room(65,40,False,False,2,7,'room11','none','none','none',room12wrap)

weaponlist = [shortsword,longsword,dagger,spear,trident,staff,sabre,flamedagger,icesword,twohandedsword,flamedagger,inigosabre,orbofimpunity,staffofbadass,wtf]
armorlist = [linens,leather,robe,chain,mail,paddedmail,blackgreenrobe,hornedhelm,plate,etherium,mailofforce,fezzikleggings,tomeofdefense,teelabrowncharm,opfield]
monsterlist = [kobold,troll,ooze,orc,mous,siciliangnome,giant,humdinkguard,goblin,pirate,skeleton,harpy,goblindealer,tiger,piraterobert]
traplist = [arrowtrap,firetrap,acidtrap,spiketrap,sonictrap]

def initial_start():
    print"-----------------------------------------------------------------------------------------------------------------------------------"
    print"                                  Welcome to the Tomb of the Pirate Robert Dread"
    print"-----------------------------------------------------------------------------------------------------------------------------------"
    print"              Explanation of Stats:"
    print"-----------------------------------------------------------------------------------------------------------------------------------"
    print"              hp (Hit Points): Amount of health you have when this reaches 0 you die."
    print"              ac (Armor Class): This will reduce the amount of damage you take."
    print"              Strength: This attribute will add to the amount of damage you do"
    print"              Dexterity: This attribute will help reduce your chance to get hit"
    print"              Constitution: This attribute will increase the amount of hp you get when you level"
    print"              Damage: The range of damage you deal.  ex (1-4)"
    print"              Directions: choose options by entering the letter in parenthesis.  ex. (N)orth : N"
    print"              If you pick up a weapon or armor the previous weapon or armor will be permanently destroyed!"
    print"-----------------------------------------------------------------------------------------------------------------------------------"
    skill_points = 8
    strength = 1
    dex = 1
    con = 1
    name = raw_input("Please enter a name for your character: ")
    print"You start with 8 skill points to add to your attributes."
    print"Add a point to:"
    while skill_points > 0:
        addpoints = raw_input("(S)trength, (D)exterity, or (C)onstitution: ")
        if addpoints == 'S' or addpoints == 's':
            strength = strength + 1
            skill_points = skill_points - 1
            print"1 Point added to strength.  Strength is now: %d" %strength
        if addpoints == 'D' or addpoints == 'd':
            dex = dex + 1
            skill_points = skill_points - 1
            print"1 Point added to dexterity.  Dexterity is now: %d" %dex
        if addpoints == 'C' or addpoints == 'c':
            con = con + 1
            skill_points = skill_points - 1
            print"1 Point added to constitution.  Constitution is now: %d" %con
        if addpoints != 'S' and addpoints != 's' and addpoints != 'D' and addpoints != 'd' and addpoints != 'C' and addpoints != 'c':
            print"Not a Valid Choice!"
        print "Skill Points Left: %d" % skill_points
    hp = random.randint(4,8)+con
    playerone=Player(name,hp,strength,dex,con)
    return playerone

def PrintDashboard(Player):
    print"\n\n\n\n\n"

    print"-----------------------------------------------------------------------------------------------------------------------------------"
    print"  _____          _           __   _   _          ___ _          _         ___     _             _     ___                  _  "
    print" |_   _|__ _ __ | |__   ___ / _| | |_| |_  ___  | _ (_)_ _ __ _| |_ ___  | _ \___| |__  ___ _ _| |_  |   \ _ _ ___ __ _ __| | "
    print"   | |/ _ \ '  \| '_ \ / _ \  _| |  _| ' \/ -_) |  _/ | '_/ _` |  _/ -_) |   / _ \ '_ \/ -_) '_|  _| |  ) | '_/ -_) _` / _` | "
    print"   |_|\___/_|_|_|_.__/ \___/_|    \__|_||_\___| |_| |_|_| \__,_|\__\___| |_|_\___/_.__/\___|_|  \__/ |___/|_| \___\__,_\__,_| "
    print"                                                                                                                                  "

    print"-----------------------------------------------------------------------------------------------------------------------------------"
    print"-----------------------------------------------------DASHBOARD --------------------------------------------------------------------"
    print"-----------------------------------------------------------------------------------------------------------------------------------"
    print"\n \n"
    print"   XP: %d         Gold: %d        Armor: %s               AC:%d                   Damage: %s(%d-%d)+%d          Name: %s "% (Player.xp,Player.gold,Player.armorname,Player.ac,Player.weaponname,Player.lowdam,Player.highdam,0.5*Player.strength,Player.name)
    print"   HP: %d/%d     Level: %d       Strength: %d                 Dexterity: %d           Constitution: %d"% (Player.currenthp,Player.maxhp,Player.level,Player.strength,Player.dexterity,Player.constitution)
    print"\n \n"
    print"-----------------------------------------------------------------------------------------------------------------------------------"
    print"Hall:%s  One:%s  Two:%s  Three:%s  Four:%s  Five:%s  Six:%s  Seven:%s  Eight:%s  Nine:%s  Ten:%s  Eleven:%s  Twelve:%s"%(hallway.cleared,room1.cleared,room2.cleared,room3.cleared,room4.cleared,room5.cleared,room6.cleared,room7.cleared,room8.cleared,room9.cleared,room10.cleared,room11.cleared,room12.cleared)
    return

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
        if item.level <= (Player.level)+1:
            levellist.append(item)
        if item.level > (Player.level)+1:
            pass
    monster_choice=random.choice(levellist)
    monster_choice.currenthp=monster_choice.hp
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
    print"\n"
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
    return (dammod)

def monster_to_hit(Player,Monster):
    base = Monster.level / (Player.level * (0.5 * Player.ac) * (0.25 * Player.dexterity))
    rolled=roll()
    hit = int(round(base*rolled))
    print"\n"
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
    return (dammod)

def Battle(Player,Monster,weaponlist,armorlist):
    print"You are fighting a %s." %Monster.name
    print"Monster Level: %d   Monster Armor: %d   Damage: %d-%d   Monster hp: %d" %(Monster.level,Monster.ac,Monster.lowdam,Monster.highdam,Monster.hp)
    print"Your Stats: Level: %d   AC: %d   Damage: %d-%d   hp: %d "%(Player.level, Player.ac, Player.lowdam, Player.highdam, Player.currenthp)
    while (Player.currenthp >= 1) and (Monster.currenthp >= 1):
        dammod = player_to_hit(Player,Monster)
        if dammod >= 0 and Monster.currenthp >= 1 and Player.currenthp >= 1:
            player_dam_done = Player.deal_damage(Player.lowdam,Player.highdam,dammod)
            Monster.take_damage(player_dam_done)
            if Monster.currenthp < 1:
                print "You killed %s!"%Monster.name
                Player.check_level(Monster.xp)
                loot(weaponlist, armorlist, Player)
            if Player.currenthp < 1:
                print"You have been defeated.  A sad day indeed."
                sys.exit()
        if dammod < 0 and Monster.currenthp >= 1 and Player.currenthp >= 1:
            player_dam_done = Player.deal_damage(Player.lowdam,Player.highdam,dammod)
            Player.take_damage(player_dam_done)
            if Monster.currenthp < 1:
                print "You killed %s!"%Monster.name
                Player.check_level(Monster.xp)
                loot(weaponlist, armorlist, Player)
            if Player.currenthp < 1:
                print"You have been defeated.  A sad day indeed."
                sys.exit()
        if (Player.currenthp >= 1) and (Monster.currenthp >= 1):
            print "%s HP: %d        %s HP: %d"%(Player.name,Player.currenthp,Monster.name,Monster.currenthp)
            dammod = monster_to_hit(Player,Monster)
            if dammod >= 0 and Monster.currenthp >= 1 and Player.currenthp >= 1:
                monster_dam_done = Monster.deal_damage(Monster.lowdam,Monster.highdam,dammod)
                Player.take_damage(monster_dam_done)
                print "%s HP: %d        %s HP: %d"%(Player.name,Player.currenthp,Monster.name,Monster.currenthp)
                if Monster.currenthp < 1:
                    print "You killed %s!" % Monster.name
                    Player.check_level(Monster.xp)
                    loot(weaponlist, armorlist, Player)
                if Player.currenthp < 1:
                    print"You have been defeated.  A sad day indeed."
                    sys.exit()
            if dammod < 0 and Monster.currenthp >= 1 and Player.currenthp >= 1:
                monster_dam_done = Monster.deal_damage(Monster.lowdam,Monster.highdam,dammod)
                Monster.take_damage(monster_dam_done)
                print "%s HP: %d        %s HP: %d"%(Player.name,Player.currenthp,Monster.name,Monster.currenthp)
                if Monster.currenthp < 1:
                    print "You killed %s!"%Monster.name
                    Player.check_level(Monster.xp)
                    loot(weaponlist, armorlist, Player)
                if Player.currenthp < 1:
                    print"You have been defeated.  A sad day indeed."
                    sys.exit()
    print "-----------------------------------------------------------------------------------------------------------------------------------"
    return

def leave_or_pick(Player,weapon_choice,armor_choice,rollweapon,rollarmor):
    if rollweapon > 12:
        print"Enemy had %s | Damage: %d-%d."%(weapon_choice.name,weapon_choice.lowdam,weapon_choice.highdam)
        equipit=raw_input("Would you like to (L)eave it alone. (P)ick up %s: "%weapon_choice.name)
        if equipit == 'P' or equipit == 'p':
            Player.equip_weapon(weapon_choice)
        if equipit == 'L' or equipit == 'l':
            pass
        if equipit != 'L' and equipit !='l' and equipit !='P' and equipit != 'p':
            print"Not a valid choice please choose (L)eave or (P)ick up"
            leave_or_pick(Player,weapon_choice,armor_choice)
    if rollweapon < 13:
        print "The enemy had no weapons."
    if rollarmor > 12:
        print"Enemy had %s | AC:%d."%(armor_choice.name,armor_choice.ac)
        equipit=raw_input("Would you like to (L)eave it alone. (P)ick up %s: "%armor_choice.name)
        if equipit == 'P' or equipit == 'p':
            Player.equip_armor(armor_choice)
        if equipit == 'L' or equipit == 'l':
            pass
        if equipit != 'L' and equipit !='l' and equipit != 'P' and equipit != 'p':
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
    print"-----------------------------------------------------------------------------------------------------------------------------------"
    print"Enemy had %d gold!"%rollgold
    weapon_choice=select_weapon(weaponlist, Player)
    armor_choice=select_armor(armorlist, Player)
    leave_or_pick(Player,weapon_choice,armor_choice,rollweapon,rollarmor)
    return

def try_disarm_trap(Player,Room):
    print "You attempt to disarm the trap"
    rolled=roll()
    print"\n"
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
        Room.clear()
        Player.check_level(50)
    return

def enter_room(Player,Room,traplist,monsterlist):
    PrintDashboard(Player)
    print Room.description
    print "The room is %d x %d"%(Room.width,Room.length)
    print "-----------------------------------------------------------------------------------------------------------------------------------"
    if Room.cleared == True:
        print"This room looks familiar, you think you have been here before"
    if Room.noofmonsters > 0 and Room.cleared == False:
        nomonsters=Room.noofmonsters
        print"There is %d creature(s) in this room!"%nomonsters
        stay_or_go = raw_input("(A)ttack or (R)un: ")
        if stay_or_go == 'A' or stay_or_go == 'a':
            while nomonsters > 0:
                Monster=select_monster(monsterlist,Player)
                Battle(Player,Monster,weaponlist,armorlist)
                nomonsters = nomonsters - 1
            Room.clear()
        if stay_or_go == 'R' or stay_or_go == 'r':
            print"You try to run away!"
            run_roll=roll()
            if run_roll > 5:
                print"\n"
                print"You were able to evade the enemy!"
            if run_roll < 6:
                print"\n"
                print"The enemy spots you and it attacks!"
                time.sleep(2.0)
                while nomonsters >0:
                    Monster=select_monster(monsterlist,Player)
                    Battle(Player,Monster,weaponlist,armorlist)
                    nomonsters = nomonsters - 1
        if stay_or_go != 'R' and stay_or_go != 'r' and stay_or_go != 'A' and stay_or_go != 'a':
            print"That was not a valid choice, your mistake has cost you as the enemy attacks!"
            while nomonsters >0:
                Monster=select_monster(monsterlist,Player)
                Battle(Player,Monster,weaponlist,armorlist)
                nomonsters = nomonsters - 1
    if Room.havetrap == True and Room.disarmed == False:
        trap_choice=Room.choose_trap(traplist)
        print trap_choice.describe
        savings=roll()
        savings = savings + Player.dexterity
        trapdam = random.randint(trap_choice.traplodam,trap_choice.traphighdam)
        if savings < 4:
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
        if savings > 15:
            print"You successfully dodge the trap!"
    choice = Room.choose_direction()
    while choice == 'D':
        try_disarm_trap(Player,Room)
        choice = Room.choose_direction()
    return choice

playerone=initial_start()
nextrm = enter_room(playerone, hallway, traplist, monsterlist)
hallway.clear()
while hallway.cleared == False or room1.cleared == False or room2.cleared == False or room3.cleared == False or room4.cleared == False or room5.cleared == False or room6.cleared == False or room7.cleared == False or room8.cleared == False or room9.cleared == False or room10 == False or room11 == False or room12 == False:
    next_room=eval(nextrm)
    nextrm = enter_room(playerone,next_room,traplist,monsterlist)
print"A figure appears from smoke in the middle of the room"
print"He says I am the Pirate Robert Dread.  You have defiled my tomb and looted my wares.  Prepare to meet your doom."
start = raw_input("Press Enter to start battle!")
Battle(playerone,piraterobert,weaponlist,armorlist)
print"You have defeated the mighty Pirate Robert Dread.  You have looted his tomb and cleared it of monsters."
print"Today is a glorious day! You head back to town to start your new life"
print"The End"