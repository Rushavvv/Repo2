'''def square(a): 
    return a**2 
s = square
print(s.__name__) # gives square

print(list(map(lambda a:a**2, [1,2,3])))


any_list = [4,5,6]
def my_own_map(func,list): 
    new_list = [] 
    for item in list:
        new_list.append(func(item))
        return new_list

def to_pow(num): 
    def calc_power(n): 
        return num**n 
    return calc_power
cube_of = to_pow(3) 
print(cube_of(3))'''

def decorator_function(any_function): 
    def wrapper_function(): 
        print("This is extra function") 
    return wrapper_function

def decorator_function2(any_function): 
    def wrapper_function(): 
        print("This is extra function") 
    return wrapper_function


# Extra line --> "This is extra function"
def fun1():
     print("function-->1")

# Extra line --> "This is extra function"
@decorator_function  # decorator_function lai call gareko 
def fun2():
     print("function-->2")



