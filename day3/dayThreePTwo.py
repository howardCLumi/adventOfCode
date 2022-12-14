 # part 2
def findPrioritySum(itemType):

    I_MAKE_DA_RULES = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 
    "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
    "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    for i in I_MAKE_DA_RULES:
        if itemType == i:
            return I_MAKE_DA_RULES.index(i)

def splitElves(lines):

    
    prioritySum = 0
    elf0 = set()
    elf1 = set()

    for i, line in enumerate(lines):
        line = line.strip()  
        print(line)

        if i % 3 == 0:
            elf0 = set(list(line))
        if i % 3 == 1:
            elf1 = set(list(line))
        if i % 3 == 2:
            #print(x)
            for x in line:
                if x in elf1 and x in elf0:
                    prioritySum += findPrioritySum(x)
                    break

    return prioritySum
                    
def getResults(lines):
    return (
        splitElves(lines)
    )

#driver program???
with open("dayThreeInputs.txt", "r") as input:
    lines = input.readlines()

print(getResults(lines))