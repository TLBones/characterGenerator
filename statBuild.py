import random

def setStat():
    hold1 = random.randrange(1,6)
    hold2 = random.randrange(1,6)
    hold3 = random.randrange(1,6)
    hold4 = random.randrange(1,6)
    holdArray=[hold1,hold2,hold3,hold4]
    holdArray.remove(min(holdArray))
    stat = holdArray[0]+holdArray[1]+holdArray[2]
    return stat
"""
strength=setStat()
dex=setStat()
con=setStat()
intel=setStat()
wis=setStat()
cha=setStat()

print("STRENGTH: " + str(strength))
print("DEXTERITY: " + str(dex))
print("CONSTITUTION: " + str(con))
print("INTELLIGENCE: " + str(intel))
print("WISDOM: " + str(wis))
print("CHARISMA: " + str(cha))
"""