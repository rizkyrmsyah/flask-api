from app import app
from app.model.user import User, UserSchema
from flask import request, Response, jsonify
from http import HTTPStatus
from datetime import datetime
from db import db

@app.route('/api/user', methods = ['GET'])
def index():
	users = User.query.all()
	output = []

	for user in users:
		data = {
			"id" : user.id, 
			"name" : user.name, 
			"email" : user.email, 
			"created_at" : str(user.created_at), 
			"updated_at" : str(user.updated_at)
		}
		output.append(data)

	return {"message" : "success", "data" : output}

@app.route('/api/user', methods = ['POST'])
def store():
	check = User.find_by_email(request.json['email'])
	if check != None:
		return {"message" : "Email sudah digunakan"}, HTTPStatus.UNPROCESSABLE_ENTITY
		
	user = User(
		email = request.json['email'],
		name = request.json['name'],
		created_at = datetime.now(), 
		updated_at = datetime.now()
	)
	User.save_to_db(user)

	return {"message" : "success"}, HTTPStatus.CREATED

@app.route('/api/user/<int:id>', methods = ['GET'])
def get(id):
	user = User.query.get(id)
	if user == None:
		return {"message" : "data tidak ditemukan"}, HTTPStatus.NOT_FOUND

	user_schema = UserSchema()
	data = user_schema.dump(user)

	return {"message" : "success", "data" : data}

@app.route("/api/user/<int:id>", methods=["DELETE"])
def delete(id):
	user = User.query.get(id)
	if user == None:
		return {"message" : "data tidak ditemukan"}, HTTPStatus.NOT_FOUND

	db.session.delete(user)
	db.session.commit()

	return {"message" : "success"}, HTTPStatus.NO_CONTENT

@app.route("/api/user/<int:id>", methods=["PUT", "PATCH"])
def update(id):
	user = User.query.get(id)
	if user == None:
		return {"message" : "data tidak ditemukan"}, HTTPStatus.NOT_FOUND

	user.name = request.json['name']
	user.email = request.json['email']
	user.created_at = datetime.now()
	
	db.session.commit()

	return {"message" : "success"}, HTTPStatus.OK