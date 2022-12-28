f = open('inputs/day9.txt')

instructions = f.read().split('\n')

class Rope :
    def __init__(self):
        self.x = 0
        self.y = 0
        self.movement_history = [(0, 0)]
    def move(self,*directions) :
        for direction in directions:
            match direction:
                case 'U':
                    self.y += 1
                case 'D':
                    self.y-=1
                case 'L':
                    self.x-=1
                case 'R':
                    self.x+=1
        if (self.x,self.y) not in self.movement_history :
            (self.movement_history).append((self.x,self.y))

head = Rope()
tail = Rope()

for instruction in instructions :
    direction = instruction.split()[0]
    for i in range(int(instruction.split()[1])):
        head.move(direction)  
        if (head.x - tail.x)==2: 
            if (head.y > tail.y):
                tail.move('U','R')
            if (head.y < tail.y):
                tail.move('D','R')

        if  (head.x - tail.x)==-2:
            if (head.y > tail.y):
                tail.move('U','L')
            if (head.y < tail.y):
                tail.move('D','L')

        if  (head.y - tail.y)==2:
            if (head.x > tail.x):
                tail.move('U','R')
            if (head.x < tail.x):
                tail.move('U','L')

        if  (head.y - tail.y)==-2:
            if (head.x > tail.x):
                tail.move('D','R')
            if (head.x < tail.x):
                tail.move('D','L')

        if abs(head.x - tail.x)==2 or abs(head.y - tail.y)==2:
            tail.move(direction)

    


print(len(tail.movement_history))
f.close()                







