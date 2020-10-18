"""This is it."""

from flask import Flask, render_template
import random

localwebsite = Flask(__name__)


@localwebsite.route("/")
def home():
    """Return."""
    phrases = ["What is your favorite quality about yourself?", "What is a social justice issue you care about?", "If you had $100, what would you spend it on and why?"]
    randomint = random.randint(0,2)
    question = phrases[randomint]
    return render_template("h.html", question = question)


@localwebsite.route("/meetingroom")
def meetingroom():
    """Return."""
    return render_template("h2.html")


if __name__ == "__main__":
    localwebsite.run()
