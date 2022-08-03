'''Syntax Error '''

# def fun: 
#     print("Done") 

'''  Indentation Error'''
# def fun(): 
# print("sth")

'''Name Error'''
# ok = 1 
# print(ko) 

'''Type Error'''
# print(1+"A") 

'''Index Error'''
# list = [1,2]
# print(list[3])

'''Value Error'''
# s = 8 
# m = "abc"
# print(int(m)) 

'''Attribure Error'''
# list = ["A","B"]
# list.haldeu("C")

'''Key Error'''
# d = {"name":"Apple"} 
# print(d["name"]) 

'''Raise Error'''
# class LmaoError(TypeError): 
#     pass
# def add(a,b): 
#     if (type(a) == int and type(b)==int): 
#         return a+b 
#     else:
#         raise LmaoError("Not int datatype") 


# print(add(2,3)) 
# print(add("2","3"))



def divide(a,b):
    try: 
        a // b
    except ZeroDivisionError as ze_msg:
        raise ZeroDivisionError("Dont divide by zero")
        

    
    except TypeError as te_msg: 
        raise TypeError("Input int only")
       
    except: 
        return ("Unexpected Error") 

    
print(divide(1,"0"))
print(divide(1,0)) 





