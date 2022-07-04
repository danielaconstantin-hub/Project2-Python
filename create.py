from application import db
from application.models import Reader, Book

db.drop_all()
db.create_all()

