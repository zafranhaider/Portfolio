from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__, template_folder='templates')

# Flask-Mail configuration for Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'zraaeae@gmail.com'  # Your Gmail email
app.config['MAIL_PASSWORD'] = 'ozwd aodx ifpg lvfm'  # Your Gmail password
app.config['MAIL_DEFAULT_SENDER'] = 'zraaeae@gmail.com'  # Your Gmail email

# Initialize Flask-Mail
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    send_email_notification(name, email, message)
    return render_template('index.html')

def send_email_notification(name, email, message):
    msg = Message('Hiring Team',
                  sender=app.config['MAIL_DEFAULT_SENDER'],
                  recipients=['zraaeae@gmail.com'])  # Your recipient email
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=False)
