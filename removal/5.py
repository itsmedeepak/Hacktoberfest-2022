# Python program to remove multiple
# elements from a list

# creating a list
list1 = [11, 5, 17, 18, 23, 50]

# items to be removed
unwanted_num = {11, 5}

list1 = [ele for ele in list1 if ele not in unwanted_num]

# printing modified list
print("New list after removing unwanted numbers: ", list1)
