from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, IntegerField

class ReaderForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    user_name = StringField("User Name")
    password = StringField("Password")
    submit = SubmitField("Submit")

class BookForm(FlaskForm):
    book_genre = ["Fiction","Cooking", "Action&Adventure","Biography", "Autobiography" ]
    book_review = ["1* out of 5*", "2*out of 5*", "3*out of 5*", "4*out of 5*", "5*out of 5*"]

    fkreader = IntegerField("Reader")
    book_title = StringField("Book Title")
    author = StringField("Author")
    genre = SelectField("Genre", choices=book_genre)
    review = SelectField("Review", choices=book_review)
    submit = SubmitField("Submit")