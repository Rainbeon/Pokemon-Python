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
        self.nature = "Serious"

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

        self.Attack = self.calculateStat(self.baseAttack, "Attack", self.level, self.IVs[1], self.EVs[1], self.nature)
        self.Defense = self.calculateStat(self.baseDefense, "Defense", self.level, self.IVs[2], self.EVs[2], self.nature)
        self.SpecialAttack = self.calculateStat(self.baseSpAttack, "Special Attack", self.level, self.IVs[3], self.EVs[3], self.nature)
        self.SpecialDefense = self.calculateStat(self.baseSpDefense, "Special Defense", self.level, self.IVs[4], self.EVs[4], self.nature)
        self.Speed = self.calculateStat(self.baseSpeed, "Speed", self.level, self.IVs[5], self.EVs[5], self.nature)

        self.gender = "Genderless"
        self.level = "100" 

        self.moves = []

    def getNatureModifier(self, nature, statType):
        return 1

    def calculateMaxHP(self, baseHP, level, IV, EV):
        maxHP = math.floor(0.01 * (2 * baseHP + IV + math.floor(0.25 * EV)) * level) + level + 10
        return maxHP

    def calculateStat(self, baseStat, statType, level, IV, EV, nature):
        natureModifier = self.getNatureModifier(nature, statType)

        stat = (math.floor(0.01 * (2 * baseStat + IV + math.floor(0.25 * EV)) * level) + 5) * natureModifier
        return stat

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
        print("Ability: " + self.ability)
        print("Atk " + str(self.Attack) + " / Def " + str(self.Defense) + " / SpA " + str(self.SpecialAttack) + " / SpD " + str(self.SpecialDefense) + " / Spe " + str(self.Speed))


#def method():
#    print("Pokemon")