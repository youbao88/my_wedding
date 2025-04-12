from flask import Flask, request, jsonify, Blueprint
from .database import insert_rsvp
from . import limiter  # Import the shared limiter instance

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/', methods=['POST'])
@limiter.limit('5 per 5 minutes')  # Apply rate limit to this route
def submit_rsvp():
    try:
        data = request.get_json()
        guest_name = data.get('guestName')
        guest_count = data.get('guestCount')

        if not guest_name or not guest_count:
            return jsonify({"error": "Invalid input"}), 400

        insert_rsvp(guest_name, int(guest_count))
        return jsonify({"message": "RSVP submitted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
