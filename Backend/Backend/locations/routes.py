from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from Backend.shared.db import db
from Backend.locations.models import Location
from Backend.locations.schemas import location_schema, locations_schema

locations = Blueprint('locations', __name__)

@locations.route('/', methods=['POST'])
@jwt_required()
def add_location():
    data = request.get_json()
    new_location = Location(name=data['name'], description=data['description'], latitude=data['latitude'], longitude=data['longitude'])
    db.session.add(new_location)
    db.session.commit()
    return location_schema.jsonify(new_location), 201

@locations.route('/<id>', methods=['DELETE'])
@jwt_required()
def delete_location(id):
    location = Location.query.get(id)
    db.session.delete(location)
    db.session.commit()
    return jsonify({'message': 'Location deleted'})

@locations.route('/', methods=['GET'])
@jwt_required()
def get_locations():
    locations = Location.query.all()
    return locations_schema.jsonify(locations)
