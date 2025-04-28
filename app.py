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
    sql = "INSERT INTO honorsurvey_responses (race, gender, pregnant, druguse, bariaticsurgery, type2diabetic, howlongtype2diabetic, a1c, pastmonthlostcontrol, numberoftimeslostcontrol, compelledtoconsumefood, compelled_to_consume_text, unabletostopeating, unable_to_stop_text, lostcontrolbeforet2d, lost_control_before_text, lostcontrolworse, lost_control_worse_text, soughttreatment, treatmentaccess, engageintreatment, mobiletechnology, tech_apps, tech_benefits, heardaboutstudy) VALUES ('"

    sql += "|".join(data.get("race", [""]))
    sql += "','"
    sql += data.get("gender", [""])[0]
    sql += "','"
    sql += data.get("pregnant", [""])[0]
    sql += "','"
    sql += data.get("druguse", [""])[0]
    sql += "','"
    sql += data.get("bariaticsurgery", [""])[0]
    sql += "','"
    sql += data.get("type2diabetic", [""])[0]
    sql += "','"
    sql += data.get("howlongtype2diabetic", [""])[0]
    sql += "','"
    sql += data.get("a1c", [""])[0]
    sql += "', '"
    sql += data.get("pastmonthlostcontrol", [""])[0]
    sql += "', '"
    sql += data.get("numberoftimeslostcontrol", [""])[0]
    sql += "', '"
    sql += data.get("compelledtoconsumefood", [""])[0]
    sql += "', '"
    sql += data.get("compelled_to_consume_text", [""])[0]
    sql += "', '"
    sql += data.get("unabletostopeating", [""])[0]
    sql += "', '"
    sql += data.get("unable_to_stop_text", [""])[0]
    sql += "', '"
    sql += data.get("lostcontrolbeforet2d", [""])[0]
    sql += "', '"
    sql += data.get("lost_control_before_text", [""])[0]
    sql += "', '"
    sql += data.get("lostcontrolworse", [""])[0]
    sql += "', '"
    sql += data.get("lost_control_worse_text", [""])[0]
    sql += "', '"
    sql += data.get("soughttreatment", [""])[0]
    sql += "', '"
    sql += "|".join(data.get("treatmentaccess", [""]))
    sql += "', '"
    sql += data.get("engageintreatment", [""])[0]
    sql += "', '"
    sql += data.get("mobiletechnology", [""])[0]
    sql += "', '"
    sql += data.get("tech_apps", [""])[0]
    sql += "', '"
    sql += data.get("tech_benefits", [""])[0]
    sql += "', '"
    sql += "|".join(data.get("heardaboutstudy", [""]))
    sql += "');"
    runQuery(sql)
    return sql
