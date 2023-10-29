##Part 1 a
#n = int(input('Give me a number over 100: '))
#if n <= 100:
#    print(n, 'is not over 100')

##Part 1 b
#age=int(input("Enter your age: "))
#if age >= 18:
#    print("Can vote")

##Part 2 a
#x = int(input('Give me a number: '))
#if x < 0:
#    print(x, 'is negative')
#else:
#    print(x, 'is positive')

##Part 2 b
#mark=float(input("Enter mark: "))
#if mark < 40:
#    print("Fail")
#else:
#    print("Pass")

##Part 2 c
#num=int(input("Enter your number: "))
#if num % 2 == 0:
#    print("Even number")
#else:
#    print("Odd number")

##Part 3 a
#f=0
#c=0

#Type=int(input("Enter 1 if you want to convert from C to F and 2 for F to C: "))

#if Type == 1:
#    c=float(input("Input celcius value: "))
#    f=(c*1.8)+32
#    print("Farenheit value is, ",f)
#elif Type == 2:
#    f=float(input("Enter farenheit value: "))
#    c=(f-32)/1.8
#    print("Celcius value is, ",c)
#else:
#    print("Invalid operation entered")
    
##Part 3 b
#Int1=0
#Int2=0
#Operator=0

#Int1=float(input("Enter first value: "))
#Int2=float(input("Enter second value: "))
#Operator=input("Enter operator: ")

#if Operator == "+":
#   Result=Int1+Int2
#    print(Result)
#elif Operator == "-":
#    Result=Int1-Int2
#    print(Result)
#elif Operator == "*":
#    Result=Int1*Int2
#    print(Result)
#elif Operator == "/":
#    if Int2 == 0:
#        print("Cannot divide by 0!")
#    else:
#        Result=Int1/Int2
#        print(Result)
#else:
#    ("Error")

##Part 3 c
#Tip=0

#Cost=float(input("Enter cost of the meal: "))

#print("""Satisfaction levels are as follows,
#Totally satisfied = 1
#Satisfied = 2
#Dissatisfied = 3""")

#SatisfactionLevel=input("Enter satisfaction level: ")

#if SatisfactionLevel == "1":
#    tip=(Cost*(20/100))
#    print("You are totally satisfied and the tip will be",tip)
#elif SatisfactionLevel == "2":
#    tip=(Cost*(15/100))
#    print("You are satisfied and the tip will be",tip)
#elif SatisfactionLevel == "3":
#    tip=(Cost*(10/100))
#    print("You are dissatisfied and the tip will be",tip)
#else:
#    print("Error!")

##Part 4 b
#m = int(input('Give me number between 1 and 10: '))
#if m >=1 and m<11:
#    print('Well done! You gave me: ', m)

##Part 4 d
#if mark < 0:
#    print("Mark is invalid!")
#elif mark > 100:
#    print("Mark is invalid!")
#elif mark >= 70:
#    print(’Exceptional result!’)
#elif mark >= 40:
#    print(’Satisfactory result!’)
#else:
#    print(’You have failed.’)

##Part 4 f
#x = 10
#if not x > 10:
#    print("not returned True")
#else:
#    print("not returned False")
    
##Part 5
#like=input("Do you like python?: ")
#like=like.lower()

#if like == "yes" or like == "y":
#    print("you are on the right course")
#elif like == "no" or like == "n":
#    print("you are on the right course")
#else:
#    print("I did not understand")

##Part 6 Q 1 a
#n = input('Give me a number over 100: ')
#try:
#    n = int(n)
#    if n <= 100:
#       print(n, 'is not over 100')
#    else:
#        print(n, 'is over 100')
#except ValueError:
#    print("Please enter a valid integer.")

##Part 6 Q 1 b
#age = input('Enter your age: ')
#ry:
#    age = int(age)
#    if age >= 18:
#        print("You can vote")
#except ValueError:
#    print("Please enter an integer")

##Part 6 Part 4 d)
#Int1=0
#Int2=0
#Operator=0

#Int1=float(input("Enter first value: "))
#Int2=float(input("Enter second value: "))
#Operator=input("Enter operator: ")

#try:
#    if Operator == "+":
#        Result=Int1+Int2
#        print(Result)
#    elif Operator == "-":
#        Result=Int1-Int2
#        print(Result)
#    elif Operator == "*":
#       Result=Int1*Int2
#        print(Result)
#    elif Operator == "/":
#        Result=Int1/Int2
#        print(Result)
#    else:
#        ("Error")
#except ZeroDivisionError:
#    print("Cannot divide by zero!")

##Part 7 a
#import random
#coin=random.randint(0,1)

#if coin == 0:
#    print("Tails")
#else:
#    print("Heads")
