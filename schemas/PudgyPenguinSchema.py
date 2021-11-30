from util.Ma import ma

class PudgyPenguinSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'status', 'image')

pudgyPenguin = PudgyPenguinSchema()

pudgyPenguins = PudgyPenguinSchema(many=True)