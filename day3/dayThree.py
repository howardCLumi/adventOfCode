"""
using supernovas convention of code
SUPERNOVA IN YOUR DAY 2 CODE, YOU KEEP USING LINES AS A PARAMETER. WHEN DO U
ACTUALLY WRITE INTO LINES FROM INPUT TEXT FILE RAAAAAAAAAAAAAAAAA

my code IS UNFIXABLE
I find the matching letter correctly. I find the correct priority of each letter.
the issue is, i cant add up the priority for a sum. 

SOLUTIONS THAT FAILED:
i've tried global variables (idk if this is even a THING)
i just kept returning the sum to driver program so i would not set prioritySum back to 0 evertime i ran findPrioritySum() BUT IT DIDNT WORK??
I've tried adding it up in every possible location. and it STILL FAILS
i can totally rewrite everything but i want it neat in all the little functions.
back to global variables. WHY GLOBAL NO WORK. I INITIALIZE UP TOP LIKE THIS
global prioritySum
IT WONT LET ME SET IT EQUAL TO 0 AND WHEN I TRY USING IT IN LOCAL FUNCTIONS, IT GIVES ME THE
unrecongizable bs. 

please refer to terminal.txt to see my masterful ability to match letters and assign them points.

"""

def findPrioritySum(itemType):

    I_MAKE_DA_RULES = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 
    "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    for i in I_MAKE_DA_RULES:
        if itemType == i:
            return I_MAKE_DA_RULES.index(i)

def commonItem(itemOne, itemTwo):

    itemType = '' #for sake of readability. i know i can just plug in i to findPrioritySum() function
    
    for i in itemOne:
        for y in itemTwo:
            if i == y:
                print("found the match! its " + i)
                itemType = i
                return findPrioritySum(itemType)

    """
    i tried to use dictionarys but i couldnt figure out how to compare the value 2 in key 1 to value 
    1 in key 2 in a for loop so F in chat (this took me like 2 hours ngl. i solved it in 2 minutes 
    using a double for loop above............................)

    itemDict = {}
    seenValues = set()

    for i in range(len(itemOne)):
        itemDict[i] = itemOne[i]
        #print(itemDict[i])

    for i in range(len(itemTwo)):
        if i in itemDict:
            itemDict[i] = (itemDict[i], itemTwo[i])
        else:
            itemDict[i] = itemTwo[i]
    #print(itemDict)

    for key, values in itemDict.items():
        if values[0] == values[1]:
            print('key: {key}: {values[0]}')
    """

def splitItem(lines):

    prioritySum = 0

    for line in lines:
        line.strip()
        itemOne, itemTwo = line[:len(line)//2], line[len(line)//2:]
        prioritySum += commonItem(itemOne, itemTwo)

    print(prioritySum)

def getResults(lines):

    return (
        splitItem(lines)
    )

#driver program???
with open("dayThreeInputs.txt", "r") as input:
    lines = input.readlines()

getResults(lines)