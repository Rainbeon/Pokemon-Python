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

        self.calculateAllStats()

        self.currentHP = self.maxHP
        self.fainted = False


        self.gender = "Genderless"
        self.level = 100 

        self.moves = []

    def calculateAllStats(self):
        self.maxHP = self.calculateMaxHP(self.baseHP, self.level, self.IVs[0], self.EVs[0])
        self.Attack = self.calculateStat(self.baseAttack, "Attack", self.level, self.IVs[1], self.EVs[1], self.nature)
        self.Defense = self.calculateStat(self.baseDefense, "Defense", self.level, self.IVs[2], self.EVs[2], self.nature)
        self.SpecialAttack = self.calculateStat(self.baseSpAttack, "Special Attack", self.level, self.IVs[3], self.EVs[3], self.nature)
        self.SpecialDefense = self.calculateStat(self.baseSpDefense, "Special Defense", self.level, self.IVs[4], self.EVs[4], self.nature)
        self.Speed = self.calculateStat(self.baseSpeed, "Speed", self.level, self.IVs[5], self.EVs[5], self.nature)

    def getNatureModifier(self, nature, statType):
        if statType == "Attack":
            if nature in ("Lonely", "Brave", "Adamant", "Naughty"):
                return 1.1
            if nature in ("Bold", "Timid", "Modest", "Calm"):
                return 0.9
            return 1
        
        if statType == "Defense":
            if nature in ("Bold", "Relaxed", "Impish", "Lax"):
                return 1.1
            if nature in ("Lonely", "Hasty", "Mild", "Gentle"):
                return 0.9
            return 1
        
        if statType == "Special Attack":
            if nature in ("Modest", "Mild", "Quiet", "Rash"):
                return 1.1
            if nature in ("Adamant", "Impish", "Jolly", "Careful"):
                return 0.9
            return 1
        
        if statType == "Special Defense":
            if nature in ("Calm", "Gentle", "Sassy", "Careful"):
                return 1.1
            if nature in ("Naughty", "Lax", "Naive", "Rash"):
                return 0.9
            return 1
        
        if statType == "Speed":
            if nature in ("Timid", "Hasty", "Jolly", "Naive"):
                return 1.1
            if nature in ("Brave", "Relaxed", "Quiet", "Sassy"):
                return 0.9
            return 1
        
        return 1

    def calculateMaxHP(self, baseHP, level, IV, EV):
        maxHP = math.floor(0.01 * (2 * baseHP + IV + math.floor(0.25 * EV)) * level) + level + 10
        return maxHP

    def calculateStat(self, baseStat, statType, level, IV, EV, nature):
        natureModifier = self.getNatureModifier(nature, statType)

        stat = (math.floor(0.01 * (2 * baseStat + IV + math.floor(0.25 * EV)) * level) + 5) * natureModifier
        return math.floor(stat)
    
    def addMove(self, moveName):
        if len(self.moves) >= 4:
            print(f"Could not add {moveName}, as the Pokemon already knows 4 moves.")
            return

        self.moves.append(moveName)
        print(self.moves)

    def getHealthPercent(self):
        return round(self.currentHP * 100 / self.maxHP, 1)

    def printBasic(self):
        print("=========================")
        print(self.name)
        print(*self.types, sep=", ")
        print("HP: " + self.getHealthPercent() + "%")

    def printDetailed(self):
        print("=========================")
        print(self.name)
        print(*self.types, sep=", ")
        print(f"HP: {self.getHealthPercent()}% ({self.currentHP}/{self.maxHP})")
        print(f"Ability: {self.ability}")
        print(f"Atk {self.Attack} / Def {self.Defense} / SpA {self.SpecialAttack} / SpD {self.SpecialDefense} / Spe {self.Speed}")

    def printMoves(self):
        moveString = ""

        for num in range(4):
            if num < len(self.moves):
                moveString += f"{num+1}. {self.moves[num]}"
            else:
                moveString += f"{num+1}. None"

            if num < 3:
                moveString += " | "

        print(moveString)

    def takeDamage(self, damageNum):
        if damageNum > self.currentHP:
            self.currentHP = 0
            self.fainted = True
        else:
            self.currentHP -= damageNum


#def method():
#    print("Pokemon")