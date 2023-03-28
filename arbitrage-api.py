from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Arbitrage(Resource):
    def get(self):
        data = pd.read_csv('arbitrage.txt')
        data = data.to_dict('records')
        return {'data' : data}, 200


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('arbitrage', required=True)
        args = parser.parse_args()

        data = pd.read_csv('arbitrage.txt')

        new_data = pd.DataFrame({
            'arbitrage'      : [args['arbitrage']],
        })

        data = data.append(new_data, ignore_index = True)
        data.to_csv('arbitrage.csv', index=False)
        return {'data' : new_data.to_dict('records')}, 201

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('arbitrage', required=True)
        args = parser.parse_args()

        data = pd.read_csv('arbitrage.csv')

        data = data[data['arbitrage'] != args['arbitrage']]

        data.to_csv('arbitrage.txt', index=False)
        return {'message' : 'Record deleted successfully.'}, 200



# Add URL endpoints
api.add_resource(Arbitrage, '/arbitrage')

if __name__ == '__main__':
    app.run()