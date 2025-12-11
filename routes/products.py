from flask import Blueprint, request, jsonify
from config.database import db

products_bp = Blueprint("products", __name__)

# GET /catalogue
@products_bp.route("/catalogue", methods=["GET"])
def get_catalogue():
    shop_id = request.args.get("shop_id")
    products = list(db.products.find({
        "shop_id": shop_id,
        "is_visible_in_catalogue": True
    }, {"_id": 0}))

    return jsonify(products)
