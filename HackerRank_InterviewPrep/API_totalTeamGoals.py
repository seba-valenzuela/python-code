

# Objective: Given a team name and year, return the total number of goals by that team

# Endpoint URL: https://jsonmock.hackerrank.com/api/football_matches

import requests

def getTotalGoals(team, year):
    total_goals = 0

    # Once for team1, then again for team2
    team_side = 1
    while team_side <= 2:
        # Get all results for (current team in while loop), for the given year
        url = 'https://jsonmock.hackerrank.com/api/football_matches?team' + str(team_side) + '=' + str(team) + '&year=' + str(year)
        r_team = requests.get(url)
        
        # This filtered data shows only results for the specified team and year
        data = r_team.json()['data']
        
        totalPages = r_team.json()['total_pages']

        # If there is only 1 page do this, else - increment through pages
        if totalPages == 1:
            # increment through all matches, adding their goals up
            for match in data:
                total_goals += int(match['team' + str(team_side) + 'goals'])
        
        else:
            # Loop from page 1 to the last page
            for page in range(1, totalPages+1):
                r_team = requests.get(url + '&page=' + page)
                # On each page, add up goals from each match
                for match in data:
                    total_goals += match['team' + team + 'goals']
        team_side += 1
    return total_goals

print(getTotalGoals('Barcelona', 2013))


