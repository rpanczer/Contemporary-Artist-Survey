from database import *

# Create the database and the db tables
postgres.create_all()

# insert default data
postgres.session.add(Votes("Marcel Eichner", 0, False))
postgres.session.add(Votes("Jeff Elrod", 0, False))
postgres.session.add(Votes("Awol Erizku", 0, False))
postgres.session.add(Votes("Hoosen", 0, False))
postgres.session.add(Votes("Zak Prekop", 0, False))
postgres.session.add(Votes("Julie Oppermann", 0, False))
postgres.session.add(Votes("David Ostrowski", 0, False))
postgres.session.add(Votes("Christian Rosa", 0, False))
postgres.session.add(Votes("Lucien Smith", 0, False))

# commit data
postgres.session.commit()
