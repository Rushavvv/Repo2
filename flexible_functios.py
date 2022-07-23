# Flexible Function 

# def dum(a,b): 
#     return a+b 

# print(dum(3,4))

# def another_sum(*args):
#     print(args)
#     print(type(args))

# print(another_sum(2,3,4)) 
user_ko_value =  input("Enter a value: ").split(",")

def calc(*val):
    
     sum = 0
     counter = 0

     for i in val:
         indexed_val = int(i[counter])
         sum += indexed_val
         
        

     return sum

print(calc(*user_ko_value)) 





# parameter -----> arg
'''def calc(num1,*val):
    sum = 0 + num1 

    for i in val:
        
        sum +=  i
    return sum

print(calc(6,4)) '''



#sum bhanne function leu tara number chai user le dincha
