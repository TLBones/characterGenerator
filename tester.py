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

#Creating Canvas and outline
#Main holder
mainList= Listbox(root, height=12, width=30, bg="powderblue")
mainList.grid(row=0,rowspan=4,column=0,padx=10,pady=10)

#Temporary Stat Holders
tempStr=10
tempDex=10
tempCon=10
tempInt=10
tempWis=10
tempCha=10
finalStr=StringVar(value=tempStr)
finalDex=StringVar(value=tempDex)
finalCon=StringVar(value=tempCon)
finalInt=StringVar(value=tempInt)
finalWis=StringVar(value=tempWis)
finalCha=StringVar(value=tempCha)
finalStats=[finalStr,finalDex,finalCon,finalInt,finalWis,finalCha]

#Stats
statList=Listbox(mainList, height=12, width=8,bg="powderblue")
statList.grid(row=0,column=0)
#Base Stats
baseTex=Label(statList,text="Base Stats")
strLabel=Label(statList,text="Strength",bg="powderblue")
strLabel.grid(column=0,row=1)
strTex=tk.Entry(statList,textvariable=finalStr,width=5)
strTex.grid(column=1,row=1)
dexLabel=Label(statList,text="Dexterity",bg="powderblue")
dexLabel.grid(column=0,row=2)
dexTex=tk.Entry(statList,textvariable=finalDex,width=5)
dexTex.grid(column=1,row=2)
conLabel=Label(statList,text="Constitution",bg="powderblue")
conLabel.grid(column=0,row=3)
conTex=tk.Entry(statList,textvariable=finalCon,width=5)
conTex.grid(column=1,row=3)
intLabel=Label(statList,text="Intelligence",bg="powderblue")
intLabel.grid(column=0,row=4)
intTex=tk.Entry(statList,textvariable=finalInt,width=5)
intTex.grid(column=1,row=4)
wisLabel=Label(statList,text="Wisdom",bg="powderblue")
wisLabel.grid(column=0,row=5)
wisTex=tk.Entry(statList,textvariable=finalWis,width=5)
wisTex.grid(column=1,row=5)
chaLabel=Label(statList,text="Charisma",bg="powderblue")
chaLabel.grid(column=0,row=6)
chaTex=tk.Entry(statList,textvariable=finalCha,width=5)
chaTex.grid(column=1,row=6)

#Mod values
#def statUpdate(finalStats):
tempStrMod=modifiers.modFind(int(strTex.get()))
tempDexMod=modifiers.modFind(int(dexTex.get()))
tempConMod=modifiers.modFind(int(conTex.get()))
tempIntMod=modifiers.modFind(int(intTex.get()))
tempWisMod=modifiers.modFind(int(wisTex.get()))
tempChaMod=modifiers.modFind(int(chaTex.get()))
strMod=StringVar(value=tempStrMod)
dexMod=StringVar(value=tempDexMod)
conMod=StringVar(value=tempConMod)
intMod=StringVar(value=tempIntMod)
wisMod=StringVar(value=tempWisMod)
chaMod=StringVar(value=tempChaMod)
modArray=[strMod,dexMod,conMod,intMod,wisMod,chaMod]

#Mod List
strModTex=tk.Entry(statList,textvariable=strMod,width=5)
strModTex.config(state=DISABLED)
strModTex.grid(column=2,row=1)
dexModTex=tk.Entry(statList,textvariable=dexMod,width=5)
dexModTex.config(state=DISABLED)
dexModTex.grid(column=2,row=2)
dexModTex.insert(END,dexMod)
conModTex=tk.Entry(statList,textvariable=conMod,width=5)
conModTex.config(state=DISABLED)
conModTex.grid(column=2,row=3)
conModTex.insert(END,conMod)
intModTex=tk.Entry(statList,textvariable=intMod,width=5)
intModTex.config(state=DISABLED)
intModTex.grid(column=2,row=4)
intModTex.insert(END,intMod)
wisModTex=tk.Entry(statList,textvariable=wisMod,width=5)
wisModTex.config(state=DISABLED)
wisModTex.grid(column=2,row=5)
wisModTex.insert(END,wisMod)
chaModTex=tk.Entry(statList,textvariable=chaMod,width=5)
chaModTex.config(state=DISABLED)
chaModTex.grid(column=2,row=6)
chaModTex.insert(END,chaMod)

#Update Modifiers regularly
def modUpdate():
    #Setting Values
    tempStrMod=modifiers.modFind(int(strTex.get()))
    tempDexMod=modifiers.modFind(int(dexTex.get()))
    tempConMod=modifiers.modFind(int(conTex.get()))
    tempIntMod=modifiers.modFind(int(intTex.get()))
    tempWisMod=modifiers.modFind(int(wisTex.get()))
    tempChaMod=modifiers.modFind(int(chaTex.get()))
    strMod=StringVar(value=tempStrMod)
    dexMod=StringVar(value=tempDexMod)
    conMod=StringVar(value=tempConMod)
    intMod=StringVar(value=tempIntMod)
    wisMod=StringVar(value=tempWisMod)
    chaMod=StringVar(value=tempChaMod)
    #Update
    strModTex.configure(textvariable=strMod)
    dexModTex.configure(textvariable=dexMod)
    conModTex.configure(textvariable=conMod)
    intModTex.configure(textvariable=intMod)
    wisModTex.configure(textvariable=wisMod)
    chaModTex.configure(textvariable=chaMod)    
    #Repeat
    root.after(1000, modUpdate)
modUpdate()

#Run and compile
root.mainloop()