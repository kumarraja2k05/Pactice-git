from flask import request
from flask_smorest import abort,Blueprint
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import ItemModel

from schemas import ItemSchema,ItemUpdateSchema

blp=Blueprint("Items",__name__,description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200,ItemSchema)
    def get(self,item_id):
        item=ItemModel.query.get_or_404(item_id)   # get data from database 
        return item
    
    def delete(self,item_id):
        item=ItemModel.query.get_or_404(item_id)
        raise NotImplementedError("Deleting an item is not implemented.")
    
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200,ItemSchema)
    def put(self,item_id,item_data):
        item=ItemModel.query.get(item_id)
        #raise NotImplementedError("Updating an item is not implemented.")
        if item:
            item.price=item_data["price"]
            item.name=item.data["name"]
        else:
            item=ItemModel(id=item_id,**item_data)

        db.session.add(item)
        db.session.commit()
        return item

@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200,ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    @blp.arguments(ItemSchema)
    @blp.response(201,ItemSchema)
    def post(self,item_data):
        item=ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500,message="An error occured while inserting the item.")
            
        return item