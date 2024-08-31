from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Access the database and collection
db = client.flask_db
collection = db.data

# Retrieve and print a document from the collection
document = collection.find_one()
print(document)
