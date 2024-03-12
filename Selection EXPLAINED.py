#SELECTION
#Selection is making a choice
#The keywords are IF ELIF ELSE
print("hello,how can I help you?")
age = int(input("How old are you?"))


password = str(input("What's the password?"))

if age >= 14 and password == "Kebab":
    print("Welcome to the secret club")
elif age == 13:
    print("Come back in 1 year")
else:
    print("You are too young")

