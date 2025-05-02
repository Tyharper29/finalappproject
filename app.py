# Import Flask functions for web app handling
from flask import Flask, request, jsonify, render_template

## This imports the configuration parser library
import configparser
import mysql.connector  # Import MySQL connector for database access

## This creates an instance of its 'ConfigParser' tool
cfg = configparser.ConfigParser()
## This reads data from 'config.ini' into that 'cfg' variable
cfg.read(".env")

# Create Flask application instance
app = Flask(__name__)


# Function to run SQL queries
def runQuery(sql):
    # Connect to MySQL database
    dbconn = mysql.connector.connect(
        user=cfg["db"]["user"],
        password=cfg["db"]["password"],
        host=cfg["db"]["host"],
        database=cfg["db"]["database"],
    )
    cursor = dbconn.cursor()  # Create cursor object to execute SQL
    cursor.execute(sql)
    dbconn.commit()
    dbconn.close()


# Route to render a HTML form
@app.route("/honorform/", methods=["GET"])
def honorform():
    return render_template("honorform.html")


# Home route (GET request), returns a simple message
@app.route("/")
def home():
    return "Hello from Flask!"


# Route to greet user via query parameters
@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name", "stranger")
    return f"Hello, {name}!"


# Route to echo back POSTed form data as JSON
@app.route("/echo", methods=["POST"])
def echo():
    data = {key: request.form.getlist(key) for key in request.form.keys()}
    print(data["heardaboutstudy"])
    return jsonify(data)


# Start Flask server if file is run directly
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)


# Route to handle form submission
@app.route("/submit-form", methods=["POST"])
def submit_form():
    # COllect all submitted form data
    data = {key: request.form.getlist(key) for key in request.form.keys()}
    # Build SQL insert statement with values from form data
    sql = "INSERT INTO honorsurvey_responses (race, gender, pregnant, druguse, bariaticsurgery, type2diabetic, HowLongType2Diabetic, a1c, pastmonthlostcontrol, numberoftimeslostcontrol, compelledtoconsumefood, unabletostopeating, lostcontrolbeforet2d, lostcontrolworse, soughttreatment, treatmentaccess, engageintreatment, mobiletechnology, tech_apps, tech_benefits, heardaboutstudy) VALUES ('"
    # Concatenate form values into the SQL string
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
    sql += data.get("HowLongType2Diabetic", [""])[0]
    sql += "','"
    sql += data.get("a1c", [""])[0]
    sql += "', '"
    sql += data.get("pastmonthlostcontrol", [""])[0]
    sql += "', '"
    sql += data.get("numberoftimeslostcontrol", [""])[0]
    sql += "', '"
    sql += data.get("compelledtoconsumefood", [""])[0]
    sql += "', '"
    sql += data.get("unabletostopeating", [""])[0]
    sql += "', '"
    sql += data.get("lostcontrolbeforet2d", [""])[0]
    sql += "', '"
    sql += data.get("lostcontrolworse", [""])[0]
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
    runQuery(sql)  # run SQL insert command
    return sql  # return executed SQL string
