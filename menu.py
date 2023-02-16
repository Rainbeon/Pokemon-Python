import random
import battle
import pokemon
import pandas
from configparser import ConfigParser

def loadSettings():
    print('Loading...')
    global pokemonData 
    pokemonData = pandas.read_csv("Pokemon.csv")

def getPokemonInfo(name):
    pokeInfo = pokemonData.loc[pokemonData['Name'] == name].iloc[0]
    return pokeInfo

def createPokemon(name):
    pokeInfo = getPokemonInfo(name)
    newPokemon = pokemon.Pokemon(pokeInfo)
    return newPokemon

def randomBattleInit():
    print('Sorry, random battles are not yet implemented!')

def teamBattleInit():
    #Import teams from Smogon
    print('Sorry, team battles are not yet implemented!')

def debugBattleInit():
    Team1 = []
    Team2 = []

    Team1.append(createPokemon('Magnezone'))
    #Team1.append(pokemon.Pokemon('Latias'))

    Team2.append(createPokemon('Tatsugiri'))
    #Team2.append(pokemon.Pokemon('Chandelure'))

    battle.battleInit(Team1, Team2)

def settingsMenu():
    print('Settings:')

def startMenu():
    print('Welcome to Pokemon Python!')

    print('What would you like to do?')
    print('1. Random Battle!')
    print('2. Team-built Battle!')
    print('3. Debug Battle!')
    print('4. Settings')

    print(pokemonData.head(1))

    userInput = input()

    match userInput:
        case '1':
            randomBattleInit()
        case '2':
            teamBattleInit()
        case '3':
            debugBattleInit()
        case '4': 
            settingsMenu()
        case _:
            print('Invalid input!')
        
loadSettings()
startMenu()