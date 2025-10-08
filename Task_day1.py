#Program to calculate the sum of two numbers -input from user
a = int(input("Enter a 1st number: "))
b = int(input("Enter a 2nd number: "))
sum= a + b
print("The sum of the two numbers is: " ,sum)

#find area of a square input from user
print("\n---Find the area of a square---")
side=int(input("Enter the side of the square:"))
area=side*side
print("The area of the square is : ",area)

# print the average of two floating point numbers take as input
print("\n---Find the average of a floating point num ---")
num1=float(input("Enter 1st number: "))
num2=float(input("Enter 2nd number: "))
avg=(num1+num2)/2
print("The average of two numbers is: ",avg)

# Find a greater number if a is greater than b retuen true else false
print("\n---Find a greater number ---")
x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))
if x>=y:
    print("True")
else:
    print("False")
