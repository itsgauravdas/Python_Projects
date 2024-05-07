#Importing libraries
import random 
import math 

#Taking input from the user
lower=int(input("Enter lower bound:-"))
upper=int(input("Enter upper bound:-"))

#System generating number between 2 limits
x=random.randint(lower,upper)

#Printing the number of guess according to users input 
print("\n\tYou've only",round(math.log(upper-lower+1,2)),"chances to guess the integer")

count=0

#Loop 
while count<math.log(upper-lower+1,2):
    count+=1
    guess=int(input("Guess a number:-"))

    if x==guess:
        print("Congratulations you did it in ",count)
        break
    elif x>guess:
        print("You guess too small")
    elif x<guess:
        print("You guess too high")

#condition to check the number of chances to guess    
if count>=math.log(upper-lower+1,2):
    print("Better luck next time")
