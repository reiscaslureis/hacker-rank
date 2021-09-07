def insert(lst, command):
    value = int(command[1])
    index = int(command[2])

    lst.insert(value, index)    

def remove(lst, command):
    index = int(command[1])

    lst.remove(index)

def append(lst, command):
    value = int(command[1])

    lst.append(value)

def sort(lst):
    lst.sort()

def pop(lst):
    lst.pop()

def reverse(lst):
    lst.reverse()

def print_list(lst):
    print(lst)

n = int(input())
lst = []

for i in range(n):
    command = input().split()

    if command[0] == 'append':
        append(lst, command)

    if command[0] == 'insert':
        insert(lst, command)

    if command[0] == 'remove':
        remove(lst, command)

    if command[0] == 'print':
        print_list(lst)

    if command[0] == 'sort':
        sort(lst)

    if command[0] == 'pop':
        pop(lst)

    if command[0] == 'reverse':
        reverse(lst)
