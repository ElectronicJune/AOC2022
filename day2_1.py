f = open('inputs/day2.txt')
score = 0
shapes = ['X','Y','Z']

for row in f:
    row = row.replace('\n','').replace('A','X').replace('B','Y').replace('C','Z')
    score += shapes.index(row[2])+1

    if row[0]==row[2]:
        score+=3
        continue

    x = shapes.index(row[2])-1
    if  shapes[x] == row[0]:
        score+=6
        continue

print(score)

f.close()