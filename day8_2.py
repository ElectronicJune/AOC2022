f = open('inputs/day8.txt')

tree_map = f.read().split('\n')

highest_scenic_score = 0

for y in range(len(tree_map)):
    for x in range(len(tree_map[0])):
        tree_height = int(tree_map[y][x])
        
        scenic_score = 1
        tree_counts = []
        tree_count = 0
        
        for i in reversed(range(x)):
            tree_count+=1
            if int(tree_map[y][i])>= tree_height:
                break
        tree_counts.append(tree_count)
        tree_count = 0
        
        for i in range(x+1,len(tree_map[0])):
            tree_count+=1
            if int(tree_map[y][i])>= tree_height:
                break
        tree_counts.append(tree_count)
        tree_count = 0
        
        for i in reversed(range(y)):
            tree_count+=1
            if int(tree_map[i][x])>= tree_height:
                break
        tree_counts.append(tree_count)
        tree_count = 0
        
        for i in range(y+1 , len(tree_map)):
            tree_count+=1
            if int(tree_map[i][x])>= tree_height:
                break
        tree_counts.append(tree_count)
        
        for i in tree_counts:
            scenic_score*=i

        if scenic_score>highest_scenic_score:
            highest_scenic_score = scenic_score

print(highest_scenic_score)        
        
f.close()