# set() function is used for printing out items without duplicate
# In below list, we have replease 1,2 but set removes 1,2 since it is repeated 2 times
# https://docs.python.org/3.3/library/stdtypes.html?highlight=set#set

list_1 = [1,2,3,4,5,6,1,2]

names = set()
names.add("Michelle")
names.add("Bob")
names.add("Michelle")
print(names)
print(set(list_1))

# Below code is basically taking a list above and using set() function to remove duplicates and assigning it to list_1_set value
list_1_set = set(list_1)
for i in list_1_set:
    print(i)