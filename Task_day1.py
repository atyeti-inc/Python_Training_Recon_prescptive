#Task1:Sum of Two numbers
#Taking input from the users
Input1=int(input("Enter the First input value:"))
Input2=int(input("Enter the Second input value:"))
#Addition Operation & Printing the output
print("The sum of",Input1,',',Input2,"is:",Input1+Input2)


#Task2:Find the area of a Square
#Taking input from the users
Side=int(input("Enter the Side of the Square:"))
#Formula to find the area of square is side*side
Area=Side*Side
#Printing the area of the square
print("The Area of Square with side",Side,"is:",Area)


#Task3:Average of two Floating numbers
#Taking input from the users
Input1=float(input("Enter the First input value:"))
Input2=float(input("Enter the Second input value:"))
#Formula to find the average of two numbers is (num1+num2)/2
Average=(Input1+Input2)/2
#Printing the average of two numbers
print("The average of two numbers",Input1,",",Input2,"is:",Average)


#Task4:Find the greater value among two inputs
#Taking input from the users
a=int(input("Enter the a value:"))
b=int(input("Enter the b value:"))
#checking a is greater than or equals to b or not
if a>=b:
    print("True")
else:
    print("False")
