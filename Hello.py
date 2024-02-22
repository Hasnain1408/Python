
print('Hello World !!\n'*10)

email ='''
Assalamu walikum, Sir.My SPL-01 is under your supervision.You gave me a task.I completed it.
If you have time,I will discuss with you tomorrow.
'''
print(email)

age=21
text="My name is Hasnain, and I am {}."
print(text.format(age))

print("Your name : ")
name=input()
print("Your age : ")
agein=int(input())
welcome="Hello, {}!\nYou are {} years old."
print(welcome.format(name,age))

x=200.08
print(isinstance(x,int))