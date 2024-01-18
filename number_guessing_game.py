import random

Max_Range = input("Enter the the max range to generate the number ")
guesses = 0

if (Max_Range.isdigit()):
    Max_Range = int(Max_Range)
if (Max_Range <= 0):
    print("please type a number larger than zero")
else:
    print("please type a number next time")
    quit()
    
random_number = random.randint(0,Max_Range)

while(True):
    guesses+=1
    user_input = int(input("Guess the Number: "))
    
    if (user_input.isdigit()):
        user_input = int(user_input)
    else:
        print("please type a number next time")
        continue

    if(user_input == random_number):
        print("You did a marvelous job!!!")
        break
    elif(user_input < random_number):
        print("Guessed Number is lower")
    else:
        print("Guessed number is higher")
        
print("you had it in", guesses ,"guesses")
    