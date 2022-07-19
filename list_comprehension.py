# your_value = int(input("Enter your number"))


# def sq(num): 
#     listu = [] 
#     for i in range(1,num+1): 
        
#         listu.append(i**2)
#     return listu 





# #OR

# def sqa(num): 
#     return[i**2 for i in range(1,num+1)]

# print(sq(your_value)) 
# print(sqa(your_value))


a = ["abc","def","ghi"]

'''def lis(val): 
    listo = []
    for i in val: 
        listo.append(i[0])

    return listo 
    
print(lis(a))


def lis(val): 
    

    return[i[0] for i in val] 
    
print(lis(a))


def filter_even(num): 
    return[ i for i in range(num+1) if (i%2==0)]

print(filter_even(10))'''


# def filter(num): 
#     return[ (i*2) if (i%2==0) else (i*-1) for i in range(num+1) ]

# print(filter(10))

'''def nested(vul): 
    return[[i for i in range(1,vul+1)]for k in range(1,vul+1)]

print(nested(3))'''






def rev(val): 
    return[i[::-1] for i in val]

print(rev(a))
