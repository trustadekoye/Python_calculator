import math

#Python Calculator

print('Select an operation to perform:')
print('1. ADD')
print('2. SUBTRACT')
print('3. MULTIPLY')
print('4. DIVIDE')
print('5. SQUARE ROOT')
print('6. RAISE TO POWER')

operation = input()

#Addition
if operation == '1':
    num1 = input ('Enter first number: ')
    num2 = input ('Enter second number: ')
    print('The sum is ' + str(int(num1) + int(num2)))

#Subtraction
elif operation == '2':
    num1 = input ('Enter first number: ')
    num2 = input ('Enter second number: ')
    print('The difference is ' + str(int(num1) - int(num2)))

#Multiplication
elif operation == '3':
    num1 = input ('Enter first number: ')
    num2 = input ('Enter second number: ')
    print('The product is ' + str(int(num1) * int(num2)))

#Division
elif operation == '4':
    num1 = input ('Enter first number: ')
    num2 = input ('Enter second number: ')
    print('The result is ' + str(int(num1) / int(num2)))

#Square Root
elif operation == '5':
    num1 = input ('Enter number: ')
    print('The squareroot is ' + str(math.sqrt(int(num1))))

#Square a number
elif operation == '6':
    num1 = int(input ('Enter number: '))
    print('The power is ' + str(math.pow(num1, 2)))

else:
    print("Invalid Entry")