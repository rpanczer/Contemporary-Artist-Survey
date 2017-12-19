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
    uniqueartistobj = Votes.query.filter_by(isdeleted=False).distinct()
    uniqueartistlist = [artist.artistname for artist in uniqueartistobj]
    compare = []
    w1 = artist
    for name in uniqueartistlist:
        w2 = name
        ratio = SequenceMatcher(None, w1, w2).ratio()
        compare.append(ratio)
    if max(compare) > 0.9:
        artist = uniqueartistlist[compare.index(max(compare))]
        compare = True
        addvote(artist, compare)
    else:
        addartist(artist)


# Adds a new artist to the list of artists
def addartist(artist):
    postgres.session.add(Votes(artist, 1, False))
    postgres.session.commit()
    print("Added {}".format(artist))


# Checks to see if incoming artist is part of the list of 9 given artists
# If the artist is in this list, shortcuts and adds vote immediately
# Else check to see if an artist like this exists
def addvote(artist, compare):
    given_artists = ('Marcel Eichner', 'Jeff Elrod', 'Awol Erizku', 'Hoosen', 'Zak Prekop', 'Julie Oppermann',
                     'David Ostrowski', 'Christian Rosa', 'Lucien Smith')
    if compare is True or artist in given_artists:
        artistvotes = Votes.query.filter_by(artistname=artist).first()
        artistvotes.votecount += 1
        postgres.session.commit()
        return
    else:
        checkartistlist(artist)


# Creates an object that contains all artist names and vote count where the artist has not been deleted
def artistlist():
    artistvotes = Votes.query.filter_by(isdeleted=False)
    return artistvotes
