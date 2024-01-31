# form_app.py
from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        title = request.form.get('title')
        author = request.form.get('author')
        publication_year = request.form.get('publication_year')
        genre = request.form.get('genre')

        # Prepare data for the API request
        data = {'title': title, 'author': author, 'publication_year': publication_year, 'genre': genre}

        # Send a POST request to the API
        response = requests.post(os.environ.get(BOOKS_API_URL), data=data)
        
        # Get the JSON response from the API
        filtered_books = response.json()

        # Render a new page to display the books as cards
        return render_template('books.html', books=filtered_books)

    # Render the form for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
