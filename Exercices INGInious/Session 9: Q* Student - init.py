class Student:
    
    id = 0
    def __init__(self,firstname, surname, birthday, email):
        self.firstname = firstname
        self.surname = surname
        self.birthday = birthday
        self.email = email
        self.id = Student.id
        Student.id +=1
        
    def __str__(self):
        return "Student number {0}: {1} {2} born the {3}, can be \ 
        reached at {4}".format(self.id, self.firstname, self.surname, self.birthday, self.email)
