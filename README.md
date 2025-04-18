# Simple Flask Backend Example for Beginning Python Students

This repo provides a simple Flask backend to support front-end JavaScript applications. It's designed for students who are learning JavaScript but are also taking an introductory Python course and want to experiment with using Flask for their backend.

---

## Requirements

- Python 3.x
- `pip` (Python package installer)
- Basic terminal knowledge

---

## Clone the Repo, Start a Virtual Environment, Install Flask, and Run your App

```bash
git clone https://github.com/jetweedy/flask-startup.git
cd flask-startup
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install flask
flask run
```

## Test it out

If your app isn't currently running, you can restart it like so:
```
cd flask-startup
source venv/bin/activate  # Windows: venv\Scripts\activate
flask run
```

Visit http://localhost:5000/ in your browser to see your running app.

You can test out your GET variables like this:

**GET:**

Simply visit this page:

http://127.0.0.1:5000/greet?name=Bilbo

**POST:**

Visit this page and submit your form:

http://127.0.0.1:5000/static/form.html


