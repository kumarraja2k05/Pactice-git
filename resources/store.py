from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from flask import request
from db import db
from flask_smorest import abort,Blueprint
from flask.views import MethodView
from models import StoreModel
from schemas import StoreSchema

blp=Blueprint("stores",__name__,description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200,StoreSchema)
    def get(self,store_id):
        store=StoreModel.get_or_404(store_id)
        return store
        
    
    def delete(self,store_id):
        store=StoreModel.query.get_or_404(store_id)
        raise NotImplementedError("Deleting an item is not implemented.")

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200,StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(200,StoreSchema)
    def post(self,store_data):
        s=StoreModel(**store_data)
        try:
            db.session.add(s)
            db.session.commit()
        except IntegrityError:
            abort(400,message="A store with that name already exists.")
        except SQLAlchemyError:
            abort(500,message="An error occured creating the store.")
        return s

        # for s in store.values():
        #     if store_data["name"]==store["name"]:
        #         abort(400,message=f"Store already exists.")
        # store_id=uuid.uuid4().hex
        # s={**store_data,"id": store_id}  
        # store[store_id]=s  
        # return s

