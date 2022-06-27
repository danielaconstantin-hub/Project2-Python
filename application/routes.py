from application import app, db
from application.models import Reader
from application.forms import ReaderForm
from flask import redirect, url_for, render_template, request

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
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

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')