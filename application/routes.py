from application import app, db
from application.models import Reader, Book
from application.forms import ReaderForm, BookForm
from flask import redirect, url_for, render_template, request

@app.route('/')
def home():
    return render_template("home.html")

# @app.route('/index')
# def index():
#    rds = Reader.query.all()
#    return render_template("readerlist.html", reader=rds)


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/add_reader', methods=['GET', 'POST'])
def add_reader():
    form = ReaderForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            readerData = Reader(
                first_name = form.first_name.data, 
                last_name = form.last_name.data,
                user_name = form.user_name.data,
                password = form.password.data
            )
            db.session.add(readerData)
            db.session.commit()
            return redirect(url_for('read_reader'))
    return render_template('reader.html', form=form)

@app.route('/read_reader', methods=['GET', 'POST'])
def read_reader():
    reader = Reader.query.all()
    return render_template('readerlist.html', reader=reader)

@app.route('/update_reader/<int:reader_id>', methods= ['GET','POST'])
def update_reader(reader_id):
    reader = Reader.query.get(reader_id)
    form = ReaderForm()
    if form.validate_on_submit():
        reader.first_name= form.first_name.data
        reader.last_name= form.last_name.data
        reader.user_name = form.user_name.data
        reader.password = form.password.data
        db.session.commit()
        return redirect(url_for('read_reader'))
    elif request.method == 'GET':
        form.first_name.data = reader.first_name
        form.last_name.data = reader.last_name
        form.user_name.data = reader.user_name
        form.password.data = reader.password 
    return render_template('update_reader.html', form=form)

@app.route('/delete_reader/<int:reader_id>')
def delete_reader(reader_id):
    reader_text = Reader.query.get(reader_id)
    db.session.delete(reader_text)
    db.session.commit()
    return redirect(url_for('read_reader'))

#-------------------------------------------------------------------------------
#CRUD for Book

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            bookData = Book(
                fkreader = form.fkreader.data,
                book_title = form.book_title.data, 
                author = form.author.data,
                genre  = form.genre.data,
                review = form.review.data
                
            )
            db.session.add(bookData)
            db.session.commit()
            return redirect(url_for('read_book'))
    return render_template('book.html', form=form)

@app.route('/read_book', methods=['GET', 'POST'])
def read_book():
    book = Book.query.all()
    return render_template('booklist.html', book=book)

@app.route('/update_book/<int:book_id>', methods= ['GET','POST'])
def update_book(book_id):
    book = Book.query.get(book_id)
    form = BookForm()
    if form.validate_on_submit():
        book.book_title= form.book_title.data
        book.author= form.author.data
        book.genre = form.genre.data
        book.review = form.review.data
        db.session.commit()
        return redirect(url_for('read_book'))
    elif request.method == 'GET':
        form.book_title.data = book.book_title
        form.author.data = book.author
        form.genre.data = book.genre
        form.review.data = book.review
    return render_template('update_book.html', form=form)

@app.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    book_text = Book.query.get(book_id)
    db.session.delete(book_text)
    db.session.commit()
    return redirect(url_for('read_book'))
