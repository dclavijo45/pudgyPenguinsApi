from os import getenv as env
import random
import string

#Server
SECRET_KEY = ''.join(random.choice(f"{string.ascii_uppercase}{string.punctuation}{string.ascii_letters}") for i in range(20))
PORT = int(env('PORT', 33507))
DEBUG = int(env('DEBUG', '1'))
HOST = env('HOST', '0.0.0.0')

#App
LIST_NAMES = [
    'Bell', 'Woods', 'Sapphire', 'Summers', 'Phoenix', 'Cookies and Cream', 'Cuddles', 'Cupcake',
    'Cupid', 'Doodles', 'Dots', 'Milky', 'Way', 'Mud', 'Muddy', 'Muffin', 'Whiskers', 'Speckle'
]
URL_BASE_IMAGES = "https://api.pudgypenguins.io/penguin/image/"
STATUS = [
    'Eating', 'Working', 'Playing', 'Resting'
]

#MySQL
MYSQL_PASSWORD = env('MYSQL_PASSWORD', 'pwd')
MYSQL_DB = env('MYSQL_DB', 'db_pudgy_penguins')
MYSQL_HOST = env('MYSQL_HOST', 'localhost')
MYSQL_USER = env('MYSQL_USER', 'pwd')