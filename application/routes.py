from application import app, db
from application.models import Reader
from application.forms import ReaderForm
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

