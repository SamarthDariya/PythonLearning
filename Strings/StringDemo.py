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


    # capitalize()	Converts the first character to upper case
    # casefold()	Converts string into lower case
    # center()	Returns a centered string
    # count()	Returns the number of times a specified value occurs in a string
    # encode()	Returns an encoded version of the string
    # endswith()	Returns true if the string ends with the specified value
    # expandtabs()	Sets the tab size of the string
    # find()	Searches the string for a specified value and returns the position of where it was found
    # format()	Formats specified values in a string
    # format_map()	Formats specified values in a string
    # index()	Searches the string for a specified value and returns the position of where it was found
    # isalnum()	Returns True if all characters in the string are alphanumeric
    # isalpha()	Returns True if all characters in the string are in the alphabet
    # isascii()	Returns True if all characters in the string are ascii characters
    # isdecimal()	Returns True if all characters in the string are decimals
    # isdigit()	Returns True if all characters in the string are digits
    # isidentifier()	Returns True if the string is an identifier
    # islower()	Returns True if all characters in the string are lower case
    # isnumeric()	Returns True if all characters in the string are numeric
    # isprintable()	Returns True if all characters in the string are printable
    # isspace()	Returns True if all characters in the string are whitespaces
    # istitle()	Returns True if the string follows the rules of a title
    # isupper()	Returns True if all characters in the string are upper case
    # join()	Converts the elements of an iterable into a string
    # ljust()	Returns a left justified version of the string
    # lower()	Converts a string into lower case
    # lstrip()	Returns a left trim version of the string
    # maketrans()	Returns a translation table to be used in translations
    # partition()	Returns a tuple where the string is parted into three parts
    # replace()	Returns a string where a specified value is replaced with a specified value
    # rfind()	Searches the string for a specified value and returns the last position of where it was found
    # rindex()	Searches the string for a specified value and returns the last position of where it was found
    # rjust()	Returns a right justified version of the string
    # rpartition()	Returns a tuple where the string is parted into three parts
    # rsplit()	Splits the string at the specified separator, and returns a list
    # rstrip()	Returns a right trim version of the string
    # split()	Splits the string at the specified separator, and returns a list
    # splitlines()	Splits the string at line breaks and returns a list
    # startswith()	Returns true if the string starts with the specified value
    # strip()	Returns a trimmed version of the string
    # swapcase()	Swaps cases, lower case becomes upper case and vice versa
    # title()	Converts the first character of each word to upper case
    # translate()	Returns a translated string
    # upper()	Converts a string into upper case
    # zfill()	Fills the string with a specified number of 0 values at the beginning

#reference W3schhol python tutorial and python official documentation