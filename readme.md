Event Management System
Overview
The Event Management System is a web application that allows users to create, manage, and view events. Key features include event creation, RSVPs, scheduling, and email notifications.

Features
Event Creation: Users can create events by providing details such as title, description, date, location, and time.
RSVPs: Attendees can RSVP to events, allowing event organizers to manage guest lists.
Scheduling: Events are scheduled with a specific date and time.
Notifications: Email notifications are sent to attendees about new events and updates.
Technologies Used
Flask: A lightweight WSGI web application framework.
Flask-SQLAlchemy: SQLAlchemy integration with Flask.
Flask-Mail: Flask extension for sending email.
SQLite: Database for storing event data.
Setup Instructions
Clone the Repository or Extract the ZIP File

If using Git: git clone <repository-url>
If using ZIP: Extract the contents to your local directory.
Install Dependencies Make sure you have Python installed. Then, install the required packages using pip:

bash
Copy code
pip install -r requirements.txt
Configuration

Update the email configuration in System Management System.py:
python
Copy code
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
Database Initialization Run the following command to create the database tables:

bash
Copy code
python System\ Management\ System.py
Run the Application Start the Flask application using:

bash
Copy code
python System\ Management\ System.py
The application will be accessible at http://127.0.0.1:5000.

Usage
Homepage: / - Displays the home page.
Create Event: /create_event - Form to create a new event.
List Events: /list_events - View all events.

Contact
For any questions, please contact: 

Email: vschandrashekarparepalli@gmail.com