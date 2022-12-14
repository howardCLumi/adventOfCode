
with open("dayThreeInputs.txt", "r") as input:
    lines = input.readlines()

iterationCounter = 0
elfCounter = 0
elf0 = set()
elf1 = set()
elf2 = set()

for line in lines:
    line = line.strip()

for elfCounter in range(10):

    if elfCounter % 3 == 1:
        print(elfCounter)
        elfCounter = 0
    else:
        print(elfCounter)

"""
    if elfCounter % 3 == 0:
            elfCounter = 0

    for char in line:

        print(char)
        elf[elfCounter] = char

    #print("this is elf {}".format(elfCounter) + " items: " + elf[elfCounter])
    elfCounter += 1
"""