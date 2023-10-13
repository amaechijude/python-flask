from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/login", methods=['POST'])
def login_func():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        age = request.form.get('age')
        email = request.form.get('email')
        response = {
            "Name": name,
            "Address": address,
            "Age": age,
            "Email": email
        }
        return jsonify(response)
    else:
        response1 = {"error": "Method not supported"}
        return jsonify(response1)

if __name__ == '__main__':
    app.run(debug=True)
