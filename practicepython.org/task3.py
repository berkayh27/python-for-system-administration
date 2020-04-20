#https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# Iterate thru list


for i in a:
    # if the items in the list less or equal to 5 prints
    if i <= 5:
        less_than_5_list = []
        less_than_5_list.append(i)
        print(less_than_5_list)
