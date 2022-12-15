def get_contained_pairs(elf1, elf2):

    if len(elf1) < len(elf2):
        for i, char in enumerate(elf1):
            print("this is i: ", i)
            print("this is char: ", char)
            if char == elf2[i]:
                print("test")

def get_sorted_list(lines):
    tuple = ()
    x = 0
    y = 0
    elfString1 = ''
    elfString2 = ''

    for line in lines:
        line = line.strip()
        line.split
        elfString1, elfString2 = line[:len(line)//2], line[len(line)//2:].replace(',', '')
        elf1 = []
        elf2 = []

        tuple = elfString1.partition('-')
        x = int(tuple[0])
        y = int(tuple[2])

        for loop in range(x, y+1):
            elf1.append(loop)

        tuple = elfString2.partition('-')
        x = int(tuple[0])
        y = int(tuple[2])

        for loop in range(x, y+1):
            elf2.append(loop)
        get_contained_pairs(elf1, elf2)
        
def get_elves_and_Schedule(lines):

    for line in lines:
        line = line.split()
    get_sorted_list(lines)

def main():
    with open("dayFourInputs.txt", "r") as input:
        lines = input.readlines()
    get_elves_and_Schedule(lines)
    
if __name__ == '__main__':
    main()

