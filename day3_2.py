f = open('inputs/day3.txt')

shared_type = []


rucksacks = []

for rucksack in f:
    rucksack = rucksack.replace('\n','')
    rucksacks.append(rucksack)

    if len(rucksacks)==3:
        for i in rucksacks[0]:
            if (i in rucksacks[1]) and (i in rucksacks[2]):
                shared_type.append(i)
                break
        rucksacks = []


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





