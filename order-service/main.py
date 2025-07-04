from fastapi import FastAPI
from datetime import datetime

# FastAPI application instance
app = FastAPI()

# Dummy data
orders_db = [
    {"id": 1, "user_id": 1, "product_id": 1, "quantity": 2, "total": 1999.98, "status": "completed", "created_at": "2024-01-15T10:30:00"},
    {"id": 2, "user_id": 2, "product_id": 2, "quantity": 1, "total": 29.99, "status": "pending", "created_at": "2024-01-16T14:20:00"},
    {"id": 3, "user_id": 1, "product_id": 3, "quantity": 1, "total": 79.99, "status": "shipped", "created_at": "2024-01-17T09:15:00"}
]

order_statuses = ["pending", "confirmed", "shipped", "delivered", "cancelled"]

@app.get("/")
def health():
    return {"message": "Order Service Running"}

@app.get("/orders")
def get_orders():
    return {"orders": orders_db}

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    order = next((o for o in orders_db if o["id"] == order_id), None)
    return order if order else {"error": "Order not found"}

@app.get("/orders/user/{user_id}")
def get_user_orders(user_id: int):
    user_orders = [o for o in orders_db if o["user_id"] == user_id]
    return {"orders": user_orders}

@app.post("/order")
def place_order(product_id: int, quantity: int, user_id: int):
    order_id = len(orders_db) + 1
    return {"message": f"Order placed for product {product_id} with quantity {quantity}", "order_id": order_id, "status": "pending"}

@app.put("/orders/{order_id}/status")
def update_order_status(order_id: int, status: str):
    return {"message": f"Order {order_id} status updated to {status}"}

@app.get("/orders/status/{status}")
def get_orders_by_status(status: str):
    filtered = [o for o in orders_db if o["status"] == status]
    return {"orders": filtered}

@app.delete("/orders/{order_id}")
def cancel_order(order_id: int):
    return {"message": f"Order {order_id} cancelled"}
