# operating system

import os

print(os.getcwd())      #current working directory
print(os.listdir())     #list files in currrent directory

# Change the Current Directory
import os
print(os.getcwd())
os.chdir("C:\\Users\\anupa\\python programs")
print("Now in:", os.getcwd())

#List Files and Folders in a Directory
files = os.listdir()
print(files)

#create new folder
os.mkdir("NewFolder01")
print("Folder Created!")

#Remove a Folder
os.rmdir("NewFolder01")

#Rename Files or Folders
os.rename("newname.txt", "newname1.txt")

# Check if a File or Folder Exists
print(os.path.exists("data.txt"))
print(os.path.exists("NewFolder"))

size = os.path.getsize("calculator.py") #Get File Size
print("File size (bytes):", size)

# os.getcwd() -- Get current working directory
# os.chdir(path) -- Change directory
# os.listdir(path) -- List all files/folders
# os.mkdir(name) -- Create new folder
# os.rmdir(name) -- Remove folder
# os.rename(old, new) -- Rename file/folder
# os.path.exists(path) -- Check existence
# os.path.isfile(path) -- Check if path is file
# os.path.isdir(path) -- Check if path is directory
# os.path.join(a, b) -- Join path safely
# os.environ.get(var) -- Access environment variable
# os.system(cmd) -- Run OS command