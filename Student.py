import sys

class error(Exception):
    pass
class RollNotExist(error):
    pass
class RollAlreadyExist(error):
    pass

class Student:
    def __init__(self):
        self.path = sys.path[0]

    def enterStudentDetails(self):
        name = input("Enter Name ")
        clas=input("Enter Class ")
        path = self.path+"/StudentData/Class"+clas+".txt"
        f = open(path,"a")
        roll = input("Enter Roll no. ")
        with open(path) as file:
            lines = file.read().split("-")
            for i in lines:
                try:
                    if (("Roll = "+roll) in i):
                        raise RollAlreadyExist()
                except RollAlreadyExist:
                    print("Roll already exist enter different roll")
                    roll = input("Enter Roll no. ")
        section = input("Enter Section ")


        print("Do you want to save this to File")
        choice = input("Y or N")
        if(choice=='Y' or choice=='y'):
            path =""
            path = self.path+"/StudentData/Class"+clas+".txt"
            writefile = open(path,"a")
            writefile.write("Roll = "+roll+"\n")
            writefile.write("Name = "+name+"\n")
            writefile.write("Section = "+section+"\n")
            writefile.write("-\n")
            writefile.close()
        else:
            print("Discarding Change")


    def viewStudentDetail(self):
        clas = input("Enter Class")
        lines = ""
        try:
            path = self.path+"/StudentData/Class"+clas+".txt"
            with open(path) as file:
                lines = file.read().split("-")

        except FileNotFoundError:
            print(" No such class created, Try again")


        roll = input("Enter Roll no.")
        try:
            for i in lines:
                if ("Roll = "+roll) in i:
                    print(i)
                raise RollNotExist()
        except RollNotExist:
            print(" Roll number entered not exist")



