from app import app

@app.route('/node/<uuid>', methods=['GET'])
def fetch_node(uuid):
    pass

@app.route('/node', methods=['POST'])
def create_node():
    pass

@app.route('/node/<uuid>', methods=['DELETE'])
def delete_node(uuid):
    pass

@app.route('node/<uuid>', methods=['PUT, PATCH'])
def update_node(uuid):
    pass