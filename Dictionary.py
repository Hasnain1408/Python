
capitals = {
    "Bangladesh":"Dhaka",
    "Pakistan":"Islamabad",
    "Bosnia":"Sarajevo",
    "Egypt":"Cairo"
}
#print(capitals)
#print(dir(capitals))
#print(help(capitals))

# print(capitals.get("Japan"))
# print(capitals["Japan"])

# if capitals.get("Egypt"):
#     print(f"The capital is {capitals.get("Egypt")}")
# else:
#     print("That capital doesn't exixts")    

capitals.update({"Japan": "Tokyo"})
capitals.update({'Pakistan': "Korachi"})
capitals["German"] = "Berlin"
# capitals.pop("Egypt")
# del capitals["Egypt"]
# capitals.popitem()
# capitals.clear() #clear all items
# del capitals     #delete the existance 
# print(len(capitals))

# for x in capitals:
#     print(x)           #key
# for x in capitals:
#     print(capitals[x]) #value

keys = capitals.keys()
values = capitals.values()
# keys, values = capitals.keys(), capitals.values()

items = capitals.items()
# for key,value in capitals.items():
#     print(f"{key}: {value}")    




car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020,
    "colors": ["red", "white", "blue"]
}
# car2 = dict(car)
# car2 = car.copy()
# car["electric"] = False



child1 = {
    "name": "Fuad",
    "age": 8
}
child2 = {
    "name": "Farahi",
    "age": 6
}
child3 = {
    "name": "Evan",
    "age": 3
}

myfamily = {
    "name": "Hussainan",
    "year": 2003,
    "child1": child1,
    "child2": child2,
    "child3": child3
}

# print(myfamily["child1"]["name"])
# print(myfamily.get("child1"))