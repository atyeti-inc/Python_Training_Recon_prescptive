#palindrom

str = input("Input a palindrom string :")
palin = str[::-1]
if str==palin:
	print(str, "is a palindrom")
else:
    print(str, "is not a palindrom")