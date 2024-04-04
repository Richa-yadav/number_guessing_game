import random
colors=['pink','green','yellow','white','red','black','blue','grey','purple','silver',
        'orange','brown']
color=random.choice(colors)
print("guess the characters of color: ")
guesses=''
turns=12 
while turns>0:
    incorrect_guess=0
    for char in color:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            incorrect_guess+=1
    if incorrect_guess==0:
        print("\nHurray......You win!!")
        print("The color is: ", color)
        break
    print()
    guess=input("guess a character: ")
    guesses+=guess
    if guess not in color:
        turns-=1
        print("Wrong guess..")
        print("You have ", +turns, "more guesses!")
        if turns==0:
            print("Better Luck next time!! The color is ", color)
