import pandas
import random
import math
import decimal
from decimal import Decimal, ROUND_HALF_DOWN

movesTable = pandas.read_csv("Moves.csv")

def getEffectivenessModifier(moveType, targetTypes):
    return 1

def getAttackDefendStats(attacker, target, moveCategory):
    if moveCategory == "Special":
        return [attacker.SpecialAttack, target.SpecialDefense]
    if moveCategory == "Attack":
        return [attacker.Attack, target.Defense]

def getMoveData(moveName):
    moveInfo = movesTable.loc[movesTable['Name'] == moveName].iloc[0]
    return moveInfo

def getCritMod(attacker, moveData, target):
    return 1

def getRandomMod():
    return 1

def getStabMod(attacker, moveData):
    return 1

def getBurnMod(attacker, moveData):
    return 1

def getOtherMod(attack, moveData, target):
    return 1

def roundHalfDown(input):
    return int(Decimal(input).quantize(Decimal('0'), ROUND_HALF_DOWN))

def dealDamage(attacker, moveData, target):
    typeEffectiveness = getEffectivenessModifier(moveData['Type'], target.types)
    if typeEffectiveness == 0:
        print("Immune")
        return

    effectiveStats = getAttackDefendStats(attacker, target, moveData['Category'])
    attackingStat = effectiveStats[0]
    defendingStat = effectiveStats[1]
    targetNumMod = 1
    weatherMod = 1
    glaiveRushMod = 1
    critMod = getCritMod(attacker, moveData, target)
    randomMod = getRandomMod()
    stabMod = getStabMod(attacker, moveData)
    burnMod = getBurnMod(attacker, moveData)
    otherMod = getOtherMod(attacker, moveData, target)

    #damage = (((2 * attacker.level)/5 + 2) * int(moveData['Base Power']) * attackingStat / defendingStat) / 50 + 2

    damage = 2 * attacker.level
    damage = roundHalfDown(damage / 5) + 2
    damage = damage * moveData['Base Power']
    damage = roundHalfDown(damage * attackingStat / defendingStat)
    damage = roundHalfDown(damage / 50) + 2

    damage = roundHalfDown(damage * targetNumMod) 
    damage = roundHalfDown(damage * weatherMod) 
    damage = roundHalfDown(damage * glaiveRushMod) 
    damage = math.floor(damage * critMod) 
    damage = math.floor(damage * randomMod)
    damage = roundHalfDown(damage * stabMod)
    damage = math.floor(damage * typeEffectiveness) 
    damage = roundHalfDown(damage * burnMod)
    damage = roundHalfDown(damage * otherMod)

    # damage = math.floor(damage)

    if damage == 0:
        damage = 1

    print(damage)



def useMove(attacker, moveName, target):
    moveData = getMoveData(moveName)
    print(f"{attacker.name} used {moveName}!")

    if not moveData['Category'] == 'Status':
        dealDamage(attacker, moveData, target)

    

    print(f"{target.name} was hit!")