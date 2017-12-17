from flask import *
import database as db
import re
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/compareArtists", methods=["POST"])
def compareArtists():
    artist = request.form['artist']
    if artist == 'Other':
        artist_other = request.form['artist_other']
        artist = artist_other
    print(artist)
    if artist is not None:
        compare = False
        db.addvote(artist, compare)
        return redirect(url_for("displayVotes"))
    else:
        e = 'Sorry, an artist\'s name cannot contain special characters or numbers. Please try voting again.'
        return redirect(url_for("/"), e = e)


@app.route("/displayVotes")
def displayVotes():
    artistvotes = db.artistlist()
    return render_template("voteresults.html", artistvotes=artistvotes)


if __name__ == "__main__":
    app.run(debug=True)
