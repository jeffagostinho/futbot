from pymongo import MongoClient
from config import database

class PlayerRepository:

    def __init__(self):
        self.players = MongoClient(database['uri']).futbinbot.players

    def save(self, filter, data, upsert=True):
        self.followers.update_one(
            filter, 
            {
                '$set': data
            }, 
            upsert
        )