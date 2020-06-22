from functools import reduce

def introduction():
    print('{:=^50}'.format('  calculator  '))
    print('\n\n select the desired operation number\n\n')
    print("1 - add \n2 - subtraction \n3 - multiplication \n4 - devision \n")
    option = int(input('type your option: '))
    print('\n')
    return option

def add(x, y):
    return x + y

def multiplication(x, y):
    return x * y

def division(numbers):
    try:
        fractional = numbers[0] / numbers[1]
        integer = numbers[0] // numbers[1]
        rest = numbers[0] % numbers[1]
        return (fractional, integer, rest)
    except ZeroDivisionError:
        print("it is not possible to divide by zero")
        return (0, 0, 0)

option = introduction()

numbers = []

if option == 1:
    numbers.append(float(input("type the first numbers: ")))
    while True:
        n = input('type another number, if you dont want to put more type "no": ')
        if n == 'no':
             break
        else:
            try:
                float(n)
            except ValueError:
                print("it is not possible to add a letter with a number")
                break
            numbers.append(float(n))

    print(f'the sum of these terms is : {reduce(add, numbers)}')

elif option == 2:
    numbers.append(float(input("type the first numbers: ")))
    while True:
        n = input('type another number, if you dont want to put more type "no": ')
        if n == 'no':
             break
        else:
            try:
                float(n)
            except ValueError:
                print("it is not possible to add a letter with a number")
                break
            numbers.append(float(n))

        result = [-x for x in numbers[1:]]
        result.append(numbers[0])

    print(f'the subtraction of terms by the first is : {reduce(add, result)}')

elif option == 3:
    numbers.append(float(input("type the first numbers: ")))
    while True:
        n = input('type another number, if you dont want to put more, type "no": ')
        if n == 'no':
             break
        else:
            try:
                float(n)
            except ValueError:
                print("it is not possible to add a letter with a number")
                break
            numbers.append(float(n))

    print(f'the multiplication between these terms is : {reduce(multiplication, numbers)}')

elif option == 4:
    numbers.append(float(input("type the first numbers: ")))
    numbers.append(float(input("type the second numbers: ")))
    result = division(numbers)
    print(f'the division between the first and the second term is : ')
    print(f'fractional : {division(numbers)[0]}\ninteger: {division(numbers)[1]}\nrest: {division(numbers)[2]}')

else:
    print('try again')