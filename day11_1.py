f = open('inputs/day11.txt')

all_lines = f.read().split('\n')

def split_list(list, char):
    splited_list = []
    list_parts = []
    for i in list:
        if i == char :
            splited_list.append(list_parts)
            list_parts = []
        else:
            list_parts.append(i)
    splited_list.append(list_parts)
    return splited_list
            

class Monkey :
    items = []
    def __init__(self,monkey_index,operation,test,test_true,test_false):
        self.monkey_index = monkey_index
        self.operation = operation
        self.test_divisible_by = int(test)
        self.test_true = test_true
        self.test_false = test_false
        self.inspect_counter = 0

    def operate(self):
        while len(Monkey.items[self.monkey_index])!=0:
            self.inspect_counter +=1
            worry_level = Monkey.items[self.monkey_index][0]
            operation = [(worry_level if i=='old' else i) for i in self.operation]
            match operation[1]:
                case '+':
                    worry_level= int(operation[0]) +int(operation[2])
                case '-':
                    worry_level= int(operation[0]) -int(operation[2])
                case '*':
                    worry_level= int(operation[0]) *int(operation[2])
                case '/':
                    worry_level= int(operation[0]) /int(operation[2])
            worry_level = worry_level//3
            if worry_level%self.test_divisible_by==0 :
                Monkey.items[self.test_true].append(worry_level)
            else:
                Monkey.items[self.test_false].append(worry_level)
            del Monkey.items[self.monkey_index][0]


monkeys = []
for monkey_info in split_list(all_lines,''):
    monkey_index = int(monkey_info[0].split()[1].strip(':'))
    operation = monkey_info[2].split()[-3:]
    test = int(monkey_info[3].split()[-1])
    test_true = int(monkey_info[4].split()[-1])
    test_false = int(monkey_info[5].split()[-1])
    monkeys.append(Monkey(monkey_index,operation,test,test_true,test_false))
    Monkey.items.append([int(i) for i in monkey_info[1].split(':')[1].strip().split(', ')])

for i in range(20):
    for monkey in monkeys:
        monkey.operate()

inspect_list = [monkey.inspect_counter for monkey in monkeys]

first = max(inspect_list)
inspect_list.remove(first)
sec = max(inspect_list)

print(first*sec)

f.close()

        
