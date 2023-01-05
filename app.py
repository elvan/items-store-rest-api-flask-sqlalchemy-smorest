from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'The Chair',
                'price': 15.99
            },
            {
                'name': 'The Table',
                'price': 25.99
            }
        ]
    }
]


@app.get('/store')
def list_stores():
    # List all the stores
    return {
        'stores': stores
    }


@app.post('/store')
def create_store():
    # Create a new store

    request_data = request.get_json()

    new_store = {}

    if request_data is not None:
        new_store = {
            'name': request_data['name'],
            'items': []
        }

        stores.append(new_store)

    return {
        'message': 'Store created',
        'store': new_store
    }, 201


@app.post('/store/<string:name>/item')
def create_item_in_store(name):
    # Create items in each store

    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            if request_data is None:
                return {
                    'message': 'Item not created, request_data is None'
                }, 400

            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }

            store['items'].append(new_item)

            return {
                'message': 'Item created',
                'item': new_item
            }, 201

    return {
        'message': 'Store not found'
    }, 404
