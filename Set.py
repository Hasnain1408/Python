#set->(unordered)

thisset={"apple",'banana',"cherry",True,1408}
#tropical={'pineaple',"mango","banana","Apple"}
mylist=["Amazon","Microsoft",'Meta']
#thisset.add(tropical) #error
#thisset.update(tropical)
#thisset.remove("bangi")#create error
thisset.discard("bangi")#no error
thisset.update(mylist)
#thisset.add("orange")
#thisset.update("orange")
x=thisset.pop()#pop randomly ->(unordered)
#print(thisset.pop())
#thisset.clear() #clear whole set ->print(empty)
#del thisset #delete the set ->nothing to print(error)

#Operation
setA={'a','b',"lambda"}
setB={97,'lambda',100}
#setResult=setA.union(setB) #same as update
#setResult=setA.intersection(setB)
#setA.intersection_update(setB)
#setResult=setA.symmetric_difference(setB) #elements that not present in BOTH sets
#setA.symmetric_difference(setB)
#setResult=setA.difference(setB) #setA-setB
#print(setResult)
#print(setA)
#z=setA.isdisjoint(setB)
#print(z)