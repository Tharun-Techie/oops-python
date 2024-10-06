class Student:
    def __init__(self,name,eng,mat,sci,soc,tam):
        self.Name = name
        self.Marks_tam = tam
        self.Marks_mat = mat
        self.Marks_soc = soc
        self.Marks_sci = sci
        self.Marks_eng = eng
        
st1 = Student("Rajesh",56,85,52,82,52)
st2 = Student("Ramenh",78,84,69,39,52)
st3 = Student("chethan",56,65,69,24,52)
st4 = Student("suresh",56,84,72,45,52)
st5 = Student("jeevith",56,52,69,25,52)
st6 = Student("venkat",56,84,69,8,52)
st7 = Student("prahalad",56,84,58,74,52)
st8 = Student("prajwal",56,84,69,43.,52)
st9= Student("pretham",56,28,57,35,52)
st10 = Student("shashank",56,84,69,5,52)


students = [st1,st2,st3,st4,st5,st6,st7,st8,st9,st10]

for student in students:
    print(student.Name)