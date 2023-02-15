import pandas

class Pokemon:
    
    def __init__(self, name):
        self.name = name

        pokemonSheet = pandas.read_csv("Pokemon.csv")

        print(pokemonSheet.head(1))
        sheetIndex = pokemonSheet.iloc[0]
        print(sheetIndex)

        #Lookup from sheet
        self.types = ["Normal"]
        self.baseHP = 10
        self.baseAttack = 10
        self.baseDefense = 10
        self.baseSpAttack = 10
        self.baseSpDefense = 10
        self.baseSpeed = 10

        self.IVs = [0, 0, 0, 0, 0, 0]
        self.EVs = [0, 0, 0, 0, 0, 0]

        self.maxHP = 10
        self.currentHP = self.maxHP

        self.gender = "Genderless"
        self.level = "100" 

        self.ability = ""
        self.moves = []

    def getHealthPercent(self):
        return (str)(self.currentHP * 100 / self.maxHP)

    def printPokemon(self):
        print("=========================")
        print(self.name)
        print(*self.types, sep=", ")
        print("HP: " + self.getHealthPercent() + "%")


#def method():
#    print("Pokemon")