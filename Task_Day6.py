# Day 7
# 1.
with open("Sample.txt", "w") as file:
    file.write("Hello, Python File Handling")

# 2.
with open("Sample.txt","r") as file:
    content=file.read()
    print(content)

# 3.
with open("Sample.txt", "a") as files:
    ##file.seek(0)
    files.write("\n This line is appended:True")

# 4.
with open("Sample.txt", "r") as f:
    content=f.read()
    print(content)

# 5.
with open("Sample.txt", "r") as f:
    count=len(f.readlines())
    print("Number of lines in the Sample.txt file:", count)

# 6. copy the file content 1 to content 2
with open("Sample.txt" , "r") as src, open('Destination.txt',"w") as dest:
    dest.write(src.read())

# 7. 
with open("Sample.txt", "r") as f:
    for line in f:
        if 'True' in line:
            print(line.strip())

# 8.
import os 
file_path="Sample.txt"
if os.path.exists(file_path):
    with open(file_path,"r") as f:
        content=f.read()
        print("File content:\n", content)
else:
    print("File does not exists")