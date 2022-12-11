with open("dayOneInputs.txt", "r") as input:
    lines = input.readlines()

calories = []
counter = 0
for line in lines:
    line = line.strip()
    if line == "":
        calories.append(counter)
        counter = 0
    else:
        counter = counter + int(line)
calories.append(counter)
print(max(calories))

calories.sort()
calories.reverse()
print(calories[0] + calories[1] + calories[2])

print(sum(calories[:-3]))
#removes the last 3 elements