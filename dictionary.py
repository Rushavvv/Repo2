
{"key":  "(value)"}

# {"age":19}

'''days = {"day1":"Sunday","day2":"Monday","day3":"Tuesday","day4":"Wednesday","day5":"Thrusday","day6":"Friday"}
print(days) 
print(type(days))'''

# Type2 
'''days2 = dict(day4 = "Wednesday", day5 = "Thursday", day6 = "Friday") 
print(days2)'''


# How to access data from dictionary 

'''print(type(days2["day4"])) 

any_dict = {
    "f_name":"Maharashi",
    "age":23,
    "fav_song":["s1","s2",11,True],
    "others":{
        "fav_game":"Football",
        "fav_programming":"Python"
    }
}

print(any_dict["fav_song"][3])
print(any_dict["others"]["fav_programming"])'''

# Task

'''dict1 = {
    "f_name":"Aryama",
    "s_name":"Sharma",
    "age":19,
    "movie":["marvel","thor"],
    "fav_food":["Pizza","chowmin"],
    "residence":"Kathmandu"


}'''

# print(dict1["movie"][1])




# Empty dict

'''empty_dict = {} 
print(empty_dict)
empty_dict["name"]="Kritika is absent" # Add gareko dict ma
empty_dict["name"]="aryama is absent" # Update gareko dict ma 
print(empty_dict)'''


# In keyword (Conditinal and looping statements)


# print(dict1)

'''if "f_name" in dict1:
    print("present")
else: 
    print("Not Present")'''


# Diff method huncha  ---> keys(),value(),items(),copy(),clear(),get()

# if "Aryama" in dict1.values():
#     print("Present")
# else: 
#     print("Not Present")



# if "Aryama" in dict1.keys():
#     print("present")
# else: 
#     print("Not Present")



# for i,j in dict1.items(): 
#     print(f"The key is {i} and the value is {j}")


# dic1 = {"day1":"Sunday","day2":" Monday"}
# dic2 = {"day3":"Wednesday","day4":" Tuesday"}


'''
6) add, update, pop and popitem method in dictionary
--> days["all_days"]=["day1","day2","day3"]
--> days.update(ANOTHER_DICTIONARY) # which returned the value of pop(key)
--> days.pop("all_days") # which returned the value of pop(key)
--> days.popitem() # randomly delete one item and returned the value of pop(key)

'''
# dic3 = dic1.copy()
# dic3["day2"]=["Nice Day","Rainny Day"]
# dic3["all_days"]=["day1","day2","day3"]
# print(dic3)

# print(dic1)
# dic1.update(dic2)
# print(dic1)

# poppe_item = dic1.pop("day1")
# print(poppe_item) 

# print(dic1)


'''
7) fromkeys, get, clear and copy method
--> days=dict.fromkeys(["day1","day2","day3"], "unknown") # can use tuple and string too
--> get method:
ex: days["apple"] --> error but days.get("day1") --> no error and result too
--> if days.get("day1"): print present else absent
ex: if None: is treated as False else True
--> days.clear() ; days.copy() ; is vs == 
'''


# Fromkeys(keys,value) method
'''days=dict.fromkeys(["day1","day2","day3"], "unknown")
print(days)'' 


# print(days["day5"]) --> Gives error 404

print(days.get("day3"))
# print(days.get("day5"))

# if dict1.get("residence"): 
#     print("Present")
# else: 
#     print("Not Present")'''



# print(days.get("day5","Not found"))

# user_info = {"f_name":"Aryama","l_name":"Sharma", "age":19,"age":1}
# print(user_info.get("age")) 






'''num = int(input("Enter a number")) 

def cube(val): 
    
    dictionary = {}
       

    for r in range(val+1): 
        dictionary[r] = r **3 
    return dictionary

print(cube(num))

nam = input("Enter your name")
def count(name): 
    diction = {} 
    for char in name: 
        diction[char] = name.lower().count(char)
    return diction 

print(count(nam))'''
