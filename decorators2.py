


def decorator_function(any_function): 
    def wrapper_function(*args,**kwargs): 
        '''This is a wrapper function'''
        print("This is extra function") 
        return any_function(*args,**kwargs) 
        
    return wrapper_function

def decorator_function2(any_function): 
    def wrapper_function(*args,**kwargs): 
        '''This is a wrapper function'''
        print("This is extra function") 
        return any_function(*args,**kwargs)
    return wrapper_function


# Extra line --> "This is extra function"
'''def fun1():
     print("function-->1")'''

# Extra line --> "This is extra function"
'''@decorator_function  # decorator_function lai call gareko 
def fun2(any_value):
     print(f"function-->2 with {any_value}")

fun2(5)'''

from functools import wraps 
# def decorator_function3(any_function): 
#     @ wraps(any_function)
#     def wrapper_function(*args,**kwargs): 
#         '''This is a wrapper function'''
#         print("This is extra function") 
#         return any_function(*args,**kwargs) 
#     return wrapper_function

# @decorator_function3
# def add(num1,num2): 
#     '''This func adds two numbers and returns sum'''
#     return num1 + num2


# add(2,3)
# print(add(2,3))
# print(add.__name__) 
# print(add.__doc__)

def decorator_for_add(value): 
    @wraps(value)
    def wrapper(*args,**kwargs): 
        print(f"Your are calling {value.__name__} function") 
        return value(*args,**kwargs)
    return wrapper
        


@decorator_for_add
def add2(n1,n2): 
    '''This is an add function'''
    return n1 + n2 

add2(2,3) 
print(add2(2,3)) 

print(add2.__doc__) 



# importing module 
import time as t
t1 = t.time()  
for i in range(100,10000,100): 
    print(i) 

t2 = t.time() 
total_required_time = t2-t1 
print(f"total required time is {total_required_time}")

def show_time(any_function):
	def wrapper_function(*args,**kwargs):
		''' this is wrapper function '''
		print(f"Executing func {any_function.__name__}")
		t1= t.time()
		returned_value=any_function(*args,**kwargs)
		t2= t.time()
		total_time = t2-t1
		print(f"This func took {total_time} time")
		return returned_value
	return wrapper_function

@show_time
def sq_finder(n):
	return [i**2 for i in range(1,n+1)]

sq_finder(500)



# decorator practice 3 

def only_int_all_out(value): 
    @wraps(value) 
    def wrapper_fucntion(*args,**kwargs):
        stored_data_type = [] 
        for arg in args: 
            stored_data_type.append(type(arg)==int)
        if all(stored_data_type): 
            return value(*args,**kwargs) 
        else: 
            print("Only int is allowed")
    return(wrapper_fucntion)


# OR 


def only_int_all_out2(value): 
    @wraps(value) 
    def wrapper_fucntion(*args,**kwargs):
        if all([type(arg)== int for arg in args]):
            return value(*args,**kwargs) 
        else: 
            print("Only int is allowed")
    return(wrapper_fucntion)



@only_int_all_out2

def add_func(*args): 
    total = 0 
    for i in args:
        total += i 
    return total 

print(add_func(1,2,3,4,[5,6,7]))


# Decorator Practice 4 
def fun(data_type): 
    def only_int_all_out3(value): 
        @wraps(value) 
        def wrapper_fucntion(*args,**kwargs):
            if all([type(arg)== data_type for arg in args]):
                return value(*args,**kwargs) 
            else: 
                print(f"Only {data_type} is allowed")
        return(wrapper_fucntion)
    return only_int_all_out3


@fun(str) 
def string_join(*args): 
    join_string = "" 
    for i in args: 
        join_string += i
    return join_string

print(string_join("Kritika"," Deo"))

