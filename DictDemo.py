# dictionary are ordered, changeable and can not contain duplicates
# declaraton can be done by writing directly or using a constructor

dict_exmpl = dict(name="Samarth",last_name="Dariya",age=22,Technology="Python")
print(dict_exmpl)

# value of a key can be accessed through get method and like using key as an index
print(dict_exmpl["name"],dict_exmpl.get("last_name"))

# values() method gives the values of dictionary in a form a list
# the list is connected to the dictionary 
# any change in the dictionary is reflected in the list 
a = dict_exmpl.values()
print(a)
dict_exmpl["college"]="BITS"
print(a) #changes are reflected in a

# keys() method gives the keys of dictionary in a form a list
# the list is connected to the dictionary 
# any change in the dictionary is reflected in the list 
b = dict_exmpl.keys()
print(b)
dict_exmpl["home_town"]="Ratlam"
print(b) #changes are reflected in b

# we can use the in and not in operator to check if the key exists in the dictionary


# dictionary can be updated or adding using the key or the update() method
dict_exmpl.update({"home_town":"indore"})
print(dict_exmpl)

# removing items in the dictionary can be done by pop() and popitem() or the del keyword
# clear() method will empty the dictionary and del keyword can also delete the dictionary completely
dict_exmpl.popitem() # remove the last added item
print(dict_exmpl) 
dict_exmpl.pop("college") # remove the item with the given key
print(dict_exmpl)

# looping through dictionary the for loop loops through the keys of the dictionary even in the short hand
[print(x) for x in dict_exmpl]

# to copy a dictionary like lists we have to use copy() method or the dict() constructor