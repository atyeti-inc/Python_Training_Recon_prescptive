#Loop 
#1. For Loop and While Loop

#Q.1) Print numbers from 1 to 100

print("Numbers from 1 to 100 for loop: ")
for i in range(1,101,1):
    print(i)

print("Numbers from 1 to 100 While loop: ")

i=1
while i<=100:
    print(i)
    i=i+1

print("------------------End of program 1---------------------")

#Q.2) Print numbers from 100 to 1

print("Numbers from 100 to 1 for loop: ")
for i in range(100,0,-1):
    print(i)

print("Numbers from 100 to 1 While loop: ")

j=100

while j>=1:
    print(j)
    j=j-1
print("------------------End of program 2---------------------")

#Q.3) Print the multiplication table of 6 using a while loop    

k=1

while k<=10:
    print("6th Table: ", k ,"* 6 =", k*6)
    k=k+1

print("------------------End of program 3---------------------")

#Q.4) Find the sum of all even numbers from 1 to 50 using a loop

print("Sum of all even number from 1 to 50 using for loop")
j=0
for i in range(0,51,1):
    if i%2==0:
        j=j+i
        
print(j)

print("Sum of all even number from 1 to 50 using While loop")

i=0
j=0
while i<=50:
    if i%2==0:
        j=j+i
    i=i+1
print(j)

print("------------------End of program 4---------------------")

#Q.5) Display the reverse of a numbers using a while loop (e.g., 123->321)   

print("reverse of a numbers using a while loop: ")

num=int(input("Enter number: "))

op=0
while(num>0):
    i=num%10
    op=op*10+i
    num=num//10
    
print(op)

print("------------------End of program 5---------------------")

#Q.6) print numbers from 1 to 20, but stop the loop if the number is 13.

print("print numbers from 1 to 20, but stop the loop if the number is 13: ")
print("For loop:")
for i in range(1,21,1):
    if (i==13):
        print("The number is 13 so for loop was terminated")
        break
        
    else:
        print(i)

print("While loop")

i=1
while (i<=20):
    if(i==13):
        print("The number is 13 so while loop was terminated")
        break
    else:
        print(i)
    i=i+1

print("------------------End of program 6---------------------")
    
#Q.7) Print numbers from 1 to 20, but skip multiples of 3
print("Print numbers from 1 to 20, but skip multiples of 3:")
print("For loop: ")

for i in range(1,21,1):
    if(i%3==0):
        continue
    else:
        print(i)

print("While loop: ")
i=1
while(i<=20):
    if(i%3==0):
        i=i+1
        continue
    print(i)
    i=i+1

print("------------------End of program 7---------------------")

#Q.8) Write a program that iterates through a string and uses pass for vowels (so only consonants are printed)

print()
str1=input("Enter a string: ")

for i in str1:
    if i.lower() in "aeiou":
        pass
    else:
        print(i, end=" ")
print()
print("------------------End of program 8---------------------")

#Q.9) Opening balance = 1000, Transations: [200,-100,300,-50,-200], closing balance = 1150.Check opening + net transations = closing, if not print "Balance mismatch found and stop(break)"

open=1000

net=[200,-100,300,-50,-200]
close=1150
sum=0
i=0
print("For loop")
for i in range(0, len(net),1):
    sum=sum+net[i]
    if i==len(net)-1 and close != sum+open:
        print("Balance mismatch found")
        break
else:
    print("Balance proofing done")    
print("While loop")

sum1=0
i1=0
while i1<len(net):
    sum1=sum1+net[i1]
    i1=i1+1
    if i1== len(net) and close != open + sum1:
        print("Balance mismatch found")
        break
else:   
    print("Balance proofing done")
print("------------------End of program 9---------------------")
    

