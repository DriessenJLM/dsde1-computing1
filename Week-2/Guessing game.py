# Here i am trying to do a guessing game, in order for this to work, i need to prompt an answer, compare this answer to a previously generated random number and then come back with an answer,
print('Hello welcome to the guessing game!')
print('what is your name?')
Username = input()
print("Hi " + Username)
print('lets play a game!')

print('pick a number between 1 and 10')
import random
ComputerGuess = random.randint(1,10)
UserGuess = input()
UserGuess = int(UserGuess)


print(UserGuess==ComputerGuess)
import sys
if UserGuess==ComputerGuess:
    sys.exit()
if UserGuess != ComputerGuess:
    print('Oh dear you were wrong')
print('try again')

print('pick a number between 1 and 10')
ComputerGuess2 = random.randint(1,10)
UserGuess2 = input()
UserGuess2 = int(UserGuess2)
print(UserGuess2==ComputerGuess2)

if UserGuess2 != ComputerGuess2 and UserGuess!=ComputerGuess2:
    print('wrong again!')
if UserGuess2 == ComputerGuess2:
    sys.exit()

print('3rd time lucky?')
print('Do you want to play again?')
print('choose Y/N')
third = input()
import sys

if third == 'Y':
    print('Lets play again!')
elif third != 'Y':
    print('I am sad to see you go')
    sys.exit()



print('pick a number between 1 and 10')
ComputerGuess3 = random.randint(1,10)
UserGuess3 = input()
UserGuess3 = int(UserGuess3)
print(UserGuess3==ComputerGuess3)

if UserGuess3 == ComputerGuess3:
    print("congrats you did it")
if UserGuess3 != ComputerGuess3:
    print('better luck next time')
# this one primarilly demonstrates the use of the if function, 