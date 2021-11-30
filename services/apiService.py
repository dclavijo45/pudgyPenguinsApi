from config import URL_BASE_IMAGES, LIST_NAMES, STATUS
import random

class ApiService:
    def get(self):
        result = []

        for item in range(20):
            result.append({
                'id': item,
                'name': random.choice(LIST_NAMES),
                'status': random.choice(STATUS),
                'image': URL_BASE_IMAGES+str(item),
            })

        return result

    def getById(self, id):
        result = {
            'id': id,
            'name': random.choice(LIST_NAMES),
            'status': random.choice(STATUS),
            'image': URL_BASE_IMAGES+str(id),
        }

        return result