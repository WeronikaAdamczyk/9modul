from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

books = [
    {"id": 1, "title": "Czuła przewodniczka", "author": "Natalia de Barbaro"},
    {"id": 2, "title": "Kicia Kocia. Wiosna!", "author": "Anita Głowińska"},
    {"id": 3, "title": "Kobieta z planem na życie.", "author": "Maye Musk"},
]


# lista książek
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# dodawanie nowej książki
@app.route('/books', methods=['POST'])
def add_book():
    new_book = {
        "id": len(books) + 1,
        "title": request.json['title'],
        "author": request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

#  pobieranie pojedynczej książki
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# usuwanie książki
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for index, book in enumerate(books):
        if book['id'] == book_id:
            del books[index]
            return jsonify({"message": "Book deleted successfully"})
    return jsonify({"error": "Book not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
