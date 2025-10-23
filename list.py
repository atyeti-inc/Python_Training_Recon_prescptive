#list
friends = ["Alice","Bob","Charlie"]
print(friends)
friends.append("David")
friends.append("Eve")
print(friends)
cp_friends=friends.copy()
print("copied list", cp_friends)
del friends
if "Alice" in cp_friends:
    print("Alice is there in copied list")
