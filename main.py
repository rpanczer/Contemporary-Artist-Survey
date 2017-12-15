from flask import *
import database as db
app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/artistCompare", methods=["POST"])
def artistCompare():
    artist = request.form['selected_artist']
    db.addvote(artist)
    return redirect(url_for("displayVotes"))

@app.route("/displayVotes")
def displayVotes():
    artistvotes = db.artistlist()
    return render_template("voteresults.html", artistvotes=artistvotes)


if __name__ == "__main__":
    app.run()
