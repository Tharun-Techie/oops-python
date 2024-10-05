class Student:
    Name = None
    Marks_tam = None
    Marks_mat = None
    Marks_soc = None
    Marks_sci = None
    Marks_eng = None
    
    def Tmarks(self):
        total = (self.Marks_eng+self.Marks_mat+self.Marks_sci+self.Marks_soc+self.Marks_tam)
        #print("Total Marks: "+ str(self.Marks_eng+self.Marks_mat+self.Marks_sci+self.Marks_soc+self.Marks_tam))
       # print("Highest Marks: "+ str(max(self.Marks_eng,self.Marks_mat,self.Marks_sci,self.Marks_soc,self.Marks_tam)))
        return self.Name , str(total)
    
    
    
stu1 = Student()
stu1.Marks_eng = 60
stu1.Marks_mat = 70
stu1.Marks_sci = 66
stu1.Marks_soc = 76
stu1.Marks_tam = 88
stu1.Tmarks()

stu2 = Student()
stu2.Marks_eng = 60
stu2.Marks_mat = 70
stu2.Marks_sci = 66
stu2.Marks_soc = 76
stu2.Marks_tam = 88
stu2.Tmarks()

stu3 = Student()
stu3.Marks_eng = 60
stu3.Marks_mat = 70
stu3.Marks_sci = 66
stu3.Marks_soc = 76
stu3.Marks_tam = 88
stu3.Tmarks()

stu4 = Student()
stu4.Marks_eng = 60
stu4.Marks_mat = 70
stu4.Marks_sci = 66
stu4.Marks_soc = 76
stu4.Marks_tam = 88
stu4.Tmarks()

stu5 = Student()
stu5.Marks_eng = 60
stu5.Marks_mat = 70
stu5.Marks_sci = 66
stu5.Marks_soc = 76
stu5.Marks_tam = 88
stu5.Tmarks()

stu6 = Student()
stu6.Marks_eng = 60
stu6.Marks_mat = 70
stu6.Marks_sci = 66
stu6.Marks_soc = 76
stu6.Marks_tam = 88
stu6.Tmarks()

stu7 = Student()
stu7.Marks_eng = 60
stu7.Marks_mat = 70
stu7.Marks_sci = 66
stu7.Marks_soc = 76
stu7.Marks_tam = 88
stu7.Tmarks()

stu8 = Student()
stu8.Marks_eng = 60
stu8.Marks_mat = 70
stu8.Marks_sci = 66
stu8.Marks_soc = 76
stu8.Marks_tam = 88
stu8.Tmarks()

stu9 = Student()
stu9.Marks_eng = 60
stu9.Marks_mat = 70
stu9.Marks_sci = 66
stu9.Marks_soc = 76
stu9.Marks_tam = 88
stu9.Tmarks()

stu10 = Student()
stu10.Marks_eng = 60
stu10.Marks_mat = 70
stu10.Marks_sci = 66
stu10.Marks_soc = 76
stu10.Marks_tam = 88
stu10.Tmarks()

print("Highest Marks Scored Student:"+ max(stu1.Tmarks(),stu2.Tmarks(),stu3.Tmarks(),stu4.Tmarks(),stu5.Tmarks(),stu6.Tmarks(),stu7.Tmarks(),stu8.Tmarks(),stu9.Tmarks(),stu10.Tmarks()))
print("Highest Marks Scored :"+ max(stu1.Tmarks(),stu2.Tmarks(),stu3.Tmarks(),stu4.Tmarks(),stu5.Tmarks(),stu6.Tmarks(),stu7.Tmarks(),stu8.Tmarks(),stu9.Tmarks(),stu10.Tmarks()))