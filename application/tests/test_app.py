# Import the necessary modules
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
        # Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
                SECRET_KEY="TEST_SECRET_KEY",
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        # Create table
        db.create_all()
        # Create test registree
        testReader = Reader(first_name="Dana",last_name="Constantin",user_name="danactin", password="root")
        # save users to database
        db.session.add(testReader)
        db.session.commit()

        testBook = Book(
            #fkreader= 1, 
            book_title="Murder in Hampstead", 
            author="Sabina Manea", 
            genre="Fiction",
            review="5* out of 5*")

        testBook2 = Book(
            #fkreader= 1, 
            book_title="Mary Berry Quick Cooking", 
            author="Mary Berry", 
            genre="Cooking",
            review="5* out of 5*")

    # Will be called after every test
    def tearDown(self):
    # Close the database session and remove all contents of the database
     db.session.remove()
     db.drop_all()

    # Write a test class to test Read functionality
class TestViewsReader(TestBase):
    def test_add_reader_get(self):
        response = self.client.get(url_for('read_reader'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dana', response.data)

    def test_read_reader_get(self):
        response = self.client.get(url_for('read_reader'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dana', response.data)

    def test_update_reader_get(self):
        response = self.client.get(url_for("read_reader", reader_id=1))
        self.assertEqual(response.status_code, 200)

    def test_delete_reader_get(self):
        response = self.client.get(url_for("read_reader", id=1))
        self.assertEqual(response.status_code, 200)

class TestViewsBook(TestBase):
    def test_add_book_get(self):
        response = self.client.get(url_for('read_book'))
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'Murder in Hampstead', response.data)

    def test_read_book_get(self):
        response = self.client.get(url_for('read_book'))
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'Murder in Hampstead', response.data)

    def test_update_book_get(self):
        response = self.client.get(url_for('read_book'))
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'Murder in Hampstead', response.data)

    def test_delete_book_get(self):
        response = self.client.get(url_for('read_book'))
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b'Mary Berry Quick Cooking', response.data)

class TestViewsHome(TestBase):
    def testHome(self):
        response = self.client.get(url_for('home')) # send a GET request
        self.assertEqual(response.status_code, 200) # assert that the response code is 200
        self.assertIn(b'Welcome to this Library', response.data) # assert that the website's title is present in the HTTP response's data

    def testAbout(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is the about page!', response.data)

class TestAddReader(TestBase):
    def test_add_reader(self):
        response = self.client.post(
            url_for('add_reader'),
            data = dict(first_name = "Daniela", 
                last_name = 'Constantin', 
                user_name = "danactin", 
                password = "1234"
            )
        )
    
        assert Reader.query.filter_by(first_name="Daniela").first().reader_id == 2   

class TestAddBook(TestBase):
    def test_add_book(self):
        response = self.client.post(
            url_for('add_book'),
            data = dict(fkreader = 1,
                book_title = "Murder in Hampstead",
                author = "Sabina Manea",
                genre = "Fiction",
                review = "5*"
            )
        )
        
        assert Book.query.filter_by(genre="Fiction").first().book_id == 2  

class TestDeleteReader(TestBase):
    def test_delete_reader(self):
        response = self.client.get(
            url_for('delete_reader', reader_id = 1)
        )
        assert len(Reader.query.all()) == 0   

class TestDeleteBook(TestBase):
    def test_delete_book(self):
        response = self.client.get(
            url_for('delete_book', book_id = 1)
        )
        assert len(Book.query.all()) == 0   

class TestUpdateReader(TestBase):
    def test_update_reader(self):
        response = self.client.post(
            'updatereader/1',
            data = dict(first_name = "Daniela",
            last_name = 'Constantin', 
            user_name = "danactin", 
            password = "1234"
            )
       
        )
        self.assertIn(b'Daniela', response.data)