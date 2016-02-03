#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament

import db


def deleteMatches():
    """Remove all the match records from the database."""
    db.DB().executeAndCloseConnection("DELETE FROM match")


def deletePlayers():
    """Remove all the player records from the database."""
    db.DB().executeAndCloseConnection("DELETE FROM player")


def countPlayers():
    """Returns the number of players currently registered."""
    conn = db.DB().execute("SELECT count(*) FROM player")
    count = conn["cursor"].fetchone()[0]
    conn["conn"].close()
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
    name: the player's full name (need not be unique).
    """
    db.DB().executeInsertAndCloseConnection(
        "INSERT INTO player (name) VALUES (%s)", (name,))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
     or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = db.DB().execute("SELECT * FROM standing s")
    cursor = conn["cursor"]
    standing = []
    DBres = cursor.fetchall()
    conn["conn"].close()
    for row in DBres:
        standing.append((int(row[0]), str(row[1]), int(row[2]), int(row[3])))
    return standing


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db.DB().executeInsertAndCloseConnection(
        "INSERT INTO match (winner, loser) VALUES (%s, %s)", (winner, loser,))


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = db.DB().execute("SELECT player_id, name from standing")
    cursor = conn["cursor"]
    pairing = []
    resultFromDB = cursor.fetchall()
    conn["conn"].close()
    for i in range(0, len(resultFromDB), 2):
        element1 = resultFromDB[i]
        element2 = resultFromDB[i+1]
        pairing.append(
            (int(element1[0]), str(element1[1]),
                int(element2[0]), str(element2[1])))
    return pairing
