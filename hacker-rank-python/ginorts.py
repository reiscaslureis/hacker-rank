def create_lists_and_sort(s):
    lower = []
    upper = []
    odds = []
    evens = []
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    for i in range(len(s)):
        if s[i].islower() == True:
            lower.append(s[i])
        elif s[i].isupper() == True:
            upper.append(s[i])
        elif s[i] in numbers:
            if int(s[i]) % 2 == 0:
                evens.append(s[i])
            else: odds.append(s[i])

    lower = sorted(lower)
    upper = sorted(upper)
    odds = sorted(odds)
    evens = sorted(evens)

    return lower, upper, odds, evens
   
s = input()
lower, upper, odds, evens = create_lists_and_sort(s)

result = ''

try:
    for i in lower:
        result += i

    for i in upper:
        result += i

    for i in odds:
        result += i

    for i in evens:
        result += i
except: pass

print(result)
