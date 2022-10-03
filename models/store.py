from db import db

class StoreModel(db.Model):   #mapping table rows with the class objects 
    __tablename__="stores"  #we are creating table name as dunder(magic methods) 
    
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    items=db.relationship("ItemModel",back_populates="store",lazy="dynamic")  #lazy dynamic speeds up the application a little bit
    tags=db.relationship("TagModel",back_populates="store",lazy="dynamic")
