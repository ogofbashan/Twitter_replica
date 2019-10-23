from app import app
from flask import render_template, url_for, redirect, flash
from app.forms import TitleForm, ContactForm, LoginForm, RegisterForm, PostForm

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

    if form.validate_on_submit():
        flash(f'You have been logged in!')

        return redirect(url_for('index'))

    return render_template('form.html', form=form, title='Login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        flash(f'You have been registered!')

        return redirect(url_for('login'))

    return render_template('form.html', form=form, title='Register')

@app.route('/profile', methods= ['GET', 'POST'])
def profile():
    person = {
        'id' : '1',
        'first_name' : 'John',
        'last_name' : 'Jingle',
        'username' : 'hiemerschmidt',
        'bio' : 'His name is my name too.',
        'age' : 180
    }

    tweets = [
        {
            'id' : 1,
            'tweet' : 'Who is stealing my name.',
            'date_posted' : '10/23/2019',
            'username' : 'hiemerschmidt'
        },

        {
            'id': 2,
            'tweet': 'Stop stealing my name.',
            'date_posted' : '10/05/2019',
            'username' : 'johnsmith'
        },
        {
            'id' : 3,
            'tweet' : 'Maybe this year, no one will steal my name.',
            'date_posted': '01/01/2019',
            'username' : 'hiemerschmidt'
        }
]

    form = PostForm()
    if form.validate_on_submit():
        tweets.insert(0, {
            'id' : len(tweets) + 1,
            'tweet' : form.tweet.data,
            'date_posted' : '10/23/2019',
            'username' : 'sample'
        })

    if form.validate_on_submit():
        print(form.tweet.data)
        #return redirect(url_for('profile'))
    return render_template('profile.html', title='Profile', person=person, tweets=tweets, form=form)
