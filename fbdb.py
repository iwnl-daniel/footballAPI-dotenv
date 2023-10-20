# daniel gregorio
# file for the FootBall DataBase(FBDB) class and mathoods
from requests import Session
# Football Database class
class FBDB:
    # class constructor
    def __init__(self, token):
        self.apiurl = 'http://api.football-data.org/v4/'
        self.headers = {'X-Auth-Token': token}
        self.session = Session()
        self.session.headers.update(self.headers)
    # get league standings
    def get_leagueStandings(self, league, season):
        url = f'{self.apiurl}competitions/{league}/standings?season={season}'
        data = self.session.get(url)
        teams = data.json()
        head = []
        tableHead = [("Position", "Club","Played","Won","Drawn","Lost","Points","Form")]
        standings = []
        # head will have the following touple 
        # [(country flag, country name, competition logo, competition name, 
        # current matchday, season-start date, season-end date)]
        head.append((teams['area']['flag'], teams['area']['name'], teams['competition']['emblem'], 
                     teams['competition']['name'], teams['season']['currentMatchday'], 
                     teams['season']['startDate'], teams['season']['endDate']))
        # standings will have the following touple
        # [(standing, team-crest, team-Name, games played, won, drawn, lost, points, form)]
        for i in range(len(teams['standings'][0]['table'])):
            standings.append((i + 1, teams['standings'][0]['table'][i]['team']['crest'], 
                              teams['standings'][0]['table'][i]['team']['shortName'],
                              teams['standings'][0]['table'][i]['playedGames'], teams['standings'][0]['table'][i]['won'],
                              teams['standings'][0]['table'][i]['draw'], teams['standings'][0]['table'][i]['lost'],
                              teams['standings'][0]['table'][i]['points'], teams['standings'][0]['table'][i]['form']))
        return head, standings, tableHead
    # get cup group standings
    def get_cupStandings(self, cup, season=2022):
        if season == 2022:
            url = f'{self.apiurl}competitions/{cup}/standings'
        else:
            url = f'{self.apiurl}competitions/{cup}/standings?season={season}'
        data = self.session.get(url)
        teams = data.json()
        head = []
        groupTeams = []
        groups = []
        # head will have the following touple
        # [(competition logo, competition name, current matchday, season-start date, season-end date)]
        head.append((teams['competition']['emblem'], teams['competition']['name'], 
                     teams['season']['currentMatchday'], teams['season']['startDate'],
                     teams['season']['endDate']))
        # loop through every group
        for i in range(len(teams['standings'])):
            # loop through every team in a group
            for j in range(len(teams['standings'][i]['table'])):
                # groupTeams will have the following touple
                # [(standing, team-crest, team-Name, games played, won, drawn, lost, points)]
                groupTeams.append((j + 1, teams['standings'][i]['table'][j]['team']['crest'], 
                                   teams['standings'][i]['table'][j]['team']['shortName'], 
                                   teams['standings'][i]['table'][j]['playedGames'],
                                   teams['standings'][i]['table'][j]['won'], teams['standings'][i]['table'][j]['draw'], 
                                   teams['standings'][i]['table'][j]['lost'], teams['standings'][i]['table'][j]['points']))
            # groups will have the following touple
            # [(groupLetter, groupTeams)]
            groups.append((chr(65 + i), groupTeams[:]))
            groupTeams.clear()
        return head, groups
    def get_cupPlayoffs(self, cup):
        stages=['LAST_16', 'QUARTER_FINALS', 'SEMI_FINALS', 'BRONZE', 'FINAL']
        gnames = ['Round of 16', 'Quarter-finals', 'Semi-finals', 'Third place play-off', 'Final']
        counter = 0
        matches = []
        games = []
        # loop through every stage
        for stage in stages:
            url = f'{self.apiurl}competitions/{cup}/matches?stage={stage}'
            data = self.session.get(url)
            teams = data.json()
            # no rounds at all
            if not teams['matches'] and not matches:
                return 0
            # no rounds left
            elif not teams['matches']:
                if stage == 'BRONZE':
                    counter += 1
                else:
                    return matches
            # loop through every match in stage
            else:
                for i in range(len(teams['matches'])):
                # game exists but has not been played yet
                    if not teams['matches'][i]['score']['winner']:
                        # games will have the following touple
                        # [(matchday, home crest, home name, home score, away score, away crest, away name)]
                        games.append((teams['matches'][i]['homeTeam']['crest'], 
                                          teams['matches'][i]['homeTeam']['shortName'], ' ', ' ', ' ', ' ',
                                          teams['matches'][i]['awayTeam']['crest'], teams['matches'][i]['awayTeam']['shortName']))
                    # game has been played out 
                    else:
                        # The game ended in a penalty shootout
                        if teams['matches'][i]['score']['duration'] == 'PENALTY_SHOOTOUT':
                            # for some reason COPA LIBERTADORES does not 'regularTime' -_-
                            if teams['matches'][i]['competition']['code'] == 'CLI':
                                games.append((teams['matches'][i]['homeTeam']['crest'], 
                                      teams['matches'][i]['homeTeam']['shortName'], 
                                      teams['matches'][i]['score']['fullTime']['home'] - teams['matches'][i]['score']['penalties']['home'], 
                                      f"({teams['matches'][i]['score']['penalties']['home']})", f"({teams['matches'][i]['score']['penalties']['away']})",
                                      teams['matches'][i]['score']['fullTime']['away'] - teams['matches'][i]['score']['penalties']['away'], 
                                      teams['matches'][i]['awayTeam']['crest'], teams['matches'][i]['awayTeam']['shortName']))
                            else:
                                games.append((teams['matches'][i]['homeTeam']['crest'], 
                                      teams['matches'][i]['homeTeam']['shortName'], 
                                      teams['matches'][i]['score']['regularTime']['home'] + teams['matches'][i]['score']['extraTime']['home'], 
                                      f"({teams['matches'][i]['score']['penalties']['home']})", f"({teams['matches'][i]['score']['penalties']['away']})",
                                      teams['matches'][i]['score']['regularTime']['away'] + teams['matches'][i]['score']['extraTime']['away'], 
                                      teams['matches'][i]['awayTeam']['crest'], teams['matches'][i]['awayTeam']['shortName']))
                        # The game ended in a extra time
                        elif teams['matches'][i]['score']['duration'] == 'EXTRA_TIME' and not teams['matches'][i]['competition']['code'] == 'CLI':
                            games.append((teams['matches'][i]['homeTeam']['crest'], 
                                      teams['matches'][i]['homeTeam']['shortName'], 
                                      teams['matches'][i]['score']['regularTime']['home'] + teams['matches'][i]['score']['extraTime']['home'], 
                                      ' ', ' ', teams['matches'][i]['score']['regularTime']['away'] + teams['matches'][i]['score']['extraTime']['away'],
                                      teams['matches'][i]['awayTeam']['crest'], teams['matches'][i]['awayTeam']['shortName']))
                        # game eneded in regular time
                        else:
                            games.append((teams['matches'][i]['homeTeam']['crest'], 
                                      teams['matches'][i]['homeTeam']['shortName'], teams['matches'][i]['score']['fullTime']['home'], ' ', ' ',
                                      teams['matches'][i]['score']['fullTime']['away'], teams['matches'][i]['awayTeam']['crest'], 
                                      teams['matches'][i]['awayTeam']['shortName']))
                matches.append((gnames[counter], games[:]))
                games.clear()
                counter += 1
        return matches
