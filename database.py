import sqlite3 as sql
from difflib import SequenceMatcher


def checkartistlist(artist):
    conn = sql.connect('art.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT artistname FROM votes WHERE isDeleted <> 1")
    uniqartistlist = c.fetchall()
    compare = []
    w1 = artist
    for name in uniqartistlist:
        w2 = name[0]
        ratio = SequenceMatcher(None, w1, w2).ratio()
        compare.append(ratio)
    if max(compare) > 0.9:
        artist = uniqartistlist[compare.index(max(compare))][0]
        print("found a match, {}!".format(artist))
        compare = True
        addvote(artist, compare)
    else:
        print(compare)
        addartist(artist)


def addartist(artist):
    conn = sql.connect('art.db')
    c = conn.cursor()
    newartist = (artist, 1, 0)
    c.execute("INSERT INTO votes (artistname, votecount, isdeleted)VALUES(?, ?, ?)", newartist)
    print("Added {}".format(artist))
    conn.commit()


def addvote(artist, compare):
    try:
        conn = sql.connect('art.db')
        c = conn.cursor()
    except Error as e:
        print(e)
    given_artists = ('Marcel Eichner', 'Jeff Elrod', 'Awol Erizku', 'Hoosen', 'Zak Prekop', 'Julie Oppermann',
                     'David Ostrowski', 'Christian Rosa', 'Lucien Smith')
    if compare is True or artist in given_artists:
        c.execute("SELECT votecount FROM votes WHERE artistname = (?) AND isDeleted <> 1", (artist,))
        votecount = c.fetchone()
        votecount = votecount[0] + 1
        addvote = (votecount, artist)
        c.execute("UPDATE votes SET votecount = (?) WHERE artistname = (?)", addvote)
        conn.commit()
    else:
        checkartistlist(artist)


def artistlist():
    try:
        conn = sql.connect('art.db')
        c = conn.cursor()
    except Error as e:
        print(e)
    c.execute("SELECT artistname, votecount FROM votes WHERE isdeleted <> 1")
    artistvotes = c.fetchall()
    return artistvotes
