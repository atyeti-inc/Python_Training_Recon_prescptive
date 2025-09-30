str = 'madam'
if str == str[::-1]:
    print ('Palindrome')
else:
    print ('Not Palindrome')
===============================================================	
	
str = "python@123"
print (str[0:6])
print (str[7:11])

===============================================================
string=" Python is fun "
str=string.replace(" ","",1)
str1=str[:-1] + ""
print(str1)
===============================================================
string=str (input ("enter the string : " ))
print(string.isalnum())

print(string.isdigit())

print(string.isnumeric())

===============================================================
string=float (input ("enter the string : " ))
print ("Positive" if string >0 else "Negative"  if string <0 else "Zero")
================================================================
string=int (input ("enter the Marks : " ))
print ("A" if (string >=90) else "B"  if (string >80 and string<90) else "C" if (string > 70 and string <=80) else "Fail")
=============================================================================
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if(a>=b and a>c):
    print("First number is greatest")
elif(b>=c):
    print("Second number is greatest")
else:
    print("Third number  is greatest")  
=============================================================================	

a=int(input("Enter a number: "))
if(a%7==0):
    print("Multiple of 7")
else:

    print("not a multiple of 7")       	
	
	
	
