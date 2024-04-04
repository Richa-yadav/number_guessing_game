import random
import math
lower_bound=int(input("Enter lower bound:- "))
upper_bound=int(input("Enter upper bound:- "))

#generating randon numbers between upper and lower bound
x=random.randint(lower_bound,upper_bound)

#calculating minimum number of cases required
print("\n\tYou have only ", 
      round(math.log(upper_bound-lower_bound+1,2)),
      " chances to guessing the right integer!\n")

#initializing the number of count that person is going to take
count=0


while count < math.log(upper_bound-lower_bound+1,2):
    count+=1
    guess=int(input("Guess a number:- "))

    if x==guess:
        print("You guessed correct in ", count, " try!")
        #once guessed, loop ends
        break
    elif x>guess:
        print("You guessed too small!")
    else:
        print("You guessed too high!")
#if guessing is more than minimum required attempts, print this.
if count>=math.log(upper_bound-lower_bound+1,2):
    print("\nThe number is %d" %x)
    print("\tBetter luck next time!!")
