# import sqlite3 as sql
from flask_sqlalchemy import *
import main
from difflib import SequenceMatcher

# Creates db object and import
postgres = SQLAlchemy(main.app)


class Votes(postgres.Model):

    __tablename__ = "votes"

    id = postgres.Column(postgres.Integer, primary_key=True)
    artistname = postgres.Column(postgres.String(100), unique=True)
    votecount = postgres.Column(postgres.Integer, nullable=False)
    isdeleted = postgres.Column(postgres.Boolean, nullable=False)

    def __init__(self, artistname, votecount, isdeleted):
        self.artistname = artistname
        self.votecount = votecount
        self.isdeleted = isdeleted

    def __repr__(self):
        return '<title {}'.format(self.title)

# check to see if an artist like the artist submitted by a user matches an artist already in the list.
# if match, add a vote to that artist
# if not, add that artist to the db
def checkartistlist(artist):
    """
    conn = sql.connect('art.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT artistname FROM votes WHERE isDeleted <> 1")
    uniqartistlist = c.fetchall()
    """
    uniqartistlist = Votes.query.filter_by(isdeleted=False).distinct()
    uniqartistlist = uniqartistlist.artistname
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
        addartist(artist)


# Adds a new artist to the list of artists
def addartist(artist):
    # conn = sql.connect('art.db')
    # c = conn.cursor()
    # newartist = (artist, 1, 0)
    # c.execute("INSERT INTO votes (artistname, votecount, isdeleted)VALUES(?, ?, ?)", newartist)
    postgres.session.add(Votes(artist, 1, False))
    postgres.session.commit()
    print("Added {}".format(artist))
    # conn.commit()


# Checks to see if incoming artist is part of the list of 9 given artists
# If the artist is in this list, shortcuts and adds vote immediately
# Else check to see if an artist like this exists
def addvote(artist, compare):
    """
    try:
        conn = sql.connect('art.db')
        c = conn.cursor()
    except Error as e:
        print(e)
    """
    given_artists = ('Marcel Eichner', 'Jeff Elrod', 'Awol Erizku', 'Hoosen', 'Zak Prekop', 'Julie Oppermann',
                     'David Ostrowski', 'Christian Rosa', 'Lucien Smith')
    if compare is True or artist in given_artists:
        """
        c.execute("SELECT votecount FROM votes WHERE artistname = (?) AND isDeleted <> 1", (artist,))
        votecount = c.fetchone()
        """
        votecount = Votes.query.filter_by(artistname=artist)
        votecount = votecount.votecount
        votecount = votecount[0] + 1
        # c.execute("UPDATE votes SET votecount = (?) WHERE artistname = (?)", addvote)
        update_data = Votes.query.filter_by(artistname=artist).first()
        update_data.votecount = votecount

        # conn.commit()
        postgres.session.commit()
    else:
        checkartistlist(artist)


# Creates an object that contains all artist names and vote count where the artist has not been deleted
def artistlist():
    """
    try:
        conn = sql.connect('art.db')
        c = conn.cursor()
    except Error as e:
        print(e)
    c.execute("SELECT artistname, votecount FROM votes WHERE isdeleted <> 1")
    artistvotes = c.fetchall()
    """
    artistvotes = Votes.query.filter_by(isdeleted=False)
    return artistvotes
