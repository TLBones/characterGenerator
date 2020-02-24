import random

classArray=[["Barbarian","Fighter"],["Rogue","Ranger"],["Barbarian","Fighter"],["Wizard","Druid"],["Wizard","Druid"],["Bard","Warlock","Socerer"]]

#Fighter, Barbarian=>Strength, constitution
#Wizards, Druids=>Wisdom, Intelligence
#Rogues, Rangers=> Dexterity
#Bards, Warlocks, Sorcerers=> Charisma

def largest(arr,n): 
  
    # Initialize maximum element 
    max = arr[0] 
  
    # Traverse array elements from second 
    # and compare every element with  
    # current max 
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max

def getClass(stats,n):
    large=largest(stats,n)
    for i in range(0,5):
        if stats[i]==large:
            tempClass=classArray[i]
            charClass=tempClass[random.randrange(0,1)]
            return charClass
    return charClass


