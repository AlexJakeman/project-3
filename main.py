import gspread
from google.oauth2.service_account import Credentials
from flask import Flask, flash, redirect, render_template, request, url_for
from pprint import pprint
from operator import itemgetter
from datetime import datetime
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

app = Flask(__name__, template_folder='app/templates')

app.secret_key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!' 

gc = gspread.service_account(filename='creds.json')

sh = gc.open_by_key('1W8zqyGt7SDpNYsbf_4ikPRKzVppZRxwFX49FG836AlA')

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

    return render_template( "base.html", words=words, n_words_added=n_words_added )

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
        flash("New term added successfully!", 'success')
    except Exception as e:
        flash(f"Error adding new term: {e}", 'danger')

    return redirect('/')
    
@app.route('/update_term/<int:id>', methods=['POST'])
def update_term(id): 
    max_id = 0
    word_records = word_sheet.get_all_records()
    
    record_to_delete = next((record for record in word_records if record['Id'] == id), None)
    
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
    
    row_id = word_records.index(record_to_delete)
    
    try:
        word_sheet.delete_row(row_id + 2)
        word_sheet.append_row(new_term)
        flash("Updated term successfully!", 'success')
    except Exception as e:
        flash(f"Error updating term: {e}", 'danger')

    return redirect('/')
    
@app.route('/delete_term/<int:id>', methods=['POST'])
def delete_term(id):
    word_records = word_sheet.get_all_records()

    record_to_delete = next((record for record in word_records if record['Id'] == id), None)

    if record_to_delete:
        row_id = word_records.index(record_to_delete)

        try:
            word_sheet.delete_row(row_id + 2)
            flash("Deleted term successfully!", 'success')
        except Exception as e:
            flash(f"Error deleting row: {e}", 'danger')
    else:
        flash(f"No record found with Id {id}", 'danger')

    return redirect('/')
    
if __name__ == "__main__":
    app.run()
