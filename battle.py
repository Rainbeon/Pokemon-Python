import random
import pokemon
import pandas
import moves

actionQueue = []

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
    #TODO: Print switch targets
    print("i. Show active pokemon information")

def createAction(pokemon, teamNum, actionType, actionParameters):
    return [pokemon, teamNum, actionType, actionParameters]

def actionSelect(activePokemon, teamNumber, team):
    actionSelected = False
    while not actionSelected:
        printActions(activePokemon, team)
        userInput = input()

        match userInput:
            case '1' | '2' | '3' | '4':
                return createAction(activePokemon, teamNumber, 'Move', int(userInput)-1)
            case 'a':
                return createAction(activePokemon, teamNumber, 'Switch', 0)
            case 'b':
                return createAction(activePokemon, teamNumber, 'Switch', 1)
            case 'c':
                return createAction(activePokemon, teamNumber, 'Switch', 2)
            case 'd':
                return createAction(activePokemon, teamNumber, 'Switch', 3)
            case 'e':
                return createAction(activePokemon, teamNumber, 'Switch', 4)
            case 'f':
                return createAction(activePokemon, teamNumber, 'Switch', 5)
            case 'i':
                activePokemon.printDetailed()
            case _:
                print("Unknown action!")

def getOpposingPokemon(activePokemonList, attackerPokemon):
    if activePokemonList[0] == attackerPokemon:
        return activePokemonList[1]
    else:
        return activePokemonList[0]

def getActiveTeam(team1, team2, teamNum):
    if teamNum == 1:
        return team1
    else:
        return team2

def battleInit(team1, team2):
    print('Battle start!')
    printTeams(team1, team2)

    battleActive = True

    activePokemonList = [team1[0], team2[0]]

    print(team1[0].moves)

    team1[0].printDetailed()
    team2[0].printDetailed()

    while(battleActive):
        userInput1 = actionSelect(activePokemonList[0], 1, team1)
        actionQueue.append(userInput1)

        userInput2 = actionSelect(activePokemonList[1], 2, team2)
        actionQueue.append(userInput2)
        
        print(actionQueue)

        while(len(actionQueue) > 0):
            action = actionQueue.pop(0) #Does not care about speed/priority yet
            activePokemon = action[0]
            actionType = action[2]

            if actionType == "Switch":
                activeTeam = getActiveTeam(team1, team2, action[2])
                switchIndex = action[3]
                print(f"{activePokemon.name} switched to {activeTeam[switchIndex].name}!")

            if actionType == "Move":
                chosenMove = activePokemon.moves[action[3]]
                opposingPokemon = getOpposingPokemon(activePokemonList, activePokemon)
                moves.useMove(activePokemon, chosenMove, opposingPokemon)

        battleActive = False