***question1

num1=int(input("enter the value of first no \n"))
num2=int(input("enter the value of second no \n"))
num3=int(input("enter the value of third no \n"))
avg=(num1+num2+num3)/3
print("the average of these three nos is",avg)
#formula for average of three numbers a,b,c =(a+b+c)/3

***question2

#This is a programm to comput a person's income tax
dependents= int(input("enter number of dependents\n"))
gross_income = float(input("Enter the gross income\n"))
taxable_income= float(gross_income-10000-(3000*dependents))
income_tax=0.2*taxable_income
print("Your net income tax is",income_tax)

***question3

#This is a program to store different data types value into a list
SID = int(input("Enter your SID\n"))
name = input("Enter your name\n")
gender = input("Enter your gender , Use Gender values : 'F' , 'M' , 'U' (For unknown)\n")
course_name = input("Enter your course name\n")
CGPA = float(input("Enter your CGPA\n"))
student = [SID , name  , gender , CGPA]
print(student)

***question4

student1=int(input("enter marks of first student\n"))
student2=int(input("enter marks of second student\n"))
student3=int(input("enter marks of third student\n"))
student4=int(input("enter marks of fourth student\n"))
student5=int(input("enter marks of fifth student\n"))
markslist=[student1,student2,student3,student4,student5]
markslist.sort()
print(markslist)

***question5

color=["red","green","white","black","pink","yellow"]
color.remove("black")
print(color)
color1 =["red","green","white","black","pink","yellow"]
color1[3:5] =["purple"]
print(color1)
