# Imports
import random
import time

# Generate a Random number
randomNum = random.random()*1000//10

# Function to check the number
def check(count):
    count = count + 1
    # User Input 
    num = int(input("Enter a number "))

    # Comparision
    if(num == randomNum):
        print("Wow! you Win in ",count," moves :)")
    else:
        if(num < randomNum):
            print("Go Up")
            check(count)
        else:
            print("Go Down")
            check(count)

check(0)

# Start again
def restart():
    re = input("To start again press 1 or type Yes : ")
    if(re == 1 or re == 'Yes'):
        check(0)
    else:
        print("Byee")
        time.sleep(1)

restart()