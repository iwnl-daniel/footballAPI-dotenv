"""
Daniel Gregorio
Riot Games Leaderboard app
"""
import pytest

from fbdb import FBDB  # Assuming your class is in a file named fbdb.py


# Create a fixture for the FBDB instance that can be reused in multiple tests
@pytest.fixture
def fbdb_instance():
    return FBDB("your_token_here")

# Test the get_leagueStandings method
def test_get_leagueStandings(fbdb_instance):
    league = "PL"
    season = "2022"
    head, standings, tableHead = fbdb_instance.get_leagueStandings(league, season)

    assert isinstance(head, list)
    assert isinstance(standings, list)
    assert isinstance(tableHead, list)

    assert len(head) == 1
    assert len(standings) > 0
    assert len(tableHead) == 1

# Test the get_cupStandings method
def test_get_cupStandings(fbdb_instance):
    cup = "CL"
    season = "2022"
    head, groups = fbdb_instance.get_cupStandings(cup, season)

    assert isinstance(head, list)
    assert isinstance(groups, list)

    assert len(head) == 1
    assert len(groups) > 0

# Test the get_cupPlayoffs method
def test_get_cupPlayoffs(fbdb_instance):
    cup = "CL"
    matches = fbdb_instance.get_cupPlayoffs(cup)

    assert isinstance(matches, list)
    assert len(matches) > 0

# Run the tests
if __name__ == "__main__":
    pytest.main()
