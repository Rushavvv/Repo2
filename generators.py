# Generators are another version of lists 
def generate_num_upto(num): 
    for i in range(1,num+1): 
        yield(i) # Yield is used instead of print 


generate_bhako = generate_num_upto(10)

for i in generate_bhako: 
    print(i) 

for i in generate_bhako: # esto garda ek choti matra print garcha 
    print(i) 



for i in  generate_num_upto(10): 
    print(i) 

for i in  generate_num_upto(10): # esto garda chai garcha multiple times 

    print(i) 

