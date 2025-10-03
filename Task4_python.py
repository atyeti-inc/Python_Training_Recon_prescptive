#lists

#----------1. Write a loop to flag all negative transactions in this list: txns = [100, -50, 200, -75] 

txns=[100,-50,200,-75]

for val in txns:
    if val<0:
        print(val)



#--------------2.txns = [100, -50, 200, -75, 300]
#tasks
# Append a new transaction -100.

txns=[100,-50,200,-75,300]
txns.append(-100)
print(txns)

# Find the index of the first negative transaction.

for val in txns:
    if val<0:
       
        print( txns.index(val))
        break

# Remove the last transaction using pop().

txns.pop()
print(txns)

# Find the maximum and minimum transaction values.

print("Maximum of list: ",max(txns))

print("Minimum of list: ",min(txns))


#3.
nums = [5, 2, 9, 1, 7, 2, 5]
# Tasks:
# Count how many times 5 occurs.
cnt=nums.count(5)
print(cnt)

# Remove the first 2.
rm=nums.remove(2)
print(nums)

# Sort the numbers in descending order.

nums.sort(reverse=True)
print(nums)

# # Slice the first 3 elements from the sorted list.

s=nums[0:3]
print(s)



#4.
friends = ["Alice", "Bob", "Charlie"]
# # Tasks:
# # Extend the list with ["David", "Eve"].

friends.append("David")
friends.append("Eve")
#print(friends)

# # Make a copy of the list and clear the original one.
friends_copy=[]
friends_copy=friends
print(friends_copy)

# friends.clear()
# print(friends)
# # Check if "Alice" is still in the copied list.
for val in friends_copy:
    if val=="Alice":
        print("Alice is in the list")
    

# # Find the total number of friends in the copied list.

print(len(friends_copy))



#5.
#  You are reconciling transactions between Bank and Custodian records.
bank = [100, 200, 300, 400, 500]
custodian = [100, 200, 250, 400, 600]
# Tasks:
# Find transactions that are only in Bank but not in Custodian.
only_in_bank=[]
for txns in bank:
    if txns not in custodian:
        only_in_bank.append(txns)
print(only_in_bank)

# Find transactions that are only in Custodian but not in Bank.

only_in_custodian=[]

for txn in custodian:
    if txn not in bank:
        only_in_custodian.append(txn)
print(only_in_custodian)        


# Combine both lists and remove duplicates (use set() or list methods).

combined=list(set(bank+custodian))
print(combined)


# Count how many total unreconciled breaks exist.

# Find Bank-only and Custodian-only
only_in_bank = [txn for txn in bank if txn not in custodian]
only_in_custodian = [txn for txn in custodian if txn not in bank]

# Combine both = total breaks
unreconciled = only_in_bank + only_in_custodian

print(unreconciled)
print(len(unreconciled))


########-------------------Tuples-------------------------

#1. create a tuple with numbers from 1 to 5
tup=(1,2,3,4,5)
print(tup)


# #2.Access the 3rd element of(10,20,30,40,50)

tup1=(10,20,30,40,50)
print(tup1[2]) # Access the 3rd element

# #3. slice (1,2,3,4,5,6,7) to get (3,4,5)

tup3=(1,2,3,4,5,6,7)
print(tup3[2:5])

# #4.Concatenate (1,2,3) and(4,5,6)

t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)


# #5.count how many times 5 appears in(5,2,3,5,4,5)

tup4=(5,2,3,5,4,5)
print(tup4.count(5))


# #6. unpack ("Python","is","fun") into three variables
var=("Python","is","fun")
a,b,c=var
print(a)
print(b)
print(c)


# #7.create a nested  tuple((1,2),(3,4),(5,6)) and access element 4
val=((1,2),(3,4),(5,6))
element=val[1][1]
print(element)


#8.convert the tuple  ("a","b","c") in to string "abc"

tup5=("a","b","c")
i=0
while i<len(tup5):
    string=tup5[i]
    i+=1
    print(string,end="")


# #9. Find the sum of all elements in(10,20,30,40)

tup6=(10,20,30,40)
i=0
sum=0
while i< len(tup6):
    sum+=tup6[i]
    i+=i
print(sum) 
# Meth2:  
tup6=(10,20,30,40)
print(sum(tup6))


#9.remove duplicates from(1,2,3,2,4,1,5)

tup_dup=(1,2,3,2,4,1,5)
unique_tuple=tuple(set(tup_dup))
print(unique_tuple)

# #using loop

unq_list=[]

for val in tup_dup:
    if val not in unq_list:
        unq_list.append(val)

con=tuple(unq_list)
print(con)



#10.nested coordinates  of points ((1, 2), (3, 4), (5, 6)). Print the y-coordinate of the second point.

points=((1,2),(3,4),(5,6))

point=points[1][1]
print(point)