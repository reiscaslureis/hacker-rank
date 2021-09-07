def check_start_number(cc):
    valid_numbers = [4, 5, 6]
    if int(cc[0]) in valid_numbers:
        return 'Valid'
    else: return 'Invalid'

def check_digits_number(cc):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    aux = 0
    for i in range(len(cc)):
        try:
            if int(cc[i]) in numbers:
                aux += 1
            else: pass
        except: pass

    if aux == 16:
        return 'Valid'
    else: return 'Invalid'

def check_hyphen_and_size(cc):
    if len(cc) == 19:
        if cc[4] == '-' and cc[9] == '-' and cc[14] == '-':
            return 'Valid'
        else: return 'Invalid'
    elif len(cc) > 19:
        return 'Invalid'
    elif len(cc) < 14:
        return 'Invalid'
    else: return 'Valid'

def consecutive_repeated_digits(cc):
    cc = cc.replace('-', '')

    for i in range(len(cc)):
        try:
            if int(cc[i]) == int(cc[i + 1]) and int(cc[i]) == int(cc[i + 2]) and int(cc[i]) == int(cc[i + 3]):
                result = 'Invalid'
                break
            else: result = 'Valid'
        except: pass
    
    return result

def check_credit_card(cc):
    if check_start_number(cc) == 'Invalid':
        return 'Invalid'
    elif check_start_number(cc) == 'Invalid':
        return 'Invalid'
    elif check_hyphen_and_size(cc) == 'Invalid':
        return 'Invalid'
    elif consecutive_repeated_digits(cc) == 'Invalid':
        return 'Invalid'
    else: return 'Valid'
    
n = int(input())    
ccs = []

for i in range(n):
    cc = input()
    ccs.append(cc)

for i in range(n):
    result = check_credit_card(ccs[i])
    print(result)