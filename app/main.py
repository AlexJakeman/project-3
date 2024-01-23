# python code goes here
import gspread
from google.oauth2.service_account import Credentials
from flask import Flask, render_template
from pprint import pprint
# from gspread import GSPREAD_CLIENT
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('game_reviews')

app = Flask(__name__)

gc = gspread.service_account(filename='creds.json')

sh = gc.open_by_key('1W8zqyGt7SDpNYsbf_4ikPRKzVppZRxwFX49FG836AlA')

user_sheet = SHEET.worksheet("users")
review_sheet = SHEET.worksheet("reviews")


class Review:
    def __init__(self, ReviewId, Username, Game, Upvotes, Rating, Summary, Date, row_idx):
        self.ReviewId = ReviewId
        self.Username = Username
        self.Game = Game
        self.Upvotes = Upvotes
        self.Rating = Rating
        self.Summary = Summary
        self.Date = Date
        self.row_idx = row_idx
        
class User:
    def __init__(self, UserId, Username, Name, Email, Joined, Password, row_idx):
        self.ReviewId = UserId
        self.Username = Username
        self.Name = Name
        self.Email = Email
        self.Joined = Joined
        self.Password = Password
        self.row_idx = row_idx
        

@app.route('/')
def review_list():
    review_records = review_sheet.get_all_records()
    reviews = []
    for idx, review in enumerate(review_records, start=2):
        review = Review(**review, row_idx=idx)
        reviews.append(review)
        
    n_game_reviews = sum(1 for review in reviews if not review.Summary)
        
    return render_template("base.html", reviews=reviews, n_game_review=n_game_reviews)

# @app.route('/')    
# def user_list():
#     user_records = user_sheet.get_all_records()
#     users = []
#     for idx, user in enumerate(user_records, start=2):
#         user = User(**user, row_idx=idx)
#         users.append(user)
        
#     n_users_w_review = sum(1 for user in users if user.Joined)
        
#     return render_template("base.html", users=users, n_users_w_review=n_users_w_review)





if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
