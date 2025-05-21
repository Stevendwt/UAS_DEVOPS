import argparse
from flask import Flask, render_template_string, request

app = Flask(__name__)

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
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5001, help='Port to run the Flask app')
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port)
