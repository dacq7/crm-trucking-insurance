from flask import Blueprint, request, jsonify
from crm_app.extensions import db
from crm_app.models.user import User

users_bp = Blueprint("users", __name__, url_prefix="/api/users")


@users_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users]), 200


@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON body provided"}), 400

    email = data.get("email")
    name = data.get("name")

    if not email or not name:
        return jsonify({"error": "email and name are required"}), 400

    existing = User.query.filter_by(email=email).first()
    if existing:
        return jsonify({"error": "User with this email already exists"}), 409

    user = User(email=email, name=name)
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201


@users_bp.route("/<int:user_id>/", methods=["PUT"])
def update_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No JSON body provided"}), 400

    email = data.get("email")
    name = data.get("name")

    if email:
        user.email = email

    if name:
        user.name = name

    db.session.commit()

    return jsonify(user.to_dict()), 200


@users_bp.route("/<int:user_id>/", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully"}), 200
