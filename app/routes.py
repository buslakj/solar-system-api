from flask import Blueprint, jsonify, abort, make_response
from app.models.planet import Planet

planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    planet_response = []
    planets = Planet.query.all()
    for planet in planets:
        planet_response.append(planet.to_json())

    return jsonify(planet_response, 200)

def validate_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return abort(make_response({"message": f"planet {planet_id} is not valid"}, 400))
    
    planet = Planet.query.get(id)
    if not planet:
        return abort(make_response({"message": f"planet {planet_id} does not exist"}, 404))

# Get single planet
@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    planet = validate_id(planet_id)
    return jsonify(planet.to_json(), 200)


