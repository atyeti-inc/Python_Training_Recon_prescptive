
# WAP Palindrme

print("Palindrome"if "madam".lower()=="madam".lower()[::-1] else "Not Palindrome")



#2.Extract letters and Digit from below

str="Python@123"

print(str[0:6]) # "Python"
print(str[7:10])  # 123


#3. clean the string(remove space)
string="Python if fun"
cleaned=string.replace(" ","")
print(cleaned)




# 4.check methods

# 1."12345"
str="12345"  # return true
print(str.isalnum())

print(str.isdigit())

print(str.isnumeric())


# 2."123 1/3"

str1="123 1/3"
print(str1.isalnum())

print(str1.isdigit())

print(str1.isnumeric())


# 3. "Python3"

str2="Python3"  # Returns false
print(str2.isalnum())

print(str2.isdigit())

print(str2.isnumeric())


# 4. Check Methods

str3="Python 3"   # Returns false
print(str3.isalnum())

print(str3.isdigit())

print(str3.isnumeric())




# 5. WAp that takes a number as input

number=int(input("Enter a number: "))
if(number>0):
    print("Positive")
elif(number<0):
    print("Negative")  
else:
    print("Zero")      



#6. write a  program to assign a grade

marks=int(input("Enter marks: "))
if(marks>=90):
    print("A")
elif(marks>80 and marks<90):
    print("B")
elif(marks>70 and marks<=80):
    print("C")
else:
    print("Fail")            




#7. WAp to find the greatest of 3 numbers entered by the user

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if(a>=b and a>=c):
    print("a is greatest")
elif(b>=c):
    print("b is greatest")
else:
    print("c is greatest")  


# WAp to check if a number is a multiple of 7  or not

number=int(input("Enter a number: "))
if(number%7==0):
    print("Multiple of 7")
else:
    print("not multiple of 7")              