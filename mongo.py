'''Mongo related class and function'''

from pymongo import MongoClient

class MongoManager():
    '''Mongo related things are encapsulated'''

    def connect_to_mongo(self, mongo_url):
        '''Connect to mongo function'''
        client = MongoClient(mongo_url)
        return client
    
    def disconnect_from_mongo(self, client):
        '''Disconnect from Mongo'''
        client.close()
        return {'message':'Client closed'}
    
    def query_to_mongo(self,client, collection,query):
        '''Query the mongo DB for data'''
        col_name = client['Indi-Moda-development'][collection]
        data = list(col_name.aggregate(query))
        print(data)
        self.disconnect_from_mongo(client)
        return data
