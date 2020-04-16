#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
age = input("How old are you?: ")

user_name = raw_input("What is your name?: ").upper()
new_age = age + 100

print("%s, you will be %s in 100 years" % (user_name, new_age))

another_number = input("Please enter another number: ")

for i in range(another_number):
    print("You will be %s" %(new_age))