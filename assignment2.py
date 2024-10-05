class Student:
    def __init__(self,name,eng,mat,sci,soc,tam):
        self.Name = name
        self.Marks_tam = tam
        self.Marks_mat = mat
        self.Marks_soc = soc
        self.Marks_sci = sci
        self.Marks_eng = eng
        
st1 = Student("Rajesh",56,84,69,100,52)
print(st1.Name)
print(st1.Marks_eng)
print(st1.Marks_mat)
print(st1.Marks_sci)
print(st1.Marks_soc)
print(st1.Marks_tam)