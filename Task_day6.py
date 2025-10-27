#Write a python program to create a new text file named Sample.Txt and write the text "Hello,Python File Handling!" into it
file_Path='C:\\Users\\ChandraLekhaGunti\\Python_Practice\\Sample(File_Handling_).txt'
with open(file_Path,'w') as file:
    file.write("Hello,Python File Handling!")

#Write a python program to read and display the contents of Sample.txt
with open(file_Path,'r') as file:
    print(file.read())
    
#Write a program to append the line "This line is appended" to an existing file
with open(file_Path,'a') as file:
    file.write("\nThis line is appended") 

#Write a program that reads a file line by line and prints each line
with open(file_Path,'r') as file:
    print(file.readlines())

#Write a program to count the number of lines in a text file.
with open(file_Path,'r') as file:
    count=len(file.readlines())
    print("Number if lines in the lines:",count)

#Write a python program to copy the contents of one file to another file.
with open("Sample(File_Handling_).txt" , "r") as src, open('Destination.txt',"w") as dest:
    dest.write(src.read())

#Write a program that reads a file and prints only the lines that contain the word "True"
with open(file_Path,'r') as file:
    for i in file:
        if 'True' in i:
            print(i)

#Write a python program to check if a file exists before opening it(Use the os module)
import os
file='Sample(File_Handling_).txt'
if os.path.exists(file):
    print("File exists")
else:
    print("File not exists")



    