import random

guessTaken = 0
chances = 3

print("Hello! What is your name?")
myName = input()

number = random.randint(1, 10)
print("Well, " + myName + " I am thinking of a number between 1 and 10. Guess what it is? You get " + str(chances) + " chances")

while guessTaken <= chances:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessTaken += 1

    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break


if guess == number:
    print("Good job " + myName + ". You guessed the number in " + str(guessTaken) + " guesses!!")

if guess != number:
    print("Nope. The number I was thinking was " + str(number))
