import pymongo
import certifi

con_string="mongodb+srv://onlinebusinessfy:Test@fsdi-107.pukor.mongodb.net/?retryWrites=true&w=majority&appName=FSDI-107"

client = pymongo.MongoClient(con_string, tlsCAFILE=certifi.where())
db = client.get_database("organika")
