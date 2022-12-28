f = open('inputs/day8.txt')

tree_map = f.read().split('\n')

visible = 0

for y in range(len(tree_map)):
    for x in range(len(tree_map[0])):
        tree_height = int(tree_map[y][x])
        #tree's left
        for i in range(x):
            if int(tree_map[y][i])>= tree_height:
                break
        else:
            visible+=1
            continue
        
        for i in range(x+1,len(tree_map[0])):
            if int(tree_map[y][i])>= tree_height:
                break
        else:
            visible+=1
            continue
        
        for i in range(y):
            if int(tree_map[i][x])>= tree_height:
                break
        else:
            visible+=1
            continue
        
        for i in range(y+1 , len(tree_map)):
            if int(tree_map[i][x])>= tree_height:
                break
        else:
            visible+=1
            continue
            
print(visible)

f.close()