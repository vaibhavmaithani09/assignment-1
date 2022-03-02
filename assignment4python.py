#****************************************************** QUESTION 1 *********************************************************
#this is a recursive python function to solve the problem of tower of Hanoi with three disks.
def hanoitower(n, initial, final, auxiliary):
    if n == 1:
        print("Move disk 1 from source", initial, "to", final)
    else:
        hanoitower(n - 1, initial, auxiliary, final)
        print("Move disk", n, "from source", initial, "to", final)
        hanoitower(n - 1, auxiliary, final, initial)


n = 4
hanoitower(n, 'A', 'B', 'C')      # A, B, C are the name of rods




#****************************************************** QUESTION 2 *********************************************************
#this is a program to print pascal's triangle for given number of rows
#USING RECURSIVE PROCEDURES
rows = int(input("Enter number of rows you want to print in Pascal's Triangle using recursive approach\n"))

def pascal(n):
    if n == 0:
        print("Please enter a positive value")
        return []
    elif n == 1:
        return [[1]]
    else:
        next_row = [1]
        result = pascal(n-1)
        previous_row = result[-1]

        for loop in range(len(previous_row) - 1):
            next_row.append(previous_row[loop] + previous_row[loop+1])

        next_row += [1]
        result.append(next_row)

        return result

print("The Pascal Triangle by using recursive method is :")
output = pascal(rows)
for i in range(rows):        # to display the output in the given pattern.
    for j in range(rows-i-1):
        print(format(" ", "<2"), end="")
    for j in range(i+1):
        print(format(output[i][j], "<3"), end=" ")
    print()

#USING ITERATIVE APPROACH
from math import factorial

n = int(input("Enter number of rows you want to print in Pascal's Triangle using iterative approach\n"))
for i in range(n):
    for j in range(n - i + 1):        # for left spacing
        print(end=" ")

    for j in range(i + 1):            # nCr = n!/((n-r)!*r!)
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()           #new line






#****************************************************** QUESTION 3 *********************************************************
dividend = int(input("Enter the dividend :\n"))
divisor = int(input("Enter the divisor :\n"))
quotient, remainder = divmod(dividend, divisor)
print("The quotient is", quotient, "and the remainder is", remainder)

print("The statement that divmod function is callable is", callable(divmod(dividend, divisor)),".")
print("The statement that quotient is callable is", callable(quotient), "and the statement that remainder is callable is", callable(remainder), ".")
print("The statement that dividend is callable is", callable(dividend), "and the statement that divisor is callable is", callable(divisor), ".")

zero_or_not = {quotient: "Quotient", remainder: "Remainder"}
check = all(zero_or_not)
print("The values we have are :", zero_or_not)
if check:
    print("The quotient and remainder are non zero values.")
else:
    print("The quotient or remainder or both are zero.")

lst = [4,5,6]
lst.append(remainder)
lst.append(quotient)
print("Adding values (4, 5, 6) to the result and filtering out the values which are greater than 4.")
result = []
for i in lst:
    if i>4:
        result.append(i)
print(result)
print("Converting it into set datatype")
set1 = set(result)
print(set1)
print("Making the set immutable")
new_set = frozenset(set1)
print(new_set)
print("The maximum value from set is", max(new_set))       #finding maximum value from the set
print("Its hash value is", hash(new_set))      #hash value of the set






#****************************************************** QUESTION 4 *********************************************************
#this is a class to assign values for name and roll number.
class student:
    count = 0
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        student.count += 1

    def displaydetails(self):
        print("Name:", self.name, ", Roll number:", self.roll_number)

s1 = student("Aaersh Kumar", 21103037)
s2 = student("Chirag", 21110332)
s3 = student("Manoj", 21102044)
s4 = student("Hammad", 21712336)
s1.displaydetails()
s2.displaydetails()
s3.displaydetails()
s4.displaydetails()
del(s2)
print("After deletion:")
s1.displaydetails()
s3.displaydetails()
s4.displaydetails()






#****************************************************** QUESTION 5 *********************************************************
#this is a program to store details of employees: name and salary using class
class Employee:
    count = 0

    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def displayDetails(self):
        print("Name:", self.name, ", Salary:", self.salary)


e1 = Employee("Mehak", 40000)
e2 = Employee("Ashok", 50000)
e3 = Employee("Viren", 60000)
print(f"There are {Employee.count} employees")
print("Details of all employee:")
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()

e1.salary = 70000
del e3
print("After updation:")
print(f"There are {Employee.count - 1} employees")
print("Details of all employee:")
e1.displayDetails()
e2.displayDetails()






#****************************************************** QUESTION 6 *********************************************************
print("Question number 6")
#input first word
word = input("Enter the first word: ")

#input a meaningful word with the exact same letters
testword = input("\nEnter a new meaningful word with the exact same letters : ")

#defining dictionary from last assignment
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

# verifing the letters of the new word
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")

#shopkeeper's input to verify the word
def userinput():
    ans = input("\nDoes the word makes sense?(y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test\n")
    elif ans == 'n':
        print("The word doesn't have a meaning,i.e. friendship is fake..\n")
    else:
        print("Invalid input, try again")
        userinput()
userinput()
