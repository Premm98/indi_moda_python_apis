''' The main file of Python APIs
'''
from os import environ
from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api, Resource

from mongo import MongoManager

load_dotenv()

mongo_url = environ['MONGO_URL']
print(mongo_url)

app = Flask(__name__)
api = Api(app)
@api.route('/hello')
class HelloWorld(Resource):
    '''Class Hello World'''
    mongo_obj = MongoManager()
    client = mongo_obj.connect_to_mongo(mongo_url=mongo_url)
    print('Oh yeah!')
    mongo_obj.disconnect_from_mongo(client)

    def get(self):
        '''The Get function'''
        
        return 'hello'
if __name__ == '__main__':
    app.run()