Task 4

#Write a loop to flag all negative transactions in this list: txns = [100, -50, 200, -75] 


txns = [100, -50, 200, -75]

for i, txn in enumerate(txns):
    if txn < 0:
        print(f"Transaction is negative: {txn}")
        
        
 '''Problem Statement:
Transactions:
txns = [100, -50, 200, -75, 300]
Tasks:
Append a new transaction -100.
Find the index of the first negative transaction.
Remove the last transaction using pop().
Find the maximum and minimum transaction values.'''
      
        
        
txns = [100, -50, 200, -75, 300]

# 1. Append a new transaction -100
txns.append(-100)
print("Updated transactions:", txns)


# 2. Find the index of the first negative transaction
txns = [100, -50, 200, -75, 300]
first_negative_index = next((i for i, txn in enumerate(txns) if txn < 0), None)
print("Index of first negative transaction:", first_negative_index)

# 3. Remove the last transaction using pop()
txns = [100, -50, 200, -75, 300]
txns.pop()
print (txns)

# 4. Find the maximum and minimum transaction values
txns = [100, -50, 200, -75, 300]
max_txn = max(txns)
min_txn = min(txns)
print("Maximum transaction value:", max_txn)
print("Minimum transaction value:", min_txn)


'''nums = [5, 2, 9, 1, 7, 2, 5]
Tasks:
Count how many times 5 occurs.
Remove the first 2.
Sort the numbers in descending order.
Slice the first 3 elements from the sorted list.'''


# 1. Count how many times 5 occurs
nums = [5, 2, 9, 1, 7, 2, 5]
count_5 = nums.count(5)
print("Count of 5:", count_5)

# 2. Remove the first occurrence of 2
nums = [5, 2, 9, 1, 7, 2, 5]
nums.remove(2)
print("List after removing first 2:", nums)

# 3. Sort the numbers in descending order
nums = [5, 2, 9, 1, 7, 2, 5]
nums.sort(reverse=True)
print(nums)

# 4. Slice the first 3 elements from the sorted list
nums = [5, 2, 9, 1, 7, 2, 5]
top_3 = nums[:3]
print("Top 3 elements:", top_3)


'''friends = ["Alice", "Bob", "Charlie"]
Tasks:
Extend the list with ["David", "Eve"].
Make a copy of the list and clear the original one.
Check if "Alice" is still in the copied list.
Find the total number of friends in the copied list.'''


# 1. Extend the list
friends = ["Alice", "Bob", "Charlie"]
friends.extend(["David", "Eve"])
print (friends)

# 2. Make a copy and clear the original
friends = ["Alice", "Bob", "Charlie"]
copied_friends = friends.copy()
friends.clear()
print("Copied Friends:", copied_friends)

# 3. Check if "Alice" is in the copied list
friends = ["Alice", "Bob", "Charlie"]
is_alice_present = "Alice" in copied_friends
print("Is Alice present?", is_alice_present)

# 4. Find the total number of friends in the copied list
friends = ["Alice", "Bob", "Charlie"]
total_friends = len(copied_friends)
print("Total number of friends:", total_friends)



'''You are reconciling transactions between Bank and Custodian records.
bank = [100, 200, 300, 400, 500]
custodian = [100, 200, 250, 400, 600]
Tasks:
Find transactions that are only in Bank but not in Custodian.
Find transactions that are only in Custodian but not in Bank.
Combine both lists and remove duplicates (use set() or list methods).
Count how many total unreconciled breaks exist.'''


# 1. Transactions only in Bank
bank = [100, 200, 300, 400, 500]
custodian = [100, 200, 250, 400, 600]
only_in_bank = list(set(bank) - set(custodian))
print("Transacions Only in Bank:", only_in_bank)


# 2. Transactions only in Custodian
bank = [100, 200, 300, 400, 500]
custodian = [100, 200, 250, 400, 600]
only_in_custodian = list(set(custodian) - set(bank))
print("Transacions Only in Custodian:", only_in_custodian)


# 3. Combine both lists and remove duplicates
bank = [100, 200, 300, 400, 500]
custodian = [100, 200, 250, 400, 600]
combined_unique = list(set(bank + custodian))
print("Combined Unique Transactions:", combined_unique)


# 4. Total unreconciled breaks
bank = [100, 200, 300, 400, 500]
custodian = [100, 200, 250, 400, 600]
total_breaks = len(bank) + len(custodian)
print("Total Unreconciled Breaks:", total_breaks)



#Create a tuple with numbers from 1 to 5.

numbers = tuple(range(1, 6))
print(numbers)

# 1. Access the 3rd element of (10, 20, 30, 40, 50)
t1 = (10, 20, 30, 40, 50)
third_element = t1[2]
print("Third element:", third_element)


# 2. Slice (1, 2, 3, 4, 5, 6, 7) to get (3, 4, 5)
t2 = (1, 2, 3, 4, 5, 6, 7)
sliced = t2[2:5]
print("Sliced tuple:", sliced)

# 3. Concatenate (1, 2, 3) and (4, 5, 6)
t3 = (1, 2, 3)
t4 = (4, 5, 6)
concatenated = t3 + t4
print("Concatenated tuple:", concatenated)


# 4. Count how many times 5 appears in (5, 2, 3, 5, 4, 5)
t5 = (5, 2, 3, 5, 4, 5)
count_5 = t5.count(5)
print("Count of 5:", count_5)


# 5. Unpack (“Python”, “is”, “fun”) into three variables
t6 = ("Python", "is", "fun")
word1, word2, word3 = t6
print("Unpacked:", word1, word2, word3)

# 6. Access element 4 from nested tuple ((1, 2), (3, 4), (5, 6))
nested = ((1, 2), (3, 4), (5, 6))
element_4 = nested[1][1]
print("Element 4:", element_4)


# 7. Convert (“a”, “b”, “c”) into a string "abc"
t7 = ("a", "b", "c")
joined_string = "".join(t7)
print("Joined string:", joined_string)


# 8. Find the sum of all elements in (10, 20, 30, 40)
t8 = (10, 20, 30, 40)
total_sum = sum(t8)
print("Sum:", total_sum)


# 9. Remove duplicates from (1, 2, 3, 2, 4, 1, 5)
t9 = (1, 2, 3, 2, 4, 1, 5)
unique = tuple(set(t9))
print("Unique values:", unique)


# 10. Print the y-coordinate of the second point in ((1, 2), (3, 4), (5, 6))
coordinates = ((1, 2), (3, 4), (5, 6))
y_second = coordinates[1][1]
print("Y-coordinate of second point:", y_second)
