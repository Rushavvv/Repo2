poem_path = r"/Users/rushavsthapit/Desktop/python_mid/python-poem.txt" 

rf = open(poem_path)  # Open le by default read mode ma open garcha 
'''print(f"Before reading , cursor position-----> {rf.tell()}") 

print(rf.read()) 
print(f"After reading , cursor position-----> {rf.tell()}") 
print("--------------------------------------------------")
rf.seek(0)
print(rf.read())'''



# Readline method() 

'''print(f"Next line -->: {rf.readline()}",end="")'''




# Readlines method() 
'''all_lines = rf.readlines() 
for line in all_lines: 
    print(f"The line is : -->{line}",end="") 
    

rf.close() '''

# Use of wit block: 
'''with open(poem_path,"r") as rf: 

    print(rf.read()) '''

#------------> Write data in file(w,a,r+) mode <------------
# Write mode

'''with open("Kritika.txt","w") as wf:''' #If there is alr a file with the same name tyo file lai delete garera naya data lekhcha or chaina bhane naya banaucha fle ani lekhcha basically override garcha 
'''    wf.write("Hello Kritika\nHow are you?")
    '''
# Append mode
'''with open("samay.txt","a") as af:''' # Esle chai delete chai gardeina baru naya banayera add gardincha last ma 
'''
     af.write("Hello samayasa\nHow are you?")'''

# R+ mode 
'''with open("file.txt","r+") as rpf:''' # Esle chai agadi override huncha 

'''    rpf.write("write in r+ mode")'''

'''with open("file.txt","r+") as rpf:''' # Esle chai agadi override huncha 
'''    rpf.seek(len(rpf.read())+1)

    rpf.write("Last ma lekha")'''

# Read and Write 
'''with open(poem_path,"r") as rf: 
    with open("samay.txt","w") as wf: 
        wf.write(rf.read())
'''

# Read Love_Story 

'''with open("love_story.txt","r") as rf:
     print(rf.encoding)
     print(rf.read()) '''

# Question

with open("Question.txt","r") as rf: 
    with open("samay.txt","w") as wf : 
        for line in rf.readlines():
            name,salary = line.split(",")
            wf.write(f"{name}'s your salary is {salary}")