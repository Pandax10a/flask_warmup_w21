# import modules to make it work
from unittest import result
from flask import Flask
import dbhelpers as dh
import json

app = Flask(__name__)

@app.get('/books')

def all_books():
    result=dh.run_statement('CALL return_all_books_author()')
    book_json = json.dumps(result, default=str)
    return book_json

@app.get('/books_authored')

def book_count():
    result=dh.run_statement('CALL author_count_of_books')
    book_json = json.dumps(result, default=str)
    return book_json

@app.get('/best_selling_book')

def best_selling():
    result=dh.run_statement('CALL most_copy_sold()')
    book_json = json.dumps(result, default=str)
    return book_json
@app.get('/best_selling_author')

def best_selling_author():
    result=dh.run_statement('CALL most_copies_sold')
    book_json = json.dumps(result, default=str)
    return book_json


app.run(debug=True)