from application import app, db
from application.models import Reader
from application.forms import ReaderForm
from flask import redirect, url_for, render_template, request

#@app.route('/', methods=['GET', 'POST'])
@app.route('/reader', methods=['GET', 'POST'])
def add_reader():
    message = ""
    form = ReaderForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        user_name = form.user_name.data
        password = form.password.data

        if len(first_name) == 0 or len(last_name) == 0 or len(user_name) == 0 or len(password) == 0 :
            message = "Please supply first name, last name, user_name and password"
        else:
            message = f'Thank you, {first_name} {last_name}'
        
           
    return render_template('home.html', form=form, message=message)


@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/reader', methods=['GET', 'POST'])
def read_reader():
    reader = Reader.query.all()
    return render_template('reader.html', reader=reader)

@app.route('/update/<int:id>', methods= ['GET', 'POST'])
def update_reader(reader_id):
    form = ReaderForm()
    reader = Reader.query.get(reader_id)
    if form.validate_on_submit():
        reader.update_reader = form.reader.data
        db.session.commit()
        return redirect(url_for('update_reader'))
    elif request.method == 'GET':
        form.reader.data = reader.update_reader
    return render_template('update_reader.html', form=form)

@app.route('/delete/<int:id>')
def delete_reader(reader_id):
    reader_text = Reader.query.get(reader_id)
    db.session.delete(reader_text)
    db.session.commit()
    return redirect(url_for('read', reader_text=reader_text))

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')