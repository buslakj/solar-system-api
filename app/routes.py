from unicodedata import name
from flask import Blueprint, jsonify

# 1. Create a virtual environment and activate it
# 1. Install the dependencies
# 1. Define a `Planet` class with the attributes `id`, `name`, and `description`, and one additional attribute
# 1. Create a list of `Planet` instances

class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color

Earth = Planet(1,"Earth","description","Blue and Green")
Mercury = Planet(2, "Mercury", "description", "color")
Neptune = Planet(3, "Neptune", "description", "color")
Jupiter = Planet(4, "Jupiter", "description", "color")

planets = [Earth, Mercury, Neptune, Jupiter]

planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planets_bp.route("", methods = ["GET"])
def get_all_planets():
    planet_response = []
    for planet in planets:
        planet_response.append({
            "id":planet.id,
            "name":planet.name,
            "description":planet.description,
            "color": planet.color
        })
    return jsonify(planet_response)
