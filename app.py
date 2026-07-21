from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hey_faiqa():
    return render_template("1-hey-faiqa.html")


@app.route("/2-something-funny.html")
def something_funny():
    return render_template("2-something-funny.html")


@app.route("/3-from-the-moment.html")
def from_the_moment():
    return render_template("3-from-the-moment.html")


@app.route("/faiqa-marry-me.html")
def marry_me():
    return render_template("faiqa-marry-me.html")


if __name__ == "__main__":
    app.run(debug=True)