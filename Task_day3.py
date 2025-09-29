
#1. print numbers 1to 100
while loop
i=1
while i<=100:
    print(i)
    i+=1

# for loop

for i in range(1,100+1,1):
    print(i)



#2. print numbers from 100 to 1
# while loop

i=100
while i>=1:
    print(i)
    i-=1

# for loop

for i in range(100,0,-1):
    print(i)

#3. print the multiplication table using a while loop

#while loop

n=int(input("Enter the number: "))
i=1
while(i<=10):
    print(n*i)
    i+=1

# for loop
n=int(input("Enter the number: ")) 
for i in range(1,10+1,1):
    print(n*i) 

#4. find the sum of all even numbers from 1 to 50

sum=0
for i in range(2,51,2):
    if i%2==0:
        sum=sum+i
print(sum)


# while loop

sum=0
i=1
while i<=50:
    if i%2==0:
        sum+=i
    i+=1
print(sum)    


#5. display the reverse of a number using while loop 123==321

n=123

while(n>0):
    rem=n%10
    print(rem)
    n=n//10

#6. print numbers 1 to 20 ,but stop the loop if the number is 13

i=1
while(i<=20):
    print(i)
    if i==13:
        break
    i+=1

# # for loop

for i in range(1,21,1):
    print(i)
    if i==13:
        break

#7. print numbers from 1 to 20,but skip multiples of 3

i=1
while(i<=20):
    if i%3==0:
        i+=1
        continue
    print(i)
    i+=1


#8. write a program thet iterrates through a string and uses pass for vowels(so only constant are printed)


string="sandeep"
i=0
while i<len(string):
    if string[i] in ('a','e','i','o','u'):
        pass
    else:
        print(string[i])
    i+=1  

 #8.  problem statement


opening_balance = 1000
transactions = [200, -100, 300, -50, -200]
expected_closing_balance = 1150

balance = opening_balance
i = 0

while i < len(transactions):
    balance += transactions[i]
    i += 1
    if i == len(transactions) and balance != expected_closing_balance:
        print("Balance mismatch found")
        break
else:
    print("Closing Balance Verified:", balance)
