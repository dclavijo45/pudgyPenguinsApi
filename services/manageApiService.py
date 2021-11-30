from schemas.PudgyPenguinSchema import pudgyPenguin, pudgyPenguins
from models.PudgyPenguin import PudgyPenguin
from util.Db import db

class ManageApiService:
    def getAll(self):
        try:
            result = PudgyPenguin.query.all()

            return pudgyPenguins.dump(result)
        except Exception as e:
            print(e)
            return {}
    
    def get(self, id):
        try:
            result = PudgyPenguin.query.get(id)

            return pudgyPenguin.dump(result)
        except Exception as e:
            print(e)
            return {}

    def create(self, name, status, image):
        try:
            new = PudgyPenguin(name, status, image)
            db.session.add(new)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
        
    def update(self, id, name, status, image):
        try:
            result = PudgyPenguin.query.get(id)

            result.name = name
            result.status = status
            result.image = image
            
            db.session.commit()

            return True
        except Exception as e:
            print(e)
            return False

    def delete(self, id):
        try:
            result = PudgyPenguin.query.get(id)
            db.session.delete(result)
            db.session.commit()

            return True
        except Exception as e:
            print(e)
            return False