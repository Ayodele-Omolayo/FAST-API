from fastapi import FastAPI

# Test comment
app = FastAPI()

# Dummy data
products_db = [
    {"id": 1, "name": "Laptop", "price": 999.99, "stock": 50, "category": "Electronics"},
    {"id": 2, "name": "Mouse", "price": 29.99, "stock": 100, "category": "Electronics"},
    {"id": 3, "name": "Keyboard", "price": 79.99, "stock": 75, "category": "Electronics"},
    {"id": 4, "name": "Monitor", "price": 299.99, "stock": 25, "category": "Electronics"},
    {"id": 5, "name": "Headphones", "price": 149.99, "stock": 60, "category": "Audio"}
]

categories = ["Electronics", "Audio", "Accessories"]

@app.get("/")
def health():
    return {"message": "Product Service Running"}

@app.get("/products")
def list_products():
    return {"products": products_db}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = next((p for p in products_db if p["id"] == product_id), None)
    return product if product else {"error": "Product not found"}

@app.get("/categories")
def get_categories():
    return {"categories": categories}

@app.get("/products/category/{category}")
def get_products_by_category(category: str):
    filtered = [p for p in products_db if p["category"].lower() == category.lower()]
    return {"products": filtered}

@app.post("/products")
def create_product(name: str, price: float, stock: int, category: str):
    return {"message": f"Product {name} created", "product_id": len(products_db) + 1}

@app.put("/products/{product_id}/stock")
def update_stock(product_id: int, stock: int):
    return {"message": f"Product {product_id} stock updated to {stock}"}
