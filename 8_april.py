# range(10)
# range(1,15)
# range(0,10,3)

# for i in range(100,0,-1):
# 	print(i,end="")

#even number from 10 to 30
# for i in range(10,31,):
# 	if i%2 ==0:
# 		print(i)



#print the leap year from 1947 to till now
# c = 0
# for i in range(1947,2025):
# 	if i%4==0:
# 		print("Leap year :- ",i)	
# 		c = c+1
# print("total Number of leap year :-",c)	


# # print the table with the help of user input
# x = int(input("enter the table name :-"))

# for i in range(1,11):
# 	print(i*x)
# 	print(f"{x} X {i} = {i*x}")		



# write a program to show the factorial of any number with the
# help of user input.

# fact = 1
# x = int(input("enter the number :-"))
# for i in range (1,x+1):
# 	fact = fact * i 

# print("the factorial of",x,"is:",fact)


# print the reverse counting from 50 to 10
# for i in range(50,9,-1):
# 	print(i)

# # print the reverse counting from 100 to 50 and stepsize should be 5
# for i in range(100,49,-5):
# 	print(i)



# x = "Himachal Pradesh"
# # while loop
# y = len(x)
# z = 0
# while y>z:
# 	print(x[z])
# 	z = z+1



# #for loop

# for i in x:
# 	print(i)



import time

# for i in range(10):
# 	print(i)
# 	time.sleep(1)



# for i in range(30,0,-1):
# 	print(i,end="\r")
# 	time.sleep(1)


#escape function

# print("Hello\tworld") #tab 
# print("Hello\nworld") #new line
# print("Hello\rworld") #replace


# print the each alphabet of "hello World"
# with the help of for loop

# x = "Hello World"
# for i in x:
#  	print(i)


# print 10time your name with the help of for loop


# for i in range(10):
# 	print("Shashank Gupta")

# x = "Shashank Gupta"
# for i in range(10):
# 	print("-------------")
# 	print(x,"✌")
# 	print("------------")	


# break 
# continue

# for i in range(1,1000):
# 	if i==50:
# 		break
# 	else:
# 		print(i)



# for i in range(1,15):
# 	if i==5 or i==10:
# 		continue
# 	else:
# 		print(i)	



# write a python program to print the number from 4 to 50 and exclude all
# the number who is divisible of 5 and 10

# for i in range(4,51):
# 	if i%5==0 or i%10==0:
# 		continue
# 	else:
# 		print(i)



# for i in range(4,51):
# 	if i%5==0 or i%10==0:
# 		pass
# 	else:
# 		print(i)



# Count the total number of even number from 1 to 20
# Find the sum o first 10 Number
# Find the sum of first 10 even Number
# count total number from 10 to 30 who is divisible of
# 2 and 3 

# count = 0
# for i in range(1,21):
# 	if i%2 ==0:
# 		print(i)

# 		count +=1

# print("the count of even numbers is:",count)		
	


# sum_numbers = 0
# for i in range(1, 11):
#     sum_numbers += i

# print("Sum of the first 10 numbers is:", sum_numbers)


# sum_even_numbers = 0
# for i in range(2,21,2):
# 		sum_even_numbers += i 

# print("Sum of the first 10 even numbers:", sum_even_numbers)



# count = 0
# for i in range(10,31):
# 	if i%2==0 and i%3==0:
# 		print(i)

# 		count += 1

# print("count of numbers divisible by 2 and 3:",count)		



# x = "india1223@$5"

# #output = i*n*d*i*a

# for i in x:
# 	if i.isdigit():
# 		break
# 	else:
# 		print(i,end="*")



# Strings Function

# x = "Hello World"

# print(x.count("o"))

# print(x.index("e"))


# x = "Himachal Pradesh"

# for i in x:
# 	if i=="a":
# 		print(i)


# show the index of the all alphabet
# x = "Himachal Pradesh"

# y = len(x)

# for i in range(y):
# 	print(x[i],"Index :-", i,"Negative Index:",i-y)




# x = "Himachal Pradesh"

# y = len(x)

# for i in range(y):
# 	if x[i]=="a":
# 		print(x[i],"index :-",i)



# x = "data123science@#$4"

# #count total number of alphabet
# count = 0

# for char in x:
#     if char.isalpha():
#         count += 1

# print("Total number of alphabetic :", count)

# #count total number of digit
# count = 0

# for char in x:
#     if char.isdigit():
#         count += 1

# print("Total number of digit :", count)

# #count total number special character
# count = 0

# for char in x:
#     if not char.isdigit() and not char.isalpha():
#         count += 1


# print("Total number of character :", count)


# x = "data123s324453@#$cience@#$4"

# n = 0
# c = 0
# s = 0

# for i in x:
# 	if i.isdigit():
# 		n = n + 1
# 	elif i.isalpha():
# 		c = c + 1
# 	else:
# 		s = s + 1


# print("Total Number of text :- ",c)
# print("Total Number of digit :- ",n)
# print("Total Number of special charactar :- ",s)


#Nested Loop -- Loop used inside another loop is
# called nested loop

# for i in range(10):
# 	for j in range(i):
# 		print("*",end ="")
# 	print()	


# for i in range(10):
# 	print("----------")
# 	for j in range(1,5):
# 		print(j)



# for i in range(10):
# 	for j in range(i):
# 		print(j, end=" ")
# 	print()


# for i in range(10):
# 	for j in range(10-i):
# 		print(j,end=" ")
# 	print()			


# x = ["apple", "mango","Guava"]

# for i in x:
# 	for j in i:
# 		print(j)


#Show the Square of each value from 1 to 20
# for i in range(1, 21):
#     s = i ** 2
#     print(f"The square of {i} is {s}")


# #Show the cube of number from 1 to 20
# for i in range(1, 21):
#     c = i ** 3
#     print(f"The cube of {i} is {c}")

# #write a program to display all the prime 
# # numbers from 25 to 50

# for i in range(25, 51):
#     if i % 2 != 0:
#         print(i)


# #reverse the given integer 
# # input = 7894
# #output + 4987 

# x = "7894"
# print(x[::-1])




# x = int(input("enter the number :-"))
# if x > 1:
# 	for i in range(2,(x//2)+1):
# 		if x % i == 0:
# 			print(x,"is not a prime number")
# 			break
# 	else:
# 		print(x,"is a prime number")
# else:
# 	print(x,"is not a prime number")				



# x = "Data Science"
  
# x = x.split()
# x = x[-1::-1]
# x = " ".join(x)
# print(x)


x = ["a","b","c","d"]

y = ["g","c","d","a","r","o"]


# for i in x:
# 	for j in y:
# 		if i==j:
# 			print(j,end=" ")	



# for i in y:
# 	if i in x:
# 		print(i)


# Count total Prime Number from 1 to 50

# count = 0
# for i in range(1, 51):
#     if is_prime(i):
#         count += 1

# print("Total prime numbers from 1 to 50:", count)


# count = 0
# for i in range(1,51):
# 	if i%2 ==0:
# 		print(i)

# 		count +=1

# print("the count of even numbers is:",count)		




#---------------------------------------------------
#                    LIST
#---------------------------------------------------

# numerical :-int, float, complex
# sequence:- tuple,list,range()
# text:-str
# mapping:- dictionary
# set:- set, frozenset
# boolean :- true,false


# List : List are used to store the multiple values in a
# single variable


# 1. List are written in Square Bracket
# 2. List is changeable or mutuable
# 3. List allow duplicate values
# 4. Here We can enter multiple type of Data
# 5. List are ordered


# x = ["ansh","simran","shashank"]

# print(x)
# print(type(x))
# print(len(x))


# Indexing: It is used to extract the single text from the list
# type of indexing: 1. Positive 2. Negative

# Slicing :- It is used to extract the range of text from the list



# x = ["ansh","simran","vishwas","manjeet","yogesh","anshu","Harmeet"]\

# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])
# print(x[5])
# print(x[6])

# print(x[-1])
# print(x[-2])
# print(x[-3])
# print(x[-4])
# print(x[-5])
# print(x[-6])


# # Slicing

# # print(x[3:6])

# x = [1,2,3,4,5,6,7,8,9,10]

# print(x[1::2])
# print(x[0::2])


#Create a list and insert all name of the month

x=["jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"]


#Delete

# 1.Remove

# print(x)
# x.remove("jan")
# print("="*50)
# print(x)

# # 2.pop by default it will delete from last, we can give the indexing to delete specific name from list
# print(x)
# x.pop()
# print("="*50)
# print(x)

# 3.clear
# print(x)
# print("------------------------")
# x.clear()
# print(x)

# 4.Del

# del x[0]

# del x

x = ["sun","mon","tue","wed","thu","fri","sat"]

# # delete the 3rd index of value
# print(x)
# del x[3]
# print (x)
# # extract ["fri", "sat"]
# print(x[4:6])
# print(x[-2:])
# extract ["sun"]
# print(x[0])
# # delete "mon"
# x.remove("mon")
# print(x)
# # delete all value from the list 
# x.clear()
# print(x)
# # delete last value from the list 
# x.pop()
# print(x)



#Adding the values in the list 

# 1.Insert :- With the help of this formua we can add the 
# values according to index


# x = ["sun","Mon","Tue"]
# print(x)
# x.insert(1,"data")
# x.insert(0,"science")
# print(x)


# # 2. Append :- It is used to add the value end of the list

# x = ["sun","Mon","Tue"]
# x.append("wed")
# print(x)
# x.append("thu")
# print(x)


# # 3. Extend :- It is used to add the multiple values in LIST

# x = ["sun","Mon","Tue"]

# x.extend(["wed","thu","Fri","sat","sun"])
# print(x)


# x = ["sun","Mon","Tue"]
# y = ["wed","thu","Fri"]

# x.extend(y)
# print(x)

# x = str(x)
# print(x.upper())


# x = [4,7,2,6,0,4,9,7,1,10,3]


#sort :- It is used to arrange the data in ascending order
# 	descending order

# ascending order
# x.sort()
# print(x)

# #descending order
# x.sort(reverse=True)
# print(x)

# x = "science"
# print(list(x))


# x = [12,45,78,89,56,10,60]

# 1. Maximum value from the LIST
# max(x)
# print(max(x))
# # 2. minimum value from the LIST
# print(min(x))
# # 3. 3rd Maximum value from the list
# x.sort()
# # print(x)
# print(x[-3])

# # 4. 2nd Maximum value from the LIST
# print(x[-2])



# print(len(x))
# print(type(x))

# To find the index from the list of a specific number :
# print(x.index(89))

# x = ["sun","mon","tue"]

# y = x.copy()
# x.clear()
# # print(y)
# # print(x)


# for i in y :
# 	i = i.upper()
# 	x.append(i)

# print(x)
# print(type(x))


# x = [45,78,89,12,45,56,23,10]

# # print all the number less than 30
# # print all the numbers greater than 40

# x.sort()
# print(x)

# print("Numbers less than 30:-")
# for i in x:
# 	if i < 30:
# 		print(i)

# print("Numbers greater than 30:-")
# for i in x:
# 	if i > 30:
# 		print(i)		


# x = [45,78,89,12,45,56,23,10]
# # delete all the values that is less than 30?
# # for i in x[:]:
# # 	if i<30:
# # 		x.remove(i)
# # print(x)

# # or

# y = x.copy()

# x.clear()

# for i in y:
# 	if i < 30:
# 		continue
# 	else:
# 		x.append(i)

# print(x)			


# # create a new blank list and add all even numbers in list
# even = []
# for i in x:
# 	if i % 2 == 0:
# 		even.append(i)

# print("List of even numbers:", even)

# y = [12,45,56,3,12,3,12,8,12]

# print all duplicate values ?
# y = [12,45,56,3,12,3,12,8,12]


# for i in y:
# 	if y.count(i)>1:
# 		print(i,end=" ")

# print all unique values?
# y = [12,45,56,3,12,3,12,8,12]
# x = []


# for i in y:
# 	if i not in x:
# 		x.append(i)

# print(x)		


# print negative and positive of all number in list? 

# y = [12,45,56,3,12,3,12,8,12]

# x = len(y)

# for i in range(x):
# 	print(y[i],"Index :",i,"Negative index :", i-x)


# x = ["jan",45,"aug",42.9,"sun",true,21j]

#write a python query to extract all the values in a new list
# but exclude text from a list?

# y = []
# for i in x:
# 	if type(i)!=str:
# 		y.append(i)


# print(y)


##------------------ Nested List------------------###

# x = [21,43,[45,67,8,100],200]

# print(x)
# print(type(x))
# print(len(x))


# x = [12,[45,78,89,100,200,456],789]

# #extract values

# # 12
# # 45
# # 200
# # 789

# print(x[0])

# print(x[1][0])

# print(x[1][4])

# print(x[2])

x = [100,200,[300,400,[500,600,700],800,900],1000]


#800
#600
# # 300
# 200
# 1000

# print(x[2][3])
# print(x[2][2][1])    
# print(x[2][0])
# print(x[1])          
# print(x[3])



# print(x[2][4])

		
# print(x[2][1])



x = [[12,78,[[14,10,11],23,56,[89,96,25]],63,[23,100],123]]
# print(x)

# Extract all Number from the List
# 1.  10

# print(x[0][2][0][1])

# # 2.  11

# print(x[0][2][0][2])

# # 3.  12

# print(x[0][0])
# # 4.  56

# print(x[0][2][2])

# # 5.  100

# print(x[0][4][1])

# # 6.  63

# print(x[0][3])

# # 7.  14
# print(x[0][2][0][0])

# # 8.  89
# print(x[0][2][3][0])

# # 9.  96

# print(x[0][2][3][1])

# # 10. 78

# print(x[0][1])

# # 11. 123

# print(x[0][5])

# x = [12,45,56,89,12,56,12,10,12]


# # 1. find the index of all 12

# print("Index of 12:")
# for i in range(len(x)):
# 	if x[i] == 12:
# 		print(i)

# # 2. find the sum of all Number with the help of loop

# sum = 0
# for i in x:
# 	sum += i
# print("Sum of Numbers :",sum)


# # 3. Count total Numbr of text from the list
# x = [1,2,4,1.2,5.9,10.8,"a","b","c",True,21j]

# y = 0
# for i in x:
# 	if type(i) == str:
# 		y += 1
# print("count of total number of text",y)		



# # 4. count all Mumerical Data from the list

# c = 0

# for i in x :
# 	if type(i) == int or type(i) == float or type(i) == complex:
# 		c +=1

# print("count of Numerical Data :",c)		

# ----------------------------------------------------------
# TUPLES
# ----------------------------------------------------------

# TUPLES :- TUPLES ARE USED TO STORE THE MULTIPLE VALUES 
# 			IN A SINGLE VARIABLE.


# 1. TUPLES ARE WRITTEN IN ROUND BRACKET.
# 2. TUPLES ARE UNCHANGEABLE.
# 3. TUPLES ALLOW DUPLICATE VALUES.
# 4. TUPLES ARE ORDERED.
# 5. TUPLES ARE INDEXED.
# 6. TUPLES ALLOW MULTIPLE TYPE OF DATA.


# How to Create a blank Tuples

# x = ()
# print(x)

 
# y = tuple()
# print(y)


# #BlanK list 

# x = []
# y = list()

# print(x)
# print(y) 

# x = ("a","b","c","d","e",1,2,3,4,True,21j)

# print(x)
# # print(type(x))
# # print(len(x))


# x = list()
# print(x)

# x = 120
# y = str(x)

# a,b = y,"10"

# print(a+b)



# Packing and Unpacking

# Packing a table
# When we created a tuple, we normally assign to it.
# This is called "Packing" a tuple:


# Unpacking a Tuple
# When we create a tuple, we normally assign values to multiple
# variable from a tuple, this called Unpacking.

# x = ("First","Second","Third")
 
# a,b,c = x 
# print(a)
# print(b)
# print(c)


# x = ("a","b","c","d","e")
# print(x)

# m,*n = x
# print(n)

# x = (45,78,89,56)
# a,*b,c = x

# print(b)


# x = ("sunday","monday","tuesday","wednesday","thursday")

# a,*b,c,*d = x

# print()

# x = (12,45,78,89,5,23,10,18,45)

# # 1. STORE ALL EVEN NUMBER FROM NEW List

# y = []

# for i in x:
# 	if i%2==0:
# 		y.append(i)
# print(y)		

# # 2. STORE ALL ODD NUMBER FROM NEW List

# y =[]

# for i in x:
# 	if i%2!=0:
# 		y.append(i)
# print(y)		

# count
# index
# sum
# min
# max
# sorted



# x = (23,34,4,45,5,6,56,6,7,6,3,3,23)
# print(x)
# print(x.count(6))

# i = x.index(4)

# print(i)

# s = sum(x)
# print("total sum :-",s)

# m = max(x)
# print("maximum values :-", m)


# n= min(x)
# print("minimum values:-",n)

# o = sorted(x)
# print("sorted list ascending :-",o) 

# o = sorted(x,reverse=True)
# print("sorted list descending :-",o) 


# o = tuple(sorted(x))
# print("sorted list ascending :-",o) 

# o = tuple(sorted(x,reverse=True))
# print("sorted list descending :-",o) 


# x = [12,45,78,15,14,48]

# y = sorted(x)
# print(y)



#sort and sorted 

# sort 
# 1. It is used in list only.
# 2. Here i am not putting any variable 


# sorted

# 1. sorted used in list tuple set dict
# 2. Here we are not putting any variable


# replacing the ram word with ramayan

# x = ["ram","sita","Krishan"]

# x[0] = "ramayan"
# print(x)


# x.pop(0)
# x.insert(0,"Rama")

# print(x)


# x = ("ram","sita","hanuman")

# x = list(x)

# x[1] = "krishna"
# print(tuple(x))


# x = list([23,45,23,12,78,10])

# x = (78,89,45,56,78,52,62,10)

# # 1. find the 2nd index of 78
# i = x.index(78)
# u = x.index(78,i+1)

# print(u)

# # 2. find the sum of last 3 Number.
# i = sum(x[5:])
# print(i)

# # 3. reverse the Tuple

# y = list(x)
# y.reverse()

# print(tuple(y))

# 4. Create a list with the help of user input

# x = list()
# y = int(input("enter the length of the list:-"))

# for i in range(y):
# 	val = int(input("enter the number in list :-"))
# 	x.append(val)

# print("list :",x)	

# 5. Create a tuple with the help of user input.


# x = list()
# y = int(input("enter the length of the LIST:-"))

# for i in range(y):
# 	val = int(input("enter the number in list :-"))
# 	x.append(val)

# z = tuple(x)

# print("tuple :",z)	



# 1. Write a program with the help of user input to display the last digit of a number

# x = int(input("enter any number:-"))
# print("Last digit of number :-",x%10)



# # 2. write a program to caluculate the electricity bill
# # if number of unit is less than 200 then 5 rupees per unit 
# # else 10 rupees per unit

# unit = float(input("Enter unit :-"))
# if unit < 200:
# 	print("Amount :-",unit*5)
# else:
# 	print("Amount :-",unit*10)	


# # 3. Write a program with the help of use input to check the Number is 
# # 		divisible of 5,7 and 9 or Not ?

# x = int(input("enter number :-"))
# if x%7==0 and x%5==0 and x%9==0:
# 	print("divisible")
# else:	
# 	print("Not divisible")

# # 4. print the statement 
# # 	HOnesty is the best Policy ---- if strings  is vowel
# # 	else print Consonent

# x = str(input("enter any alphabet :-"))
# if x in ("a","e","i","o","u"):
# 	print("Honesty is the best policy")
# else:	
# 	print("Consonent")

# # 5. write a program with the help of two user input if the sum of two Number is even then print 
# # even Number with the value of sum else print number is odd with values.




# # 6. If Number is between the 100 to 200 and 400 to 600 then Print
# # 	Done else print Not Done

# # 7. write a program with the help of user input and print the Number
# # 	if Number is divisible of 2,4 and 6 else print Number is not
# # 	divisible of 2,4 and 6

# # 8. Write a python program to show if length of text is greater than 5 then show the last 2 alphabet
# # 	else show beginning of 2 alphabet.
 
# # 9. Write a python program to print the number from 1 to 50 the Number who is divisible of 5 and 4 

# x = str(input("enter any text :-"))
# y = len(x)

# if y > 5:
# 	print(x[-2:])
# else:
# 	print(x[0:3])


# 10. Write a python program witht the help of user input to compare in three number and show greatest number.



# String :- Strings are written in dual quotation or single
# quotation.

# Diff between While and FOR


# typeCasting


#print the total even number between 1 to 15

# print("Even numbers between 1 and 15:")
# for i in range(1, 16):
#     if i % 2 == 0:
#         print(i)
        
# #count all odd number between 1 to 20

# odd = 0
# for i in range(1, 21):
#     if i % 2 != 0:
#         odd += 1

# print("Total odd numbers between 1 and 20:", odd)

# # find the average of first 5 number
# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# average = total / len(numbers)

# print("Average of the first 5 numbers:", average)


# print the number from 1 to 10 with the help of while
# loop and skip 4,6,and 8

# While Loop
# x = 0 

# while x <=10:
# 	x+=1
# 	if x==4 or x==6 or x==8:
# 		continue
# 	else:
# 		print(x)


# # For Loop
# for i in range(1,11):
# 	if i in (2,4,6):
# 		continue
# 	else:
# 		print(i)


#Print the Table with the help of user input

# x = int(input("enter any table name :-"))
# for i in range(1,11):
# 	print(i*x)


# x = int(input("Enter the table name :-"))
# y = 0
# while y<10:
# 	y+=1
# 	print(f"{x} x {y} = {x*y}")


# x = "data310science23"

# # 1.print all number from text
# for i in x:
# 	if i.isdigit():
# 		print(i,end=" ")

# # 2.print all alphabet from text

# for i in x:
# 	if i.isalpha():
# 		print(i,end=" ")


# x = "df34@##sd$%"

# for i in x:
#     if not i.isdigit() and not i.isalpha():
#     	print(i)	


# x = [34,5,56,6,7,71,12,45,78]

# # 1. Replace second value 5 at the place of 100.

# x[1] = 100
# print(x)

# # 2. Print all even number from the list.

# z = []
# for i in x:
# 	if i%2!=0:
# 		z.append(i) 


# # 3. Delete 3rd indx of value.
# x.pop(3)

# # 4. Count all odd number.
  # c=0	
# for i in x:
# 	if i%2==1:
# 		c+=1


# print("total odd number :-",c)


# x = (12,45,7,89,5,65)

# # sort in ascending order
# y = sorted(x)
# print(tuple(y))

# # sort in descending order
# y = sorted(x,reverse=True)
# print(tuple(y))


# # reverse the tuple
# y = reversed(x)
# print(tuple(y))

# #show the index of 7

# print(x.index(7))


# x = "data science"

# # #find the second index of a 
# f = x.find("a",2)
# print(f)

# # sci
# y = x[5:8]
# print(y)
# # ta
# z = x[2:4]
# print(z)
# # last three alphabet
# o = x[-3:]
# print(o)


# x = (12,45,78,45,12,45,56,89,45,12)

# #extract all duplicate values

# for i in x:
#  	if x.count(i)>1:
#  		print(i)


# #show all unique values

# y = []
# for i in x:
# 	if i not in y:
#  		y.append(i)

# y = tuple(y)
# print(y)	 



# #Change the data type in stirng in tuple
# y = list()
# for i in x:
# 	y.append(str(i))

# y = tuple(y)
# print(y)	


# --------------Sets-------------------
# Set :- Set are used to store the multiple values in a single variable.
# 1. set are wtitten in curly Bracket.
# 2. set are un-ordered.
# 3. set are un-indexed.
# 4. set do not allow duplicate values 


# #blank set
# x = set()

# x = {"data",45,56,25,34j,True}

# print(x)
# print(type(x))
# print(len(x))




# x = {23,23,23,23,23,23,23,45}
# print(x)



# x = {12,45,7,84,5,4,12,12,12}
# y = set(x)

# print(y)


# #how to add values in a set
# #add :- with the help of this you can add the values in a set.

# x.add(100)
# x.add(41)
# print(x)

#How to delete the values from set.
#1. remove
#2. pop
#3. clear


# how to remove duplicate values from a set
# x = {"state","capital","Capital","State"}

# y = []
# for i in x:
# 	i = i.title()
# 	y.append(i)

# x = set(y)
# print(x)

# Delete all capital letter of text
# x = {"sunday","MONDAY","WEDNESDAY","friday"}

# y = []
# for i in x:
# 	if i.islower():
# 		y.append(i)

# x = set(y)
# print(x)


# # Combine the two set.

# x = {1,2,3}
# y = {4,5,6}

# x = list(x)
# y = list(y)

# x.extend(y)

# x = set(x)
# print(x)


# x = {1,2,3}
# y = {4,2,1}

# z = y.difference(x)
# print(z)

# x = {1,2,3}
# y = {4,2,1}

# x.diiference_update(y)
# print(x)

# # discard()- remove the specified item
# x = {12,45,78,56}
# x.discard()
# print(x)

# #intersection() 
# x = {1,2,3}
# y = {3,2,6}
# z = x.intersection(y)
# print(z)


# intersection_update() Removes the items 

# x = {3,5,7}
# y = {7,5,2}
# x.intersection_update(y)
# print(x)

# x = {3,5,7}
# y = {7,5,2}
# a = x.symmetric_difference(y)
# print(a)



# difference_update() -- Removes the items in this set that are also included in another,specified set


# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others



x = "Python is a programming language"
y = "Python is an object oriented programming language"

#Extract all uncommon text from sentences

# output: "a an object oriented"

# x = x.lower()
# y = y.lower()
# x = x.split()
# y = y.split()

# print(x)
# print(y)
# print("-"*70)

# z = []
# for i in x:
# 	if i not in y:
# 		z.append(i)


# for i in y:
# 	if i not in x:
# 		z.append(i)


# z = " ".join(z)		
# print(z)


# x = x.lower()
# y = y.lower()
# x = x.split()
# y = y.split()

# print(x)
# print(y)
# print("-"*70)

# z = []
# for i in x:
# 	if i in y:
# 		z.append(i)


# # for i in y:
# # 	if i in x:
# # 		z.append(i)


# z = " ".join(z)		
# print(z)


# Create a dict base of student and his mark and five students


# x = {"Vishwas":87,"Shashank":99,"Sneha":77,"Dolly":88,"manjeet":54}

# print(x)

# x.update({"suraj":45,"Kishan":66})
# print(x)





# show the state and and capital with the help of user input?

#   state           =  capital
# x={"Andhra Pradesh" : "Amaravati",
# "Arunachal Pradesh" : "Itanagar",
# "Assam" : "Dispur",
# "Bihar" : "Patna",
# "Chhattisgarh" : "Raipur",
# "Goa" :	"Panaji",
# "Gujarat" :	"Gandhinagar",
# "Haryana" :	"Chandigarh",
# "Himachal Pradesh": "Shimla",
# "Jharkhand" : "Ranchi",
# "Karnataka" :	"Bengaluru",
# "Kerala" :	"Thiruvananthapuram",
# "Madhya Pradesh" :	"Bhopal",
# "Maharashtra":	"Mumbai",
# "Manipur":	"Imphal",
# "Meghalaya": "Shillong",
# "Mizoram" :	"Aizawl",
# "Nagaland" : "Kohima",
# "Odisha" :	"Bhubaneswar",
# "Punjab" :	"Chandigarh",
# "Rajasthan" :	"Jaipur",
# "Sikkim" : "Gangtok",
# "Tamil Nadu" :	"Chennai",
# "Telangana" :	"Hyderabad",
# "Tripura" : "Agartala",
# "Uttar Pradesh" :	"Lucknow",
# "Uttarakhand" :	"Dehradun", 
# "West Bengal" :	"Kolkata"}

# y = str(input("enter any state :-")).title()
# print("-"*70)
# print(f"the capital of {y} is : {x[y]}")
# print("-"*70)



# dic = {"A":45,"F":56,"C":39,"E":89,"B":50}

# print(dic)

# 1.popitem :- It is used to delete the key and values from the LIST.
# 2.pop :- It is used to delete the key and values according to keys.
# 3. Clear :-
# 4. Del : -

# a = dic.popitem()
# print(dic)

# dic.pop("B")
# print(dic)

# dic.clear()
# print(dic)

# del dic["A"]
# print(dic)

# del dic
# print(dic)

# Create a dictionary with the help of user input.

# d = {}
# x = int(input("Enter the length of the dictionary:- "))
# for i in range(x):
# 	key = input("enter the key :-")
# 	val = input("enter values :-")
# 	d[key] = val

# print(d)

# x = {'A': '44', 'C': '33', 'D': '55'}

# # convert all the values in key and key to values

# a = {}

# for key, value in x.items():
# 	a[value] = key

# print(a)	


# y = x.items()
# for i,j in y:
# 	a[j] = i

# print(x)
# print("---------------------After the Update:------------------------")
# print(a)


#Sorting 

# x = {1:"A",5:"C",4:"B",2:"R",6:"T"}

# sort the dictionary base of keys in ascending order.

# y = x.items()
# z = sorted(y)
# x = dict(z)
# print(x)

#Sorting the dictionary by keys
# x = {1:"A",5:"C",4:"B",2:"R",6:"T"}

# y ={}

# s = sorted(x.items(),reverse=True)
 
# for i,j in s:
#  	y[i] = j

# print(y) 	



x = "Programming"

# # Output = "PrOgRaMmInG"

# y = len(x)

# for i in range(y):
# 	if i % 2 ==0:
# 		print(x[i].upper(),end=" ")
# 	else:
# 		print(x[i].lower(),end=" ")
		
# x = [-1,-2,4,6,10]


# extract minimum value from the list

# y = min(x)		
# print(y)

# print(x[1])

# y = len(x)

# for i in range(y):
# 	if i % 2 ==0:
#  		print(x[i].upper(),end=" ")
#  	else:
#  		print("*",end=" ")
		


# --------------Nested dictionary---------------------


# Nested Dict : When we use dictionary inside another dictionary is called nested dictionary

# a = {"Name":"Shashank","Age":22,"City":"Delhi"}
# b = {"Name":"Raja","Age":24,"City":"Noida"}
# c = {"Name":"Ram","Age":21,"City":"Jaipuraipur"}
# d = {"Name":"Virat","Age":34,"City":"Chennai"}


# x = {1:a,2:b,3:c,4:d}

# print(x)

# print("*"*70)

# print(x.keys())

# print(x.values())


# print(x[1]["age"])



# 1. show all the values of roll no 3 

# print(x[2].values())

# # 2. show all the keys of roll no 2 

# print(x[2].keys())

# # 3. show the city of Virat

# print(x[4]["City"])

# # 4. show the name of the roll no 1 

# print(x[1]["Name"])

# # 5. show all keys of roll no 4

# print(x[4].keys())

# # 6. find the age of roll no 4 with get formula 

# print(x[4].get("Age"))


# a = {"Name":"Shashank","Age":22,"City":"Delhi"}
# b = {"Name":"Raja","Age":24,"City":"Noida"}
# c = {"Name":"Ram","Age":21,"City":"Jaipur"}
# d = {"Name":"Virat","Age":34,"City":"Chennai"}


# x = {1:a,2:b,3:c,4:d}


# # add marks in roll no 3 
# x[3]["Marks"] = 256
# print(x)


# x[2].update({"Marks":356,"State":"UP"})

# print(x[2])



# x = {"car":{"Brand":["Kia","Honda","BMW"],
# 			"Color":["Red","Black","White"],
# 			"Model":["BS6","BS4","BS6"],
# 			"Year":[2015,2018,2016]},
# 	"Bike":{"Brand":["TVS","Bajaj","Hero"],
# 			"Model":["A150","Pulser150","110"],
# 			"Color":["Red","Black","White"],
# 			"Year":[2019,2018,2020]}



# 	}		

# print(x)


# a = x['car']
# # print(a)


# d = a["Brand"]
# # print(d[-1])

# print(x["car"]["Brand"][-1])



# Add Bike in Fuel = ["Petrol", "CNG"]

# x["Bike"]["Fuel"] = ["Petrol", "CNG"]

# # print(x)

# # add color in bike green

# x["Bike"]["Color"].append("green")

# # print(x)


# # Delete the year from car

# del x["car"]["Year"]

# print(x)


# dic={ 
#      "prince":{"maths":56,"sci":56,"sst":78,"eng":89,"hnd":75},
# 	 "simran":{"maths":85,"sci":100,"sst":99,"eng":98,"hnd":97},
#       "Dolly":{"maths":89,"sci":58,"sst":36,"eng":38,"hnd":77},
#       "mohit":{"maths":75,"sci":76,"sst":74,"eng":79,"hnd":73},
#        "gulshan":{"maths":88,"sci":68,"sst":66,"eng":48,"hnd":87},
#        "Diya":{"maths":90,"sci":52,"sst":55,"eng":57,"hnd":41},
#        "vansh":{"maths":74,"sci":47,"sst":25,"eng":22,"hnd":23},
#        "nanu":{"maths":12,"sci":85,"sst":78,"eng":96,"hnd":89},
#        "minny":{"maths":84,"sci":45,"sst":91,"eng":18,"hnd":56},
#        "sumit":{"maths":59,"sci":50,"sst":30,"eng":30,"hnd":70},
# 		"prince":{"math":68,"sc":89,"sst":98,"eng":91,"hnd":75},
# 		"simran":{"math":87,"sc":89,"sst":43,"eng":90,"hnd":76},
# 		"parul":{"math":45,"sc":65,"sst":23,"eng":93,"hnd":78},
# 		"samrath":{"math":33,"sc":99,"sst":41,"eng":49,"hnd":77},
# 		"ram":{"math":34,"sc":35,"sst":36,"eng":37,"hnd":38},
# 		"preeti":{"math":42,"sc":44,"sst":46,"eng":54,"hnd":65},
# 		"anshu":{"math":21,"sc":96,"sst":67,"eng":12,"hnd":12},
# 		"anshumam":{"math":11,"sc":18,"sst":20,"eng":30,"hnd":39},
# 		"muskan":{"math":71,"sc":87,"sst":19,"eng":59,"hnd":44},
# 		"sumit":{"math":66,"sc":88,"sst":99,"eng":22,"hnd":83},
# 		"Prince"  :{"Eng":88,"Hnd":80,"Mth":79,"Sci":67,"Sst":78},
#       "Yogesh"  :{"Eng":83,"Hnd":90,"Mth":69,"Sci":63,"Sst":68},
#       "Shashank":{"Eng":89,"Hnd":69,"Mth":83,"Sci":75,"Sst":87},
#       "Simran"  :{"Eng":88,"Hnd":80,"Mth":79,"Sci":67,"Sst":78},
#       "Vishwas" :{"Eng":76,"Hnd":67,"Mth":89,"Sci":73,"Sst":77},
#       "Ansh"    :{"Eng":83,"Hnd":84,"Mth":75,"Sci":66,"Sst":71},
#       "Dolly"   :{"Eng":81,"Hnd":89,"Mth":74,"Sci":87,"Sst":73},
#       "Manjeet" :{"Eng":78,"Hnd":70,"Mth":69,"Sci":61,"Sst":88},
#       "Kshitij" :{"Eng":84,"Hnd":79,"Mth":75,"Sci":84,"Sst":83},
# 	  "Harsh"   :{"Eng":80,"Hnd":82,"Mth":70,"Sci":62,"Sst":73},
# 	  "prince":{"maths":56,"science":73,"sst":78,"eng":65,"hnd":75},
# 	"vishwas":{"maths":65,"science":73,"sst":80,"eng":75,"hnd":56},
# 	"dolly":{"maths":75,"science":66,"sst":54,"eng":69,"hnd":52},
# 	"aman":{"maths":50,"science":60,"sst":40,"eng":63,"hnd":71},
# 	"simran":{"maths":55,"science":56,"sst":60,"eng":53,"hnd":65},
# 	"ansh":{"maths":40,"science":59,"sst":68,"eng":71,"hnd":69},
# 	"annu":{"maths":56,"science":73,"sst":70,"eng":60,"hnd":74},
# 	"gurveer":{"maths":60,"science":70,"sst":73,"eng":67,"hnd":50},
# 	"parmod":{"maths":52,"science":55,"sst":78,"eng":66,"hnd":45},
# 	"sahil":{"maths":50,"science":45,"sst":61,"eng":56,"hnd":78},
# 	"Prince":{"Maths":56,"Science":66,"SST":74,"English":89,"Hindi":75},
# 	"Shashank":{"Maths":86,"Science":56,"SST":78,"English":83,"Hindi":95},
# 	"Vishwas":{"Maths":46,"Science":86,"SST":38,"English":93,"Hindi":65},
# 	"Dolly":{"Maths":56,"Science":46,"SST":71,"English":73,"Hindi":55},
# 	"Simran":{"Maths":76,"Science":36,"SST":75,"English":84,"Hindi":45},
# 	"Harmeet":{"Maths":46,"Science":46,"SST":79,"English":43,"Hindi":63},
# 	"Manjeet":{"Maths":82,"Science":56,"SST":85,"English":82,"Hindi":35},
# 	"Sneha":{"Maths":66,"Science":51,"SST":98,"English":53,"Hindi":73},
# 	"Yogesh":{"Maths":46,"Science":56,"SST":78,"English":83,"Hindi":95},
# 	"Ansh":{"Maths":69,"Science":80,"SST":72,"English":88,"Hindi":75}
# }


# # print(dic)

# print("-"*60)
# name = input("enter the name of the student :-").title()

# d = dic[name]  #passing the parameter of each student by user input

# marks = d.values()  #show all the values of each student

# marks = sum(marks) #its show obtained 

# print(d)

# print("Total marks = ", marks)

# per =  marks/5

# per2 = str(round(per,1)) + "%"

# # print(per)

# print("Total Percentage =",per2)


# #Applying the division

# if per>=60:
# 	div = "First Division"

# elif per>=45:
# 	div = "Second division"

# elif per>=33:
# 	div = "Third division"

# else:
# 	div = "fail"	


# print(div)

# #-------------------------------------------------------

# print("-"*70)
# print("-"*70)
# print("Full Marks :",500)
# print("-"*70)
# time.sleep(2)
# print("Obtained Marks :",marks)
# print("-"*70)
# time.sleep(1)
# print("Percentage :",per2)
# print("-"*70)
# time.sleep(2)
# print("division :",div)
# time.sleep(2)
# print("-"*70)





# dic={ 
#      "prince":{"maths":56,"sci":56,"sst":78,"eng":89,"hnd":75},
# 	 "simran":{"maths":85,"sci":100,"sst":99,"eng":98,"hnd":97},
#       "Dolly":{"maths":89,"sci":58,"sst":36,"eng":38,"hnd":77},
#       "mohit":{"maths":75,"sci":76,"sst":74,"eng":79,"hnd":73},
#       "gulshan":{"maths":88,"sci":68,"sst":66,"eng":48,"hnd":87}
#     }   

# # print(dic)

# roll no = {1:"prince",2:"simran",3:"Dolly",4:"mohit",5:"gulshan"}

# while True:

# 	r = int(input("Enter your Roll Number :-"))
# 	x = roll_no[r]
# 	y = result[x]
# 	v = sum(y.values())


# 	per = v/5

# 	p = str(per)+"%"

# 	if per>=60:
# 		div = "First Division"

# 	elif per>=45:
# 		div = "Second division"

# 	elif per>=33:
# 		div = "Third division"

# 	else:
# 		div = "fail"	



# 	print("-"*70)
# 	print("Total Marks :",500)
# 	print("-"*70)
# 	print("Obtained Marks :",v)
# 	print("-"*70)
# 	print("Percentage :",per)
# 	print("-"*70)
# 	print("division :",div)


# 	var = int(input("Press 1 for Next Student \n Press 0 for Exit :"))
# 	if var == 1:
# 		continue
# 	else:
# 		break




# 1. What is Function?
# 	 A function is a back of code which only runs when 
# 	 it is called. You can pass data, known as parameter,
# 	 into a function.

# 	 A function can return data into a result.


# 2. Creatimg a function 
# 	In python function is defined using the def keyword:

# There are mainky two functions :

# 1. User defined function : The ser defined function user 
# perform specific task.


# 2. Built in Function : The built in function are those function
# that are pre-defined in python Ex:- Sum min max soretd len type 




#Creating a Function 
# def greet():
# 	#greeting
# 	print("Hello World")


# #Calling the function 
# greet()


# def prince(x):
# 	s = 0
# 	for i in x:
# 		s+=1
# 	print("Total Number of Sum : ",s)
	


# def abc(x,y):
# 	z = x+y 
# 	print(z)


# x = 10
# y =45
# abc(x,y)


# --Create a fucntion to  find the cube value of any number 
#   with tht ehelp of user input 



# def cube(x):
# 	print(f"Cube value of {x} is :- {x**3}")

# x = int(input("enter any number :-"))
# cube(x)


# # Create a function to show the last three alphabet of any
# # text 


# def text(x):
# 	print(x[-3:])


# x =  input("Enter any alphabet:-")

# text(x)


# #Create a function to print who is eligible for vote or not

# def vote():
#     if age >= 18:
#         print("You are eligible to vote.")
#     else:
#         print("You are not eligible to vote.")

# age = int(input("Enter your age: "))
# vote()


# #Create a function to calculate the average of any numbers

# def avg(x,y,z):
#  	a = x+y+z
#  	av = a/3
#  	print("average of numbers:-",av)

# x = int(input("Enter any number:"))
# y = int(input("Enter any number:"))
# z = int(input("Enter any number:"))
# avg(x,y,z)


#Create a function to show the first 2 alphabet and last 2
# alphabet in capital letter and rest alphabet in small letter.	

# def prince(x):
# 	x = "Himachal"

# 	a = x[0:2].upper()
# 	c = x[-2:].upper()
# 	l = len(x)-4
# 	b = x[2:l+2]

# 	print(a+b+c)

# prince(x)



# ------------------------------------Numpy----------------------------------------


# What is Numpy ?
# Numpy is the library of python where we complete all calculations related to mathematics.

# Numpy is Numerical python

#Array 
#Dimension


# import numpy


# ar = numpy.array([12,45,78,"Data",20.4,21j,True])
# print(ar)
# print(type(ar))

# what is the difference between list and numpy array?


import numpy as np 

# x = np.array([[[[12,45,78,89]]]])
# print(x)
# print(type(x))

# x = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(x)

# x = [[1,2,3],[4,5,6,],[7,8,9]]
# print(x)

# x = np.array((12,23,45,56))
# print(x)

# x = [12,45,78,89]
# ar = np.array(x)
# print(ar)


# #Creating a 1 dimension array

# x = np.array([12,45,78,"Science",21j,])
# print(x)

# print(type(x))  #Its shows the data type of variable

# print(np.ndim(x))	#Its shows the number of dimension

# print(x.shape)	#it shows the shape of the array

# print(x.dtype) 	#High complexity of data in array



# #Two Dimension Array (2D Array)

# x = np.array([[12,45,78,89]])
# print(x)
# print("Type :-", type(x))
# print("Data Type :-", x.dtype)
# print("Number of Dimension :-",np.ndim(x))
# print("Shape of Array :-", x.shape)



# Create a Three dimension array and include all data
# 1. Check the data type of variable
# 2. Check the data type of array
# 3. Check the length of array
# 4. Show the number of dimension.



# x = np.array([[[12,45,78,"Science",21j,20.5]]])
# print(x)
# print(type(x))
# print(x.dtype)
# print(np.ndim(x))
# print(len(x))


# x = [[1,2,3,4],[9,10,11,12],[13,14,15,16]]

# ar = np.array(x)
# print(ar)
# print("Shape of the matrix :-", ar.shape)
# print(np.ndim(ar))

# t = ar.shape

# print(f"There are {t[0]} Rows and {t[1]} columns")


# Indexing and Slicing 

import numpy as np
# x = np.array([12,45,78,89])


# x = np.array([[12,45,56,],[98,87,36]])

# print(x)

# Extract the values 
# 1. 45
# 2. 36
# 3. 89
# 4. 12
# 5. 98

# print(x[1][1]) or x[0,1] #87
# print(x[1][2]) or x[1,2] #36
# print(x[0][1]) or x[0,1] #45
# print(x[0][0]) or x[0,0] #12
# print(x[1][0]) or x[1,0] #98


# 12,45 x[0][0:2] or x[0,0:2]
# 87,36 x[1][1:1] or x[1,1:1]	
# 45,56 x[0][1:]  or x[0,1:]


# Advantage of using Numpy Arrays Over Python Lists:
# 1. Consumes less memory
# 2. Fast as compared to python Lists
# 3. Convenient to use


# Creating N/ Multi dimensional array 

arn  = np.array([1,2,3,4], ndmin = 10)

print(arn)
print(arn.ndim)



