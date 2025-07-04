from fastapi import FastAPI

# Test comment
app = FastAPI()

# Dummy data
inventory_db = [
    {"product_id": 1, "warehouse_id": 1, "quantity": 50, "reserved": 5, "location": "A1-B2"},
    {"product_id": 2, "warehouse_id": 1, "quantity": 100, "reserved": 10, "location": "A2-B1"},
    {"product_id": 3, "warehouse_id": 2, "quantity": 75, "reserved": 0, "location": "B1-C3"},
    {"product_id": 4, "warehouse_id": 1, "quantity": 25, "reserved": 2, "location": "C1-D1"},
    {"product_id": 5, "warehouse_id": 2, "quantity": 60, "reserved": 8, "location": "D2-E1"}
]

warehouses = [
    {"id": 1, "name": "Main Warehouse", "location": "New York"},
    {"id": 2, "name": "West Coast Hub", "location": "California"}
]

@app.get("/")
def health():
    return {"message": "Inventory Service Running"}

@app.get("/inventory")
def get_inventory():
    return {"inventory": inventory_db}

@app.get("/inventory/product/{product_id}")
def get_product_inventory(product_id: int):
    product_inventory = [i for i in inventory_db if i["product_id"] == product_id]
    return {"inventory": product_inventory}

@app.get("/inventory/warehouse/{warehouse_id}")
def get_warehouse_inventory(warehouse_id: int):
    warehouse_inventory = [i for i in inventory_db if i["warehouse_id"] == warehouse_id]
    return {"inventory": warehouse_inventory}

@app.post("/inventory/reserve")
def reserve_inventory(product_id: int, quantity: int):
    return {"message": f"Reserved {quantity} units of product {product_id}"}

@app.post("/inventory/release")
def release_inventory(product_id: int, quantity: int):
    return {"message": f"Released {quantity} units of product {product_id}"}

@app.put("/inventory/restock")
def restock_inventory(product_id: int, warehouse_id: int, quantity: int):
    return {"message": f"Restocked {quantity} units of product {product_id} in warehouse {warehouse_id}"}

@app.get("/warehouses")
def get_warehouses():
    return {"warehouses": warehouses}