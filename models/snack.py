from models.database import db

class Snack(db.Model):
    # id (int), name(txt), description(txt), time(txt), date(txt), in_diet(True or False):

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(80), nullable=False)

    description = db.Column(db.String(80), nullable=False)
    
    date = db.Column(db.String(80), nullable=False)

    time = db.Column(db.String(80), nullable=False)
    
    in_diet = db.Column(db.String(80), nullable=False)

