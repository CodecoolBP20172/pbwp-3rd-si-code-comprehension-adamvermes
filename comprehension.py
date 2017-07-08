import random  # import random module

guessesTaken = 0  # make the value of guessesTaken variable equal zero

print('Hello! What is your name?')  # print to console
myName = input()  # make the value of myName variable equal user input

number = random.randint(1, 20)  # make the number variable return a random integer between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # print to console with string plus MyName

while guessesTaken < 6:  # put into a while loop and if guessesTaken is less than 6
    print('Take a guess.')  # print to console
    guess = input()  # make guess variable equal user input
    guess = int(guess)  # convert guess variable to an integer

    guessesTaken += 1  # add 1 to guessesTaken variable

    if guess < number:  # if guess is less than the randomized number
        print('Your guess is too low.')  # then print to console

    if guess > number:  # if guess is more than the randomized number
        print('Your guess is too high.')  # then print to console

    if guess == number:  # if guess is equal to the randomized number
        break  # then break loop

if guess == number:  # if guess is equal to the randomized number
    guessesTaken = str(guessesTaken)  # convert guessesTaken to to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # print the strings to console plus MyName plus guessesTaken

if guess != number:  # if guess is not equal to the randomized number
    number = str(number)  # then convert number to a string
    print('Nope. The number I was thinking of was ' + number)  # and print string plus number
