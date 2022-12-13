set1 = set()
set2 = set()

with open("dayThreeInputs.txt", "r") as input:
    lines = input.readlines()

i = 1
for line in lines:
        #set[i] = line.strip()
        if i % 3 == 0:
            i = 1
        print(set[i])
        i += 1
    
