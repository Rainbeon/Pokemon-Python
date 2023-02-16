import math
import pandas

class Pokemon:
    def __init__(self, pokemonData):
        self.name = pokemonData['Name']
        self.level = 100

        #Lookup from sheet
        self.types = [pokemonData['Type 1']]
        if not pandas.isna(pokemonData['Type 2']):
            self.types.append(pokemonData['Type 2'])

        #Should be a better way to do this?
        self.possibleAbilities = [pokemonData['Ability 1']]
        if not pandas.isna(pokemonData['Ability 2']):
            self.possibleAbilities.append(pokemonData['Ability 2'])
        if not pandas.isna(pokemonData['Hidden Ability']):
            self.possibleAbilities.append(pokemonData['Hidden Ability'])

        self.ability = self.possibleAbilities[0]

        self.baseHP = pokemonData['HP']
        self.baseAttack = pokemonData['Attack']
        self.baseDefense = pokemonData['Defense']
        self.baseSpAttack = pokemonData['Special Attack']
        self.baseSpDefense = pokemonData['Special Defense']
        self.baseSpeed = pokemonData['Speed']

        self.IVs = [31, 31, 31, 31, 31, 31]
        self.EVs = [0, 0, 0, 0, 0, 0]

        self.maxHP = self.calculateMaxHP(self.baseHP, self.level, self.IVs[0], self.EVs[0])
        self.currentHP = self.maxHP

        self.gender = "Genderless"
        self.level = "100" 

        self.ability = ""
        self.moves = []

    def calculateMaxHP(self, baseHP, level, IVs, EVs):
        maxHP = math.floor(0.01 * (2 * baseHP + IVs + math.floor(0.25 * EVs)) * level) + level + 10
        return maxHP
    
    def calculateStat(self, baseStat, EVs, IVs):
        return 1

    def getHealthPercent(self):
        return (str)(self.currentHP * 100 / self.maxHP)

    def printBasic(self):
        print("=========================")
        print(self.name)
        print(*self.types, sep=", ")
        print("HP: " + self.getHealthPercent() + "%")

    def printDetailed(self):
        print("=========================")
        print(self.name)
        print(*self.types, sep=", ")
        print("HP: " + self.getHealthPercent() + "% (" + str(self.currentHP) + "/" + str(self.maxHP) + ")")


#def method():
#    print("Pokemon")