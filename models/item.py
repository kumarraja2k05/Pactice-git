from enum import unique
from db import db

class ItemModel(db.Model):   #mapping table rows with the class objects 
    __tablename__="items"  #we are creating table name as dunder(magic methods) 
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    price=db.Column(db.Float(precision=2),unique=False,nullable=False)
    store_id=db.Column(db.Integer, db.ForeignKey("stores.id"),unique=False,nullable=False)
    store=db.relationship("StoreModel",back_populates="items")