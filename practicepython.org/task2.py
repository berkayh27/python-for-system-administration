#https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

number1 = input("Please enter a number: ")
number2 = input("Pleae enter another number: ")
#The % sign is like division only it checks for the remainder, so if the number divided by 2 has a remainder of 0 it's even otherwise odd.


if number1 % 2 == 0:
    print("This is an even number")
    if  number1 % number2 == 0:
        print("This is divided")
    else:
        print("Cant be divided")
else:
    print("This is an odd number")