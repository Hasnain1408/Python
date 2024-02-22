
def my_function(*kids): #arbitrary number of arguments
    print(kids[1])
    
my_function("Fuad",'Evan',"Alvi")

def name_fun(**name):
    print("First name : "+name["fname"]+"\n"+"Last name : "+name["lname"])
    
name_fun(lname="Sheikh",fname="Hasnain")