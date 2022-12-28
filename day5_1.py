f = open('inputs/day5.txt')
all_lines = f.read().split('\n')
drawing = all_lines[:(all_lines.index('')-1)]
instructions = all_lines[(all_lines.index('')+1):]

crate_stacks = ['' for i in range(9)]  

for i in range(len(drawing)):
    counter = 0
    j = 1
    while j < len(drawing[i]):
        crate_stacks[counter] += drawing[i][j]
        counter+=1
        j+=4

for i in range(len(crate_stacks)):
    crate_stacks[i] = crate_stacks[i].strip()

for instruction in instructions:
    move = int(instruction.split()[1])
    from_ = int(instruction.split()[3])-1
    to = int(instruction.split()[5])-1
    crates_to_move = crate_stacks[from_][:move]
    crates_to_move = crates_to_move[-1::-1]
    crate_stacks[from_] = crate_stacks[from_][move:]
    crate_stacks[to] = crates_to_move + crate_stacks[to]

for i in crate_stacks:
    print(i[0],end='')

f.close()