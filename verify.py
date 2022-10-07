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