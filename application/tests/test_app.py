from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from application import app, db
from application.models import Reader,Book
from application.forms import ReaderForm,BookForm
from flask import redirect, url_for, render_template, request

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. 
        # use sqlite database
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                SECRET_KEY="TEST_SECRET_KEY",
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

  def setUp(self):
        # Create table
        db.create_all()
        rootReader = Reader(first_name="root",last_name="root",user_name="root", password="root")
        db.session.add(rootReader)
        db.session.commit()

        rootReader = Reader(first_name="admin",last_name="admin",user_name="admin", password="admin")
        db.session.add(rootReader)
        db.session.commit()

        rootReader= Reader(message="root" ,reader_id=1)
        db.session.add(rootReader)
        db.session.commit()

        root= Book(message="admin" ,userID=2)
        db.session.add(rootBook)
        db.session.commit()