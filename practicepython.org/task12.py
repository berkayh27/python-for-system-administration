a = [5, 10, 15, 20, 25,5, 10, 15, 20, 20]

def list_creator(given_list):
    for i in given_list:
        newlist = [given_list[0],  given_list[-1]]
        print(newlist)

list_creator(a)