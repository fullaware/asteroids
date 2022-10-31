from asteroids import *

URIPATH = "/api/asteroids"


class AsteroidList(Resource):
    def get(self):
        return jsonify(AsteroidsModel.get_all_asteroids())

    def post(self):
        '''Function to add new asteroid to our database'''
        request_data = request.get_json()  # getting data from client
        print(request_data)
        AsteroidsModel.add_asteroid_json(request_data)
        response = Response("asteroid added", 201, mimetype='application/json')
        return response


class AsteroidById(Resource):
    def get(self, asteroid_id):
        return_value = AsteroidsModel.get_asteroid(asteroid_id)
        return jsonify(return_value)

    def put(self, asteroid_id):
        request_data = request.get_json()
        AsteroidsModel.update_asteroid_json(asteroid_id, request_data)
        response = Response("asteroid Updated", status=200,
                            mimetype='application/json')
        return response

class AsteroidMineById(Resource):
    def get(self, asteroid_id):
        return_value = AsteroidsModel.get_asteroid(asteroid_id)
        return jsonify(return_value)

    def put(self, asteroid_id):
        request_data = request.get_json()
        AsteroidsModel.update_asteroid_json(asteroid_id, request_data)
        response = Response("asteroid Updated", status=200,
                            mimetype='application/json')
        return response

class AsteroidSearch(Resource):
    def post(self):
        json_search = request.get_json()
        search_string = json_search['search']
        print(search_string)

        return AsteroidsModel.search_all_asteroids(search_string)

class AsteroidScanRange(Resource):
    def post(self):
        json_request = request.get_json()
        range = json_request['range']
        location = json_request['location']

        return AsteroidsModel.scanrange_asteroids(range, location)

class AsteroidAnalytics(Resource):
    def get(self):
        return jsonify(AsteroidsModel.analyze_asteroids())


api.add_resource(AsteroidList, URIPATH)
api.add_resource(AsteroidById, f"{URIPATH}/<asteroid_id>")
api.add_resource(AsteroidMineById, f"{URIPATH}/mine/<asteroid_id>")
api.add_resource(AsteroidSearch, f"{URIPATH}/search")
api.add_resource(AsteroidAnalytics, f"{URIPATH}/analytics")
api.add_resource(AsteroidScanRange, f"{URIPATH}/scan")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8088, debug=True)
