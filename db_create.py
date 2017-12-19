from main import db
from models import createDatabase

# Create the database and the db tables
db.create_all()

# insert default data
db.session.add(createDatabase("Marcel Eichner", 0, 0))
db.session.add(createDatabase("Jeff Elrod", 0, 0))
db.session.add(createDatabase("Awol Erizku", 0, 0))
db.session.add(createDatabase("Hoosen", 0, 0))
db.session.add(createDatabase("Zak Prekop", 0, 0))
db.session.add(createDatabase("Julie Oppermann", 0, 0))
db.session.add(createDatabase("David Ostrowski", 0, 0))
db.session.add(createDatabase("Christian Rosa", 0, 0))
db.session.add(createDatabase("Lucien Smith", 0, 0))

# commit data
db.session.commit()