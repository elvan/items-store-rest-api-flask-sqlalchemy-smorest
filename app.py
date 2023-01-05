from flask import Flask

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
def get_stores():
    return {
        'stores': stores
    }
