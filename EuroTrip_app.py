
from flask import Flask
from flask import render_template
import csv
import json
import os

app = Flask(__name__)


print(os.getcwd())

@app.route('/')
def my_runs():
    runs = []

    with open("runs.csv", "r") as runs_file:
        reader = csv.DictReader(runs_file)

        for row in reader:
            runs.append(row["polyline"])

    # return render_template("jsTests.html", runs = json.dumps(runs))

    # return render_template("AllFeatures.html", runs = json.dumps(runs))
    return render_template("index.html", runs = json.dumps(runs))
    # return render_template("AllFeatures_dev2.html", runs = json.dumps(runs))



if __name__ == "__main__":
    app.run(port = 5002)