#first type
# class studentdetails:
#     no_of_students = 26
#     pass
# kaushik_dhar=studentdetails() # object of the class student details
# rahul_dutta=studentdetails()
# ashish_paul=studentdetails()
#
# kaushik_dhar.age=20 # defining the value of every objects. which is called inheritance
# kaushik_dhar.roll=1
# kaushik_dhar.parent="Soma Dhar"
#
# rahul_dutta.age=21
# rahul_dutta.roll=2
# rahul_dutta.parent="Subhasis Dutta"
#
# ashish_paul.age=24
# ashish_paul.roll=18
# ashish_paul.parent="Roma Paul"

#now printing the objects value which i want to know

# print(f"Your roll is {kaushik_dhar.roll} and the total number of students are {studentdetails.no_of_students}")

#second type
# class studentdetails:
#     no_of_students = 26
#
#     # to initialize the values where the self will get the variable object name and the other will be defined as the values
#     def __init__(self,now_age,now_roll,parent_name):
#         self.age=now_age
#         self.roll=now_roll
#         self.parent=parent_name
#     def print_details(self):
#         return f"Your age is {self.age}\nYour roll number is {self.roll}\nYour parent's name is {self.parent}"
#
# kaushik_dhar=studentdetails(20,1,"Soma Dhar")
# rahul_dutta=studentdetails(21,2,"Subhasis Dutta")
# ashish_paul=studentdetails(24,18,"Roma Paul")
#
# print(rahul_dutta.print_details())

class studentdetails:
    no_of_students = 26

    # to initialize the values where the self will get the variable object name and the other will be defined as the values
    def __init__(self,now_age,now_roll,parent_name):
        self.age=now_age
        self.roll=now_roll
        self.parent=parent_name

    def print_details(self):
        return f"Your age is {self.age}\nYour roll number is {self.roll}\nYour parent's name is {self.parent}\n"
    #class as the alternative construction
    @classmethod
    def from_slash(cls,string): #if any value is derived as a string then it initialize class value then the string value
     soma=string.split("/") # it will split the string by /
     return cls(soma[0],soma[1],soma[2]) # return the derived string values from the position value as a class then it will send the value to the student details function
    @staticmethod
    def printgood(string):
        return f"This is good {string}\n"
kaushik_dhar=studentdetails(20,1,"Soma Dhar")
rahul_dutta=studentdetails(21,2,"Subhasis Dutta")
ashish_paul=studentdetails(24,18,"Roma Paul")
kamal_dhar=studentdetails.from_slash("42/19/Arati Dhar")
print(kamal_dhar.print_details())
print(studentdetails.printgood("programme"))
