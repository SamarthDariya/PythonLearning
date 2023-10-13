# tuple is collection which is unchangeable and ordered
# tuple can contatin duplicates can even contain different datatypes in it
# tuples can be indexed 
# len() function can be used to find the length of the tuple

tuple_example = ("this","is","actually","like","vector","in","mathematics")
# tuple can be indexed and sliced like to lists with negative index as well 

# updating a tuple can be done in only two ways
# making a new list perform addition or deletion operation and the converting the list back to tuple
# adding two vectors is allowed in python so we can add data at the back or at the front by making a new tuple

y = ("new","tuple")
tuple_example=y+tuple_example
print(tuple_example)

# unpacking a tuple is assigning variables values from a tuple
(x1,x2,x3,x4,x5,x6,x7,x8,x9) = tuple_example
print(x1,x2,x3,x4,x5,x6,x7,x8,x9)
# if L.H.S has less variables we can use the * operator and it will give a list
(x,y,*z)=tuple_example
(e,*r,t)=tuple_example
print(e,r,t)
print(x,y,z)

# looping in tuple is same as that in the list
# we also have the short hand for loop as in lists
[print("in the loop",x) for x in tuple_example]
#this is same as below
for x in tuple_example:
            print("in the loop",x)