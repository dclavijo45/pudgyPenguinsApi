from os import getenv as env
import random
import string

#Server
SECRET_KEY = ''.join(random.choice(f"{string.ascii_uppercase}{string.punctuation}{string.ascii_letters}") for i in range(20))
PORT = int(env('PORT', 33507))
HOST = env('HOST', '0.0.0.0')
DEBUG = int(env('DEBUG', '1'))

#App
URL_BASE_IMAGES = "https://api.pudgypenguins.io/penguin/image/"
LIST_NAMES = [
    'Bell', 'Woods', 'Sapphire', 'Summers', 'Phoenix', 'Cookies and Cream', 'Cuddles', 'Cupcake',
    'Cupid', 'Doodles', 'Dots', 'Milky', 'Way', 'Mud', 'Muddy', 'Muffin', 'Whiskers', 'Speckle'
]
STATUS = [
    'Eating', 'Working', 'Playing', 'Resting'
]

#MySQL
MYSQL_HOST = env('mysql_host', 'localhost')
MYSQL_USER = env('mysql_user', 'pwd')
MYSQL_PASSWORD = env('mysql_password', 'pwd')
MYSQL_DB = env('mysql_db', 'db_pudgy_penguins')