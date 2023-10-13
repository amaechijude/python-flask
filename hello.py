from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World"

@app.route("/mul")
def mul():
    def multiply_keys(param_dictionary):
        output = 1
        param = []
        for key in param_dictionary:
            param.append(param_dictionary[key])
            output = output * param_dictionary[key]
        return f"The mulpiplication of {param} = {output}"

    my_dictionary = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4
    }
    return jsonify(multiply_keys(my_dictionary))

@app.route("/dict")
def value_length():
    names = {
        1: "Amaechi",
        2: "GitStatusdiff",
        3: "Jude",
        4: "VsCode",
        5: "University"
    }
    result = {}
    for key in names:
        lenght = len(names[key])
        new_dictionary = {}
        new_dictionary[names[key]] = lenght
    
        result[key] = new_dictionary
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)