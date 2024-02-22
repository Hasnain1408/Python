
ls =["abc","tematha",47,True,"shit",420,7.30]
[print(x) if type(x)==int else print('Not int') for x in ls ]

fruits=["apple",'banana','cherry',"kiwi","mango"]
multiList=fruits*2
print(multiList)
newList=[x.upper() if x!="banana" else "orange" for x in fruits ]
print(newList)
newList2=[x for x in fruits if 'a' in x]
print(newList2)

odd={x for x in range(100) if (x%2 == 1)}
print(odd)


