class Laptop: 
    def __init__(self,brand,model_name,price): 
        self.brand = brand
        self.model_name=model_name
        self.__price=price  # privare (for nameing convention) 


new_laptop = Laptop("Lenovo","i7",70000) 
new_laptop._Laptop__price = 50000

# print(help(Laptop)) 
print(new_laptop._Laptop__price)
# print(new_laptop.__price)


class Laptop: 
    def __init__(self,brand,model_name,price): 
        self.brand = brand
        self._price=max(price,0)
        self.model_name = model_name
       

    @property # Getter 
    def price(self): 
        return self._price

    
    @price.setter # Setter 
    def price(self,new_price): 
        self._price = max(new_price,0)
    @property
    def full_spec(self): 
        return f"The brand is {self.brand} and price is {self._price}"




new_laptop = Laptop("Lenovo","i7",-70000) 
new_laptop.price = -50000
print(new_laptop._price)
print(new_laptop.full_spec)
print(new_laptop.price)





