import random

classArray=[["Barbarian","Fighter","Monk"],["Rogue","Ranger","Monk"],["Barbarian","Monk","Fighter","Cleric"],["Wizard","Druid"],["Wizard","Druid","Cleric"],["Bard","Warlock","Socerer"]]

#Fighter, Barbarian=>Strength, constitution
#Wizards, Druids=>Wisdom, Intelligence
#Rogues, Rangers=> Dexterity
#Bards, Warlocks, Sorcerers=> Charisma

def largest(arr,n): 
    # Initialize maximum element 
    max = arr[0] 
    # Traverse array elements from second and compare every element with current max 
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max

def getClass(stats,n):
    large=largest(stats,n)
    for i in range(0,6):
        if stats[i]==large:
            tempClass=classArray[i]
            tempClassLength=len(tempClass)
            charClass=tempClass[random.randrange(0,tempClassLength)]
            return charClass
