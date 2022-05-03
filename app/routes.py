from flask import Blueprint, jsonify, abort, make_response

# 1. Create a virtual environment and activate it
# 1. Install the dependencies
# 1. Define a `Planet` class with the attributes `id`, `name`, and `description`, and one additional attribute
# 1. Create a list of `Planet` instances

# class Planet:
#     def __init__(self, id, name, description, color):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.color = color
    
#     def to_json(self):
#         return {"id": self.id,
#                 "name": self.name,
#                 "description": self.description,
#                 "color": self.color
#                 }

# earth = Planet(1,"Earth","home planet","blue, brown, green, and white")
# mercury = Planet(2, "Mercury", "closest planet to the sun", "grey")
# neptune = Planet(3, "Neptune", "eight planet, farthest from sun", "blue")
# jupiter = Planet(4, "Jupiter", "fifth planet from the sun, largest planet", "brown, orange and tan")

# planets = [earth, mercury, neptune, jupiter]

planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    planet_response = []
    planets = planet.query.all()
    for planet in planets:
        planet_response.append(planet.to_json())

    return jsonify(planet_response, 200)

def validate_id(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        return abort(make_response({"message": f"planet {planet_id} is not valid"}, 400))
    
    # for planet in planets:
    #     if planet.id == planet_id:
    #         return planet
    planet = planet.query.get(id)
    if not planet:
        return abort(make_response({"message": f"planet {planet_id} does not exist"}, 404))

# Get single planet
@planets_bp.route("/<planet_id>", methods = ["GET"])
def get_one_planet(planet_id):
    planet = validate_id(planet_id)
    return jsonify(planet.to_json(), 200)


