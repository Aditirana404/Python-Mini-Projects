import random
n = input('Name of the player? ')
c = 0
u = 0
print('\n*** MATCH OF 3 ROUNDS ***')
for i in range(3):
    l = ['R', 'P', 'S']
    comp = random.choice(l)
    user = input('''\nChoose R for Rock / P for Paper / S for Scissors: ''').upper()
    print('computer : ', comp)
    print(f'{n}     : ', user)
    if comp == 'R' and user == 'S':
        c += 1
        print('Computer score   : ', c)
        print('Your score       : ', u) 
    elif comp == 'P' and user == 'R':
        c += 1
        print('Computer score   : ', c)
        print('Your score       : ', u) 
    elif comp == 'S' and user == 'P':
        c += 1
        print('Computer score   : ', c)
        print('Your score       : ', u) 
    elif comp == user:
        c += 1
        u += 1
        print('Computer score   : ', c)
        print('Your score       : ', u) 
    else:
        u += 1
        print('Computer score   : ', c)
        print('Your score       : ', u) 
else:
    print('\nComputer total score   : ', c)
    print('Your total score       : ', u) 
    if c > u:
        print('\n*** COMPUTER WON ***')
    elif c == u:
        print('\n*** DRAW ***')
    else:
        print('\n*** YOU WON ***')



 