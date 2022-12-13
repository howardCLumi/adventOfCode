 # part 2
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