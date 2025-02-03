from flask import Flask, render_template, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/dbname'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Define your routes here or import them from another module

@app.route('/')
def index():
    return redirect(url_for('alarm'))

@app.route('/alarm')
@login_required
def alarm():
    alarms = []  # Later, fetch from your database
    return render_template('alarm.html', alarms=alarms)

@app.route('/timer')
@login_required
def timer():
    timers = []  # Later, fetch from your database
    return render_template('timer.html', timers=timers)

@app.route('/reminders')
@login_required
def reminders():
    reminders_list = []  # Later, fetch from your database
    return render_template('reminders.html', reminders=reminders_list)

# Admin route example
@app.route('/admin')
@login_required
def admin():
    if not getattr(current_user, 'is_admin', False):
        abort(403)
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
