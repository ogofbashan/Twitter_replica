from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import TitleForm, ContactForm, LoginForm, RegisterForm, PostForm
from app. models import Post, User
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/index')
@app.route('/index/<word>', methods=['GET'])
def index(word = ''):
    products = [
        {
            'id': 1001,
            'title' : 'Twitter Bot',
            'price' : 150,
            'desc' : 'This twitter bot will destroy your enemies, muahahaha!'
        },
        {
            'id': 1002,
            'title' : 'Twitter T-Shirt',
            'price' : 15,
            'desc' : 'You\'ll look pretty ok in this.'
        },
        {
            'id': 1003,
            'title' : 'Stickers',
            'price' : 5,
            'desc' : 'These stickers will stick to anything with their stickiness.'
        },
        {
            'id': 1004,
            'title' : '100k Follower Account',
            'price' : 5000,
            'desc' : 'Be an influencer today! Christiano Ronaldo gets paid $950,000 for every post he makes.'
        },
    ]
    return render_template('index.html', title='Home', products=products, word = word)

@app.route('/title', methods=['GET', 'POST'])
def title():
    form =TitleForm()

    # handle form submission

    if form.validate_on_submit():
        text= form.title.data

        return redirect(url_for('index', word = text))

    return render_template('form.html', title='Title', form=form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        flash(f'Thanks {form.name.data}, your message has been received. We have sent a copy of the submission to {form.email.data}.')

        return redirect(url_for('index'))

    return render_template('form.html', form=form, title='Contact Us')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    #if user is already logged in, redirect them
    if current_user.is_authenticated:
        flash('You are already logged in!')
        return redirect(url_for('profile', username=current_user.username))

    if form.validate_on_submit():

        # query the db for the user information, and log them in if everything is validators
        user = User.query.filter_by(email=form.email.data).first()

        # if user doesn't exist, reload page and flash message

        if user is None or not user.check_password(form.password.data):
            flash('Invalid Credentials.')
            return redirect(url_for('login'))

        #if the user does exist, and credentials are correct, log them in
        login_user(user)
        flash(f'You have been logged in!')
        return redirect(url_for('profile', username=current_user.username))

    return render_template('form.html', form=form, title='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            username = form.username.data,
            email = form.email.data,
            age = form.age.data,
            bio = form.bio.data,
        )

        #include password to user
        user.set_password(form.password.data)

        #add to stage and commit

        db.session.add(user)
        db.session.commit()

        flash(f'You have been registered!')

        return redirect(url_for('login'))

    return render_template('form.html', form=form, title='Register')

@app.route('/profile')
@app.route('/profile/<username>', methods= ['GET', 'POST'])
def profile(username = ''):
    #if username is empty
    if not username:
        return redirect(url_for('login'))
    form = PostForm()

    person = User.query.filter_by(username=username).first()

    if form.validate_on_submit():
        tweet = form.tweet.data
        post = Post(user_id=current_user.id, tweet=tweet)

        # commit to database
        db.session.add(post)
        db. session.commit()

        return redirect(url_for('profile', username=username))

    return render_template('profile.html', title='Profile', form=form, username=username, person=person)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
