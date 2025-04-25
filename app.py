from flask import Flask, request, jsonify, render_template

## This imports the configuration parser library
import configparser

## This creates an instance of its 'ConfigParser' tool
cfg = configparser.ConfigParser()
## This reads data from 'config.ini' into that 'cfg' variable
cfg.read(".env")
import mysql.connector

app = Flask(__name__)


def runQuery(sql):
    dbconn = mysql.connector.connect(
        user=cfg["db"]["user"],
        password=cfg["db"]["password"],
        host=cfg["db"]["host"],
        database=cfg["db"]["database"],
    )
    cursor = dbconn.cursor()
    cursor.execute(sql)
    dbconn.commit()
    dbconn.close()


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
    print(data["heardaboutstudy"])
    return jsonify(data)


# # POST route with form data
# @app.route("/submit-form", methods=["POST"])
# def submit_form():
#     data = {key: request.form.getlist(key) for key in request.form.keys()}
#     return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)


# POST route with form data
@app.route("/submit-form", methods=["POST"])
def submit_form():
    data = {key: request.form.getlist(key) for key in request.form.keys()}
    # return jsonify(data)
    # sql = "INSERT INTO honorsurvey_responses (gender, a1c, heardaboutstudy) VALUES ('150', 'male', 'event|email');"
    sql = "INSERT INTO honorsurvey_responses (gender, a1c, heardaboutstudy) VALUES ('"
    sql += data["a1c"][0]
    sql += "', '"
    sql += data["gender"][0]
    sql += "', '"
    sql += "|".join(data["heardaboutstudy"])
    sql += "');"
    runQuery(sql)
    return sql
