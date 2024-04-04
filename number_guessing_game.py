import random
import math
lower_bound=int(input("Enter lower bound:- "))
upper_bound=int(input("Enter upper bound:- "))
x=random.randint(lower_bound,upper_bound)
print("\n\tYou have only ", 
      round(math.log(upper_bound-lower_bound+1,2)),
      " chances to guessing the right integer!\n")
count=0
while count < math.log(upper_bound-lower_bound+1,2):
    count+=1
    guess=int(input("Guess a number:- "))

    if x==guess:
        print("You guessed correct in ", count, " try!")
        break
    elif x>guess:
        print("You guessed too small!")
    else:
        print("You guessed too high!")
if count>=math.log(upper_bound-lower_bound+1,2):
    print("\nThe number is %d" %x)
    print("\tBetter luck next time!!")
