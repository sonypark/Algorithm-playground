n = int(input())

class Stack() :
    list = []

    def push(self,a):
        self.list.append(a)

    def pop(self):
        if self.empty():
            return -1
        return self.list.pop()

    def top(self):
        if self.empty():
            return -1
        return self.list[-1]

    def size(self):
        return len(self.list)

    def empty(self):
        if len(self.list) ==0:
            return 1
        else:
            return 0

stack = Stack()

for _ in range(n):
    c= input()
    if c.startswith('push'):
       p,m = c.split()
       stack.push(m)
    if c == 'top':
        print(stack.top())
    if c == 'size':
        print(stack.size())
    if c == 'pop':
        print(stack.pop())
    if c == 'empty':
        print(stack.empty())

