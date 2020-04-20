user_name = raw_input("Please enter your name: ")
if len(user_name) == 1 or len(user_name) == 2:
    print("Please enter a proper name")
    exit()
else:
    count = 0
    print("Hello %s" % (user_name))
    print("""
        Lets play a game.
        The rule is simple. We are heading to forest for camping. What would you pick with yourself?
        Make sure the item is important for camping. 
        Today, you only have 10 tries
    """)
    #I keep lower case here because if I put on top it gives a hint to a user
    user_name = user_name.lower()
    
    user_input = raw_input("Please enter an item name here: ").lower()
    #Checks if the user input is 1 character long or 2 character long. if the item is short it will exit
    if len(user_input) == 1 or len(user_input) == 2:
        print("Please enter a proper item name")
        exit()
    # If user puts item name and username same, it will quit
    elif user_name == user_input:
        print("You entered the same name for Item and your name")
        print("Repeat again")
    else:
        # If user guesses, it will ask 3 times with below code 
        if user_name[0] == user_input[0]:
            print("Please try another item. Lets see one more time")
            for i in range(1):
                user_input = raw_input("Please enter another item name again: ").lower()
                if user_name[0] == user_input[0]:
                    print("So Close")
                    for i in range(1):
                        user_input = raw_input("Please enter another item one last time: ").lower()
                        if user_name[0] == user_input[0]:
                            print("Seems like you guessed it. Please do not share")
        # Repeats if user cant find it
        while user_name[0] != user_input[0]:
            user_input = raw_input("Please try again, this does not work: ").lower()
            # This will quit if user cant find it in 10 guesses
            count += 1
            if count == 10:
                print("You were not able to find in 10 times")
                print("Come back again tomorrow")
                break

