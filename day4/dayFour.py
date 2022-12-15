def get_contained_pairs(elf_dictionary):
    print("hi")

def get_sorted_list(lines):
    tuple = ()
    x = 0
    y = 0
    elfString1 = ''
    elfString2 = ''
    elf_dictionary = {}
    cheating = len(lines)
    lumi = int(cheating)
    """
    HOW AM I GOING TO SORT THIS LIST WTF
    update:
    i took a single line and was able to create 2 elves and give them their schedule. (issues with 2nd elf)
    TODO:
    i can either create a million elves be more memory efficeint by
    creating 2 elfs, adding their schedules to a master array and then creating over those 2 elfs and repeat.
    sort the array by their X value. oh god i can already think of a million issues. i sleep good bye
    the next day me:
    fine ill use a dictionary
    """
    for i, line in enumerate(lines):
        line = line.strip()
        line.split
        elfString1, elfString2 = line[:len(line)//2], line[len(line)//2:].replace(',', '')
        tuple = elfString1.partition('-')
        x = int(tuple[0])
        y = int(tuple[2])

        for loop in range(x, y+1):
            elf_dictionary.setdefault(i, []).append(loop)

        tuple = elfString2.partition('-')
        x = int(tuple[0])
        y = int(tuple[2])

        for loop in range(x, y+1):
            elf_dictionary.setdefault(i+lumi, []).append(loop)
    get_contained_pairs(elf_dictionary)

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
    
if __name__ == '__main__':
    main()
