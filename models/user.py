from db import db

class UserModel(db.model):
    __tablename__="users"

    id=db.Column(db.Integer,primary_key=True)
    username =db.Coumn(db.String(80),unique=True,nullable=False)
    password=db.Column(db.String(80),nullable=False)
    
