# Print from 1 to 100
#For Loop
print("Print Numbers from 1 to 100:")
for i in range(0,101,1):
    print(i)
	
#While Loop
print("Print Numbers from 1 to 100:")
i=0
while i<100:
  i=i+1
  print(i)


# Print from 1 to 100
#For Loop
print("Print Numbers from 100 to 1:")
for i in range(100,0,-1):
    print(i)
	
#While Loop
i=101
while i>0:
  i=i-1
  print(i)
  
#Print Multiplication table of 6
#While Loop 
  i=1
while i<=5:
    print("Multiply 6 of",i,"is:",i*6)
    i=i+1
    
#For
for i in range(1,6,1):
 print("Multiply 6 of",i,"is:",i*6)


print numbers from 1 to 20, but stop the loop if the number is 13.
i=1
while (i<=20):
    if(i==13):
        print("The number is 13 so while loop was terminated")
        break
    else:
        print(i)
    i=i+1


#Print numbers from 1 to 20, but skip multiples of 3
#For loop
for i in range(1,21,1):
    if(i%3==0):
        continue
    else:
        print(i)
        
#While loop
i=1
while (i<=20):
    if(i%3==0):
        i=i+1
        continue
    print(i)
    i=i+1

#Write a program that iterates through a string and uses pass for vowels (so only consonants are printed)
str1=input("Enter a string: ")

for i in str1:
    if i.lower() in "aeiou":
        pass
    else:
        print(i, end=" ")


#Opening balance = 1000, Transations: [200,-100,300,-50,-200], closing balance = 1150.Check opening + net transations = closing, if not print "Balance mismatch found and stop(break)"
open=1000
net=[200,-100,301,-50,-200]
close=1151
sum=0
for i in net:
    sum=sum+i
print("Total net transations: ", sum)
j=open+sum
print("Opening:",open," + net: ",sum,"= closing", j)
if(close==j):
    print("Balance proofing done")
else:
    print("Actual closing was",close,"so Balance mismatch found")        