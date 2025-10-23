#file_handling

import os
# Define the file name and path
directory = r"C:\Timir\Practice Codes"
file_name = "sample_file.txt"
file_path = os.path.join(directory, file_name)


# Ensure the directory exists
#if os.makedirs(directory, exist_ok=True):
if os.path.exists(file_path):
    print("File exists")
    
else:
        print("No file exists")


# Define the content to write into the file
content = "Hello Python, File Handling."

# Open the file in write mode and write the content
with open(r"C:\Timir\Practice Codes\sample_file.txt", "w") as file:
    file.write(content)
    
#Read the content
with open(file_name, "r") as file:
    file.read()
    print(content)

# append new line
append = "\nThis line is appended"
with open(r"C:\Timir\Practice Codes\sample_file.txt", "a") as file:
    file.write(append)
    print(append)

#read file line by line
print(" # Read File line by line has been created with sample content.")
with open(r"C:\Timir\Practice Codes\sample_file.txt", "r") as file:
    line_count=0
    for line in file:
        print(line.strip())
        line_count += 1

print("no: of lines in file is : ",line_count)

#create a new file and copy content
cp_file_name = "copy_sample_file.txt"
with open(r"C:\Timir\Practice Codes\sample_file.txt", "r") as source_file,open(r"C:\Timir\Practice Codes\copy_sample_file.txt", "w") as dest_file:
    for line in source_file:
        dest_file.write(line)

print("Lines copied to new file", cp_file_name)






