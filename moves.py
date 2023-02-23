import pandas
import random

movesTable = pandas.read_csv("Moves.csv")

def getEffectivenessModifier(moveType, targetTypes):
    return 1

def calcDamage(attacker, move, target):
    return 0

def useMove(attacker, moveName, target):
    print(f"{attacker.name} used {moveName}!")


    print(f"{target.name} was hit!")