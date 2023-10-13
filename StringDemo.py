#declaring a string
single_line_string = "This is a single line string"
multiple_line_string = '''This is a multiple line string
isn't it'''

example_string = "this is a example string"

#strings can be used as an array indexed like them 
print(example_string[3])

#length of the string can be given by len()
print(len(example_string))

#check if some string is in the other string or not
print("example" in example_string) 
print("example" not in example_string)

#strings can be sliced in many ways
print(example_string[3:11]) #slice from one position to another position (end not included)
print(example_string[:11]) #slice from start to a given position (end not included)
print(example_string[3:]) #slice from given position to the end
print(example_string[-8:-3]) #slicing by using negative positions (starting position not included)


#the below functions works as their namesake they return a new string
print(example_string.upper())
print(example_string.lower())
print(example_string.replace('s','W'))
s = "     whitespaces will be removed    "
print(s.strip())

#original string remains the same
print(example_string,s)

#split() method returns list of string by given character
print(example_string.split(" "))


# todo write on format strings
format_example = "when print directly nothing happens but using format the variable will appear {}"
print(format_example.format("see the variable is appearing"))
#original string remains unchanged
print(format_example)
#formatting can be indexed 
format_example_2 = "my name is {1}, my surname is {2}, i work at {0}"
print(format_example_2.format("an it company","samarth","dariya"))

#all strings method returns a new string and do not change the original string
