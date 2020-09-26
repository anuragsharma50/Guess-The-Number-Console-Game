# Generate a Random number
import random
randomNum = random.random()*1000//10

# Initialize count to zero
count = 0

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

check(count)
