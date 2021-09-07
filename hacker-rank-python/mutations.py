def mutate_string(string, position, character):
    s_new = ''
    for i in range(len(string)):
        if i == position:
            s_new = s_new + character
        else: s_new = s_new + string[i]
    return s_new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)