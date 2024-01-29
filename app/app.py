from flask import Flask, request, jsonify
import requests


app = Flask(__name__)


@app.route('/books', methods=['GET'])
def books():
    queries = request.args.to_dict()
    books = requests.get('http://sse-book-api-server.fpf7gvfpdfacbxby.uksouth.azurecontainer.io/books').json()
    filtered_books = []

    if queries:
        for book in books:
            # Check if each key-value pair in queries matches the corresponding pair in the book
            if all(str(book.get(key, None)) == value for key, value in queries.items()):
                filtered_books.append(book)
        return jsonify(filtered_books)
    else:
        return jsonify(books)  # Return all books if there are no query parameters

if __name__ == '__main__':
    app.run(debug=True)
