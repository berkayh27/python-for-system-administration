try:
    user_input = input("Please find a hidden number: ")
except SyntaxError:
    print("That is not a number")
    user_input = input("Please enter a  number: ")

count = 0
while user_input != 23:
    try: 
        user_input = input("Try again: ")
    except SyntaxError:
        print("That is not a number: ")
    if user_input == 23:
        print("Finally you found it")

        
    # This will quit if user cant find it in 10 guesses
    count += 1
    if count == 10:
        print("You were not able to find in 10 times")
        break