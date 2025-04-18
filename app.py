from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# render templates
@app.route("/honorform/", methods=["GET"])
def honorform():
    return render_template("honorform.html")


# Home route (GET request)
@app.route("/")
def home():
    return "Hello from Flask!"


# GET route with query parameters
@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "stranger")
    return f"Hello, {name}!"


# POST route with JSON body
@app.route("/echo", methods=["POST"])
def echo():
    data = {key: request.form.getlist(key) for key in request.form.keys()}
    return jsonify(data)


# POST route with form data
@app.route("/submit-form", methods=["POST"])
def submit_form():
    name = request.form.get("name")
    email = request.form.get("email")
    return f"Received form submission: {name}, {email}"


if __name__ == "__main__":
    app.run(debug=True)
