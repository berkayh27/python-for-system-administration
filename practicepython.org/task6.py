#https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

string_1 = raw_input("Please enter a name: ")
string_2 = string_1[::-1]

if string_1 == string_2:
    print("This is palindrome")
else:
    print("This is not palindrome")