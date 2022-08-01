import os 
print(os.getcwd()) 
path = r"/Users/rushavsthapit/Desktop/Python2"



if os.path.exists("any"): 
    print("Already exists") 
else: 
    os.mkdir("any")


# Open or make new file 
open("file.docs","a").close() # a--> append mode 

# Change directory 

#1)--> os.chdir(r"\abc")

list_dir_path = r"/Users/rushavsthapit/Desktop/Python2/any"
print(os.listdir(list_dir_path)) 



change_dir_path = r"/Users/rushavsthapit/Desktop/Python2/any"

os.chdir(change_dir_path)
print(os.getcwd()) 
os.chdir(path)
print(os.getcwd()) 

# to find path of files 

for item in os.listdir(): 
    file_path = os.path.join(os.getcwd(),item)
    print(f" The path of this file {item} is: --> {file_path}")


# To walk in ath of files: 
print(os.walk(path))
file_walk = os.walk(path) 
for current_path, folder_name,file_name in file_walk: 
    print(f"The current_path is: --> {current_path}") 
    print(f"The folder_name is: --> {folder_name}") 
    print(f"The file_name is: --> {file_name}") 



import shutil 
print(os.getcwd())
'''shutil.rmtree("any")''' #permanently delete 

copy_garne_path = path + "/any2/any" # copy garne folder is any ani copy lagera rakhne folder is any2 

shutil.copytree(path + "/any",copy_garne_path) 
file_path = path + "/file.txt" 
file_ko_copy_garne_path = path + "/any2/file.png"
shutil.copy(file_path,file_ko_copy_garne_path)



