# 📘 Ekthaa – Public Catalogue (Mini Project)

## 🌟 Project Overview
This project is a small functional slice of the upcoming **Ekthaa Catalogue** feature.  
Its purpose is simple:

- Shop owners can **add products**, and  
- Customers can view **only publicly visible products** through a clean catalogue page.

The project demonstrates the core data flow:

➡️ Save product data → Fetch visible products → Display them in a neat, searchable catalogue

No login, no complex UI — just the basics done well.

---

## 🚀 Key Features

### ✔️ Add Products Easily  
Products are added using the `POST /add-product` API with a simple JSON body.  
No image upload — only an **image URL** is required.

### ✔️ Public Catalogue View  
The catalogue displays only those products where:
is_visible_in_catalogue = true




Each visible product shows its **image, name, price, and stock status**.

### ✔️ Live Search
A built-in search bar filters products **instantly** as the user types.

### ✔️ Category Filters
Users can filter products by categories for a clean and organised browsing experience.

---

## 🧰 Tech Stack

### 🔹 Backend
- Python Flask  
- NoSQL Database (MongoDB)

### 🔹 Frontend
- HTML  
- CSS  
- JavaScript  
- **Jinja2 Templates** for dynamic rendering via Flask

### 🔹 Image Handling
- No uploads  
- Only **image URL strings** stored in the database

---

## ▶️ How to Run the Project

### **1. Clone the repository**
```bash
git clone https://github.com/VansDubey/Assignment_ekthaa.git
cd Assignment_ekthaa

2. Install dependencies
pip install -r requirements.txt

3. Add your environment variables

Create a .env file:

MONGO_URI="mongodb+srv://dvanshika32_db_user:51dhlBH2j8LSuLRR@cluster0.ykgxqsr.mongodb.net/?appName=Cluster0"
DB_NAME="ekthaa"

4. (Optional) Activate your virtual environment
Windows
venv\Scripts\activate

macOS / Linux
source venv/bin/activate

If you're not using a virtual environment, skip this step.

5. Run the Flask server
python main.py

Open your browser and go to:
👉 http://localhost:5000/

