from flask import Flask, redirect, url_for, jsonify, request
app = Flask(__name__)

@app.route('/')
def welcome_message():
    return "Welcome to our website"

@app.route("/admin")
def admin_message():
    return "We welcome our admin"

@app.route("/user/<guest>")
def guest_message(guest):
    if guest == "admin":
        return redirect(url_for('admin_message'))
    elif guest == "home":
        return redirect(url_for('welcome_message'))
    else:
        return f"{guest} is our guest"

if __name__ == '__main__':
    app.run(debug=True)