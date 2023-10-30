# footballAPI (local)

Daniel Gregorio-Torres

11/22 - 12/22

Personal Project

## Purpose of this project

RUNNING APP LOCALLY WITH `.env` FILE

The purpose of this small web app is to demonstrate some of the information that can be obtained using the https://www.football-data.org/ Free API Subscription. This application displays the current table standings for up to 9 leagues including (Premier League, Primera Division, Bundesliga, ...). It also includes group stage and playoff games for tournaments such as the Champions League, Copa Libertadores, and the 2022 World Cup.

## Navigation

- [Setup](#setup)
- [Installation](#installation)
- [Tests](#tests)
- [Previews](#previews)

## Setup

Create a `.env` file with the following contnets:

```.env
API_KEY="<YOUR API KEY>"
```

More documentation can be found here
[[1]](https://www.football-data.org/documentation/quickstart)
[[2]](https://docs.football-data.org/general/v4/lookup_tables.html)

## Installation

###### Unix/ macOS:

```shell
python3 -m venv env
source env/bin/activate
pip3 install --upgrade -r requirements.txt
python3 app.py
```

###### Windows:

```shell
py -m venv env
.\env\Scripts\activate
pip install --upgrade -r requirements.txt
python3 app.py
```

## Tests

The application comes with the following tests:

1. Test the get_leagueStandings method
1. Test the get_cupStandings method
1. Test the get_cupPlayoffs method

In order to run the test the enter the following command:

```shell
pytest
```

## Previews

###### Home Page

![Home Page](https://github.com/iwnl-daniel/footballAPI-dotenv/blob/main/pagePreviews/index.png?raw=true)

###### League Standings

![League Standings](https://github.com/iwnl-daniel/footballAPI-dotenv/blob/main/pagePreviews/league_standings.png?raw=true)

###### World Cup

![World Cup](https://github.com/iwnl-daniel/footballAPI-dotenv/blob/main/pagePreviews/world_cup.png?raw=true)

###### Champions League

![Champions League](https://github.com/iwnl-daniel/footballAPI-dotenv/blob/main/pagePreviews/champions_league.png?raw=true)

###### Copa Libertadores

![Copa Libertadores](https://github.com/iwnl-daniel/footballAPI-dotenv/blob/main/pagePreviews/copa_libertadores.png?raw=true)
