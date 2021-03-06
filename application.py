
from flask import Flask
from flask import render_template
import csv
import json
import os

application = app = Flask(__name__)

print(os.getcwd())

@app.route('/')
def my_runs():
    runs = []

    with open("runs.csv", "r") as runs_file:
        reader = csv.DictReader(runs_file)

        for row in reader:
            runs.append(row["polyline"])

    return render_template("index.html", runs = json.dumps(runs))



if __name__ == "__main__":
    application.run(host='0.0.0.0', port = 8080, debug=True)
