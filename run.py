import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About Betsy's Book Reviews")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact Us")


@app.route("/books")
def books():
    return render_template("books.html", page_title="Latest Books")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)