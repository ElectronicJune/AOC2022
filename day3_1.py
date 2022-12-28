f = open('inputs/day3.txt')

priorities_sum = 0

shared_type = []

for rucksack in f:
    rucksack = rucksack.replace('\n','')
    length = len(rucksack)

    compartment1 = rucksack[:int(length/2)]
    compartment2 = rucksack[int(length/2):]

    for i in compartment1:
        if i in compartment2 :
            shared_type.append(i)
            break
    
    

def to_priority(types):
    priorities = []
    for i in types :
        if i.islower() :
            priorities.append(ord(i)-96)
            continue

        priorities.append(ord(i)-38)
    return priorities

priorities_sum = sum(to_priority(shared_type))

print(priorities_sum)

f.close()            





