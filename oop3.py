class Phone: 
    def __init__(self,brand,model,price): 
        self.brand = brand
        self.price = price
        self.model = model

    def full_spec(self): 
        print(f"The full spec of this phone is: {self.brand} {self.model} and price is: {self.price}")

class SmartPhone(Phone): 
    def __init__(self,brand,model,price,ram,memory,camera):
        super().__init__(brand,model,price)
        self.ram = ram
        self.memory = memory 
        self.camera = camera
    
    
    def full_spec(self): 
        print(f"The full spec of this phone is: {self.brand} {self.model} and price is: {self.price}")



class FlagshipPone(SmartPhone): 
    def __init__(self,brand,model,price,ram,memory,camera,security):
        super().__init__(brand,model,price,ram,memory,camera) 
        self.security = security 

    def full_spec(self): 
        print(f"The full spec of this phone is: {self.brand} {self.model} and price is: {self.price} with high security {self.security}")

phone1 = Phone("Maharshi","Landline",4500)
sp = SmartPhone("mi","note5",45000,"3gb","64gb","20mp")
fp = FlagshipPone("Samsung","S10+",45000,"8gb","256gb","100mp","chuna maru")

print(fp.full_spec()) 
print(FlagshipPone.mro) 
print(isinstance(sp,FlagshipPone))
print(issubclass(sp,FlagshipPone))
