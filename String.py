
# =============================================================================
# STRING BASICS
# =============================================================================

# String Creation (Immutable)
text1 = 'Single quotes'
text2 = "Double quotes"
text3 = '''Multi-line
string with
triple quotes'''
text4 = """Another multi-line
string example"""

print("String creation examples:")
print(f"text1: {text1}")
print(f"text2: {text2}")
print(f"text3: {text3}")
print(f"text4: {text4}")
print()

# =============================================================================
# STRING INDEXING AND SLICING
# =============================================================================

s = "Python Programming"
print("String indexing and slicing:")
print(f"Original string: '{s}'")
print(f"s[0]: '{s[0]}'")          # First character
print(f"s[-1]: '{s[-1]}'")        # Last character
print(f"s[1:4]: '{s[1:4]}'")      # Slice from index 1 to 3
print(f"s[:6]: '{s[:6]}'")        # From start to index 5
print(f"s[7:]: '{s[7:]}'")        # From index 7 to end
print(f"s[:]: '{s[:]}'")          # Full copy
print(f"s[::-1]: '{s[::-1]}'")    # Reversed string
print()

# =============================================================================
# STRING ALIGNMENT METHODS
# =============================================================================

word = "Hello"
print("String alignment methods:")
print(f"Original: '{word}'")
print(f"center(15, '*'): '{word.center(15, '*')}'")
print(f"ljust(15, '-'): '{word.ljust(15, '-')}'")
print(f"rjust(15, '-'): '{word.rjust(15, '-')}'")

print(f"zfill(11): '{word.zfill(11)}'")
print()

# =============================================================================
# ENCODING/DECODING
# =============================================================================

print("Encoding and decoding:")
original = "Hello World! 🌍"
encoded = original.encode('utf-8')
decoded = encoded.decode('utf-8')
print(f"Original: {original}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")
print()

# =============================================================================
# STRING FORMATTING
# =============================================================================

name = "Alice"
age = 25
score = 95.67

print("String formatting examples:")
# Old style formatting
print("Old style: Hello %s, you are %d years old" % (name, age))

# str.format() method
print("str.format(): Hello {}, you scored {:.2f}".format(name, score))

# f-strings (Python 3.6+)
print(f"f-string: Hello {name}, you are {age} and scored {score:.2f}")
print()

# =============================================================================
# ESCAPE CHARACTERS AND RAW STRINGS
# =============================================================================

print("Escape characters:")
print("Line 1\nLine 2")           # Newline
print("He said \"Hello!\"")       # Quotes
print("Path: C:\\Users\\Alice")   # Backslash
print("Tab\tSeparated\tValues")   # Tab

print("\nRaw strings:")
raw_path = r"C:\Users\Alice\Documents"
print(f"Raw string: {raw_path}")
print()

# =============================================================================
# STRING REVERSAL METHODS
# =============================================================================

text = "Python"
print("String reversal methods:")
print(f"Original: {text}")
print(f"Using slicing: {text[::-1]}")
print(f"Using reversed(): {''.join(reversed(text))}")
# test = 12345
# test = list(str(test))
# print(f"Reversed list of digits: {''.join(reversed(test))}")
print()

# =============================================================================
# STRING ⟷ LIST CONVERSION
# =============================================================================

print("String to List and List to String:")
string_example = "abc"
list_from_string = list(string_example)
print(f"String to list: '{string_example}' → {list_from_string}")

list_example = ['a', 'b', 'c']
string_from_list = ''.join(list_example)
print(f"List to string: {list_example} → '{string_from_list}'")

# With separator
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)
print(f"Join with space: {words} → '{sentence}'")
print()

# =============================================================================
# COMMON INTERVIEW TRICKS
# =============================================================================

print("Common interview tricks:")

# Palindrome check
def is_palindrome(s):
    return s == s[::-1]

test_word = "racecar"
print(f"'{test_word}' is palindrome: {is_palindrome(test_word)}")

# Anagram check
def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

word1, word2 = "listen", "silent"
print(f"'{word1}' and '{word2}' are anagrams: {are_anagrams(word1, word2)}")

# Character frequency
from collections import Counter
text_for_count = "programming"
char_count = Counter(text_for_count)
print(f"Character frequency in '{text_for_count}': {dict(char_count)}")
print()

# =============================================================================
# ALL STRING METHODS WITH EXAMPLES
# =============================================================================

print("=" * 50)
print("COMPLETE STRING METHODS REFERENCE")
print("=" * 50)

# capitalize()
text = "hello world"
print(f"capitalize(): '{text}' → '{text.capitalize()}'")

# casefold()
text = "HELLO WörLD"
print(f"casefold(): '{text}' → '{text.casefold()}'")

# center()
text = "hi"
print(f"center(10, '*'): '{text}' → '{text.center(10, '*')}'")

# count()
text = "banana"
print(f"count('a'): '{text}' → {text.count('a')}")

# encode()
text = "hello"
print(f"encode(): '{text}' → {text.encode()}")

# endswith()
filename = "script.py"
print(f"endswith('.py'): '{filename}' → {filename.endswith('.py')}")

# expandtabs()
text = "Name:\tAge:\tCity"
print(f"expandtabs(4): '{text}' → '{text.expandtabs(8)}'")

# find()
text = "hello world"
print(f"find('o'): '{text}' → {text.find('o')}")

# rfind()
text = "hello world"
print(f"rfind('o'): '{text}' → {text.rfind('o')}")

# index()
text = "hello world"
print(f"index('w'): '{text}' → {text.index('w')}")

# rindex()
text = "hello world"
print(f"rindex('o'): '{text}' → {text.rindex('o')}")

# format()
template = "Name: {}, Age: {}"
print(f"format(): '{template}' → '{template.format('Bob', 30)}'")

# format_map()
template = "Name: {name}, Age: {age}"
data = {'name': 'Carol', 'age': 28}
print(f"format_map(): '{template}' → '{template.format_map(data)}'")

# isalnum()
test_cases = ["abc123", "abc", "123", "abc!"]
for case in test_cases:
    print(f"isalnum(): '{case}' → {case.isalnum()}")

# isalpha()
test_cases = ["hello", "hello123", "HELLO"]
for case in test_cases:
    print(f"isalpha(): '{case}' → {case.isalpha()}")

# isdigit()
test_cases = ["123", "12.3", "abc"]
for case in test_cases:
    print(f"isdigit(): '{case}' → {case.isdigit()}")

# isnumeric()
test_cases = ["123", "²³⁴", "abc", "12.3"]
for case in test_cases:
    print(f"isnumeric(): '{case}' → {case.isnumeric()}")

# isdecimal()
test_cases = ["123", "12.3", "²³⁴"]
for case in test_cases:
    print(f"isdecimal(): '{case}' → {case.isdecimal()}")

# isascii()
test_cases = ["hello", "héllo", "🙂"]
for case in test_cases:
    print(f"isascii(): '{case}' → {case.isascii()}")

# islower()
test_cases = ["hello", "Hello", "HELLO"]
for case in test_cases:
    print(f"islower(): '{case}' → {case.islower()}")

# isupper()
test_cases = ["HELLO", "Hello", "hello"]
for case in test_cases:
    print(f"isupper(): '{case}' → {case.isupper()}")

# isspace()
test_cases = [" ", "\t\n", "hello"]
for case in test_cases:
    print(f"isspace(): '{repr(case)}' → {case.isspace()}")

# istitle()
test_cases = ["Hello World", "hello world", "HELLO WORLD"]
for case in test_cases:
    print(f"istitle(): '{case}' → {case.istitle()}")

# isidentifier()
test_cases = ["var1", "1var", "my_var", "class"]
for case in test_cases:
    print(f"isidentifier(): '{case}' → {case.isidentifier()}")

# join()
separator = " | "
items = ["apple", "banana", "cherry"]
print(f"join(): '{separator}'.join({items}) → '{separator.join(items)}'")

# ljust()
text = "hi"
print(f"ljust(8, '-'): '{text}' → '{text.ljust(8, '-')}'")

# rjust()
text = "hi"
print(f"rjust(8, '-'): '{text}' → '{text.rjust(8, '-')}'")

# lower()
text = "HELLO World"
print(f"lower(): '{text}' → '{text.lower()}'")

# upper()
text = "hello World"
print(f"upper(): '{text}' → '{text.upper()}'")

# title()
text = "hello world python"
print(f"title(): '{text}' → '{text.title()}'")

# swapcase()
text = "HeLLo WoRLd"
print(f"swapcase(): '{text}' → '{text.swapcase()}'")

# lstrip()
text = "   hello world   "
print(f"lstrip(): '{text}' → '{text.lstrip()}'")

# rstrip()
text = "   hello world   "
print(f"rstrip(): '{text}' → '{text.rstrip()}'")

# strip()
text = "   hello world   "
print(f"strip(): '{text}' → '{text.strip()}'")

# partition()
text = "name:value:extra"
print(f"partition(':'): '{text}' → {text.partition(':')}")

# rpartition()
text = "name:value:extra"
print(f"rpartition(':'): '{text}' → {text.rpartition(':')}")

# replace()
text = "apple pie"
print(f"replace('apple', 'cherry'): '{text}' → '{text.replace('apple', 'cherry')}'")

# split()
text = "apple,banana,cherry"
print(f"split(','): '{text}' → {text.split(',')}")

# rsplit()
text = "apple,banana,cherry,date"
print(f"rsplit(',', 2): '{text}' → {text.rsplit(',', 2)}")

# splitlines()
text = "Line 1\nLine 2\nLine 3"
print(f"splitlines(): '{repr(text)}' → {text.splitlines()}")

# startswith()
filename = "document.pdf"
print(f"startswith('doc'): '{filename}' → {filename.startswith('doc')}")

# zfill()
number = "42"
print(f"zfill(6): '{number}' → '{number.zfill(6)}'")

print()

# =============================================================================
# DIGIT MANIPULATION EXAMPLES
# =============================================================================

print("=" * 50)
print("DIGIT MANIPULATION EXAMPLES")
print("=" * 50)

n = 197
print(f"Original number: {n}")
print(f"Type: {type(n)}")

# Convert to list of digit characters
list_of_digit_chars = [digit for digit in str(n)]
# list_of_digit_chars = list(str(n))
print(f"List of digit characters: {list_of_digit_chars}")

# Convert to list of digit integers
list_of_digit_ints = [int(digit) for digit in str(n)]
print(f"List of digit integers: {list_of_digit_ints}")

# Sum of squares of digits
sum_of_squares = sum(int(digit)**2 for digit in str(n))
print(f"Sum of squares of digits: {sum_of_squares}")

# Additional digit operations
product_of_digits = 1
for digit in str(n):
    product_of_digits *= int(digit)
print(f"Product of digits: {product_of_digits}")

# Reverse the number
reversed_number = int(str(n)[::-1])
print(f"Reversed number: {reversed_number}")

# Check if number is palindrome
is_palindromic = str(n) == str(n)[::-1]
print(f"Is palindromic: {is_palindromic}")

print()
print("=" * 50)
print("END OF EXAMPLES")
print("=" * 50)