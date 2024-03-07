''' The main file of Python APIs
'''

from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)
@api.route('/hello')
class HelloWorld(Resource):
    '''Class Hello World'''

    def get(self):
        '''The Get function'''
        
        return 'hello'
if __name__ == '__main__':
    app.run()