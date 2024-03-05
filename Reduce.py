from functools import reduce

numbers: list[int] = {1, 2, 3, 4, 5}
result: float = reduce(lambda a, b: a + b, numbers)

strings: list[str] = ['a1', 'b2', 'c3', 'd4', 'e5']
result: str = reduce(lambda a, b: f'{a}-{b}', strings, 'Hi')

print(result)