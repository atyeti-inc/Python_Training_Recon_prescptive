#Task 1:Print numbers from 1 to 100
#Using While loop:
n=int(input("enter the 'n'end value:"))
i=1
while i<=n:
    print(i)
    i+=1
#Using for loop:
n1=int(input("enter the 'n1' end value:"))
for i in range(1,(n1+1),1):
   print(i)



#Task 2:Print numbers from 100 to 1
#Using While loop:
n=int(input("enter the start value:"))
i=1
while i<=n:
    print(n)
    n-=1
#Using for loop:
n1=int(input("Enter the start number:"))
for i in range(n1,0,-1):
   print(i)



#Task 3:Print the multiplication table using looping statements
#Using while loop:
Table=int(input("Enter the table value:"))
i=1
while i<=10:
    print(Table,'*',i,"=",Table*i)
    i+=1
#Using for loop:
Table=int(input('Enter the table value:'))
for i in range(1,11,1):
    print(Table,'*',i,'=',Table*i)


#Task 4:Find the sum of all even numbers from 1 to 50 using loop
#using while loop:
n=int(input("Enter the end value:"))
i=1
sum=0
while i<=n:
    if(i%2==0):
        sum=sum+i
    i+=1
print(sum)
#Using for loop:
n1=int(input("Enter the end value:"))
sum=0
for i in range(1,n1+1,1):
    if(i%2==0):
        sum=sum+i
print(sum)




#Task 5:Display the reverse of a number using while loop
number=int(input("Enter the number:"))
reverse=0
temp=0
while number>0:
    temp=number%10
    reverse=reverse*10+temp
    number=number//10
print(reverse)


#Task 6:Print the numbers from 1 to 20 but stop the loop if number is 13
#Using while loop:
n=int(input("Enter the value:"))
i=1
while(i<=n):
    if(i==13):
        break
    print(i)
    i+=1
#Using for loop:
n=int(input("Enter the value:"))
for i in range(1,n+1,1):
    if(i==13):
        break
    print(i)



#Task 7:Print numbers from 1 to 20 but skip multiples of 3
#Using while loop:
n=int(input("Enter the value:"))
i=1
while(i<=n):
    if(i%3==0):
         i+=1
         continue
    print(i)
    i+=1
#Using for loop:
n=int(input("Enter the value:"))
for i in range(1,n+1,1):
     if(i%3==0):
          i+=1
          continue
     print(i)


#Task 8:Write a program that iterates through a string and uses pass for vowels(so only consonants are printed)
#Using While loop
str=input("enter the string:")
i=0
while i<len(str):
    if str[i].lower() in ['a','e','i','o','u']:
         pass
    else:
        print(str[i])
    i=i+1
#Using for loop
str=input("enter the string:")
for i in range(0,len(str),1):
    if str[i].lower() in ['a','e','i','o','u']:
        pass
    else:
        print(str[i])


#Task 9:problem statement 
'''opening_balance = 1000
transactions = [200, -100, 300, -50, -200]
expected_closing_balance = 1150
'''
opening_Balance=1000
Transactions=[200,-100,300,-50,-200]
closing_balance=1150
length=len(Transactions)
i=0
net_transactions=opening_Balance
while i<len(Transactions):
    net_transactions=net_transactions+Transactions[i]
    i+=1
    if i==len(Transactions) and closing_balance!=(net_transactions):
        print("Balance mismatch found")
        break
else:
    print("Balance matched")
#Using for loop:
opening_Balance=1000
Transactions=[200,-100,300,-50,-200]
closing_balance=1150
i=0
net_transactions=opening_Balance
for i in range (0,len(Transactions),1):
    net_transactions=net_transactions+Transactions[i]
    if i==(len(Transactions)-1) and closing_balance!=(net_transactions):
        print("Balance mismatch found")
        break
else:
    print("Balance matched")