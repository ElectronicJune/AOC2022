f = open('inputs/day2.txt')

score = 0
endings = ['X','Y','Z']
shapes = ['A','B','C']

for row in f:
    score += endings.index(row[2]) *3

    if row[2]=='Z' : #win 
        score += (shapes.index(row[0])+1)%3 +1
        continue
    if row[2]=='Y':#draw
        score += shapes.index(row[0])+1
        continue

    #lose 
    score += (shapes.index(row[0])+2)%3 +1

print(score)

f.close()
