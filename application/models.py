from application import db

class Reader(db.Model):
    reader_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    user_name = db.Column(db.String(50))
    password = db.Column(db.String(50))

