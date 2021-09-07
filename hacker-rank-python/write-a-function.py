def case_one(year):
    if year % 400 == 0:
        leap = True
    else: leap = False

    return leap

def case_two(year):
    if year % 4 == 0:
        leap = True
    else: leap = False

    return leap

def is_leap(year):
    x = str(year)

    if x[2:] == '00':
        leap = case_one(year)
    else: leap = case_two(year)

    return leap

year = int(input())
print(is_leap(year))