from flask import Blueprint, request, jsonify
from config.database import db

products_bp = Blueprint("products", __name__)

