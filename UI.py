import tkinter as tk
from tkinter import *
import os
import charBuild
import random
import raceBuild
import statBuild
import modifiers
import classes

#Establishing Root
root = tk.Tk()
root.minsize(600,400)
root.maxsize(600,400)
root.wm_title("5E Characters")

finalStr=0
finalDex=0
finalCon=0
finalInt=0
finalWis=0
finalCha=0
strMod=0
dexMod=0
conMod=0
intMod=0
wisMod=0
chaMod=0

#Create Canvas
#Stats
statList= Listbox(root, height=12, width=30, bg="powderblue")
statList.grid(row=0, rowspan=4, column=0, padx=10, pady=10)
baseText=Listbox(statList,height=1,width=15,bg="powderblue")
baseText.grid(row=0,column=0)
baseText.insert(END, "Base Stats")
#Modifiers
modText=Listbox(statList,height=1,width=10,bg="powderblue")
modText.grid(row=0,column=1)
modText.insert(END, "Mods")
mainStats= Listbox(statList, height=12,width=15,bg="powderblue")
mainStats.grid(row=1,column=0)
modStats= Listbox(statList, height=12,width=10,bg="powderblue")
modStats.grid(row=1,column=1)

#Other Details
detailList= Listbox(root, height=12, width=30, fg="powderblue", bg="powderblue")
detailList.grid(row=0, rowspan=4, column=1, padx=10, pady=10)
#Name
nmText=Listbox(detailList,height=1,width=5,bg="powderblue")
nmText.grid(row=0,column=0)
nmText.insert(END, "Name:")
tempName=StringVar()
tempName="John Smith"
charName=tk.Entry(detailList,bg="powderblue",textvariable=tempName)
charName.grid(row=0,column=1)
charName.insert(0, tempName)
#Race Display
raceText=Listbox(detailList,height=1,width=5,bg="powderblue")
raceText.grid(row=1,column=0)
raceText.insert(END, "Race:")
raceBox=Listbox(detailList,height=1,width=20,bg="powderblue")
raceBox.grid(row=1,column=1)
raceBox.insert(END, "Human")


#Set default displays
types=["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]
"""strengthLabel=Label(statList,text="Strength",justify=LEFT)
strengthLabel.grid(row=0,column=0)
dexLabel=Label(statList,text="Dexterity",justify=LEFT)
dexLabel.grid(row=2,column=0)
conLabel=Label(statList,text="Constitution",justify=LEFT)
conLabel.grid(row=4,column=0)
intLabel=Label(statList,text="Intelligence",justify=LEFT)
intLabel.grid(row=6,column=0)
wisLabel=Label(statList,text="Wisdom",justify=LEFT)
wisLabel.grid(row=8,column=0)
chaLabel=Label(statList,text="Charisma",justify=LEFT)
chaLabel.grid(row=10,column=0)"""
finalStats=[finalStr,finalDex,finalCon,finalInt,finalWis,finalCha]
modtypes=["\n","\n","\n","\n","\n","\n"]
finalMods=[str(strMod),str(dexMod),str(conMod),str(intMod),str(wisMod),str(chaMod)]
for i in range(6):
    mainStats.insert(END,types[i])
    mainStats.insert(END,finalStats[i])
for i in range(6):
    modStats.insert(END,modtypes[i])
    modStats.insert(END,finalMods[i])

#Function for creating a random character
def newChar():
    #Delete previous list on button click
    mainStats.delete('0','end')
    modStats.delete('0','end')
    raceBox.delete('0','end')
    #Get base stats
    strength=statBuild.setStat()
    dex=statBuild.setStat()
    con=statBuild.setStat()
    intel=statBuild.setStat()
    wis=statBuild.setStat()
    cha=statBuild.setStat()
    #Set random Race
    temp = random.randrange(0,8)
    race=raceBuild.setRace(temp)
    raceBox.insert(END, str(race))
    #Get race attributes
    raceStats=raceBuild.setRaceStats(temp)
    raceStr=raceStats[0]
    raceDex=raceStats[1]
    raceCon=raceStats[2]
    raceInt=raceStats[3]
    raceWis=raceStats[4]
    raceCha=raceStats[5]
    #Combine values
    finalStr=strength+raceStr
    finalDex=dex+raceDex
    finalCon=con+raceCon
    finalInt=intel+raceInt
    finalWis=wis+raceWis
    finalCha=cha+raceCha
    #Get Class
    finalStats=[finalStr,finalDex,finalCon,finalInt,finalWis,finalCha]
    n=len(finalStats)
    classGet=classes.getClass(finalStats,n)
    #Get modifiers
    strMod=modifiers.modFind(finalStr)
    dexMod=modifiers.modFind(finalDex)
    conMod=modifiers.modFind(finalCon)
    intMod=modifiers.modFind(finalInt)
    wisMod=modifiers.modFind(finalWis)
    chaMod=modifiers.modFind(finalCha)
    finalMods=[str(strMod),str(dexMod),str(conMod),str(intMod),str(wisMod),str(chaMod)]
    finalStats=[str(finalStr),str(finalDex),str(finalCon),str(finalInt),str(finalWis),str(finalCha)]
    for i in range(6):
        mainStats.insert(END,types[i])
        mainStats.insert(END,finalStats[i])
    for i in range(6):
        modStats.insert(END,modtypes[i])
        modStats.insert(END,finalMods[i])


#Make Buttons
makeNew=Button(root, text="New Character", fg="black",bg="gray", command=newChar)
makeNew.grid(row=5, column=0, padx=10, pady=5, sticky=S)
bringSave=Button(root, text="Saved Characters", fg="black",bg="gray")
bringSave.grid(row=5, column=1, padx=10, pady=5, sticky=S)

root.mainloop()