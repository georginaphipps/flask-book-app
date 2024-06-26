import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html", page_title="About Betsy's Book Reviews")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have signed you up!" .format(request.form.get("name")))
    return render_template("contact.html", page_title="Contact Us")


@app.route("/books")
def books():
    data = []
    with open("data/reviews.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("books.html", page_title="Latest Books", reviews=data)


@app.route("/books/<book_name>")
def books_book(book_name):
    book = {}
    with open("data/reviews.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == book_name:
                book = obj
    return render_template("book-review.html", book=book)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=False)