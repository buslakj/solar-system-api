from app import db

class Moons(db.Model):
    moon_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    description = db.Column(db.String)
    name = db.Column(db.String)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id")) 
    planet = db.relationship("Planet", back_populates = "moons")