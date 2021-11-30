from util.Db import db

class PudgyPenguin(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15))
    status = db.Column(db.String(7))
    image = db.Column(db.String(30))

    def __init__(self, name, status, image):
        self.name = name
        self.status = status
        self.image = image
