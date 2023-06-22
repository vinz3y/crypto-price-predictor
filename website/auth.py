from flask import Blueprint, render_template, request, flash

#define that this file is the auth of the application

auth = Blueprint('auth',__name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", text="Testing")
#variables can be passed with the above function as param

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/signup', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) <6:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) <7:
            flash('Password must be greater than 7 characters.', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("sign_up.html")