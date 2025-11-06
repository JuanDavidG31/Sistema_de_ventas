from pymongo import MongoClient
from django.conf import settings
from decouple import config  

client = MongoClient(config('DATABASE_URL'))
db = client["juguete"]
