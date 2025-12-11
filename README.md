📘 Ekthaa – Public Catalogue (Mini Project)
🌟 Project Overview

This project is a small functional slice of the upcoming Ekthaa Catalogue feature.
Its purpose is simple: shop owners can add products, and customers can view only the publicly visible products through a clean catalogue page.

The project focuses on proving the core data flow:

Save product data → fetch visible products → show them in a neat, searchable catalogue.

No login, no advanced UI — just the basics done well.

🚀 Key Features:
Add Products Easily: Products are added using the POST /add-product API with a simple JSON body—no image upload needed, just an image URL.

Public Catalogue View: The catalogue displays only those products where is_visible_in_catalogue = true, showing their image, name, price, and stock status.

Live Search: A search bar lets users instantly filter products by name as they type.

Category Filters: Users can filter products based on categories for quicker and organised browsing.

🧰 Tech Stack
🔹 Backend

Python Flask
Database

🔹 Frontend

HTML + CSS + JavaScript
Jinja2 Templates (used to generate the catalogue page dynamically from Flask)

🔹 Image Handling
No uploads — only URL strings stored in the database.

▶️ How to Run the Project
1. Clone the repository
git clone https://github.com/VansDubey/Assignment_ekthaa.git
cd Assignment_ekthaa

2. Install dependencies
pip install -r requirements.txt

3. Add your environment variables

Create a .env file:
MONGO_URI="mongodb+srv://dvanshika32_db_user:51dhlBH2j8LSuLRR@cluster0.ykgxqsr.mongodb.net/?appName=Cluster0"
DB_NAME="ekthaa"

4. If you created a virtual environment:
Windows
venv\Scripts\activate

macOS/Linux
source venv/bin/activate
If you are NOT using a virtual environment, you can skip this part.

5. Run the Flask server
python main.py

Open your browser and go to:

👉 http://localhost:5000/