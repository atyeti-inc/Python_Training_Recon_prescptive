## Day 5
## 1.Flag negative transactions in the list
tnxns=[100,-50,200,-75]
for txn in tnxns:
    if txn < 0:
        print(f"Negative transaction flagged: {txn}")

## 2.Problem Statement
txns=[100,-50,200,-75,300]
# Append a new transaction -100
txns.append(-100)
print("After appending -100:", txns)

# Index of first negative transaction
for i, txn in enumerate(txns):
    if txn < 0:
        print("Index of first negative transaction is:", i)
        break

# Remove last transaction using pop()
last_txn = txns.pop()
print("After popping last transaction:", txns)
print("Popped transaction:", last_txn)

# Find max and min transaction values
max_txn=max(txns)
min_txn=min(txns)
print("Maximum transaction:", max_txn)
print("Minimum transaction:", min_txn)


## 3.
nums=[5,2,9,1,7,2,5]
# Count how manu times 5 occurs
count=nums.count(5)
print("5 occurs:",count, "times")

# Remove the first 2
nums.remove(2)
print("After removing 2:", nums)

#Sort the numbers in descending order
nums.sort(reverse=True)
print("Numbers after sorted in descending order:", nums)

#Slic the first 3 elements from the sorted list
first_3=nums[:3]
print("First three elements from the sorted list:", first_3)

## 4
friends=["Alice", "Bob", "Charlie"]

# Extend the list
friends.extend(["David", "Eve"])
print("After Extending:", friends)

# Copy of the list and clear the original one
friends_copy=friends.copy()
friends.clear()
print("Copied list:", friends_copy)

# Check if alice is in copied list
is_alice_in_copy="Alice" in friends_copy
print("Is Alice is in copied list?", is_alice_in_copy)

# Total number os friends in copied list
total_friends=len(friends_copy)
print("Total number of friends is:", total_friends)

## 5
bank=[100,200,300,400,500]
custodian=[100,200,250,400,600]

# Txn only in bank
banks=[txn for txn in bank if txn not in custodian]
print("Transactions only in bank:",  banks)

# Txn only in custodian
cust=[txn for txn in custodian if txn not in bank]
print("Transactions only in custodian:", cust)

# Combine both lists and remove duplicates
combine=list(set(bank + custodian))
print("Combined unique transactions are:", combine)

# Count total unreconciled breaks:
total_unreconciled = len(banks) + len(cust)
print("Total unreconciled breaks:", total_unreconciled)

## 6. Tuple with numbers from 1 t 5
numbers=tuple(range(1,6))
print(numbers)

## 7. Access the third element
nums=(10,20,30,40,50)
third_element=nums[2]
print("Third element:", third_element)

## 8. Slice tuple
nums1=(1,2,3,4,5,6,7)
slice=nums1[2:5]
print(slice)

## 9. Concatenate
first=(1,2,3)
second=(4,5,6)
combined=first + second
print(combined)

## 10.count how many times 5 appears in tuple
digits=(5,2,3,5,4,5)
count=digits.count(5)
print("5 appears",count,"times")

## 11.Unpack
words=("Python", "is", "fun")
a,b,c=words
print(a)
print(b)
print(c)

## 12. Nested Tuple
nested_tuple=tuple((i,i+1) for i in range(1,6,2))
print(nested_tuple)
element=nested_tuple[1][1]
print("The element accessed", element)

## 13.convert the tuple
tuple=("a","b","c")
result="".join(tuple)
print(result)

## 14. sum of all elements
nums2=(10,20,30,40)
total=sum(nums2)
print("Sum of all numbers in a tuple:", total)

## 15. Remove duplicates
nums3=(1,2,3,2,4,1,5)
output=tuple(set(nums3))
print(output)

## 16. Y coordinate
points=((1,2),(3,4),(5,6))
y_coordinate=points[1][1]
print("Y-Coordinate of second point is:", y_coordinate)