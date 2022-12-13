 # part 2
def findPrioritySum(itemType):

    I_MAKE_DA_RULES = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 
    "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    for i in I_MAKE_DA_RULES:
        if itemType == i:
            return I_MAKE_DA_RULES.index(i)

def commonItem(elf):
    
    for i in itemOne:
        for y in itemTwo:
            if i == y:
                print("found the match! its " + i)
                itemType = i
                return findPrioritySum(itemType)

def splitElves(lines):

    iterationCounter = 0
    elfCounter = 0
    elf = ' '
    elf1 = set()
    elf2 = set()

    for line in lines:
        line = line.strip()
        iterationCounter += 1
        elfCounter += 1
        elf[elfCounter] = line
        print("this is elf {}".format(elfCounter) + " items: " + elf[elfCounter])

        if iterationCounter % 3 == 0:
            elfCounter = 0
            iterationCounter = 0
            commonItem(elf)


def getResults(lines):
    return (
        splitElves(lines)
    )

#driver program???
with open("dayThreeInputs.txt", "r") as input:
    lines = input.readlines()

getResults(lines)