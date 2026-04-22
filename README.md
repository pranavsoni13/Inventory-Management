# 📦 Inventory Management System (Full Stack)

A full-stack Inventory Management System built using **React (Frontend)** and **FastAPI (Backend)** with JWT-based authentication and a modern UI powered by Tailwind CSS.

---

## 🚀 Live Demo

* 🌐 Frontend: https://inventory-frontend-zeta-one.vercel.app
* ⚙️ Backend API: https://inventory-management-production-29a.up.railway.app/docs

---

## 🧠 Features

### 🔐 Authentication

* User Signup & Login
* JWT Token-based Authentication
* Protected Routes (Dashboard access only after login)

### 📦 Inventory Management

* Add Products
* View Products
* Delete Products
* Real-time updates

### 🎨 UI/UX

* Clean and responsive UI using Tailwind CSS
* Dashboard layout with components
* Simple and intuitive user flow

---

## 🛠️ Tech Stack

### Frontend

* React.js
* React Router
* Axios
* Tailwind CSS

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* JWT (python-jose)
* Passlib (bcrypt)

---

## 📁 Project Structure

```
Inventory-Management/
│
├── backend/
│   ├── auth/
│   ├── routes/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── inventory.db
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── api.js
│   │   ├── App.js
│   │   └── index.js
│   └── tailwind.config.js
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 Backend Setup

```bash
cd backend
python -m venv inven
inven\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

👉 Runs on: http://127.0.0.1:8000

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm start
```

👉 Runs on: http://localhost:3000

---

## 🔐 API Endpoints

### Auth

* `POST /auth/signup` → Register user
* `POST /auth/login` → Get access token

### Products (Protected)

* `GET /products/` → Get all products
* `POST /products/` → Add product
* `DELETE /products/{id}` → Delete product

---

## 🧪 Testing Flow

1. Signup a new user
2. Login → get token
3. Access dashboard
4. Add/Delete products
5. Verify protected routes

---

## 🚀 Deployment

* Frontend deployed on **Vercel**
* Backend deployed on **Railway**

⚠️ CORS configured to allow frontend domain

---

## 🧠 Key Learnings

* Full-stack architecture using React + FastAPI
* JWT Authentication & protected routes
* API integration with Axios
* Deployment & CORS handling
* Debugging real-world errors

---

## 📌 Future Improvements

* Edit/Update product feature
* Pagination & search
* User roles (Admin/User)
* Better UI (cards/table layout)
* Dark mode 🌙

---

## 👨‍💻 Author

**Pranav**
B.Tech AI & DS Student

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork & improve!

---
