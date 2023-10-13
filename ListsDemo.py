# list is an ordered and changeable datastructure 
# list can be indexed and can contain duplicate entries
# it is also possible to store two or more different data types in a list
list_example = ["samarth",22,"dariya","27/01/2001",7.7,True]
print(list_example)

#len() will give the length of the list
for x in range(len(list_example)):
            print(list_example[x])


#list and strings common features
# can be negative indexed
# can be sliced (using negative indexing as well)
# checked for occurrence of a particular element using the in and not in operator

#changing elements in list is easy
list_example[0]="saksham"
print(list_example)
# we can even change the range of indexes
list_example[0:4]=["saksham",19,"dariya","27/04/2004"] 
#here 4th index will remain the same everything starting from 0th and before fourth index is removed and
#the list items on the RHS would be added starting from the start index after the RHS list items are added the 
# original list items will fllow starting from the end index as specified
print(list_example)
# we can also use insert() function to specify the index and insert any entry in a list
list_example.insert(len(list_example),"S.G.S.I.T.S")
print(list_example)

#append() and extend() functions will add entries at the end of the list
# append() is used for a single entry while extend() will take any iterable as an argument and 
# add them to the end of the list

# remove(element) function is used to remove a particular element 
# pop(index) function is used to remove the element on the specified index
# clear() method can be used to empty the lists
# del keyword can be used to delete any specified element as well as the list itself

#looping through list
# there is a shorthand for loop for looping through lists
[print(x) for x in list_example]
#this is same as
for x in list_example:
                print(x)

#list comprehension can be used to form any new lists from any given iterable
# syntax newlist = [expression for item in iterable if condition == True]
new_list_example = ["anything "+ str(x) for x in list_example if x!=True]
print(new_list_example)

# we can use the sort() method to sort the list in any manner with using 
# reverse = True for descending and even use a custom function as a key
# reverse() method can be used to reverse a list 

# list1 = list2 will not make a copy of list2 but it would point to same memory
# we can use copy() method for making copy of list
# list() constructor can also be used
