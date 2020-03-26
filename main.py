import random
import os

FILENAME = 'boggleboard.txt'
GRIDLINE = '+---+---+---+---+\n'
DICE_LIST = [
    ['R', 'I', 'F', 'O', 'B', 'X'],
    ['I', 'F', 'E', 'H', 'E', 'Y'],
    ['D', 'E', 'N', 'O', 'W', 'S'],
    ['U', 'T', 'O', 'K', 'N', 'D'],
    ['H', 'M', 'S', 'R', 'A', 'O'],
    ['L', 'U', 'P', 'E', 'T', 'S'],
    ['A', 'C', 'I', 'T', 'O', 'A'],
    ['Y', 'L', 'G', 'K', 'U', 'E'],
    ['Qu', 'B', 'M', 'J', 'O', 'A'],
    ['E', 'H', 'I', 'S', 'P', 'N'],
    ['V', 'E', 'T', 'I', 'G', 'N'],
    ['B', 'A', 'L', 'I', 'Y', 'T'],
    ['E', 'Z', 'A', 'V', 'N', 'D'],
    ['R', 'A', 'L', 'E', 'S', 'C'],
    ['U', 'W', 'I', 'L', 'R', 'G'],
    ['P', 'A', 'C', 'E', 'M', 'D'],
]

def main():
    while (True):
        # get random ordering of dice
        randomOrdering = getRandomDiceOrdering()
        print(randomOrdering)

        # for each die, get a random letter
        boggleBoardLetters = [getRandomLetterForDie(idx) for idx in randomOrdering]
        print(boggleBoardLetters)

        boggleBoardOutput = getOutputStrForLetters(boggleBoardLetters)
        print(boggleBoardOutput)

        with open(FILENAME, 'w') as f:
            f.write(boggleBoardOutput)
        
        os.system(FILENAME)



def buildLineForLetters(lineLetters):
    line = '|'
    for letter in lineLetters:
        if (letter == 'Qu'):
            line += ' {}|'.format(letter)
        else:
            line += ' {} |'.format(letter)
    return line + '\n'


def getOutputStrForLetters(letters):
    output = GRIDLINE
    for x in range(0, 4):
        output += buildLineForLetters(letters[x*4:(x+1)*4]) + GRIDLINE
    return output

def getRandomLetterForDie(dieIdx):
    return DICE_LIST[dieIdx][random.randint(0, len(DICE_LIST[dieIdx]) - 1)]

def getRandomDiceOrdering():
    masterDiceNumList = list(range(16))
    randomOrderList = []
    for x in range(16):
        randomOrderList.append(masterDiceNumList.pop(random.randint(0, len(masterDiceNumList) - 1)))
    return randomOrderList

main()
