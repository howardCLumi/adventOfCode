def get_sorted_list(lines):
    tuple = ()
    x = 0
    y = 0
    elfString1 = ''
    elfString2 = ''
    elf1 = set()
    elf2 = set()
    """
    HOW AM I GOING TO SORT THIS LIST WTF
    update:
    i took a single line and was able to 
    """
    for i, line in enumerate(lines):
        line.split
        elfString1, elfString2 = line[:len(line)//2], line[len(line)//2:].replace(',', '')
        tuple = elfString1.partition('-')
        x = int(tuple[0])
        y = int(tuple[2])

        for loop in range(x, y+1):
            elf1.add(loop)

        print(elf1)

        tuple = elfString2.partition('-')
        x = int(tuple[0])
        y = int(tuple[2])

        for loop in range(x, y):
            elf2.add(loop)
        
        print(elf2)

# Convert a string to an integer

#string = "1234"
#number = int(string)
#print(number)  # Output: 1234


def get_elves_and_Schedule(lines):

    for line in lines:
        line = line.split()
    get_sorted_list(lines)
""" method 1
['2-4,6-8']
['2-3,4-5']
['5-7,7-9']
['2-8,3-7']
['6-6,4-6']
['2-6,4-8']
create a million arrays
each index in line = 1 array.
create x and y variable.
set x to everything before '-'
set y to everthing after '-'
add x-y to array.
eg 5-8
array1 = [5,6,7,8]
compare array 1 to every other array for matches
horrible efficeincy. 
"""

"""method 2
create sets
create x and y variable.
set x to everything before '-'
set y to everthing after '-'
add x-y to set
use intersection to find matches between each set. 
a little bit better efficiency?
maybe sort before adding into set. sort how? can we sort by x variable? 
ex. 1
[1-20,5-8, 8-25, 2-50, 500-3000] = [1-8, 2-50, 5-8, 8-25, 500-3000]
using this method, we can take the greatest x or y, and the smallest x or y,
split it in halfs so for ex 1
the first index 1-8 will only check with numbers between 1 and 250. 
note: this is only checking for x variable so the format x-y, y can be any number
we sort by x, so we check by x if that makes sense
much better time complexity! lets do that
"""




def main():
    with open("dayFourInputs.txt", "r") as input:
        lines = input.readlines()
    get_elves_and_Schedule(lines)
    
#if __name__ == '__main__':
    #main()

string = "2-4,6-8"
tuple = ()
x = 0
y = 0
elfString1 = ''
elfString2 = ''
elf1 = set()
elf2 = set()

elfString1, elfString2 = string[:len(string)//2], string[len(string)//2:].replace(',', '')
tuple = elfString1.partition('-')
x = int(tuple[0])
y = int(tuple[2])

for loop in range(x, y+1):
     print(loop)
     elf1.add(loop)
print(elf1)

tuple = elfString2.partition('-')
x = int(tuple[0])
y = int(tuple[2])

for loop in range(x, y+1):
    print(loop)
    elf2.add(loop)

print(elf2)