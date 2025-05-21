from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Template login
login_template = '''
<!doctype html>
<title>Login</title>
<h2>Login Page</h2>
<form method="post">
  Username: <input type="text" name="username"><br><br>
  Password: <input type="password" name="password"><br><br>
  <input type="submit" value="Login">
</form>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            return '<h1>Login successful!</h1>'
        else:
            return '<h1>Login failed. Try again.</h1>'
    return render_template_string(login_template)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
