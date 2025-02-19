from pymongo import MongoClient


client = MongoClient('localhost', 27017)
db = client['stressbook']  # Replace with your MongoDB database name

users_collection = db['users']
events_collection = db['events']
seats_collection = db["seats"]