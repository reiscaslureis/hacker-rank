def check_number(command):
    if command % 2 != 0:
        print('Weird')

    elif command <= 5 and command >= 2:
        print('Not Weird')

    elif command >= 6 and command <= 20:
        print('Weird')

    else:
        print('Not Weird')

command = int(input())

check_number(command)