##Ex 1 Part A
#hidden = 6

#guess = int(input("Enter a number between 1 and 20: "))

#while guess != hidden:
#    print("Guess is not correct.")
#    guess = int(input("Enter your next guess (a number between 1 and 20): "))

#print("Your guess was correct!")

##Ex 1 Part B
#import random

#hidden = random.randint(1, 20)

#guess = int(input("Enter a number between 1 and 20: "))

#while guess != hidden:
#    print("Guess is not correct.")
#    guess = int(input("Enter your next guess (a number between 1 and 20): "))

#print("Your guess was correct!")

##Ex 1 Part C
#import random

#hidden = random.randint(1, 20)

#guess = int(input("Enter a number between 1 and 20: "))

#while guess != hidden:
#    if guess < hidden:
#        print("Guess is too low.")
#    else:
#        print("Guess is too high.")
#    guess = int(input("Enter your next guess (a number between 1 and 20): "))

#print("Your guess was correct!")

##Ex 2
#total = 0  
#count = 0  

#score = int(input("Enter score (Enter -9 to end): "))
#if score == -9:
#    print("Please enter atleast one score")
#    score = int(input("Enter score (Enter -9 to end): "))

#while score != -9:
#    total += score  
#    count += 1  
#    score = int(input("Enter score (Enter -9 to end): "))

#average = float( total ) / count
#print("Class average is", average)

##Ex 3
#while True:
#    n = input("Please enter an integer: ")
#    try:
#        n = int(n)
#        break
    
#    except ValueError:
#        print("Requires a valid integer! Please try again.")

#print("You successfully entered an integer.")

##Ex 4 to 7
#total=0

#num1=input("Enter 1st number")
#num2=input("Enter 2nd number")
#num3=input("Enter 3rd number")
#num4=input("Enter 4th number")
#num5=input("Enter 5th number")

#total=num1+num2+num3+num4+num5
#total = 0

#for i in range(5):
#    if i == 0:
#        num = input("Enter 1st number: ")
#    elif i == 1:
#        num = input("Enter 2nd number: ")
#    elif i == 2:
#        num = input("Enter 3rd number: ")
#    else:
#        num = input(f"Enter {i + 1}th number: ")
#    total += float(num)

#print(f"The total of the 5 numbers is: {total}")

##Ex 5
#for i in range (1,21):
#    if i % 2 != 0:
#        print(i)

##Ex 6
#num_stars = int(input("How many stars do you want? "))

#for i in range(num_stars):
#    print("*", end="")

##Ex 7
#import random

#count = 0


#num_rolls = 100

#for i in range(num_rolls):
#    dice1 = random.randint(1, 6)  
#    dice2 = random.randint(1, 6)  

#    if dice1 == dice2:
#        count += 1  


#print(f"Out of {num_rolls} you rolled {count} doubles")

##Ex 8
#for i in range(1, 4):
#    print("*" * i)

##B
#for i in range(3,0,-1):
#    print(""*(3-i), "*"*i)

##Ex 9
#while True:
#    print("\nMenu:")
#    print("1. Option 1")
#    print("2. Option 2")
#    print("3. Option 3")
#    print("4. Quit")

#    try:
#        choice = int(input("Enter your choice (1/2/3/4): "))

#        if choice == 1:
#            print("You chose Option 1")
#        elif choice == 2:
#            print("You chose Option 2")
#        elif choice == 3:
#            print("You chose Option 3")
#        elif choice == 4:
#            print("Goodbye!")
#            break
#        else:
#            print("Unrecognized option! Please select a valid option.")

#    except ValueError:
#        print("Invalid input! Please enter a number.")

##Ex 10
#import random

#hidden_number = random.randint(1, 20)

#max_attempts = 5
#attempts = 0

#while attempts < max_attempts:
#    guess = int(input("Guess the number between 1 and 20: "))
#    attempts += 1

#    if guess == hidden_number:
#        print(f"Congratulations! You guessed the number {hidden_number} in {attempts} attempts.")
#        break
#    else:
#        if guess < hidden_number:
#            print("The hidden number is higher than your guess.")
#        else:
#            print("The hidden number is lower than your guess.")


#if attempts == max_attempts:
#    print(f"Sorry, you didn't guess the number. The hidden number was {hidden_number}.")



