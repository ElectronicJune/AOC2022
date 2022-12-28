f = open('inputs/day10.txt')
instructions = f.read().split('\n')
x = 1
cycles = 0


def add_cycle() :
    global cycles
    cycles += 1
    horizontal_index = (cycles-1)%40
    
    if abs(horizontal_index-x)<=1:
        print('#',end='')
    else :
        print('.',end='')

    if horizontal_index == 39:
        print()

for instruction in instructions:
    if instruction == 'noop':
        add_cycle()
    else :
        add_cycle()
        add_cycle()
        x += int(instruction.split()[1])
        


f.close()

    