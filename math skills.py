import random
from operator import add, sub, mul, truediv
import sys

title = "** This Program Tests Primary School Childrens' Math Skills **"
print("*" * len(title))
print(title)
print("*" * len(title))
file = open("Results.txt","w")
file.write("Student ID\tQuestion ID\tQuestion\tRight Answer\tGiven Answer\t ")
file.write("\n")
file.write("----------      ----------      ----------      ----------      -----------")



def student_ID():
    global ID
    liste = []
    for a in range(99,1000):
        liste.append(str(a))

    ID =input("Enter the Student ID: ")
    if ID in liste:
        question(1)
    else:
        print("Please enter 3-digit number!")
        student_ID()


def question (z):
    
        ops = ['+','-','*','/']
        op = random.choice(ops)
        x = random.randint(1,101)
        y = random.randint(1,101)

        if op == '+':
            print("What is", x, "+",y, "? ")
            student_answer = float(input())
            right_answer = (x+y)
            
        elif op == '-':
            print("What is", x, "-", y, "? ")
            student_answer = float(input())
            right_answer = (x-y)
            
        elif op == '*':
            print("What is", x, "x", y, "? ")
            student_answer = float(input())
            right_answer = (x*y)
            
        elif op == '/':
            print("What is", x, "/", y, "? ")
            student_answer = float(input())
            right_answer = (x/y)
        file.write("\n{}".format(ID))
        file.write("\t\t{}".format(z))
        file.write("\t\t{}{}{}".format(x,op,y))
        file.write("\t\t{}".format(right_answer,".2f"))
        file.write("\t\t{}".format(student_answer))

        if right_answer == student_answer :
            print("Congrats it's true. :)")
            new_question=input("Next question(y/n) : ")
            if new_question=='y':
                question(z+1)
            elif new_question=='n':
                next_student=input("Do you want the next student(y/n) : ")
                if next_student=='y':
                    student_ID()
                elif next_student=='n':
                    print("Program is closing!")
                    file.close()
                    sys.exit()

        else:
            print("Wrong answer")
            new_question=input("Next question(y/n) : ")
            if new_question=='y':
                question(z+1)
            elif new_question=='n':
                next_student=input("Do you want the next student(y/n) : ")
                if next_student=='y':
                    student_ID()
                elif next_student=='n':
                    print("Program is closing! GOOD BYE!")
                    file.close()
                    sys.exit()
        
        

student_ID()        
