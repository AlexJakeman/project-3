# from flask import Flask, render_template
# import os

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/about")
# def about():
#     return render_template("about.html")


# @app.route("/help")
# def help():
#     return render_template("help.html")


# @app.route("/games")
# def games():
#     return render_template("games.html")

# if __name__ == "__main__":
#     app.run(
#         host=os.environ.get("IP", "0.0.0.0"),
#         port=int(os.environ.get("PORT", "5502")),
#         debug=True)
