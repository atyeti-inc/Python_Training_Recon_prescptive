#Q1:Write a one-liner to check if"madam" is a palindrome
#Taking input from user
str1=input("enter the value:")
#checking the input is a palindrome or not by using the reverse slicing
print("Palindrome" if str1.lower()==str1.lower()[::-1] else "Not a Palindrome")
   

#Q2:Extract the letters and numbers from "Python@123"
str="Python@123"
#Slicing the letters & Numbers from Python@123
Letters=str[0:6]
Numbers=str[7:10]
#Printing the results
print("Letters:",Letters)
print("Numbers:",Numbers)


#Q3:removing the spaces
'''Eg:" Python is fun "
   o/p:"Python is fun"
'''
Str1=" Python is Fun "
#Triming the leading and ending spaces using strip method
Str2=Str1.strip()
#Printing the output
print(f'"{Str2}"')


#Q4:Check Methods:
#"12345"
C1="12345"
print(C1.isalnum())
print(C1.isnumeric())
print(C1.isdigit())
C2="123 1/3"
print(C2.isalnum())
print(C2.isnumeric())
print(C2.isdigit())
C3="Python3"
print(C3.isalnum())
print(C3.isnumeric())
print(C3.isdigit())
C4="Python 3"
print(C3.isalnum())
print(C3.isnumeric())
print(C3.isdigit())


#Q5:Write a program that takes a number as input and determine if number is positive or negative or zero.
#Taking the input from the user
num=int(input("Enter the number:")) 
#Checking whether the number is positive or negative or zero and printing the results
if (num>0):
    print("Positive")
elif (num<0):
    print("Negative")
else:
    print("Zero")


'''Q6:Write a program to assign a grade
90+ print "A"
80-90 print "B"
70-79 print "C"
<70 print "Fail'''
#Taking the input from user
Percentage=int(input("Enter the Percentage:"))
#Checking the grades and printing the results
if Percentage>90:
    print("Grade A")
elif Percentage>=80 and Percentage<=90:
    print("Grade B")
elif Percentage>=70 and Percentage<=79:
    print("Grade C") 
else:
    print("Fail")


#Q7:Write a program to find the greatest of 3 numbers entered by the user.
#Taking the input from user
n1=int(input("Enter the value of n1:"))
n2=int(input("Enter the value of n2:"))
n3=int(input("Enter the value of n3:"))
#Checking which number is greatest number among the 3 numbers given by the user
if(n1>n2) & (n1>n3):
    print(f'n1:{n1} is greatest number')
elif(n2>n3):
    print(f'n2:{n2} is greatest number')
else: 
    print(f'n3:{n3} is greatest number')


#Q8:Write a program to check a number is multiple of 7 or not.
#Taking the input from the user
Number=int(input("Enter the Number:"))
#Checking whether the number given by the user is multiple by 7 or not and printing the result.
if(Number%7==0):
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")