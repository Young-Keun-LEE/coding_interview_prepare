import sys
input = sys.stdin.readline
class Stack:
    
    def __init__(self):
        self.cur = -1
        self.stack = []

    def is_empty(self):
        if self.cur == -1:
            return True
        else:
            return False
        
    def push(self, x):
        self.cur += 1
        self.stack.append(x)
    
    def pop(self):
        if not self.is_empty():
            self.cur -= 1
            return self.stack.pop()
        
        else:
            return -1
            
    def lookup(self):
        if not self.is_empty():
            return self.stack[self.cur]
        else:
            return -1

    def count(self):
        return self.cur + 1
        
N = int(input()) #The number of commandline
stack = Stack()
result = []

for _ in range(N):
    commandline = input().strip()
    command = commandline.split(" ")[0]
    
    match command:
        case "1":
            element = int(commandline.split(" ")[1])
            stack.push(element)

        case "2":
            result.append(stack.pop())

        case "3":
            result.append(stack.count())

        case "4":
            if stack.is_empty():
                result.append("1")
            else:
                result.append("0")

        case "5":
            result.append(stack.lookup())
        
for r in result:
    sys.stdout.write(str(r) + " \n")
    