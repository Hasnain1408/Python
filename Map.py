# map(function, iterables)

def make_even(num):
    if num%2 == 1:
        return num+1
    else:
        return num

x = [1, 4, 5, 7, 10, 11, 12, 15, 16, 17, 20]    
y = list(map(make_even, x))
print(y) 


store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_euros = lambda data: (data[0], data[1]*0.82)

store_euros = list(map(to_euros, store))
for i in store_euros:
    print(i)



def concat(a, b):
  return a + b

x = map(concat, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))
