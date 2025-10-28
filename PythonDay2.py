# Code to get 2 numbers from user and output the sum
Digit1=int(input('Please enter a number: '))
Digit2=int(input('Please enter one more number: '))
print('The sum of given numbers are: ', Digit1+Digit2);

# To calculate the area of square
Side=int(input('Please enter length of a side: '))
print('The total area of square is:', Side**2)

# To calculate the average of 2 numbers
Number1=float(input('Please enter number one: '))
Number2=float(input('Please enter number two: '))
Avg=(Number1+Number2)/2
print('The average of the given numbers:', Avg)

# To calculate greater side
Side1=int(input('Please enter length of first side: '))
Side2=int(input('Please enter length of second side: '))
if Side1>Side2:
    print('The First Side - ', Side1, 'is greater than Second Side - ', Side2)
else:
    print('The Second Side - ', Side2, 'is greater than First Side - ', Side1)