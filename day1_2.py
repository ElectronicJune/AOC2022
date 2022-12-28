f = open('inputs/day1.txt')

top3 = [0,0,0]
calories = 0

for line in f:
    line = line.replace('\n','')
    if line == '' :
        for i in range(3):
            if calories > top3[i]:
                top3.insert(i, calories)
                del top3[len(top3)-1]
                break
        

        calories=0
        continue
    calories += int(line)
    

print(sum(top3))
    
f.close()