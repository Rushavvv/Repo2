# Syntax: 
'''number = int(input("enter value"))
def prac(val): 
    
    return {i:"even" if (i%2==0) else "odd" for i in range(val+1)}
    
print(prac(number))'''




 

# def prac(val): 
#     dictionary  = {} 
#     for i in range(val+1): 
#         dictionary[i] = (f"even:{i%2==0}")
#     return dictionary 

'''def prac(val): 
    dictionary  = {} 
    for i in range(val+1): 
        sq = i**2
        if sq%2==0: 
            dictionary[sq] = "even"
        else: 
            dictionary[sq] = "odd"
    return dictionary 

print(prac(number))'''

# val = str(input("enter your name"))
# def lett(value): 
#     return {i:(value.lower().count(i.lower())) for i in value.lower() }

# print(lett(val))

# number = int(input("enter value"))
# def prac(val): 
    
#     return {(i,i**2) for i in range(val+1)}
    

# ok = prac(number)
# print(ok)

'''name,name2 = input("Enter names: ").split(",")
name_list = [name,name2]

def ans(list_of_name): 
    return{name[0] for name in list_of_name}

wau = ans(name_list)
print(wau)'''



