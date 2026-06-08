# 🚀 FastAPI Product API

A hands-on FastAPI project built while learning how modern APIs can be used to serve data and eventually deploy Machine Learning models into production.

## 🎯 Why I Built This

As an aspiring Data Scientist / ML Engineer, I wanted to understand how trained models interact with applications in the real world.

FastAPI is widely used for:

* Model Serving
* AI Applications
* Backend APIs
* MLOps Workflows
* Microservices

This project helped me learn the foundations before moving toward ML model deployment.

---

## ✨ Features

✅ Product Listing API

✅ Product Search

✅ Product Filtering

✅ Pagination

✅ Sorting

✅ UUID-Based Product Retrieval

✅ Request Validation with Pydantic

✅ Custom Validators

✅ Error Handling

✅ Interactive Swagger Documentation

---

## 🛠️ Tech Stack

| Technology | Purpose           |
| ---------- | ----------------- |
| Python     | Core Programming  |
| FastAPI    | API Framework     |
| Pydantic   | Data Validation   |
| JSON       | Data Storage      |
| Swagger UI | API Documentation |

---

## 📂 Project Structure

```bash
app/
│
├── service/
│   └── products.py
│
├── schema/
│   └── product.py
│
├── data/
│   └── products.json
│
└── main.py
```

---

## 🔗 API Endpoints

### Get All Products

```http
GET /products
```

### Get Product By UUID

```http
GET /products/{product_uuid}
```

### Create Product

```http
POST /products
```

---

## 🔍 Query Parameters

| Parameter     | Description     |
| ------------- | --------------- |
| name          | Search products |
| limit         | Limit results   |
| offset        | Pagination      |
| sort_by_price | Sort products   |
| order         | asc / desc      |

---

## 📸 Preview

### Swagger Documentation



---

### Product API Response



---

### Project Structure



---

## 🧠 Key Learnings

Through this project I learned:

* Building APIs using FastAPI
* Working with Path Parameters
* Using Query Parameters
* Pagination & Sorting
* Data Validation with Pydantic
* Custom Field Validators
* Exception Handling
* API Documentation

---

## 🚀 Future Improvements

* Database Integration (PostgreSQL)
* SQLAlchemy ORM
* JWT Authentication
* Docker Support
* Machine Learning Model Deployment
* CI/CD Pipeline

---

## 🤝 Connect With Me

I'm currently learning:

📊 Data Science

🤖 Machine Learning

⚙️ FastAPI

🚀 MLOps

If you're on a similar journey, feel free to connect and share your insights.

---

⭐ If you found this project interesting, consider giving it a star.
