from itertools import count


class Person: 
    #init method/constructor 
    def __init__(self,name,age,address):   #name,age,address ==> attribute
        print("My beautiful method called")
        # instance variables 
        self.name = name 
        self.age = age 
        self.address = address
        self.gender = "M" 

    def user_info(self): 
        print(f"Your name is {self.name} and your age is {self.age}")

p1 = Person("Samay",21,"Ktm") 
p2 = Person("Rushav",21,"Ktm") 
print(p1.user_info())
print(p1.gender) 

'''class Laptop:
    discount_percent = 0  # class variable 
    def __init__(self,name,price,color,model): 
        self.name = name 
        self.price = price 
        self.color = color 
        self.model = model 
        self.f_name = name + " " + model
        
        
    def apply_discount(self): 
        self.discount_per = self.price - ((Laptop.discount_percent/100) * self.price )
        
        return self.discount_per

l1 = Laptop("Dell",50000,"Black","inspiron 15")
l2 = Laptop("Lenovo",60000,"Silver","thinkpad 2")
print(l1.f_name)
print(l1.__dict__)


print(l2.apply_discount())
Laptop.discount_percent = 10 
print(l1.apply_discount())'''
# Question 
# snapping one two where are you???


class Laptop:
    discount_percent = 0 
    counts = 0  # class variable 
    def __init__(self,name,price,color,model): 
        
        self.name = name 
        self.price = price 
        self.color = color 
        self.model = model 
        self.f_name = name + " " + model
        Laptop.counts += 1 
    @staticmethod 
    def my_func(): 
        print("Hello World") 

        
    @classmethod 
    def count_all_laptop(own_class): 
        return f"You have a total of {own_class.counts} laptops in your {own_class.__name__} store"

    def apply_discount(self): 
        self.discount_per = self.price - ((self.discount_percent/100) * self.price )
        
        return self.discount_per

l1 = Laptop("Dell",50000,"Black","inspiron 15")
l2 = Laptop("Lenovo",60000,"Silver","thinkpad 2")
print(l1.f_name)
print(l1.__dict__)

print(l2.apply_discount())
l1.discount_percent = 10 
print(l1.apply_discount())
print(Laptop.counts)
print(Laptop.count_all_laptop())
