from application import db

class Reader(db.Model):
    reader_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    user_name = db.Column(db.String(50))
    password = db.Column(db.String(50))

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    review = db.Column(db.String(50), nullable=False)
    first_name= db.relationship(db.String, db.ForeignKey('reader.first_name'))
