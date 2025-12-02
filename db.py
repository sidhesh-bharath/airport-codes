from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AirportInfo(db.Model):
    __tablename__ = "Airports"

    code = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())
    location = db.Column(db.String(80))

    def __init__(self, code, name, location):
        self.code = code
        self.name = name
        self.location = location

    def __repr__(self):
        return f"{self.code}: {self.name} - {self.location}"