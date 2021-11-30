from services.paginatorService import PaginatorService
from flask.views import MethodView
from flask import jsonify

class PaginatorPudgyPenguinsController(MethodView):
    def get(self, page=0):
        service = PaginatorService()

        try:
            page = int(page)

            if page < 0:
                page = 0
            
            if page > 444:
                page = 444
        except Exception as e:
            print(e)
            page = 0

        data = service.paginate(page)

        response = {
            'info': {
                'total': 8888,
                'current_page': page,
                'pages': 444,
                'next': page + 1 if page != 444 else None,
                'prev': page - 1 if page != 0 else None
            },
            'data': data
        }

        return jsonify(response), 200