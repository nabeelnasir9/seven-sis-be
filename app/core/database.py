from pymongo import MongoClient
from .config import settings

client = MongoClient(settings.DATABASE_URL, tls=True, tlsAllowInvalidCertificates=True)
db = client[settings.DATABASE_NAME]
product_collection = db[settings.COLLECTION_NAME]
