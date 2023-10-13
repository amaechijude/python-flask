from flask import Flask
app = Flask(__name__)
@app.route("/<name>")
def hello(name):
    return f"Hello {name}"
    
@app.route('/add/<num>')
def add_num(num):
    n = int(num)
    result = n**3
    output = str(result)
    return f"The square of {num} is {output}"

if __name__ == '__main__':
    app.run(debug=True)