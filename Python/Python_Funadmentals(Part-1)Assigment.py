#AssignmentProblems

#Q1
#Write a program that asks the user for their name and age,then prints a sentence like:
#Hello Ali, you are 21 years old!
#Solve
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# age = int(age)
# print("Hello, " + name + "," "you are " + str(age) + " years old.")

#Q2
#Take two numbers as input from the user and print their sum, difference, product, and quotient.
#Solve
# first_number = input("Enter your first number: ")
# second_number = input("Enter your second number: ")
# first_number = int(first_number)
# second_number = int(second_number)
# sum = first_number + second_number
# print("Sum :" + str(sum))
#
# difference  = first_number - second_number
# print("difference  :" + str(difference))
#
# product = first_number * second_number
# print("product :" + str(product))
#
# quotient = first_number / second_number
# print("quotient :" + str(quotient))

#Q3
#Ask the user to enter two integer and one float. Convert them all to floats and print their average.
#Solve
# first_int = float(input("Enter the first integer: "))
# second_int = float(input("Enter the second integer: "))
# first_float = float(input("Enter the first float: "))
#
# average = (first_float + first_int + second_int ) / 3
# print("The average is: ", average)


#Q4
#The user enters a string containing a number (e.g.45,).Convert it to an integer a float a string a gain
#Solve
# user_num = input("Enter a number: ")
# user_num_int = int(user_num)
# user_num_float = float(user_num)
# user_num_str = str(user_num_int)
# print(user_num_int,type(user_num_int) )
# print(user_num_float,type(user_num_float))
# print(user_num_str,type(user_num_str))


#Q5
#Evaluate and print the result of the following expression
# x =10+3*2**2
#Solve
# x = 10+3*2**2
# print(x)


#Q6
#Write a program to SWAP values of two numbers entered by user
#Solve
# num_one = input("Enter a number: ")
# num_two = input("Enter a number: ")
# Without Third Variable
# print(num_one, num_two)
# num_one = int(num_one) + int(num_two)
# num_two = int(num_one) - int(num_two)
# num_one = int(num_one) - int(num_two)
# print(num_one, num_two)
# With third Variable
# print(num_one, num_two)
# num_three = int(num_one)
# num_one = int(num_two)
# num_two = int(num_three)
# print(num_one, num_two)

#Q7
#Ask the user for a temperature in Celsius(string input).Convert it to FLOAT,then calculate and print temperature in Fahrenheit.
#Slove
# tmp = input("Enter a Tmp: ")
# tmp = float(tmp)
# FahrenheitTemp = tmp * 1.8 + 32
# print(FahrenheitTemp)

#Q8
#Take the radius(r) as user input and print the area.
#Solve
# r = int(input("Enter a radius: "))
# py = 3.14
# area = py * r**2
# print("The area of the circle is", area)

#Q9
#Ask the user for : Principal(P), Rate(R), Time(T)
#Slove
# P = float(input("Enter the value of P: "))
# R = float(input("Enter the value of R: "))
# T = float(input("Enter the value of T: "))
#
# SI = (P * R * T)/100
# print(SI)

#Q10
# Take a decimal number as input and output its integer and fractional parts
#Slove
# num = float(input("Enter a number: "))
# int_num = int(num)
# fractional_num = num - int_num
# print(int_num)
# print(round(fractional_num, 2))




