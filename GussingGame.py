import random
print("Number Gussing Game")

number=random.randint(1,9)
print("guess the number between 1 to 9")

chances=0

while chances < 5:
    guess=int(input("Enter your guess:-"))

    if(guess==number):
        print("congrats you won..!!")
    elif guess < number :
        print("your guess was too low : you guess a number higher than",guess)
    else:   
        print("guess was too heigh : guess a number than ",guess)

    chances +=1

if(not chances < 5):
        print("YOU LOST!! THE NUMBER IS ",number)