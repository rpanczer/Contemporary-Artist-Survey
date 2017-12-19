class createDatabase(postgres.Model):

    _tablename__ = "votes"

    id = postgres.Column(postgres.Integer, primary_key=True)
    artistname = postgres.Column(postgres.String, nullable=False)
    votecount = postgres.Column(postgres.Integer, nullable=False)
    isdeleted = postgres.Column(postgres.Boolean, nullable=False)

    def __init__(self, artistname, votecount, isdeleted):
        self.artistname = artistname
        self.votecount = votecount
        self.isdeleted = isdeleted

    def __repr__(self):
        return 'title {}'.format(self.title)