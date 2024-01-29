from flask import Flask, request, jsonify
import requests


app = Flask(__name__)

@app.route('/books', methods=['GET'])
def books():
    queries = request.args.to_dict()
    books = requests.get('https://sse-book-api-server.fpf7gvfpdfacbxby.uksouth.azurecontainer.io/books').json()
    filtered_books = []
    if queries:
        for book in books:
            if all(query in book for query in queries):
                filtered_books.append(book)
        return jsonify(filtered_books)
    else:
        return books


if __name__ == '__main__':
    app.run(debug=True)