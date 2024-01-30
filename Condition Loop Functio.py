email ='''
Assalamu walikum, Sir.My SPL-01 is under your supervision.You gave me a task.I completed it.
If you have time,I will discuss with you tomorrow.
'''
#print(email)

i=1;
while i<6:
  #  print(i)
    i=i+1
else:
    pass
  # print("i is no longer less than 6")
  
for x in range(1,6):
    print(x)
    if x==3:
        break
else:
  #  pass
    print("Finally finished!")
  
def my_function(*kids): #arbitrary number of arguments
    pass
   # print(kids[1])
    
#my_function("Fuad",'Evan',"Alvi")

def name_fun(**name):
    print("First name : "+name["fname"]+"\n"+"Last name : "+name["lname"])
    
name_fun(lname="Sheikh",fname="Hasnain")
