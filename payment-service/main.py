from fastapi import FastAPI

app = FastAPI()

# Dummy data
payments_db = [
    {"id": 1, "order_id": 1, "amount": 1999.98, "method": "credit_card", "status": "completed", "transaction_id": "txn_123456", "created_at": "2024-01-15T10:35:00"},
    {"id": 2, "order_id": 2, "amount": 29.99, "method": "paypal", "status": "pending", "transaction_id": "txn_789012", "created_at": "2024-01-16T14:25:00"},
    {"id": 3, "order_id": 3, "amount": 79.99, "method": "debit_card", "status": "failed", "transaction_id": "txn_345678", "created_at": "2024-01-17T09:20:00"},
    {"id": 4, "order_id": 4, "amount": 299.99, "method": "stripe", "status": "completed", "transaction_id": "txn_901234", "created_at": "2024-01-18T16:10:00"},
    {"id": 5, "order_id": 5, "amount": 149.99, "method": "bank_transfer", "status": "processing", "transaction_id": "txn_567890", "created_at": "2024-01-19T11:45:00"}
]

payment_methods = ["credit_card", "debit_card", "paypal", "stripe", "bank_transfer"]
statuses = ["pending", "processing", "completed", "failed", "refunded"]

@app.get("/")
def health():
    return {"message": "Payment Service Running"}

@app.get("/payments")
def get_payments():
    return {"payments": payments_db}

@app.get("/payments/{payment_id}")
def get_payment(payment_id: int):
    payment = next((p for p in payments_db if p["id"] == payment_id), None)
    return payment if payment else {"error": "Payment not found"}

@app.post("/payments")
def process_payment(order_id: int, amount: float, method: str):
    payment_id = len(payments_db) + 1
    return {"message": "Payment processed", "payment_id": payment_id, "status": "pending", "transaction_id": f"txn_{payment_id}23456"}

@app.get("/payments/order/{order_id}")
def get_payment_by_order(order_id: int):
    payment = next((p for p in payments_db if p["order_id"] == order_id), None)
    return payment if payment else {"error": "Payment not found"}

@app.put("/payments/{payment_id}/refund")
def refund_payment(payment_id: int):
    return {"message": f"Payment {payment_id} refunded"}