from main import db

class createDatabase(db.Model):

    _tablename__ = "votes"

    id = db.Column(db.Integer, primary_key=True)
    artistname = db.Column(db.String, nullable=False)
    votecount = db.Column(db.Integer, nullable=False)
    isdeleted = db.Column(db.Boolean, nullable=False)

    def __init__(self, artistname, votecount, isdeleted):
        self.artistname = artistname
        self.votecount = votecount
        self.isdeleted = isdeleted

    def __repr__(self):
        return 'title {}'.format(self.title)