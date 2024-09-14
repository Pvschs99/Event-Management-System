from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail,Message
from datetime import datetime, timedelta
from flask_migrate import Migrate

app=Flask(__name__)
# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'xabcabc163@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'Eagle@8181'   # Replace with your email password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail=Mail(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
migrate=Migrate(app,db)
# Define the Event model
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    schedule = db.relationship('Schedule', backref='event', lazy=True)
    attendees = db.relationship('Attendee', backref='event', lazy=True)
class Attendee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    rsvp_status = db.Column(db.String(10), nullable=False)  # Yes, No, Maybe
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
class Schedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frequency = db.Column(db.String(20), nullable=False)  # e.g., daily, weekly, monthly
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)


def send_email_notification(event, attendee):
    try:
        msg = Message(
            subject=f"Reminder: {event.title}",
            sender='your-email@gmail.com',
            recipients=[attendee.email]
        )

        msg.body = f"""
                Dear {attendee.name},

                This is a reminder for the upcoming event:
                Title: {event.title}
                Description: {event.description}
                Date: {event.date}
                Time: {event.time}
                Location: {event.location}

                Please mark your calendar!

                Regards,
                Event Management Team
            """
        mail.send(msg)
        print("Email sent successfully")
    except Exception as e:
        print("message sent")

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/send_reminders")
def send_reminders():
    events = Event.query.all()
    for event in events:
        event_date = datetime.strptime(event.date, '%Y-%m-%d')
        # Send reminder 2 days before event
        if event_date - timedelta(days=2) == datetime.today().date():
            for attendee in event.attendees:
                send_email_notification(event, attendee)
    return "Reminders sent!"
@app.route("/create_event",methods=["GET","POST"])
def create_event():
    if request.method=='POST':
        title=request.form['title']
        description=request.form['description']
        date=request.form['date']

        location=request.form['location']

        new_event = Event(title=title, description=description, date=date,  location=location)
        db.session.add(new_event)
        db.session.commit()


        send_email_notification(new_event)
        return redirect(url_for('list_events'))
    return render_template("create_event.html")
@app.route("/list_events")
def list_events():
    events=Event.query.all()
    return render_template("list_events.html",events=events)

with app.app_context():
    db.create_all()



if __name__=="__main__":
    app.run(debug=True)