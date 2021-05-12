import pymongo

import private


class Database:
    URI = private.uri
    DATABASE = None

    @staticmethod
    def initialize():
        #client = pymongo.MongoClient(Database.URI, ssl=True, ssl_cert_reqs='CERT_NONE')
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client[private.db_name]

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_latest(collection, query):
        return Database.DATABASE[collection].find(query).sort([("$natural", -1)])

    @staticmethod
    def find_latest_sort(collection, query):
        return Database.DATABASE[collection].find(query).sort([("time_int", -1)])

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def find_one_latest(collection, query):
        return Database.DATABASE[collection].find(query).sort([("$natural",-1)]).limit(1)

    @staticmethod
    def update(collection, query, data):
        return Database.DATABASE[collection].update(query, data, upsert=True)

    @staticmethod
    def update_one(collection, query, data):
        return Database.DATABASE[collection].update_one(query, data, upsert=True)

    @staticmethod
    def remove(collection, data):
        return Database.DATABASE[collection].remove(data)

    @staticmethod
    def count(collection, query):
        return Database.DATABASE[collection].count_documents(query)
