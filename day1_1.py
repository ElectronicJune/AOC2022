f = open('inputs/day1.txt')

max = 0

calories = 0

for line in f:
    line = line.replace('\n','')
    if line == '' :
        if calories>max:
            max = calories
            calories = 0
        else:
            calories = 0
        continue
    calories += int(line)
    
print(max)
    
f.close()