from turtle import circle


class Computers:
        company = "Dell"

        def __init__(self,model,processor,ram):
            self.model = model
            self.processor = processor
            self.ram = ram
        
        def run(self):
            print("running {} {} with {} and {}gb ram".format(self.company,self.model,self.processor,self.ram))
        
        def __del__(self):
            print("dismantelling the PC")
        

Samarth_PC = Computers("inspiron","i5","8")
Computers.company = "Asus"
print(Computers.company,Samarth_PC.company)
Samarth_PC.company = "Lenovo"
print(Computers.company,Samarth_PC.company)
Computers.company = "Dell"
print(Computers.company,Samarth_PC.company)

Samarth_PC.run()

class Father:

        def __init__(self):
                print("father initialized")


        def calling(self):
                print("father's calling")

class Mother:

        def __init__(self):
                print("Mother initialized")

        def calling(self):
                print("inside Mother's calling")

class Son(Father,Mother):
        def __init__(self):
                print("son initialized")
                super().__init__()
        def calling(self):
            print("samarth's calling")
            super().calling()

samarth = Son()
samarth.calling()
Mother.calling(samarth)

# super()
# The super() comes to a conclusion, 
# on which method to call with the help of 
# the method resolution order (MRO).
class Class1:
	def m(self):
         print("In class1")

class Class2(Class1):
	def m(self):
         print("In Class2")
         super().m()

class Class3(Class1):
	def m(self):
		print("In Class3")

class Class4(Class2, Class3):
	def m(self):
		print("In Class4") 
		super().m()
	
obj = Class4()
obj.m()

# har object ka ek MRO ban jaega aur jab apan super keyword lagaenge toh uske agle vale
# ko bulaya jaega not necessary jiske under super laga hai uska parent
# jis bhi object k liye bula rahe hai uska MRO dekhenge aur us hisab se resolve karenge

print("\nproperty vala section\n")

class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._dia = 2*radius

    @property
    def dia(self):
        print("getting dia")
        return self._dia

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    @dia.setter
    def dia(self,value):
        self._dia = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )

circle = Circle(9)
circle._radius = 34 # this is still working 
print(circle.radius)