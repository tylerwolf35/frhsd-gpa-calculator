# GPA Calculator (FRHSD) by Tyler Wolf

print("Calculate your GPA on the FRHSD scale. If there are more courses\nthen you have just input '0' for both values.\n")

q1 = float(input("What is the weight of the grade? ")) 
tc1 = float(input("How many credits is it worth? "))
qp1 = q1*tc1

q2 = float(input("What is the weight of the grade ?"))
tc2 = float(input("How many credits is it worth? "))
qp2 = q2*tc2

q3 = float(input("What is the weight of the grade? "))
tc3 = float(input("How many credits is it worth? "))
qp3 = q3*tc3

q4 = float(input("What is the weight of the grade? "))
tc4 = float(input("How many credits is it worth? "))
qp4 = q4*tc4

q5 = float(input("What is the weight of the grade? "))
tc5 = float(input("How many credits is it worth? "))
qp5 = q5*tc5

q6 = float(input("What is the weight of the grade? "))
tc6 = float(input("How many credits is it worth? "))
qp6 = q6*tc6

q7 = float(input("What is the weight of the grade? "))
tc7 = float(input("How many credits is it worth? "))
qp7 = q7*tc7

q8 = float(input("What is the weight of the grade? "))
tc8 = float(input("How many credits is it worth? "))
qp8 = q8*tc8

TQP = qp1+qp2+qp3+qp4+qp5+qp6+qp7+qp8
TCA = tc1+tc2+tc3+tc4+tc5+tc6+tc7+tc8

GPA = TQP/TCA

print("Your GPA is: ",GPA)
