from flask import Flask, redirect, url_for, request, jsonify

app = Flask(__name__)
@app.route("/")
def home_page():
    return "Welcome back"

@app.route("/login")
def login_func():
    response = {
        "Name": "name",
        "Address": "address",
        "Age": "age",
        "Email": "email"
        }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)