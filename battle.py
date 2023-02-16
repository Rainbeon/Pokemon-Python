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

def battleInit(team1, team2):
    print('Battle start!')
    printTeams(team1, team2)

    team1[0].printDetailed()