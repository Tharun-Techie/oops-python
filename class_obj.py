class Human:
    #States
    Name = None
    Age = None
    Weight = None
    Height = None   
    
    #behaviours
    def run(self):
        print(self.Name + " Bro can run Faster than Light")
    
person1 = Human()
person1.Name = "Rajan"
person1.Age=29
person1.Weight = 78
person1.Height = "112 cm"

print(person1.Name)
print(person1.Age)
print(person1.Height)
print(person1.Weight)
person1.run()


dicr = {"Name":"Tharun R"}

print(dicr["Name"])