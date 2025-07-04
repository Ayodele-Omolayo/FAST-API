from fastapi import FastAPI

# FastAPI application instance
app = FastAPI()

# Dummy data
notifications_db = [
    {"id": 1, "user_id": 1, "type": "email", "subject": "Order Confirmed", "message": "Your order has been confirmed", "status": "sent", "created_at": "2024-01-15T10:40:00"},
    {"id": 2, "user_id": 2, "type": "sms", "subject": "Payment Failed", "message": "Payment processing failed", "status": "pending", "created_at": "2024-01-16T14:30:00"},
    {"id": 3, "user_id": 1, "type": "push", "subject": "Order Shipped", "message": "Your order is on the way", "status": "delivered", "created_at": "2024-01-17T09:25:00"},
    {"id": 4, "user_id": 3, "type": "email", "subject": "Welcome!", "message": "Welcome to our platform", "status": "sent", "created_at": "2024-01-18T08:15:00"},
    {"id": 5, "user_id": 2, "type": "push", "subject": "Payment Successful", "message": "Your payment was processed successfully", "status": "delivered", "created_at": "2024-01-19T12:00:00"},
    {"id": 6, "user_id": 1, "type": "sms", "subject": "Delivery Update", "message": "Your package will arrive today", "status": "failed", "created_at": "2024-01-20T15:30:00"}
]

notification_types = ["email", "sms", "push"]
notification_statuses = ["pending", "sent", "delivered", "failed"]

@app.get("/")
def health():
    return {"message": "Notification Service Running"}

@app.get("/notifications")
def get_notifications():
    return {"notifications": notifications_db}

@app.get("/notifications/user/{user_id}")
def get_user_notifications(user_id: int):
    user_notifications = [n for n in notifications_db if n["user_id"] == user_id]
    return {"notifications": user_notifications}

@app.post("/notifications/email")
def send_email(user_id: int, subject: str, message: str):
    notification_id = len(notifications_db) + 1
    return {"message": "Email sent", "notification_id": notification_id}

@app.post("/notifications/sms")
def send_sms(user_id: int, message: str):
    notification_id = len(notifications_db) + 1
    return {"message": "SMS sent", "notification_id": notification_id}

@app.post("/notifications/push")
def send_push(user_id: int, title: str, message: str):
    notification_id = len(notifications_db) + 1
    return {"message": "Push notification sent", "notification_id": notification_id}

@app.get("/notifications/{notification_id}")
def get_notification(notification_id: int):
    notification = next((n for n in notifications_db if n["id"] == notification_id), None)
    return notification if notification else {"error": "Notification not found"}