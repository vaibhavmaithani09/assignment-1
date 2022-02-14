********************QUESTION1**********************************
# this a program to count no of occurrences of each word or character in the string entered by the user 
#defining a function to count the number of occurences of each word
def freq(str):
  str=str.split()
  str3=[]
  for i in str:
   if i not in str3:
    str3.append(i)
  for i in range(0,len(str3)):
    print("The frequency of",str3[i],"is",str.count(str3[i]))

user_str=input("Enter a string\n")
length=len(user_str.split())
if length>1:
  freq(user_str)
else:
  charr={i:user_str.count(i) for i in set(user_str)}
  print("the count of all characters in the given string is :\n",str(charr))

*******************************QUESTION 2*********************************************
 #this is a script to print next date of input date.

i=0
while i<1:
   date=int(input("enter the date (1-31)\n"))
   month=int(input("enter the month (1-12)\n")) 
   year=int(input("enter the year (1800-2025)\n"))
   print("the input date is",date,"/",month,"/",year)
 
   if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and date == 31 and (year<=2025 and year>=1800):
        print("the next date is", 1, "/", month+1, "/", year)
        break

   elif month == 12 and date == 31 and (year<=2025 and year>=1800):
        print("the next date is", 1, "/", 1, "/", year+1)
        break

   elif (month == 4 or month == 6 or month == 9 or month == 11) and date == 30 and (year<=2025 and year>=1800):
        print("the next date is", 1, "/", month+1, "/", year)
        break

   elif month == 2 and date == 28 and year%4 != 0 and (year<=2025 and year>=1800):
        print("the next date is", 1, "/", 3, "/", year)
        break

   elif month == 2 and date == 29 and year%4 == 0 and (year<=2025 and year>=1800):
        print("the next date is", 1, "/", 3, "/", year)
        break

   elif month == 2 and date > 29 and year%4 == 0 and (year<=2025 and year>=1800):
        print("wrong input")
        continue

   elif month == 2 and date > 28 and year%4 != 0 and (year<=2025 and year>=1800):
        print("wrong input")
        continue

   elif (month<=12 and month>=1) and (year<=2025 and year>=1800) and (date>=1 and date<=31):
        print("the next date is", date+1, "/", month, "/", year)
        break

   else:
        print("wrong input")
        continue











#***************************************************** QUESTION 3 ************************************************************

#this is a program to create a list of tuples with the first element as the number and Second element as the square of the number.

list1 = []      #creating an empty list
j = 0
while j<1:
    tn = input("Type 'y' to enter number / Type 'n' to cancel\n") #asking if user wants to enter the number or not
    if tn == 'n' or tn == 'N':
        break

    elif tn == 'y' or tn == 'Y':
        num = int(input("Enter the number\n"))
        list1.append(num)          #adding the number to list1
        continue

    else:
        print("Wrong input, please try again")
        continue

print("Numbers you entered are :", list1)
list2 = [(i, i*i) for i in list1]        #creating another list with original number and its square for numbers which are present in list 1
print("Given number, square of that number :", list2)










#***************************************************** QUESTION 4 ************************************************************

#this is a program to prompt the user for a grade between 4 and 10

grade = int(input("Please enter the grade (4-10)\n"))
if grade == 10:
    print("Your Grade is ‘A+’ and Outstanding Performance.\n")
elif grade == 9:
    print("Your Grade is ‘A’ and Excellent Performance.\n")
elif grade == 8:
    print("Your Grade is ‘B+’ and Very Good Performance.\n")
elif grade == 7:
    print("Your Grade is ‘B’ and Good Performance.\n")
elif grade == 6:
    print("Your Grade is ‘C+’ and Average Performance.\n")
elif grade == 5:
    print("Your Grade is ‘C’ and Below Average Performance.\n")
elif grade == 4:
    print("Your Grade is ‘D’ and Poor Performance.\n")
else:
    print("Error, grade is out of range, please enter grade between 4 to 10\n")










#***************************************************** QUESTION 5 ************************************************************

#this is a program to write alphabets in a reverse pyramid pattern
n=6
for i in range(0,n):
    for j in range(0,i):
        print(' ', end='')
    for j in range(0, 2*(n-i)-1):
        print(chr(65+j), end='')
    print()








#***************************************************** QUESTION 6 ************************************************************

#this is a python script that repeatedly ask user to enter name and SID of students (use ‘Y’ or ‘N’) and store them in a dictionary whose keys are SID’s and
#values are student’s name.

dict1 = {}
i = 0
while i < 1:
    tn = input("Type 'y' to enter Name and SID / Type 'n' to cancel\n")
    if tn == 'n' or tn == 'N':
        break

    elif tn == 'y' or tn == 'Y':
        sid = input("Enter the SID\n")
        name = input("Enter the Name\n")
        dict1.update({sid: name})
        continue

    else:
        print("wrong input, please try again")
        continue

print(dict1)
sortedbykey = {k: v for k, v in sorted(dict1.items())}
sortedbyval = {k: v for k, v in sorted(dict1.items(), key=lambda v: v[1])}

print("Dictionary after sorting it by key is :", sortedbykey)
print("Dictionary after sorting it by value is :", sortedbyval)

studentfind = input("Enter the student's SID which you want to find\n")
print("Name of the student whose SID is", studentfind, "is", dict1.get(studentfind))









#***************************************************** QUESTION 7 ************************************************************

#this is a program to print Fibonacci sequence and also print average of the resultant Fibonacci series.

def fibo(n):         #defining the fibonacci sequence function, each term is the sum of its previous two terms
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

nterms = int(input("Enter the number of terms you want to print in the fibonacci sequence\n"))
list1 = []        #creating an empty list to add fibonacci sequence into it

if nterms <= 0:        # check if the number of terms is valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       list1.append(fibo(i))

print(list1)
average = sum(list1)/nterms
print("The average of fibonacci sequence upto",nterms, " terms is", average)









#***************************************************** QUESTION 8 ************************************************************

set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

print("Set of all elements that are in Set1 and Set2 but not in both is", set1.union(set2).difference(set1.intersection(set2)))
           #new set of all elements that are in Set1 and Set2 but not both.


universal = set1.union(set2.union(set3))
set1_inter_set2 = set1.intersection(set2)
set2_inter_set3 = set2.intersection(set3)
set1_inter_set3 = set1.intersection(set3)
one_of_3_sets = universal.difference(set1_inter_set2).difference(set2_inter_set3).difference(set1_inter_set3)
           #new set of all elements that are in only one of the three sets Set1, Set2 and Set3.
print("Set of all elements that are in only one of the three sets Set1, Set2 and Set3 is", one_of_3_sets)


two_of_3_sets = universal.difference(one_of_3_sets)
           #new set of elements that are exactly two of the sets Set1, Set2 and Set3.
print("Set of elements that are exactly two of the sets Set1, Set2 and Set3 is", two_of_3_sets)


set4 = {1,2,3,4,5,6,7,8,9,10}
not_in_set1 = set4.difference(set1)
          #new set of all integers in the range 1 to 10 that are not in Set1.
print("Set of all integers in the range 1 to 10 that are not in Set1 is", not_in_set1)


not_in_universal = set4.difference(universal)
          #new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3.
print("set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3 is", not_in_universal)

