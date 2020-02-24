import random
strength=0
dex=0
con=0
intel=0
wis=0
cha=0
charStats=[strength, dex, con, intel, wis, cha]

dragonborn=[2,0,0,0,0,1]
dwarf=[0,0,2,0,0,0]
elf=[0,2,0,0,0,0]
gnome=[0,0,0,2,0,0]
halfElf=[0,0,0,0,0,2]
halfling=[0,2,0,0,0,0]
halfOrc=[2,0,1,0,0,0]
human=[1,1,1,1,1,1]
tiefling=[0,0,0,1,0,2]
races=["Dragonborn","Dwarf","Elf","Gnome","Half-Elf","Halfling","Half-Orc","Human","Tiefling"]
raceArray=[dragonborn,dwarf,elf,gnome,halfElf,halfling,halfOrc,human,tiefling]

def setRace(n):
    race=races[n]
    print(race)
    return race

def setRaceStats(n):
    raceStats=raceArray[n]
    return raceStats
