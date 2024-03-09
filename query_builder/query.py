list_products = [
    {
        '$project': {
            'title': 1, 
            'price': 1, 
            'imageUrl': 1, 
            'company': 1, 
            'sizes': 1, 
            'id': 1, 
            '_id': 0
        }
    }
]