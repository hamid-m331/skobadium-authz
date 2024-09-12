from flask_restful import abort, request
from authz import db
from authz.decorator import auth_required
from authz.model import User
from authz.schema import UserSchema

class UserController:
    @auth_required
    def create_user():
        if request.content_type != "application/json":
            abort(415)  # Bad Media Type
        user_schema = UserSchema(only=["username","password"])
        try:
            data = user_schema.load(request.get_json())  # Validate user data
        except:
            abort(400)  # INVALID Request
        if not data["username"] or not data["password"]:
            abort(400)  # Empty Data
        user = User.query.filter_by(username=data["username"]).first()
        if user is not None:
            abort(409)  # User already registered
        user = User(username=data["username"], password=data["password"])
        try:
            db.session.add(user)  # add to database session
        except:
            abort(500)  #  database error
        try:
            db.session.commit()  # database create query
        except:
            db.session.rollbask()  
            abort(500)  # database error
        user_schema = UserSchema()
        return {
            "user": user_schema.dump(user)
        }, 200
    @auth_required
    def get_users():
        try:
            users = User.query.all() 
        except:
            abort(500)  # database error
        users_schema = UserSchema(many=True)
        return {
            "user": users_schema.dump(users)
        },200

    def get_user(user_id):
        try:
            user = User.query.get(user_id) 
        except:
            abort(500)  # database error
        user_schema = UserSchema()
        if user is None:
            return abort(404)
        return {
            "user": user_schema.dump(user)
        },200 
    @auth_required
    def update_user(user_id):
        if request.content_type != "application/json":
            abort(415)
        user_schema = UserSchema(only=["password"])
        try:
            data = user_schema.load(request.get_json()) # validate request data
        except:
            abort(400)
        if not data["password"]:
            abort(400)
        user = User.query.get(user_id)  # select the user
        if user is None:
            return abort(404)
        user.password = data["password"]
        try:
            db.session.commit()  # database update query
        except:
            db.session.rollback()
            abort(500)  # database error
        user_schema = UserSchema()
        return {
            "user": user_schema.dump(user)
        }, 200
    @auth_required
    def delete_user(user_id):
        try:
            user = User.query.get(user_id)
        except:
            abort(500)  # database error 
        db.session.delete(user)  # create deletion in session
        try:
            db.session.commit()  # delete entry
        except:
            db.session.rollback()  # database creation rollback
        return{}, 204