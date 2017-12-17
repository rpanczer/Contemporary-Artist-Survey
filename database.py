import sqlite3 as sql
from difflib import SequenceMatcher


def checkartistlist(artist):
    conn = sql.connect('art.db')
    c = conn.cursor()
    qry = "SELECT DISTINCT artistname FROM votes WHERE isDeleted <> 1"
    artistlist = c.execute(qry)
    compare = []
    w1 = artist
    for name in artistlist:
        w2 = name
        ratio = SequenceMatcher(None, w1, w2).ratio()
        compare.append(ratio)
    if max(compare) > 0.9:
        artist = artistlist[max(compare).index()]
        addvote(artist)
    else:
        addartist(artist)



def addartist(artist):
    conn = sql.connect('art.db')
    c = conn.cursor()
    newartist = (artist, 1, 0)
    c.execute("INSERT INTO votes (artistname, votecount, isdeleted)VALUES(?, ?, ?)", newartist)
    conn.commit()



def addvote(artist):
    try:
        conn = sql.connect('art.db')
        c = conn.cursor()
    except Error as e:
        print(e)
    print(artist)
    given_artists = ['Marcel Eichner', 'Jeff Elrod', 'Awol Erizku', 'Hoosen', 'Zak Prekop', 'Julie Oppermann',
                     'David Ostrowski', 'Christian Rosa', 'Lucien Smith']
    if artist in given_artists:
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






