# -----file to write-----
# file = open("example.txt",'w')
# # file.write("Hello this is from python...")
# file.write("Hello this is second line...")
# file.close()

# ------file to read------
# file = open("example.txt",'r')
# content = file.read()
# print(content)

# ------append - not overwrite,it added to existing------ 
# file = open("example.txt",'a')
# file.write("\nThis line was added later...")

# -----there is another simple way,no need to call file.close() manually-----
# with open("example.txt","r") as file:
#     content = file.read()
#     print(content)

# -----reading line by line  ,  this is efficient for large files-----
# with open("example.txt","r") as file:
#     for line in file:
#         print(line.strip())   

# -----exists,rename,remove-----
import os
# chek if file exists
print(os.path.exists("example.txt"))
# rename
os.rename("example.txt","fileOpTest.txt")
# delete
os.remove("newfile.txt")