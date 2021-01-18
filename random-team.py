#!usr/bin/python3

# K.Wilczynski 2020

from random import choice


def random_teams(users, desired_team_size, organizers = [""]):
    teams = []
    for _ in range(number_of_teams):
        teams.append([])

    # If organizers preference was supplied, assign the organizers as the first user in each team
    if len(organizers) == number_of_teams:
        for team in teams:
            organizer = organizers.pop()
            team.append(organizer)
            users.remove(organizer)
    elif len(organizers) == 1 and organizers[0] == "":
        print("No organizers supplied, they will be chosen randomly (the first person in each team)")
        pass
    else:
        raise ValueError("You have supplied a list of organizers that is different in length than the number of teams")

    # Assign the users into teams randomly, until each team has the desired team size
    for team in teams:
        while len(team) < desired_team_size:
            random_user = choice(users)
            team.append(random_user)
            users.remove(random_user)

    # Assign the remaining users to the teams one by one, starting from the last team
    if len(users) != 0:
        assign_to = number_of_teams - 1
        while len(users) != 0:
            teams[assign_to].append(users.pop())
            assign_to -= 1

    return teams


def print_teams(teams):
    # Print out the generated teams (teams: list of lists)
    i = 1
    for team in teams:
        print("\nTeam {0}:".format(i))
        i += 1
        for member in team:
            print(member)

if __name__ == "__main__":
    # Inputs
    desired_team_size = int(input("Minimum team size (maximum may be 1 more member in some teams): "))
    users = input("List of usernames separated by whitespaces: ").split(" ")
    number_of_teams = len(users) // desired_team_size
    print("There will be {0} teams according to the entered data".format(number_of_teams))
    organizers = input("List of organizers separated by whitespaces (optional, must be as many as the number of teams): ").split(" ")

    # Assign users to groups randomly
    teams = random_teams(users, desired_team_size, organizers)

    # Print out the randomly generated teams
    print_teams(teams)