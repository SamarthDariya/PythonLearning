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

