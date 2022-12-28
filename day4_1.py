f = open('inputs/day4.txt')

pairs = 0

for pair in f:
    pair = pair.replace('\n','')
    pair_arr = pair.split(',')
    first = [int(i) for i in pair_arr[0].split('-')]
    sec = [int(i) for i in pair_arr[1].split('-')]

    if (first[0]<=sec[0] and first[1]>=sec[1]) or (first[0]>=sec[0] and first[1]<=sec[1]):
        pairs+=1

print(pairs)

f.close()