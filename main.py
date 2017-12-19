from flask import *
from flask_sqlalchemy import *
import re


# Create the app object
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ydjxpextmymfpr:2bfcf54577559dad34468623d82ca24c8e6da5d4ef5e5e887d' \
                                        '79273eb7500f13@ec2-54-163-233-103.compute-1.amazonaws.com:5432/d7okp7kjfvra58'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import database as db


# Route allows a user to vote for an artist
@app.route("/")
def main():
    return render_template("index.html")


# Route processes the vote for an artist
@app.route("/compareArtists", methods=["POST"])
def compareArtists():
    artist = request.form['artist']
    g.artist = artist
    if artist == 'Other':
        artist_other = request.form['artist_other']
        artist = artist_other
        g.artist = artist
        if re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', artist):
            compare = False
            db.addvote(artist, compare)
            return redirect(url_for("displayVotes"))
        else:
            e = 'Sorry, an artist\'s name cannot contain special characters or numbers. Please try voting again.'
            return redirect(url_for("/", e=e))
    else:
        compare = False
        db.addvote(artist, compare)
        return redirect(url_for("displayVotes"))


# Route displays the votes system-wide in a table for the user to view
@app.route("/displayVotes")
def displayVotes():
    artistvotes = db.artistlist()
    return render_template("voteresults.html", artistvotes=artistvotes, artistname='Bobby')


if __name__ == "__main__":
    app.run(debug=False)
