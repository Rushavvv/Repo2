from pkg_resources import empty_provider


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

dict1 = {
    "f_name":"Aryama",
    "s_name":"Sharma",
    "age":19,
    "movie":["marvel","thor"],
    "fav_food":["Pizza","chowmin"],
    "residence":"Kathmandu"


}

print(dict1["movie"][1])




# Empty dict

empty_dict = {} 
print(empty_dict)
empty_dict["name"]="Kritika is absent"
print(empty_dict)