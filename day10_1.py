f = open('inputs/day10.txt')
instructions = f.read().split('\n')
x = 1
cycles = 0
stop_at = 20
signal_strengths = 0

def add_cycle() :
    global cycles
    global signal_strengths
    global stop_at
    cycles += 1
    if cycles == stop_at :
        signal_strengths += x * cycles 
        stop_at += 40

    if cycles == 220 :
        print(signal_strengths)
        exit()
    
for instruction in instructions:
    if instruction == 'noop':
        add_cycle()
    else :
        add_cycle()
        add_cycle()
        x += int(instruction.split()[1])
        


f.close()

    