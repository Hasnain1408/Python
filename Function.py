
def my_function(*kids): #arbitrary number of arguments
    print(kids[1])
    
my_function("Fuad",'Evan',"Alvi")

def name_fun(**name): #arbitrary number of keyword arguments
    print("First name : "+name["fname"]+"\n"+"Last name : "+name["lname"])
    
name_fun(lname="Sheikh",fname="Hasnain")

def my_country(name="Hasnain",country = "Bangladesh"):
    print(f"I am {name},from {country}")

my_country()
my_country("Sadik","Pakistan")
my_country("Fuad","Saudi Arabia")
my_country(country="Palestine")



##sort function
def myfun(n):
    return abs(n-50)

numList=[100,50,65,82,23]
#numList.sort()
#numList.sort(reverse=True)
numList.sort(key=myfun,reverse=True)
print(numList)


def print_list(ls):
    for x in ls*2:
        print(x)

fruits=["apple",'banana','cherry',"kiwi","mango"]
print_list(fruits*2)
