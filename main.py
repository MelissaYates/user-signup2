from flask import Flask, request, redirect, render_template
import cgi
import os
import re
import jinja2

#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config["DEBUG"] = True

def isemail(email_text):
    return email_text.count('@') == 1 and email_text.count('.') == 1 and email_text.count(' ') == 0
#' ' in email

@app.route('/') #goes to 127.0.0.1:5000
def index():
    return render_template('signup.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    username = ''
    username_error = ''
    password_error = ''
    verify_password_error = ''
    email = ''
    email_error = ''
    
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']

        #username validation
        if username == '':
            username_error = 'You must input a username.'
        elif ' ' in username:
            username_error = "Username cannot contain spaces."

        if len(username)<3 or len(username)>20:
            username_error = "Username must be between 3 and 20 characters."
        

        #password validation
        if password == '':
            password_error = 'You must input a password.'
        elif ' ' in password:
            password_error = "Password cannot contain spaces."

        if len(password)<3 or len(password)>20:
            password_error = "Username must be between 3 and 20 characters."

        if verify_password != password:
            verify_password_error = "Passwords do not equal."


        # for i in username:
        #     if i.isspace():
        #         username_error = 'Username cannot contain spaces.'
        #         username = ' '

        #email validation

        if len(email)> 0 and not isemail(email):
            email_error = 'Email is not valid.'
            
                

        # if " " in email:
        #     email_error = "Email cannot contain spaces."
        # elif "@" not in email
            
            
    if (username_error == "" and password_error == "" and verify_password_error == "" and email_error == ""):
        return render_template('hello_greeting.html', username=username)
    else:
        return render_template('signup.html', username=username, email=email, username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)


@app.route('/hello_greeting')
def hello_greeting():
    title = "Welcome 'username'!"
    username = request.args.get('username')
    return render_template('hello_greeting.html', title='title', username='username')

if __name__ == ('__main__'):
    app.run()
