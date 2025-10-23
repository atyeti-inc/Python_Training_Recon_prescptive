#only print line where word TRUE/true/True is present

import os
# Define the file name and path
directory = r"C:\Timir\Practice Codes"
file_name = "true.txt"
file_path = os.path.join(directory, file_name)

#set of word
keywords = {'true','TRUE','True'}

#find word in file and print sentence
with open(file_path,'r') as file:
    for line in file:
        if any(word in line for word in keywords):
            print(line.strip())
