import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the Jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# Generate sitemap
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# ✅ Get all family members
@app.route('/members', methods=['GET'])
def get_all_members():
    return jsonify(jackson_family.get_all_members()), 200

# ✅ Get a single family member
@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member:
        return jsonify(member), 200
    return jsonify({"message": "Member not found"}), 404

# ✅ Add a new member
@app.route('/members', methods=['POST'])
def add_member():
    try:
        data = request.get_json(force=True)

        if not data or "first_name" not in data or "age" not in data or "lucky_numbers" not in data:
            return jsonify({"message": "Missing required fields"}), 400

        new_member = jackson_family.add_member(data)

        if not new_member:
            return jsonify({"message": "Failed to add member"}), 400

        return jsonify(new_member), 200  

    except Exception as e:
        return jsonify({"message": "Invalid request", "error": str(e)}), 400


# ✅ Delete a member
@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    result = jackson_family.delete_member(member_id)
    if result:
        return jsonify(result), 200
    return jsonify({"message": "Member not found"}), 404

# Run the app
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
