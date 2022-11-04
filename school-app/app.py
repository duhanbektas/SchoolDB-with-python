from dbmanager import DbManager
from Student import Student
import datetime

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Student List\n2-Add Student\n3-Edit Student\n4-Delete student\n5-Add Teacher\n6-Lessons for Classes\n7-Exit(y/n)"
        while True:
            print(msg)
            option = input("Option: ")
            if option == '1':
                self.displayStudents()
            elif option == '2':
                self.addStudent()
            elif option == '3':
                self.editStudent() 
            elif option == '4':
                self.deleteStudent() 
            elif option == 'y':
                break
            else:
                print('Wrong Choice')


    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Student ID: '))

        self.db.deleteStudent(studentid)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Student ID: '))

        student = self.db.getStudentById(studentid)

        student[0].name = input('name:') or student[0].name
        student[0].surname = input('surname:') or student[0].surname
        student[0].gender = input('Gender (M/F):') or student[0].gender
        student[0].classid = input('class: ') or student[0].classid

        year = input("year: ") or student[0].birthdate.year
        month = input("month: ") or student[0].birthdate.month
        day = input("day: ") or student[0].birthdate.day

        student[0].birthdate = datetime.date(year,month,day)
        self.db.editStudent(student[0]) 


    def addStudent(self):
        self.displayClasses()
        
        classid = int(input('class: '))
        number = input('no: ')
        name = input('name')
        surname = input('surname')
        year = int(input('year'))
        month = int(input('month'))
        day = int(input('day'))
        birthdate = datetime.date(year,month,day)
        gender = input('Gender (M/F)')

        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}: {c.name}')

    def displayStudents(self):       
        self.displayClasses()
        classid = int(input('hangi sınıf: '))

        students = self.db.getStudentsByClassId(classid)
        print("Öğrenci Listesi")
        for std in students:
            print(f'{std.id}-{std.name} {std.surname}')

        return classid

    



app = App()     
app.initApp()
