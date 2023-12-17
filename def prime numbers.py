#Find prime numbers
def primeN(n):
    if n > 1:
        for i in range(2, int(n/2)):             # n/2: shorter range : efficient 
            if n % i == 0:
                print('Non Prime Number!')
                break
        else:                                    # else block of *for loop
            print(f'{n} is a Prime Number!')               
    else:
        print(f'{n} is a Non Prime Number!')

#function calling
n = int(input('Enter number: '))
primeN(n)




