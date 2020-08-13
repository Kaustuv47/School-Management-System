from Student import Student
from ClearScreen import ClearScreen
class Admin(Student):

    def __init__(self):
        super(Admin,self).__init__()
        choice = True
        while(choice):
            choice =int(input("Enter Choice\n1: Add Student\n2: Display Student Data\n3: Exit\n"))
            if choice == 1:
                super(Admin,self).enterStudentDetails()
            elif choice == 2:
                super(Admin,self).viewStudentDetail()
            elif choice == 3:
                break
            else:
                print("Wrong Choice! Try again")
            ClearScreen()


ob = Admin()
