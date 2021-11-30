from services.apiService import ApiService
from flask.views import MethodView
from flask import jsonify

class ApiPudgyPenguinsController(MethodView):
    def get(self, id=None):
        service = ApiService()
        
        if id:
            try:
                id = int(id)

                if id < 0 or id > 8888:
                    return jsonify({"error": "Invalid id, min: 0 and max: 8888"}), 400
            except Exception as e:
                print(e)
                return jsonify({"error": "Invalid id, min: 0 and max: 8888"}), 400

            data = service.getById(id)
            return jsonify(data), 200
        else:
            data = service.get()

        response = {
            'info': {
                'total': 8888,
                'current_page': 0,
                'pages': 444,
                'next': 1,
                'prev': None
            },
            'data': data
        }

        return jsonify(response), 200