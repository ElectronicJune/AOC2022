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

rb = [Rope() for i in range(10)]    #rope bodies
     
for instruction in instructions :
    direction = instruction.split()[0]
    for i in range(int(instruction.split()[1])):
        rb[0].move(direction)  
        for i in range(1,len(rb)):
            if (rb[i-1].x - rb[i].x)==2: 
                if (rb[i-1].y > rb[i].y):
                    rb[i].move('U','R')
                    continue
                if (rb[i-1].y < rb[i].y):
                    rb[i].move('D','R')
                    continue
                rb[i].move('R')

            if  (rb[i-1].x - rb[i].x)==-2:
                if (rb[i-1].y > rb[i].y):
                    rb[i].move('U','L')
                    continue
                if (rb[i-1].y < rb[i].y):
                    rb[i].move('D','L')
                    continue
                rb[i].move('L')

            if  (rb[i-1].y - rb[i].y)==2:
                if (rb[i-1].x > rb[i].x):
                    rb[i].move('U','R')
                    continue
                if (rb[i-1].x < rb[i].x):
                    rb[i].move('U','L')
                    continue
                rb[i].move('U')

            if  (rb[i-1].y - rb[i].y)==-2:
                if (rb[i-1].x > rb[i].x):
                    rb[i].move('D','R')
                    continue
                if (rb[i-1].x < rb[i].x):
                    rb[i].move('D','L')
                    continue
                rb[i].move('D')

        #graphics
        # ymax = max([i.y for i in rb])+1 if max([i.y for i in rb])+1 >0 else 1
        # ymin = min([i.y for i in rb]) if min([i.y for i in rb])<0 else 0
        # xmax = max([i.x for i in rb])+1 if max([i.x for i in rb])+1 >0 else 1
        # xmin = min([i.x for i in rb]) if min([i.x for i in rb])<0 else 0
        # for y in reversed(range(ymin,ymax)):
        #     for x in range(xmin,xmax):
        #         for i in range(len(rb)):
        #             if rb[i].x==x and rb[i].y==y :
        #                 print(i,end='')
        #                 break
        #         else:
        #             print('S' if (x==0 and y==0) else '.',end='')
        #     print()
        # print('###')


print(len(rb[9].movement_history))

f.close()                











