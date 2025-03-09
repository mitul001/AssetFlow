# 📌 AssetFlow
*A comprehensive inventory management system built with Django.*

## 🚀 Features
- **Contact Management** - Add, update, and delete contacts (Customers & Suppliers).
- **Product Management** - Manage product details, pricing, and availability.
- **Inventory Transactions** - Handle buying and selling of products.
- **Automatic Pricing** - Fetch product prices dynamically.
- **User-Friendly UI** - Bootstrap-styled responsive design.

## 📸 Screenshots
### 🔹 Dashboard
<img src="https://github.com/mitul001/AssetFlow/blob/main/images/home.png?raw=true" width="500">

### 🔹 Contact Management
<img src="https://github.com/mitul001/AssetFlow/blob/main/images/contact_list.png?raw=true" width="500">
<img src="https://github.com/mitul001/AssetFlow/blob/main/images/create_contact.png?raw=true" width="500">
<img src="https://github.com/mitul001/AssetFlow/blob/main/images/update_contact.png?raw=true" width="500">

### 🔹 Product Management
<img src="https://github.com/mitul001/AssetFlow/blob/main/images/product_list.png?raw=true" width="500"> 
<img src="https://github.com/mitul001/AssetFlow/blob/main/images/create_product.png?raw=true" width="500">
<img src="https://github.com/mitul001/AssetFlow/blob/main/images/update_product.png?raw=true" width="500"> 

### 🔹 Inventory Transactions 
<img src="https://github.com/mitul001/AssetFlow/blob/main/images/inventory_list.png?raw=true" width="500"> 
<img src="https://github.com/mitul001/AssetFlow/blob/main/images/create_inventory.png?raw=true" width="500">

## 🛠️ Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/mitul001/AssetFlow.git
cd AssetFlow
```
### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5️⃣ Create Superuser
```bash
python manage.py createsuperuser
```
### 6️⃣ Run the Server
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your browser.

## 📜 Usage
- **Contacts**: Manage customers & suppliers.
- **Products**: Add & update products.
- **Inventory**: Log buy/sell transactions.

## 📂 Project Structure
```
AssetFlow/
│── assetflow/
│   │── contact_app/
│   │── product_app/
│   │── inventory/
│   └── static/
│── images/
│── manage.py
│── requirements.txt
└── README.md
```

🚀 **Developed by [mitul001](https://github.com/mitul001/)**
