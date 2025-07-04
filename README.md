# Backend Services

FastAPI microservices for e-commerce platform.

## Services

| Service | Port | Description |
|---------|------|-------------|
| user-service | 8001 | User management and authentication |
| order-service | 8002 | Order processing and management |
| product-service | 8003 | Product catalog and inventory |
| payment-service | 8004 | Payment processing |
| notification-service | 8005 | Email, SMS, push notifications |
| inventory-service | 8006 | Stock and warehouse management |

## Run Commands

### Individual Services
```bash
# User Service
cd user-service && uvicorn main:app --reload --port 8001

# Order Service  
cd order-service && uvicorn main:app --reload --port 8002

# Product Service
cd product-service && uvicorn main:app --reload --port 8003

# Payment Service
cd payment-service && uvicorn main:app --reload --port 8004

# Notification Service
cd notification-service && uvicorn main:app --reload --port 8005

# Inventory Service
cd inventory-service && uvicorn main:app --reload --port 8006
```

### Run All Services (Parallel)
```bash
# Using background processes
cd user-service && uvicorn main:app --reload --port 8001 &
cd order-service && uvicorn main:app --reload --port 8002 &
cd product-service && uvicorn main:app --reload --port 8003 &
cd payment-service && uvicorn main:app --reload --port 8004 &
cd notification-service && uvicorn main:app --reload --port 8005 &
cd inventory-service && uvicorn main:app --reload --port 8006 &
```

## API Documentation
Each service provides interactive API docs at:
- `http://localhost:{port}/docs` (Swagger UI)
- `http://localhost:{port}/redoc` (ReDoc)

## Dependencies
```bash
pip install fastapi uvicorn
```