"""
# A X = Rock 1
# B  Y = Paper 2
# C  Z = Scissors 3
# Lose = 0
# Draw = 3
# Win = 6
# [x y, x y] X = enemy Y = you
"""

"""
If I was smart, i would use a hashmap. but i read somewhere to use the 
method that comes to mind first. unfortunately for me, its a million
if statements. but i do plan on going back to creating a more efficient
algorithm. 
could also use enums!!!!
could represent rock paper scissors as bits
rock paper scissors (0, 1, -1)
use cases
"""

#Points counter
pointCounter = 0

#array to see if I correctly got rid of all \n
fileWithOutLines = []

#reading input file and putting contents into input array
with open("dayTwoInputs.txt", "r") as input:
    inputs = input.readlines()

#getting rid of \n in inputs file and putting results into new array fileWithoutLines
for line in inputs:
    line = line.strip()
    fileWithOutLines.append(line)
#print(fileWithOutLines)

"""
possible combinations for C
C A WIN 7 points
C B LOSS 2 points
C C DRAW 6 points
possible combinations for B
B A LOSS 1 point
B B DRAW 5 points
B C WIN 9 points
possible combinations for A
A A DRAW 4 points
A B WIN 8 points
A C LOSS 3 points
"""

# PART I
"""
edit: it works now. I read my inputs as A B C instead of X Y Z
y this no work. my output for pointCounter = 0
for loop for array fileWithOutLines (this is correct. inputs are formatted correctly. line 32 shows inputs)
if first index starts with C, it will then check for what it ends with and it will count the amount of points.
what is suppose to happen via my head is if index starts with C. it will enter if block lines 56-62. I didnt 
include else since i am assuming there are no errors in input AND even when i included 
else:
    pass
it still failed.
dont tell me tho. i just showing you for funsies. ill figure it out in the morning
"""

'''
for index in fileWithOutLines:
    if index.startswith('C'):
        if index.endswith('X'):
            pointCounter = pointCounter + 7
        elif index.endswith('Y'):
            pointCounter = pointCounter + 2
        elif index.endswith('Z'):
            pointCounter = pointCounter + 6
    elif index.startswith('B'):
        if index.endswith('X'):
            pointCounter = pointCounter + 1
        elif index.endswith('Y'):
            pointCounter = pointCounter + 5
        elif index.endswith('Z'):
            pointCounter = pointCounter + 9
    elif index.startswith('A'):
        if index.endswith('X'):
            pointCounter = pointCounter + 4
        elif index.endswith('Y'):
            pointCounter = pointCounter + 8
        elif index.endswith('Z'):
            pointCounter = pointCounter + 3
    else:
        pass
print(pointCounter)
'''

# PART II
"""
X = NEED TO LOSE
Y = DRAW
Z = NEED TO WIN
"""
# A = Rock 1
# B = Paper 2
# C = Scissors 3
for index in fileWithOutLines:
    if index.startswith('C'):
        if index.endswith('X'):
            pointCounter = pointCounter + 2
        elif index.endswith('Y'):
            pointCounter = pointCounter + 6
        elif index.endswith('Z'):
            pointCounter = pointCounter + 7
    elif index.startswith('B'):
        if index.endswith('X'):
            pointCounter = pointCounter + 1
        elif index.endswith('Y'):
            pointCounter = pointCounter + 5
        elif index.endswith('Z'):
            pointCounter = pointCounter + 9
    elif index.startswith('A'):
        if index.endswith('X'):
            pointCounter = pointCounter + 3
        elif index.endswith('Y'):
            pointCounter = pointCounter + 4
        elif index.endswith('Z'):
            pointCounter = pointCounter + 8
    else:
        pass
print(pointCounter)