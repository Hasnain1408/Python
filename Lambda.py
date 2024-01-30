
def x(a):
   # print("hi")
    return a+10

#x = lambda a : a+10
#print(y)

x=lambda a,b,c : a+b+c
#print(x(1,2,3))

x=lambda a : a*a*a
#print(x(7))

def myfun(n):
    return lambda a : (a+1)*n 

doubleFun=myfun(2)
print(doubleFun(8))