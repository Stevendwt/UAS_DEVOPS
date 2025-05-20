from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret-key"

# Dummy user data
users = {"admin": "password123"}

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in users and users[username] == password:
            return f"Welcome, {username}!"
        else:
            flash("Invalid username or password")
            return redirect(url_for('login'))
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
