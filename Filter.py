
family = {
    # "name": "Hussainan",
    # "year": 2003,

    "child1": {
    "name": "Fuad",
    "age": 16
    },

    "child2": {
    "name": "Farahi",
    "age": 14
    },

    "child3": {
    "name": "Evan",
    "age": 3
    }
}

def myFunc(child):
  if int(child["age"]) >= 10:
    return True
  else:
    return False


val = family.values()
adolescents = filter(myFunc, val)
# adults = filter(myFunc, [child for child in children if isinstance(child, dict)])


# for x in adolescents:
#   print(x["name"])


people = {
  "person1":
  {
    "name": "Alice",
    "age": 22
  },
  "person2":
  {
    "name": "Bob",
    "age": 17
  },
  "person3":
  {
    "name": "Charlie",
    "age": 25
  },
  "person4":
  {
    "name": "David",
    "age": 19
  },
  "person5":
  {
    "name": "Eve",
    "age": 12
  },
  "person6":
  {
    "name": "Drath",
    "age": 23
  }
}

def is_voter(person):
    return person["age"] >= 18  

voters = filter(is_voter, people.values())

# print(dict(voters)) 
 
for x in voters:
  print(x["name"])

# print(people.items())
