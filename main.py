import os
from datetime import datetime
from flask import Flask, render_template,request,jsonify
from routes.products import products_bp
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("DB_NAME", "ekthaa_db")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]       
products_col = db["products"]

# register routes
app.register_blueprint(products_bp)

def _serialize_product(doc):
    """Convert Mongo doc to JSON-friendly dict"""
    return {
        "_id": str(doc.get("_id")),
        "shop_id": doc.get("shop_id"),
        "name": doc.get("name"),
        "sku": doc.get("sku"),
        "cost_price": doc.get("cost_price"),
        "selling_price": doc.get("selling_price"),
        "stock_quantity": doc.get("stock_quantity"),
        "description": doc.get("description"),
        "image_url": doc.get("image_url"),
        "is_visible_in_catalogue": doc.get("is_visible_in_catalogue", False),
        "created_at": doc.get("created_at").isoformat() if doc.get("created_at") else None,
    }

@app.route("/")
@app.route('/', methods=['GET'])
def home():
    # fetch products from MongoDB
    products = list(db.products.find({}))

    # convert ObjectId for safety (optional)
    for p in products:
        p['_id'] = str(p['_id'])

    # render template with data
    return render_template('catalouge.html', deals=products)


@app.route("/add-product")
def add():
    return render_template("addProducts.html")

@app.route("/add-product", methods=["POST"])
def add_product():
  
    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify({"error": "Invalid or missing JSON"}), 400

    # minimal validation
    required = ["shop_id", "name", "cost_price", "selling_price", "stock_quantity", "description", "image_url"]
    missing = [f for f in required if f not in data]
    if missing:
        return jsonify({"error": "Missing fields", "missing": missing}), 400

    product = {
        "shop_id": str(data.get("shop_id")),
        "name": str(data.get("name")),
        "sku": data.get("sku"),
        "cost_price": float(data.get("cost_price")),
        "selling_price": float(data.get("selling_price")),
        "stock_quantity": int(data.get("stock_quantity")),
        "category": str(data.get("category")), 
        "description": str(data.get("description")),
        "image_url": str(data.get("image_url")),
        "is_visible_in_catalogue": bool(data.get("is_visible_in_catalogue", False)),
        "created_at": datetime.utcnow(),
    }

    result = products_col.insert_one(product)
    inserted = products_col.find_one({"_id": result.inserted_id})
 
    return jsonify({"message": "Product added", "product": _serialize_product(inserted)}), 201

@app.route("/catalogue", methods=["GET"])
def catalogue():
    """Return only products with is_visible_in_catalogue = true."""
    cursor = products_col.find({"is_visible_in_catalogue": True}).sort("created_at", -1)
    products = [_serialize_product(doc) for doc in cursor]
    return jsonify({"products": products}), 200

@app.route("/search")
def search_products():
    query = request.args.get("query", "")

    if query.strip() == "":
        products = list(db.products.find())
    else:
        products = list(db.products.find({
            "$or": [
                {"name": {"$regex": query, "$options": "i"}},
                {"description": {"$regex": query, "$options": "i"}},
                {"sku": {"$regex": query, "$options": "i"}}
            ]
        }))

    return render_template("catalouge.html", deals=products)


if __name__ == "__main__":
    app.run(debug=True)
