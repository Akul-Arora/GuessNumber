import random
print("NUMBER GUESSING GAME")
randomnumber=random.randint(1,9)

chances=1
print("Guess A Number Between 1 TO 9. You Have Five Chances. All The Best!!!")
while chances < 6:
    guess=int(input('Enter your Guess:-'))
    if guess==randomnumber:
        print("Congratulations!! You Won!!👍👍")
        break
    elif guess<randomnumber:
        print("Your Guess Was Too Low. Guess Some number higher than",guess)
    else:
        print("Your Guess Was Too High. Guess Some Number Lower than",guess)
    chances+=1
    if not chances < 6:
        print("You Lost!!😢😢 ‍The Number was",randomnumber)