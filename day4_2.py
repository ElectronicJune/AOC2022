f = open('inputs/day4.txt')

pairs = 0

for pair in f:
    pair = pair.replace('\n','')
    pair_arr = pair.split(',')
    first = [int(i) for i in pair_arr[0].split('-')]
    sec = [int(i) for i in pair_arr[1].split('-')]

    for i in first:
        if (i >= sec[0] and i<= sec[1]):
            pairs +=1
            break
    else:
        for i in sec:
            if (i >= first[0] and i<= first[1]):
                pairs +=1
                break
    

print(pairs)

f.close