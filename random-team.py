#!usr/bin/python3

# K.Wilczynski 2020

from random import choice

desired_team_size = int(input("Desired team size: "))

users = input("List of usernames separated by whitespaces: ").split(" ")

number_of_teams = len(users) // desired_team_size

teams = []
for _ in range(number_of_teams):
    teams.append([])

for team in teams:
    while len(team) < desired_team_size:
        random_user = choice(users)
        team.append(random_user)
        users.remove(random_user)

if len(users) != 0:
    assign_to = number_of_teams - 1
    while len(users) != 0:
        teams[assign_to].append(users.pop())
        assign_to -= 1

i = 1
for team in teams:
    print("\nTeam {0}:".format(i))
    i += 1
    for member in team:
        print(member)