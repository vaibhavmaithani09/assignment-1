***question1***
inputstring="Python is a case sensitive language."
print("length of the input string is",len(inputstring))
print(inputstring[::-1])
newstring=inputstring[10:26]
print(newstring)
print(inputstring.replace("a case sensitive","object oriented"))
print("index of a in input string is ",inputstring.index("a"))
print(inputstring.replace(" "," "))

***question2***
name="Vaibhav Maithani"
sid="21103048"
department="Computer Science and Engineering"
cgpa="9.8"
print("hey,",name,"here!\nMy sid is",sid,"\nI am from",department,"department and my cgpa is",cgpa)

***question3***
a=56
b=10
print("a&b is",a&b)
print("a|b is",a|b)
print("a^b is ",a^b)
print("left shifting both a and b with two bits gives a=",a<<2," and b=",b<<2)
print("right shifting a with 2 bits and b with 4 bits gives a=",a>>2,"and b=",b>>4)

***question 4***
#program to find greatest no in three nos entered by user
num1=int(input("enter first number\n"))
num2=int(input("enter second number\n"))
num3=int(input("enter third number\n"))
if num1>num2:
  if num1>num3:
    print("the greatest of three nos is ",num1)
  else:
     print("the greatest of three nos is ",num3)
else:
 if num2>num3:
   print("the greatest of three nos is",num2)
 else:
   print("the greatest of three nos is",num3)



***question5***
s=input("enter a string") 
if 'name' in s:
  print("yes")
else:
  print("no")



***question6***
#program to check whether given lengths form a triangle or not
a=int(input("enter length of first side\n"))
b=int(input("enter length of second side\n"))
c=int(input("enter length of third side\n"))
if a+b>=c and b=c>=a and a+c>=b:
  print("yes, triangle can be formed.")
else:
  print("no,triangle cannot be formed.")

