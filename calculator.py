c = 0
n1 = float(input('\nEnter an integer: '))
n2 = input("Choose an operand ( +  -  *  / ): ")
n3 = float(input('Enter an integer: '))
if n2 == '+':
    c = n1 + n3
    print('\nResult: ', c)
elif n2 == '-':
    c = n1 - n3
    print('\nResult: ', c)
elif n2 == '*':
    c = n1 * n3
    print('\nResult: ', c)
elif n2 == '/':
    c = n1 / n3
    print('\nResult: ', c)
while True:
    n2 = input('''\nChoose an operand ( +  -  *  / )
or Choose X to exit:  ''').lower()
    if n2 == 'x':
        break
    n4 = float(input('Enter an integer: '))
    if n2 == '+':
        c = c + n4
        print('\nResult: ', c)
    elif n2 == '-':
        c = c - n4
        print('\nResult: ', c)
    elif n2 == '*':
        c = c * n4
        print('\nResult: ', c)
    elif n2 == '/':
        c = c / n4
        print('\nResult: ', c)


    
    