import uuid
from flask import Flask, request
from db import items, stores

app = Flask(__name__)

@app.get("/store") # http://127.0.0.1:5000
def get_stores():
    """
    Get all stores.
    
    Returns:
        dict: A dictionary containing all stores and their items
    """
    return {"stores": list(stores.values())}

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
    store_data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store, 201

@app.post("/item")
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
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item

    return item, 201

@app.get("/store/<string:store_id>")
def get_store(store_id):
    """
    Get a specific store by name.
    Argus:
        name (str): The name of the store to retrieve.
        
    Returns: 
        dict: The store with the specified name, or an error message with
        a 404 status code if not found.
    """
    try:
        return stores[store_id]
    except:
        return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/item")
def get_item(item_id):
    """
    Get all items in a specific store.
    Argus: 
        name (str): The name of the store whose itme to retrieve.
        
        Returns:
            dict: A dictionary containing all items in the specified store,
            or an error message with a 404 status code if the store is not found.
    """
    try:
        return items[item_id]
    except KeyError:
        return {"message": "Item not found"}, 404