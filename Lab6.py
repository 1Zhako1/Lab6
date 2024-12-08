 import pickle
 class Course_Grade:
   def __init__(self):
     course.name = ""
     stu_ID = []
     grades = []

     #course.name = "OOP"
     #stu_ID = [107, 24, 108]
     #grades = [100, 100, 100]
  def get details(self):
        self.course_name = input("Enter the name of the course: ")
        for i in range(0,4):
            self.stu_ID.append(input("Enter the name of the course: "))
        for i in range(0,4):
            self.grades.append(input("Enter the grades: "))
   def display(self):
       print("Name of the course:", self.course_name)
       print("Student ID:", self.stu_ID)
       print("Student's grades:", self.grades)

data = pickle.load(f)
print(data.name)
print(data.stu_ID)
print(data.grades)
except (EOFError):
break
f.close()

#Objects
course1 = Course_Grade()
course1.get_details()

course2 = Course_Grade()
course2.get_details()

course3 = Course_Grade()
course3.get_details()

course4 = Course_Grade()
course4.get_details()

#Write the objects into a *dat.file
#f = open('myCourse_Grade.dat', 'rb')
f=open('myCourseGrade.dat', 'ab')
pickle.dump(course1, f)
pickle.dump(course2,f)
pickle.dump(course3,f)
pickle.dump(course4,f)
f.close()
#use iterations to read the objects from the file and print the attributes of the class
while 1:
try:
data = pickle.load(f)
print(data.name)
print(data.dob)
print(data.courses)
except (EOFError):
break
f.close()

with open("zz1.txt", 'a') as f:
for key, value in dict_users.items():
f.write('%s:%s\n' % (Course_Grade, value))
with open("zz1.txt",'r') as f:
data = f.read()
print(data)