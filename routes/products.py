from flask import Blueprint, request, jsonify
from config.database import db

products_bp = Blueprint("products", __name__)

# POST /add-product
@products_bp.route("/add-product", methods=["POST"])
def add_product():
    data = request.json
    db.products.insert_one(data)
    return jsonify({"message": "Product added successfully"}), 201

# GET /catalogue
@products_bp.route("/catalogue", methods=["GET"])
def get_catalogue():
    shop_id = request.args.get("shop_id")
    products = list(db.products.find({
        "shop_id": shop_id,
        "is_visible_in_catalogue": True
    }, {"_id": 0}))

    return jsonify(products)
