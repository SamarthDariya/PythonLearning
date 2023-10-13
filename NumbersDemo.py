#declaring
integer_example = 5 #int
float_example = 6.3 #float
complex_example = 5 +0j #complex
print(integer_example,float_example,complex_example)

#type function will return the type of the number(veriable in general)
print(type(integer_example),type(float_example),type(complex_example),type("string"))

#type conversion can be done by using int() float() complex()
# print(int(complex_example),float(complex_example)) #this will generate an error
print(int(float_example)) #this will simply return the floor of the number
