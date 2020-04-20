# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
student_list1 = ["bob", "sam", "tim"]

student_list2 = ["bob", "kim", "dan"]


# Iterate thru list1 and use each iteration in if sentence
for i in student_list1:
    # if iterated item above is in list 2 print list2
    if i in student_list2:
        print(i)