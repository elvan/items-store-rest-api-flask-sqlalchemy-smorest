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
    return {
        'stores': stores
    }


@app.post('/store')
def create_store():
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
