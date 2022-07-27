# Flexible Function 

# def dum(a,b): 
#     return a+b 

# print(dum(3,4))

# def another_sum(*args):
#     print(args)
#     print(type(args))

# print(another_sum(2,3,4)) 
'''user_ko_value =  input("Enter a value: ").split(",")

def calc(*val):
    
     sum = 0
     counter = 0

     for i in val:
         indexed_val = int(i[counter])
         sum += indexed_val
      
         
        

     return sum

print(calc(*user_ko_value))'''





# parameter -----> arg
'''def calc(num1,*val):
    sum = 0 + num1 

    for i in val:
        
        sum +=  i
    return sum

print(calc(6,4)) '''



# user_ko_value =  input("Enter a value: ").split(",")

# def calc(*val):
    
#      sum = 0
#      counter = 0

#      for i in val:
#          indexed_val = int(i[counter])
#          sum += indexed_val
#          return sum

# print(calc(*user_ko_value)) 

'''List = [3,4,5,6]
power = int(input("Enter a number: "))



def sqa(val,*args): 
    if args: 
        return [i**val for i in args]
    else: 
        return "You didnt enter a valid number"
 
print(sqa(power,*List))
'''

# def sum_all_num(**kwargs): # kwargs --> key word argument 

#     print(kwargs)
#     index = 0 
# for key,value in kwargs.items():
#         print(f"Your first name is {key}:{value}")


# print(sum_all_num(first_name="Aryama",last_name="Sharma")) 

'''dictionary = {"a":1,"b":2,"c":3}
def sum(**kwargs): 

    index = 0 
    for value in kwargs.values(): 
        index = index + value  
    return index 


print(sum(**dictionary))'''

#PADK ---> parameter(name), argument(*args), deafault(age = 9), kwargs(**kwargs)



list_names = ["aryama","rushav","samay","maharshi","kritika"]
def rev(name_list,**kwargs): 
    '''To reverse you must give {is_reverse = True} either True or False''' #doc string bhancha ellai
    if kwargs.get("is_reverse"): 
        return [name[-1::-1].title() for name in name_list]
    else: 
        return [name.title() for name in name_list]

print(rev(list_names,is_reverse = True ))
print(rev.__doc__)

