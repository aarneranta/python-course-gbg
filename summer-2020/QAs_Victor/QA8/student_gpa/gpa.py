# gpa.py
#    Program to find student with highest GPA

class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

    def addGrade(self,gradePoint,credits):
        self.qpoints = self.qpoints + (gradePoint * credits)
        self.hours = self.hours + credits

def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def main():
    test=Student("test",0,0)

    test.addGrade(4,5)
    test.addGrade(3,10)
    print(test.gpa())


if __name__ == '__main__':
    main()
