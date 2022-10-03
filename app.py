from flask import Flask
import os
import secrets
from flask_smorest import abort,Api
from db import db
import models
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint

def create_app(db_url=None):
    app=Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"]=True
    app.config["API_TITLE"]="Stores REST API"
    app.config["API_VERSION"]="v1"
    app.config["OPENAPI_VERSION"]="3.0.3"
    app.config["OPENAPI_URL_PREFIX"]="/"
    app.config["OPENAPI_SWAGGER_UI_PATH"]="/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"]="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"]=db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
    db.init_app(app)  
    migrate=Migrate(app,db)
    api=Api(app)

    app.config["JWT_SECRET_KEY"]=secrets.SystemRandom().getrandbits(128)    #getting a secret key
    jwt=JWTManager(app)

    @app.before_first_request
    def creat_tables():
        db.create_all

    
    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    return app


# from email import message
# from flask import Flask,request
# import uuid
# from db import items,store

# @app.get("/store")
# def get_stores():
#     return {"stores":list(store.values())}

# @app.post("/store")
# def create_store():
#     store_data=request.get_json()   #used to get data from get request
#     if "name" not in store_data:
#         abort(
#           400,
#           message="Bad request. Ensure 'name' is included in the JSON payload",  
#         )
#     for s in store.values():
#         if store_data["name"]==store["name"]:
#             abort(400,message=f"Store already exists.")
#     store_id=uuid.uuid4().hex
#     s={**store_data,"id": store_id}    # used to get new json data from the user
#     store[store_id]=s  # storing requested data in store list
#     return s, 201  # giving status code as of succesfull creation of resource

# @app.post("/item")   # this <string:name> will point to the store list "name": "Store"
# def create_item():
#     item_data=request.get_json()
#     if (
#         "price" not in item_data
#         or "store_id" not in item_data
#         or "name" not in item_data
#     ):
#         abort(
#             400,
#             message="Bad Request,Ensure 'price','store_id, and 'name' are included in the JSON payload.",
#         )
#     for item in items.values():
#         if(
#             item_data["name"]==item["name"]
#             and item_data["store_id"]==item["store_id"]
#         ):
#             abort(400,message="Item already exists.")
#     if item_data["store_id"] not in store:
#         abort(404,message= "Store not found")

#     item_id=uuid.uuid4().hex
#     item={**item_data,"id": item_id}    # used to get new json data from the user
#     items[item_id]=item  # storing requested data in store list
#     return item, 201
    
# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}


# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         return store[store_id]
#     except KeyError:
#         abort(404,message= "Store not found")

# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404,message= "Store not found")


# @app.delete("/item/<string:item_id>")
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message":"Item deleted."}
#     except KeyError:
#         abort(404,message="Item not found.")

# @app.put("/item/<string:item_id>")
# def update_item(item_id):
#     item_data=request.get_json()
#     if "price" not in item_data or "name" not in item_data:
#         abort(400,message="Bad request. Ensure 'price', and 'name' are included in Json payload.")

#     try:
#         item=items[item_id]
#         item!=item_data
#         return item

#     except KeyError:
#         abort(404,message="Item not found.")
        
# @app.delete("/item/<string:store_id>")
# def delete_store(store_id):
#     try:
#         del store[store_id]
#         return {"message":"Item deleted."}
#     except KeyError:
#         abort(404,message="Item not found.")