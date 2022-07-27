# Enumerating 
'''list_of_names=["kritika","aryama","rushav","samay","maharshi"]

position = 0 
for i in list_of_names: 
    print(f"The name {i} is in {position} position")
    position += 1 '''

#OR 

'''for loc,name in enumerate(list_of_names): 
    print(f"The name {name} is in {loc} position")'''


# name_user = input("Enter a name")
# def finds(name,target_name): 
    
#     for loc,name in enumerate(name):
#         if name.title() == target_name.title(): 
#             return f"The name {name} is in {loc} position"
         
#     return("No name")
      

# print(finds(list_of_names,name_user))


# Map Functins (Map ma ek choti matra loop chalaunu milcha)
 
lists = [1,2,3,4]   # Iterables ( Loop chalaune na sakine is called iterables)
'''def square(value): 
    return value**2 '''

#print(square(lists))

# OR

'''k_ho = map(square,lists) '''# This is iterator( Loop chalauna sakine is called iterator) 
'''for i in k_ho:
    print(f"k_ho--> {i}") '''

# OR 
'''k_ho = list(map(lambda a: a**2,lists))
print(k_ho) '''


# Iter --> iterator ma convert garne 
''' how loop works'''
'''iterator_converted = iter(lists)
print(next(iterator_converted))  
print(next(iterator_converted))  
print(next(iterator_converted))  
print(next(iterator_converted))  

for i in lists: 
    print(i)'''



# Filter Functions 

''' Using map '''
# try_func = list(map(lambda a: a%2==0,lists))
# print(try_func)


''' Using List comprehension '''
# def even(number): 
#     return[i%2==0 for i in number]

# print(even(lists))


''' Using normal method '''
# def even2(value):
#     dummy_list = []  
#     for i in value: 
#         if i%2==0: 
#             dummy_list.append(i)
#     return dummy_list

# print(even2(lists))

''' Even more efficient use of map functions and filter functions'''
'''print(list(filter(lambda a: a%2==0,lists)))''' # Filter le list ko content dincha
'''print(map(filter(lambda a: a%2==0,lists)))''' # Map le True/False ma dincha


big_char_list = ["A","B","C"]
char_list = ["a","b","c"]
#num_list = [1,2,3,4,5,6,7,8]

'''print(list(zip(big_char_list,char_list)))'''

'''Dictionary can only be done in two lists'''

# For unzip
'''l = list(zip(big_char_list,char_list))
print(l)



l1,l2 =zip(*l)
print(l1,l2)'''

# Question 1

# user_input_name = [input("Enter a number")]

# Question 2 
q_list = [[1,2,3],[4,5,6],[7,8,9]]

'''def q2(value): 
    list = []
    count = 0
    
    return[((i[count]))//3 for i in value  ]
    

print(q2(q_list))'''

# ave_calculator = lambda *args: [(sum(pair)//len(pair)) for pair in zip(*args) ]
# print(ave_calculator(*q_list))


# Any and all functions

num_list1 = [2,4,6,8,10] 
num_list2 = [1,3,5,7,9]

print(any(list(map(lambda a: a%2==0, num_list1))))

def sum(*args): 
    if all([(type(args)==int or type(args)==float) for arg in args]): 
        total = 0 
        for num in args:
            total += num 
        return total
    else: 
        return "Input a float or an integer value" 

print(type(sum(1,3.0)))