from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.get("/store") # http://127.0.0.1:5000
def get_sotres():
    """
    Get all stores.
    
    Returns:
        dict: A dictionary containing all stores and their items
    """
    return {"stores": stores}

@app.post("/store")
def create_store():
    """
    Create a new store.

    Request Body (JSON):
        {
            "name": "Store Name"
        }
    
    Returns:
        dict: the newly created store with a 201 status code.
    """
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    """
    Create a new item in a specific store.

    Request Body (JSON):
        {
            "name": "Item Name",
            "price": 9.99
        }
    
    Returns:
        dict: the newly created item with a 201 status code, or an error message
        with a 404 status code if the store is not found.
   """
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>")
def get_store(name):
    """
    Get a specific store by name.
    Argus:
        name (str): The name of the store to retrieve.
        
    Returns: 
        dict: The store with the specified name, or an error message with
        a 404 status code if not found.
    """
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    """
    Get all items in a specific store.
    Argus: 
        name (str): The name of the store whose itme to retrieve.
        
        Returns:
            dict: A dictionary containing all items in the specified store,
            or an error message with a 404 status code if the store is not found.
    """
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404