from flask.views import MethodView
from flask_smorest import abort,Blueprint
from db import db
from models import StoreModel
from schemas import UserSchema
from passlib.hash import pbkdf2_sha256

blp=Blueprint("stores",__name__,description="Operations on stores")

@blp.route("/store/<int:store_id>")
class Store(MethodView):
    def get(self,store_id):
        store=StoreModel.query.get_or_404(store_id)
        return store

    