from config import URL_BASE_IMAGES, LIST_NAMES, STATUS
import random

class PaginatorService:
    def paginate(self, page):
        result = []

        for item in range(20):
            if(page * 20 + item == 8889):
                break

            result.append({
                'id': page * 20 + item,
                'name': random.choice(LIST_NAMES),
                'status': random.choice(STATUS),
                'image': URL_BASE_IMAGES+str(page * 20 + item),
            })

        return result