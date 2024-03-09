''' The main file of Python APIs
'''
from os import environ
from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api, Resource
import json
from bson import ObjectId
from query_builder.query import list_products
from mongo import MongoManager

load_dotenv()

mongo_url = environ['MONGO_URL']

app = Flask(__name__)
api = Api(app, title='Indi Moda APIs', version='1.0.0', default_label='Mongo APIs', default='Indi-Moda-Developement')
@api.route('/hello')
class HelloWorld(Resource):
    '''Class Hello World'''
    

    def get(self):
        '''The Get function'''
        mongo_obj = MongoManager()
        client = mongo_obj.connect_to_mongo(mongo_url=mongo_url)
        data = mongo_obj.query_to_mongo(client=client,collection='product_details',query=list_products)
        def serialize(obj):
            if isinstance(obj, ObjectId):
                return str(obj)
            return obj
        # return json.dumps(data, default=serialize, indent=2)
        return list(data)
    

if __name__ == '__main__':
    app.run()