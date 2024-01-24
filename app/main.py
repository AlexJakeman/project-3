import gspread
from google.oauth2.service_account import Credentials
from flask import Flask, flash, redirect, render_template, request, url_for
from pprint import pprint
from operator import itemgetter
from datetime import datetime
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
SHEET = GSPREAD_CLIENT.open('gamer_lingo')

app = Flask(__name__)

app.secret_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!' 

gc = gspread.service_account(filename='creds.json')

sh = gc.open_by_key('1W8zqyGt7SDpNYsbf_4ikPRKzVppZRxwFX49FG836AlA')

user_sheet = SHEET.worksheet("users")
review_sheet = SHEET.worksheet("reviews")
word_sheet = SHEET.worksheet("lingo")


class Words:
    def __init__(self, Word, Context, Meaning, Added_by, Test, Date, Id, row_idx):
        self.Word = Word
        self.Context = Context
        self.Meaning = Meaning
        self.Added_by = Added_by
        self.Test = Test
        self.Date = Date
        self.Id = Id
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
def word_list():
    word_records = word_sheet.get_all_records()

    for record in word_records:
        record['Date'] = datetime.strptime(record['Date'], '%d/%m/%Y %H:%M:%S')

    sorted_word_records = sorted(word_records, key=itemgetter('Date'), reverse=True)

    newest_word_records = sorted_word_records[:1000]

    words = []
    for idx, word in enumerate(newest_word_records, start=2):
        word['Date'] = word['Date'].strftime('%d/%m/%Y %H:%M:%S')
        
        word = Words(**word, row_idx=idx)
        words.append(word)

    n_words_added = sum(1 for word in word_records if not word['Test'])

    return render_template("base.html", words=words, n_words_added=n_words_added)

@app.route('/', methods=['POST'])
def add_term():
    max_id = 0
    word_records = word_sheet.get_all_records()
    for record in word_records:
        record_id = int(record['Id'])
        if record_id > max_id:
            max_id = record_id

    new_id = max_id + 1

    today_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    name = request.form['name']
    term = request.form['term']
    context = request.form['context']
    meaning = request.form['meaning']

    new_term = [term, context, meaning, name, today_date, new_id]

    try:
        word_sheet.append_row(new_term)
        flash("New term added successfully!", 'success')  # Flash a success message
    except Exception as e:
        flash(f"Error adding new term: {e}", 'danger')  # Flash an error message

    return redirect('/')
    
@app.route('/delete/<int:id>', methods=['POST'])
def delete_term(id):
    word_records = word_sheet.get_all_records()

    record_to_delete = next((record for record in word_records if record['Id'] == id), None)

    if record_to_delete:
        row_id = word_records.index(record_to_delete)

        try:
            word_sheet.delete_row(row_id + 2)
            flash("Deletion successful", 'success')  # Flash a success message
        except Exception as e:
            flash(f"Error deleting row: {e}", 'danger')  # Flash an error message
    else:
        flash(f"No record found with Id {id}", 'danger')  # Flash an error message

    return redirect('/')
    
# @app.route('/users')
# def user_list():
#     user_records = user_sheet.get_all_records()
#     users = []
#     for idx, user in enumerate(user_records, start=2):
#         user = User(**user, row_idx=idx)
#         users.append(user)
        
#     n_users_w_review = sum(1 for user in users if user.Joined)
        
#     return render_template("base.html", users=users, n_users_w_review=n_users_w_review)

# @app.route('/filter_game', methods=['GET'])
# def filter_game():
#     game_to_filter = request.args.get('game_name')  # Get the game name from the URL parameter
#     reviews = []

#     if not game_to_filter:
#         return "Please provide a game name to filter."

#     filtered_reviews = [review for review in reviews if review.Game == game_to_filter]
#     n_filtered_reviews = sum(1 for review in filtered_reviews if review.Summary)

#     return render_template("filtered_reviews.html", reviews=filtered_reviews, n_game_review=n_filtered_reviews)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
