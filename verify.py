def verify(num):
    value = input()
    if num == 2:
        while value != 'A' and value != 'a' and value != 'b' and value != 'B':
            print('Please make a valid input!')
            value = input()
        return(value)
    elif num == 3:
        while value != 'A' and value != 'a' and value != 'b' and value != 'B' and value != 'c' and value != 'C':
            print('Please make a valid input!')
            value = input()
        return(value)
    elif num == 4:
        while value != 'A' and value != 'a' and value != 'b' and value != 'B' and value != 'c' and value != 'C' and value != 'd' and value != 'D':
            print('Please make a valid input!')
            value = input()
        return(value)
    elif num == 5:
        while value != 'A' and value != 'a' and value != 'b' and value != 'B' and value != 'c' and value != 'C' and value != 'd' and value != 'D' and value != 'e' and value != 'E':
            print('Please make a valid input!')
            value = input()
        return(value)
    elif num == 6:
        while value != 'A' and value != 'a' and value != 'b' and value != 'B' and value != 'c' and value != 'C' and value != 'd' and value != 'D' and value != 'e' and value != 'E' and value != 'f' and value != 'F':
            print('Please make a valid input!')
            value = input()
        return(value)
    elif num == 7:
        while value != 'A' and value != 'a' and value != 'b' and value != 'B' and value != 'c' and value != 'C' and value != 'd' and value != 'D'and value != 'e' and value != 'E' and value != 'f' and value != 'F' and value != 'g' and value != 'G':
            print('Please make a valid input!')
            value = input()
        return(value)

def numConvert(input):
    if input == 'a' or input == 'A':
        num = 0
        return num
    elif input == 'b' or input == 'B':
        num = 1
        return num
    elif input == 'c' or input == 'C':
        num = 2
        return num
    elif input == 'd' or input == 'D':
        num = 3
        return num
    elif input == 'e' or input == 'E':
        num = 4
        return num
    elif input == 'f' or input == 'F':
        num = 5
        return num
    elif input == 'g' or input == 'G':
        num = 6
        return num