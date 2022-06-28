from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField

class ReaderForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    user_name = StringField("User Name")
    password = StringField("Password")
    submit = SubmitField("Submit")

