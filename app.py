# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy.orm import scoped_session
from database import SessionLocal, init_db
from models import User, Task

app = Flask(__name__)
app.secret_key = 'cookie dough'

# Initialize the database and tables
init_db()

# Use a scoped session for thread safety
db = scoped_session(SessionLocal)


@app.route('/')
def home():
    users = db.query(User).all()
    return render_template('index.html', students=users)


@app.route('/insert', methods=['POST'])
def insert():
    name = request.form['name']
    email = request.form['email']
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    flash("User added successfully")
    return redirect(url_for('home'))


@app.route('/delete/<int:id>')
def delete(id):
    user = db.query(User).get(id)
    if user:
        db.delete(user)
        db.commit()
        flash("User deleted successfully")
    else:
        flash("User not found")
    return redirect(url_for('home'))


@app.route('/update', methods=['POST'])
def update():
    id = request.form['id']
    user = db.query(User).get(id)
    if user:
        user.name = request.form['name']
        user.email = request.form['email']
        db.commit()
        flash("User updated successfully")
    else:
        flash("User not found")
    return redirect(url_for('home'))


@app.route('/get_all_task/<int:user_id>')
def get_all_task(user_id):
    user = db.query(User).get(user_id)
    if not user:
        flash("User not found")
        return redirect(url_for('home'))

    tasks = db.query(Task).filter_by(user_id=user_id).all()
    return render_template('user_tasks.html', user=user, tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    user_id = request.form['user_id']
    title = request.form['title']
    description = request.form['description']
    status = request.form.get('status', 'new')
    task = Task(user_id=user_id, title=title, description=description, status=status)
    db.add(task)
    db.commit()
    flash("Task added successfully")
    return redirect(url_for('get_all_task', user_id=user_id))


@app.route('/update_task', methods=['POST'])
def update_task():
    task_id = request.form['task_id']
    task = db.query(Task).get(task_id)
    if task:
        task.title = request.form['title']
        task.description = request.form['description']
        task.status = request.form['status']
        user_id = task.user_id  # Get user_id before committing
        db.commit()
        flash("Task updated successfully")
        return redirect(url_for('get_all_task', user_id=user_id))
    else:
        flash("Task not found")
        return redirect(url_for('home'))


@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    task = db.query(Task).get(task_id)
    if task:
        user_id = task.user_id  # Capture before deletion
        db.delete(task)
        db.commit()
        flash("Task deleted successfully")
        return redirect(url_for('get_all_task', user_id=user_id))
    else:
        flash("Task not found")
        return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)
