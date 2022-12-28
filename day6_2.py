f = open('inputs/day6.txt')

datastream = f.read()

counter = 0
marker = ''
for i in datastream:
    counter+=1
    marker+=i
    if len(marker)>14:
        marker = marker[1:]
        for j in marker:
            if marker.count(j) != 1:
                break
        else:
            print(counter)
            exit()

f.close()