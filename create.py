from application import db
from application.models import Reader, Book

db.drop_all()
db.create_all()

#testreader = readers(first_name='Daniela',last_name='Constantin', user_name='danactin',password='1234') # Extra: this section populates the table with an entry
#db.session.add(testreader)
#db.session.commit()