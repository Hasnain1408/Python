
ls =["abc","tematha",47,True,"shit",420,7.30]
#print(x) x if type(x)==int for x in ls ]

fruits=["apple",'banana','cherry',"kiwi","mango"]
multiList=fruits*2
print(multiList)
newList=[x.upper() if x!="banana" else "orange" for x in fruits ]
#print(newList)

odd={x for x in range(100) if (x%2 == 1)}
#print(odd)

##sort function

def myfun(n):
    return abs(n-50)

numList=[100,50,65,82,23]
#numList.sort()
#numList.sort(reverse=True)
#numList.sort(key=myfun)
#print(numList)
