# daniel gregorio
# informational website using football-data free API subscription
import flask
import os
import dotenv
from fbdb import FBDB
# variables from .env file
dotenv.load_dotenv()
# flask app
app = flask.Flask(__name__)
# route for Home Page (index)
@app.route('/',  methods=['GET'])
def index():
    return flask.render_template('index.html')
# route for League Standings Page (leagueStandings)
@app.route('/leagueStandings',  methods=['POST', 'GET'])
def leagueStandings():
    # get user's data
    if flask.request.method == 'POST':
        # no league and/ or season was picked 
        if flask.request.form['league'] == 'none' or flask.request.form['season'] == 'none':
            return flask.render_template('leagueStandings.html')
        league = flask.request.form['league']
        season = flask.request.form['season']
        head, standings, tableHead = test.get_leagueStandings(league, season)
        return flask.render_template('leagueStandings.html', head=head, standings=standings, tableHead=tableHead)
    return flask.render_template('leagueStandings.html')
# route for World Cup (worldCup)
@app.route('/worldCup',  methods=['GET'])
def worldCup():
    # Free API KEY only has access to 2022 World Cup
    head, groups = test.get_cupStandings('WC')
    playoffs = test.get_cupPlayoffs('WC')
    if playoffs == 0:
        return flask.render_template('worldCup.html', head=head, groups=groups)
    return flask.render_template('worldCup.html', head=head, groups=groups, playoffs=playoffs)
# route for Champions League (championsLeague)
@app.route('/championsLeague',  methods=['GET'])
def championsLeague():
    # Free API KEY only has access to 2022 Champions League
    head, groups = test.get_cupStandings('CL')
    playoffs = test.get_cupPlayoffs('CL')
    if playoffs == 0:
        return flask.render_template('championsLeague.html', head=head, groups=groups)
    return flask.render_template('championsLeague.html', head=head, groups=groups, playoffs=playoffs)
# route for Copa Libertadores (copaLibertadores)
@app.route('/copaLibertadores',  methods=['GET'])
def copaLibertadores():
    # Free API KEY only has access to 2022 Copa Libertadores
    head, groups = test.get_cupStandings('CLI')
    playoffs = test.get_cupPlayoffs('CLI')
    if playoffs == 0:
        return flask.render_template('copaLibertadores.html', head=head, groups=groups)
    return flask.render_template('copaLibertadores.html', head=head, groups=groups, playoffs=playoffs)
# main
if __name__ == '__main__':
    test = FBDB(os.getenv('API_KEY'))
    app.run(debug=False)

# DOCUMENTATION
# https://www.football-data.org/documentation/quickstart
# https://docs.football-data.org/general/v4/lookup_tables.html

# ----------------------------------------------------------------------------------
#                    Available competitions With FREE API KEY                       
# ----------------+---------------+-------------------------------+-----------------
# Competition Id  | League-Code   | Caption                       |Country
# ----------------+---------------+-------------------------------+-----------------
# 2002            | BL1           | Bundesliga                    | Germany
# 2003            | DED           | Eredivisie                    | Netherlands
# 2013            | BSA           | Campeonato Brasileiro Série A | Brazil
# 2014            | PD            | Primera Division              | Spain
# 2015            | FL1           | Ligue 1                       | France
# 2016            | ELC           | Championship                  | England
# 2017            | PPL           | Primeira Liga                 | Portugal
# 2019            | SA            | Serie A                       | Italy
# 2021            | PL            | Premier League                | England
# ----------------+---------------+-------------------------------+-----------------
# Competition Id  | Cup-Code      | Caption                       |Country
# ----------------+---------------+-------------------------------+-----------------
# 2000            | WC            | FIFA World Cup                | World
# 2001            | CL            | UEFA Champions League         | Europe
# 2018            | EC            | European Championship         | Europe
# 2152            | CLI           | Copa Libertadores             | South America

# European Championship is broken ATM. Will implement if it gets fixed