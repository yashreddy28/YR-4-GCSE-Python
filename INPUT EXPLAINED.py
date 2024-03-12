#Input explained

#here is a veriable

name = "dave"
print(name)
#but my name is NOT dave
#I want to enter my own name
#I can do this with a function called "input"

name = input("Enter name>>>")
print(name)
#Input defaults to strings
#If you wamt other data types
#you have to CAST for it e.g.

age = int(input("Enter your age"))
print(age)

price = float(input("how much is it?"))
print(price)

#More about CASTING
a = 10
b = 20
c = a + b
print(c)

a = str(10)
b = str(20)


# This is CONCATENATION - Glues stuff together

c = a + b

print(c)


a = float(10)#casting for float
b = float(20)#casting for float
c = a + b
print(c)
