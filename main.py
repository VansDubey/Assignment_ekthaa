from flask import Flask
from routes.products import products_bp

app = Flask(__name__)

# register routes
app.register_blueprint(products_bp)

@app.route("/")
def home():
    return "Ekthaa Catalogue API Running!"

if __name__ == "__main__":
    app.run(debug=True)
