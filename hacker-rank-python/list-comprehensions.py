def list_create_all(x, y, z):
    alllist = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                arr = []
                arr.append(i)
                arr.append(j)
                arr.append(k)
                alllist.append(arr)

    return alllist

def list_create_blacklist(alllist, n):
    blacklist = []
    for i in range(len(alllist)):
        if alllist[i][0] + alllist[i][1] + alllist[i][2] == n:
            blacklist.append(alllist[i])

    return blacklist

x = int(input())
y = int(input())
z = int(input())
n = int(input())

alllist = list_create_all(x, y, z)
blacklist = list_create_blacklist(alllist, n)

print([i for i in alllist if i not in blacklist])
