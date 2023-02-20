import random
import pokemon
import pandas

def getTeamString(team):
    teamString = ""

    for pokemon in team:
        teamString += pokemon.name + " "

    return teamString

def printTeams(team1, team2):
    team1String = getTeamString(team1)
    team2String = getTeamString(team2)

    print(team1String + "vs " + team2String)

def printActions(selectedPokemon, team):
    print("=================")
    print(f"Actions for {selectedPokemon.name}:")
    selectedPokemon.printMoves()
    print("i. Show active pokemon information")

def actionSelect(activePokemon, team):
    printActions(activePokemon, team)
    userInput = input()

    return userInput

def battleInit(team1, team2):
    print('Battle start!')
    printTeams(team1, team2)

    battleActive = True

    activePokemonIndex1 = 0
    activePokemonIndex2 = 0

    print(team1[0].moves)

    team1[0].printDetailed()
    team2[0].printDetailed()

    while(battleActive):
        userInput1 = actionSelect(team1[activePokemonIndex1], team1)
        userInput2 = actionSelect(team2[activePokemonIndex2], team2)

        print(userInput1)
        battleActive = False