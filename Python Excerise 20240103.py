#Combine And Sort Lists

#Instructions
#Place the two lists in a .py file.

#Add some code that combines the two lists into one single list.

#Removes any duplicates from the combined list.

#Sort the combined list in ascending order.

#Print out the sorted list.


#Solutions:

#Can use dictionary to perform the same task, as dictionaries can't have duplicates
#need to convert dictionary into a list to revert it back to a list


list1 = [5, 3, 8, 6, 3]
list2 = [7, 2, 5, 9, 8]

list3 = list(dict.fromkeys(list1 + list2))

print(list3)




#Can also create a function to perform this task

def my_function (no_duplicates):
    return list(dict.fromkeys(no_duplicates))

no_duplicates = my_function((list1+list2))

print(list(no_duplicates))



