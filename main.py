from flask import *
import database as db
import re
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/compareArtists", methods=["POST"])
def compareArtists():
    artist = request.form['selected_artist']
    if re.match('^[A-Z]*$]', artist):
        db.addvote(artist)
        return redirect(url_for("displayVotes"))
    else:
        e = 'Sorry, an artist\'s name cannot contain special characters or numbers. Please try voting again.'
        return redirect(url_for("index.html"), e = e)


@app.route("/displayVotes")
def displayVotes():
    artistvotes = db.artistlist()
    return render_template("voteresults.html", artistvotes=artistvotes)


if __name__ == "__main__":
    app.run(debug=True)
