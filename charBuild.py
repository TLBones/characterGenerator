import random
import raceBuild
import statBuild
import modifiers
import classes

def newChar():
    strength=statBuild.setStat()
    dex=statBuild.setStat()
    con=statBuild.setStat()
    intel=statBuild.setStat()
    wis=statBuild.setStat()
    cha=statBuild.setStat()

    temp = random.randrange(0,8)
    raceBuild.setRace(temp)
    raceStats=raceBuild.setRaceStats(temp)
    raceStr=raceStats[0]
    raceDex=raceStats[1]
    raceCon=raceStats[2]
    raceInt=raceStats[3]
    raceWis=raceStats[4]
    raceCha=raceStats[5]

    finalStr=strength+raceStr
    finalDex=dex+raceDex
    finalCon=con+raceCon
    finalInt=intel+raceInt
    finalWis=wis+raceWis
    finalCha=cha+raceCha

    finalStats=[finalStr,finalDex,finalCon,finalInt,finalWis,finalCha]
    n=len(finalStats)
    classGet=classes.getClass(finalStats,n)
    
    print(classGet)
    print("Final Stats")
    print(finalStr)
    print(finalDex)
    print(finalCon)
    print(finalInt)
    print(finalWis)
    print(finalCha)
    
    strMod=modifiers.modFind(finalStr)
    strDex=modifiers.modFind(finalDex)
    strCon=modifiers.modFind(finalCon)
    strInt=modifiers.modFind(finalInt)
    strWis=modifiers.modFind(finalWis)
    strCha=modifiers.modFind(finalCha)
    
    print("Modifiers")
    print(strMod)
    print(strDex)
    print(strCon)
    print(strInt)
    print(strWis)
    print(strCha)
    