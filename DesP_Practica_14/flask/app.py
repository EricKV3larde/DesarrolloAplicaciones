from flask import Flask, render_template, jsonify, request
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

# Configurar la conexión con Firebase
cred = credentials.Certificate('credenciales.json')
default_app = initialize_app(cred)
db = firestore.client()

@app.route('/')
def home():
    return render_template('index.html')

# Operación CREATE - Agregar un nuevo dato a Firebase
@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()
    doc_ref = db.collection('items').document()
    doc_ref.set(data)
    return jsonify({'message': 'Data added successfully'})

# Operación READ - Obtener todos los datos de Firebase
@app.route('/get', methods=['GET'])
def get_data():
    items = db.collection('items').get()
    data = []
    for item in items:
        item_dict = item.to_dict()
        item_dict['id'] = item.id
        data.append(item_dict)
    return jsonify(data)

# Operación UPDATE - Actualizar un dato en Firebase
@app.route('/update/<item_id>', methods=['PUT'])
def update_data(item_id):
    data = request.get_json()
    db.collection('items').document(item_id).update(data)
    return jsonify({'message': 'Data updated successfully'})

# Operación DELETE - Eliminar un dato de Firebase
@app.route('/delete/<item_id>', methods=['DELETE'])
def delete_data(item_id):
    db.collection('items').document(item_id).delete()
    return jsonify({'message': 'Data deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
