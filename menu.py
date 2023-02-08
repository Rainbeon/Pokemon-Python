import random
import battle
import pokemon
from configparser import ConfigParser

def loadSettings():
    print('Loading...')

def randomBattleInit():
    print('Sorry, random battles are not yet implemented!')

def teamBattleInit():
    #Import teams from Smogon
    print('Sorry, team battles are not yet implemented!')

def debugBattleInit():
    Team1 = []
    Team2 = []

    Team1.append(pokemon.Pokemon('Magnezone'))
    Team1.append(pokemon.Pokemon('Latias'))

    Team2.append(pokemon.Pokemon('Tatsugiri'))
    Team2.append(pokemon.Pokemon('Chandelure'))

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