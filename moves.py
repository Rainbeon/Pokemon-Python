import pandas
import random
import math
import decimal
from decimal import Decimal, ROUND_HALF_DOWN

movesTable = pandas.read_csv("Moves.csv")

def applyModifier(targetTypes, typeName, effect):
    if not typeName in targetTypes:
        return 1
    
    if effect == "Weak":
        return 2
    elif effect == 'Resist':
        return 1/2
    elif effect == "Immune":
        return 0
    else:
        print(f"applyModifier(): {effect} not recognized as a valid type effect, under {typeName}")

def getEffectivenessModifier(moveType, targetTypes):
    modifier = 1

    match moveType:
        case 'Normal':
            modifier *= applyModifier(targetTypes, 'Rock', 'Resist')
            modifier *= applyModifier(targetTypes, 'Steel', 'Resist')
            modifier *= applyModifier(targetTypes, 'Ghost', 'Immune')
        case 'Fighting':
            modifier *= applyModifier(targetTypes, 'Dark', 'Weak')
            modifier *= applyModifier(targetTypes, 'Ice', 'Weak')
            modifier *= applyModifier(targetTypes, 'Normal', 'Weak')
            modifier *= applyModifier(targetTypes, 'Rock', 'Weak')
            modifier *= applyModifier(targetTypes, 'Steel', 'Weak')
            modifier *= applyModifier(targetTypes, 'Bug', 'Resist')
            modifier *= applyModifier(targetTypes, 'Fairy', 'Resist')
            modifier *= applyModifier(targetTypes, 'Flying', 'Resist')
            modifier *= applyModifier(targetTypes, 'Poison', 'Resist')
            modifier *= applyModifier(targetTypes, 'Psychic', 'Resist')
            modifier *= applyModifier(targetTypes, 'Ghost', 'Immune')
        case 'Flying':
            modifier *= applyModifier(targetTypes, 'Bug', 'Weak')
            modifier *= applyModifier(targetTypes, 'Fighting', 'Weak')
            modifier *= applyModifier(targetTypes, 'Grass', 'Weak')
            modifier *= applyModifier(targetTypes, 'Electric', 'Resist')
            modifier *= applyModifier(targetTypes, 'Rock', 'Resist')
            modifier *= applyModifier(targetTypes, 'Steel', 'Resist')
        case 'Poison':
            modifier *= applyModifier(targetTypes, 'Fairy', 'Weak')
            modifier *= applyModifier(targetTypes, 'Grass', 'Weak')
            modifier *= applyModifier(targetTypes, 'Poison', 'Resist')
            modifier *= applyModifier(targetTypes, 'Ground', 'Resist')
            modifier *= applyModifier(targetTypes, 'Rock', 'Resist')
            modifier *= applyModifier(targetTypes, 'Ghost', 'Resist')
            modifier *= applyModifier(targetTypes, 'Steel', 'Immune')
        case 'Ground':
            modifier *= applyModifier(targetTypes, 'Electric', 'Weak')
            modifier *= applyModifier(targetTypes, 'Fire', 'Weak')
            modifier *= applyModifier(targetTypes, 'Poison', 'Weak')
            modifier *= applyModifier(targetTypes, 'Rock', 'Weak')
            modifier *= applyModifier(targetTypes, 'Steel', 'Weak')
            modifier *= applyModifier(targetTypes, 'Bug', 'Resist')
            modifier *= applyModifier(targetTypes, 'Grass', 'Resist')
            modifier *= applyModifier(targetTypes, 'Flying', 'Immune')
        case 'Rock':
            modifier *= applyModifier(targetTypes, 'Bug', 'Weak')
            modifier *= applyModifier(targetTypes, 'Fire', 'Weak')
            modifier *= applyModifier(targetTypes, 'Flying', 'Weak')
            modifier *= applyModifier(targetTypes, 'Ice', 'Weak')
            modifier *= applyModifier(targetTypes, 'Fighting', 'Resist')
            modifier *= applyModifier(targetTypes, 'Ground', 'Resist')
            modifier *= applyModifier(targetTypes, 'Steel', 'Resist')
        case 'Bug':
            modifier *= applyModifier(targetTypes, 'Dark', 'Weak')
            modifier *= applyModifier(targetTypes, 'Grass', 'Weak')
            modifier *= applyModifier(targetTypes, 'Psychic', 'Weak')
            modifier *= applyModifier(targetTypes, 'Fairy', 'Resist')
            modifier *= applyModifier(targetTypes, 'Fighting', 'Resist')
            modifier *= applyModifier(targetTypes, 'Fire', 'Resist')
            modifier *= applyModifier(targetTypes, 'Flying', 'Resist')
            modifier *= applyModifier(targetTypes, 'Ghost', 'Resist')
            modifier *= applyModifier(targetTypes, 'Poison', 'Resist')
            modifier *= applyModifier(targetTypes, 'Steel', 'Resist')
        case 'Ghost':
            modifier *= applyModifier(targetTypes, 'Ghost', 'Weak')
            modifier *= applyModifier(targetTypes, 'Psychic', 'Weak')
            modifier *= applyModifier(targetTypes, 'Dark', 'Resist')
            modifier *= applyModifier(targetTypes, 'Normal', 'Immune')
        case 'Steel':
            modifier *= applyModifier(targetTypes, 'Fairy', 'Weak')
            modifier *= applyModifier(targetTypes, 'Ice', 'Weak')
            modifier *= applyModifier(targetTypes, 'Rock', 'Weak')
            modifier *= applyModifier(targetTypes, 'Electric', 'Resist')
            modifier *= applyModifier(targetTypes, 'Fire', 'Resist')
            modifier *= applyModifier(targetTypes, 'Steel', 'Resist')
            modifier *= applyModifier(targetTypes, 'Water', 'Resist')
        case 'Fire':
            modifier *= applyModifier(targetTypes, 'Bug', 'Weak')
            modifier *= applyModifier(targetTypes, 'Grass', 'Weak')
            modifier *= applyModifier(targetTypes, 'Ice', 'Weak')
            modifier *= applyModifier(targetTypes, 'Steel', 'Weak')
            modifier *= applyModifier(targetTypes, 'Dragon', 'Resist')
            modifier *= applyModifier(targetTypes, 'Fire', 'Resist')
            modifier *= applyModifier(targetTypes, 'Rock', 'Resist')
            modifier *= applyModifier(targetTypes, 'Water', 'Resist')
        case 'Water':
            modifier *= applyModifier(targetTypes, 'Fire', 'Weak')
            modifier *= applyModifier(targetTypes, 'Ground', 'Weak')
            modifier *= applyModifier(targetTypes, 'Rock' 'Weak')
            modifier *= applyModifier(targetTypes, 'Dragon', 'Resist')
            modifier *= applyModifier(targetTypes, 'Grass', 'Resist')
            modifier *= applyModifier(targetTypes, 'Water', 'Resist')
        case 'Grass':
            modifier *= applyModifier(targetTypes, 'Ground', 'Weak')
            modifier *= applyModifier(targetTypes, 'Rock', 'Weak')
            modifier *= applyModifier(targetTypes, 'Water', 'Weak')
            modifier *= applyModifier(targetTypes, 'Bug', 'Resist')
            modifier *= applyModifier(targetTypes, 'Dragon', 'Resist')
            modifier *= applyModifier(targetTypes, 'Fire', 'Resist')
            modifier *= applyModifier(targetTypes, 'Flying', 'Resist')
            modifier *= applyModifier(targetTypes, 'Grass', 'Resist')
            modifier *= applyModifier(targetTypes, 'Poison', 'Resist')
            modifier *= applyModifier(targetTypes, 'Steel', 'Resist')
        case 'Electric':
            modifier *= applyModifier(targetTypes, 'Flying', 'Weak')
            modifier *= applyModifier(targetTypes, 'Water', 'Weak')
            modifier *= applyModifier(targetTypes, 'Dragon', 'Resist')
            modifier *= applyModifier(targetTypes, 'Electric', 'Resist')
            modifier *= applyModifier(targetTypes, 'Grass', 'Resist')
            modifier *= applyModifier(targetTypes, 'Ground', 'Immune')
        case 'Psychic':
            modifier *= applyModifier(targetTypes, 'Fighting', 'Weak')
            modifier *= applyModifier(targetTypes, 'Poison', 'Weak')
            modifier *= applyModifier(targetTypes, 'Psychic', 'Resist')
            modifier *= applyModifier(targetTypes, 'Steel', 'Resist')
            modifier *= applyModifier(targetTypes, 'Dark', 'Immune')
        case 'Ice':
            modifier *= applyModifier(targetTypes, 'Dragon', 'Weak')
            modifier *= applyModifier(targetTypes, 'Flying', 'Weak')
            modifier *= applyModifier(targetTypes, 'Grass', 'Weak')
            modifier *= applyModifier(targetTypes, 'Ground', 'Weak')
            modifier *= applyModifier(targetTypes, 'Fire', 'Resist')
            modifier *= applyModifier(targetTypes, 'Ice', 'Resist')
            modifier *= applyModifier(targetTypes, 'Steel', 'Resist')
            modifier *= applyModifier(targetTypes, 'Water', 'Resist')
        case 'Dragon':
            modifier *= applyModifier(targetTypes, 'Dragon', 'Weak')
            modifier *= applyModifier(targetTypes, 'Steel', 'Resist')
            modifier *= applyModifier(targetTypes, 'Fairy', 'Immune')
        case 'Dark':
            modifier *= applyModifier(targetTypes, 'Ghost', 'Weak')
            modifier *= applyModifier(targetTypes, 'Psychic', 'Weak')
            modifier *= applyModifier(targetTypes, 'Dark', 'Resist')
            modifier *= applyModifier(targetTypes, 'Fairy', 'Resist')
            modifier *= applyModifier(targetTypes, 'Fighting', 'Resist')
        case 'Fairy':
            modifier *= applyModifier(targetTypes, 'Dark', 'Weak')
            modifier *= applyModifier(targetTypes, 'Dragon', 'Weak')
            modifier *= applyModifier(targetTypes, 'Fighting', 'Weak')
            modifier *= applyModifier(targetTypes, 'Fire', 'Resist')
            modifier *= applyModifier(targetTypes, 'Poison', 'Resist')
            modifier *= applyModifier(targetTypes, 'Steel', 'Resist')

    print(f"Modifier = {modifier}")
    return modifier

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
    if moveData['Type'] in attacker.types:
        return 1.5

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

    originalHpPercent = target.getHealthPercent()
    target.takeDamage(damage)
    newHpPercent = target.getHealthPercent()
    lostHpPercent = round(originalHpPercent - newHpPercent, 1)

    print(f"({target.name} lost {lostHpPercent}% of its health!)")

def useMove(attacker, moveName, target):
    moveData = getMoveData(moveName)
    print(f"{attacker.name} used {moveName}!")

    if not moveData['Category'] == 'Status':
        dealDamage(attacker, moveData, target)