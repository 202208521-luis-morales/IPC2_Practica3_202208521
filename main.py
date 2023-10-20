from flask import Flask, request, jsonify

app = Flask(__name__)

"""
Data structure:
{ 
  "movieId": 2,
  "name": "SAW X",
  "genre": "Terror"
}
"""

data_store = []

@app.route("/api/new-movie", methods=['POST'])
def add_movie():
  if request.method == 'POST':
    data = request.json
    print(data)
    data_store.append(data)    

    return 'Datos guardados correctamente', 201
  
@app.route("/api/all-movies-by-genre/<genre>", methods=['GET'])
def get_movies_by_genre(genre):
  if request.method == 'GET':
    return jsonify([movie for movie in data_store if genre == movie["genre"]]), 201
  
@app.route("/api/update-movie", methods=['PUT'])
def update_movie():
  if request.method == 'PUT':
    data = request.json
    print(data)
    indice_elemento = next((index for (index, d) in enumerate(data_store) if d['movieId'] == data["movieId"]), None)

    if indice_elemento is not None:
        data_store[indice_elemento].update(data)
        return jsonify(data_store[indice_elemento]), 201
    else:
        return 'Elemento no encontrado', 400

    

if __name__ == '__main__':
    app.run(debug=True)