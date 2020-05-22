import random
import string


def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

# Prints out random string of 10 by default
print("Random String is ", randomString())

# Prints out random string of 8 as user defined
print("Random String is ", randomString(8))

# Prints out random string of 19 as user defined
print("Random String is ", randomString(19))


# Below code takes an input from user
users_input = input("Please enter a number: ")
users_input = int(users_input)
print("Random String is ", randomString(users_input))
