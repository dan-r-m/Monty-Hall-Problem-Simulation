import random
import numpy as np
SIZE = 3
NUMATTEMPTS = 100000

#generate a 1D array of bools
#of size "size"
#all elements will be set to False
#except one which is randomly selected to be True
def generateDoors(size):
    randomIndex = np.random.randint(low=0, high=size, size=1)
    doors = np.zeros(size, dtype=bool)
    doors[randomIndex] = True
    return doors


#contestant recieves the doors
#and randomly guesses in range(0, size)
#the index of the guess is returned
def contestantGuess(doors, size):
    guess = np.random.randint(low=0, high=size, size=1)
    guess = guess.item(0)
    return guess

#Monty recieves the doors, and the contestant's
#guess. He then selects an index that is both
#False and not the contestants guess at random
#the index of Monty's selection is then returned
def monty(doors, guess):
    for door in range(0, doors.size):
        if door == guess:
            continue
        elif doors[door] == False:
            return door

#recieves the doors, the contestant's original
#guess, and the door Monty revealed
#returns the index of the remaining door
def doorSwitch(doors, guess, montysDoor):
    for door in range(0, doors.size):
        if door == guess or door == montysDoor:
            continue
        else:
            return door
    

#shows off the whole process of a round
#from start to finish (where contestant always switches doors)
#with print statements to justify the logic
def demo():
    doors = generateDoors(SIZE)
    print(doors)
    guess = contestantGuess(doors, SIZE)
    print("the contestant's guess is: ",  guess)
    montysDoor = monty(doors, guess)
    print("monty reveals the goat behind door: ", montysDoor)
    finalGuess = doorSwitch(doors, guess, montysDoor)
    print("Finally, the contestant picks: ", finalGuess)
    if doors[finalGuess] == True:
        return True
    else:
        return False

#shows off the whole process of a round
#from start to finish (where contestant never switches doors)
#with print statements to justify the logic
def demoNoSwitch():
    doors = generateDoors(SIZE)
    print(doors)
    guess = contestantGuess(doors, SIZE)
    print("the contestant's guess is: ",  guess)
    montysDoor = monty(doors, guess)
    print("monty reveals the goat behind door: ", montysDoor)
    finalGuess = guess
    print("Finally, the contestant picks: ", finalGuess)
    if doors[finalGuess] == True:
        return True
    else:
        return False

#just goes through a round
#from start to finish (where contestant always switches doors)
#returns True if the contestant was correct
#and returns False if the contestant was not correct
def roundWithSwitch():
    doors = generateDoors(SIZE)
    guess = contestantGuess(doors, SIZE)
    montysDoor = monty(doors, guess)
    finalGuess = doorSwitch(doors, guess, montysDoor)
    if doors[finalGuess] == True:
        return True
    else:
        return False

#just goes through a round
#from start to finish (where contestant never switches doors)
#returns True if the contestant was correct
#and returns False if the contestant was not correct
def roundNoSwitch():
    doors = generateDoors(SIZE)
    guess = contestantGuess(doors, SIZE)
    montysDoor = monty(doors, guess)
    finalGuess = guess
    if doors[finalGuess] == True:
        return True
    else:
        return False

if __name__ == '__main__':
    correct = 0
    correctNoSwitch = 0
    demo_mode = False

    if demo_mode:
        for i in range(0, 3):
            demo()
            demoNoSwitch()
            print("\n")


    if not demo_mode:
        for i in range(0, NUMATTEMPTS):
                if roundWithSwitch():
                    correct = correct+1
                if roundNoSwitch():
                    correctNoSwitch = correctNoSwitch+1
        print("Here's how we did:...")
        print("When we always switch doors:", correct, "guesses correct out of", NUMATTEMPTS, "\nThat's", correct/NUMATTEMPTS*100, "%.")
        print("When we never switch doors:", correctNoSwitch, "guesses correct out of", NUMATTEMPTS, "\nThat's", correctNoSwitch/NUMATTEMPTS*100, "%.")
