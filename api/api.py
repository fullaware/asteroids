from asteroids import *



@app.route('/api/asteroids', methods=['GET'])
def get_asteroids():
    '''Function to get all the asteroids in the database'''
    return jsonify(Asteroids.get_all_asteroids())


# route to get asteroid by id
@app.route('/api/asteroids/<int:id>', methods=['GET'])
def get_asteroid_by_id(id):
    return_value = Asteroids.get_asteroid(id)
    return jsonify(return_value)


# route to add new asteroid
@app.route('/api/asteroids', methods=['POST'])
def add_asteroid():
    '''Function to add new asteroid to our database'''
    request_data = request.get_json()  # getting data from client
    print(request_data)
    Asteroids.add_asteroid(request_data["name"], request_data["sizekg"],request_data["hazard"],
                         request_data["diameterkm"], request_data["rotationh"], request_data["spectraltype"], request_data["au"])
    response = Response("asteroid added", 201, mimetype='application/json')
    return response


# route to update asteroid with PUT method
@app.route('/api/asteroids/<int:id>', methods=['PUT'])
def update_asteroid(id):
    '''Function to edit asteroid in our database using asteroid id'''
    request_data = request.get_json()
    Asteroids.update_asteroid(id, request_data["name"], request_data["sizekg"],request_data["hazard"],
                         request_data["diameterkm"], request_data["rotationh"], request_data["spectraltype"], request_data["au"])
    response = Response("asteroid Updated", status=200,
                        mimetype='application/json')
    return response


# route to delete asteroid using the DELETE method
'''
@app.route('/api/asteroids/<int:id>', methods=['DELETE'])
def remove_asteroid(id):
    # Function to delete asteroid from our database
    Asteroids.delete_asteroid(id)
    response = Response("asteroid Deleted", status=200,
                        mimetype='application/json')
    return response
'''
# route to search all asteroids by string


@app.route('/api/asteroids/search', methods=['POST'])
def search_asteroids():
    json_search = request.get_json()
    search_string = json_search['search']
    print(search_string)
    
    return Asteroids.search_all_asteroids(search_string)

@app.route('/api/asteroids/analytics', methods=['GET'])
def analyze_asteroids():
    '''Function to get all the asteroids in the database'''
    return jsonify(Asteroids.analyze_asteroids())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088, debug=True)