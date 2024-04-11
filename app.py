from flask import Flask, render_template, redirect,request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from model import db, Contact
from flask_mail import Mail, Message
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '12345'  # Add your secret key here
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'zraaeae@gmail.com'  # Add your Gmail email here
app.config['MAIL_PASSWORD'] = 'ozwd aodx ifpg lvfm'  # Add your Gmail password here

# Initialize Flask extensions
mail = Mail(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')


#Contacts
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    contact = Contact(name=name, email=email, message=message)
    db.session.add(contact)
    db.session.commit()
        # Add the new contact to the database

        # Send email notification
    send_email_notification(name, email, message)
    
    return render_template('index.html')
def send_email_notification(name, email, message):
    msg = Message('Hiring Team',
                  sender=email,
                  recipients=['zraaeae@gmail.com'])  # Add your email here
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)
if __name__ == '__main__':
    db.create_all()
    app.run(debug=False)
