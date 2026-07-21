from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hey_faiqa():
    return render_template("hey-faiqa.html")


@app.route("/something-funny.html")
def something_funny():
    return render_template("something-funny.html")


@app.route("/from-the-moment.html")
def from_the_moment():
    return render_template("from-the-moment.html")


@app.route("/would-u-marry-me.html")
def marry_me():
    return render_template("would-u-marry-me.html")


if __name__ == "__main__":
    app.run(debug=True)