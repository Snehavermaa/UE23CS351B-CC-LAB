# 🧱 Cloud Computing Lab – Monolithic Architecture (FastAPI)

This repository contains **Lab 2: Monolithic Architecture** for the **Cloud Computing** course.
The lab demonstrates how a **monolithic application** behaves under failure and load, and how **code-level optimizations** can improve performance — all implemented using **FastAPI** and **Locust**.

---

## 📌 Lab Objectives

* Understand **Monolithic Architecture** through a real-world analogy and implementation
* Observe how a **single bug can crash the entire system**
* Fix runtime failures in a monolithic app
* Perform **load testing** using Locust
* Optimize API routes and analyze **before vs after performance**
* Understand limitations of monoliths compared to microservices

---

## 🛠 Tech Stack

* **Backend Framework:** FastAPI
* **Database:** SQLite
* **Load Testing Tool:** Locust
* **Language:** Python
* **Architecture:** Monolithic

---

## 📂 Project Structure

```
CC_LAB2/
│
├── main.py
├── requirements.txt
├── fest.db
├── insert_events.py
│
├── checkout/
│   └── __init__.py
│
├── events/
│   └── __init__.py
│
├── my_events/
│   └── __init__.py
│
├── locust/
│   ├── checkout_locustfile.py
│   ├── events_locustfile.py
│   └── myevents_locustfile.py
│
└── PES1UG23AM309_LAB2.pdf
    ├── SS1.png
    ├── SS2.png
    ├── ...
    └── SS9.png
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd CC_LAB2
```

### 2️⃣ Create Virtual Environment

**Windows**

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Initialize Database

```bash
python insert_events.py
```

### 5️⃣ Run the Server

```bash
uvicorn main:app --reload
```

If `uvicorn` is not recognized:

```bash
python -m uvicorn main:app --reload
```

Server runs at:
👉 **[http://localhost:8000](http://localhost:8000)**

---

## 🌐 Application Endpoints

| Feature   | URL          |
| --------- | ------------ |
| Register  | `/register`  |
| Login     | `/login`     |
| Events    | `/events`    |
| My Events | `/my-events` |
| Checkout  | `/checkout`  |

> ⚠️ Events and Checkout pages are accessible **only after login**

---

## 💥 Observing Monolithic Failure

* Visiting `/checkout` initially crashes the entire server
* This demonstrates the **single point of failure** in monolithic architecture
* A single runtime error affects the whole application

📸 **Screenshot:** SS2

---

## 🛠 Bug Fix

* Commented out the faulty line in:

```
checkout/__init__.py
```

* Restarted server
* Checkout route works correctly

📸 **Screenshot:** SS3

---

## ⚙️ Load Testing with Locust

Start Locust UI:

```bash
locust -f locust/checkout_locustfile.py
```

Open:
👉 **[http://localhost:8089](http://localhost:8089)**

### Test Configuration

* Users: `1`
* Ramp-up: `1`
* Duration: `30 seconds`

📸 **Screenshot:** SS4 (Before Optimization)

---

## 🚀 Performance Optimization

### Checkout Route (`/checkout`)

* Removed inefficient loops
* Optimized calculation logic

📸 **Screenshots:**

* Before Optimization → SS4
* After Optimization → SS5

**Result:**

* Lower average response time
* Same throughput (RPS)

---

### Events Route (`/events`)

* Bottleneck: redundant loops and inefficient processing
* Optimization: simplified iteration and reduced computation

📸 **Screenshots:**

* Before → SS6
* After → SS7

---

### My Events Route (`/my-events`)

* Bottleneck: repeated filtering and aggregation
* Optimization: cleaner and direct data handling

📸 **Screenshots:**

* Before → SS8
* After → SS9

---

## 🧠 Key Learnings

* Monolithic apps are **easy to build** but **hard to scale**
* A single bug can bring down the **entire system**
* Performance can be improved with **code-level optimization**
* Architectural limitations still remain — motivating **microservices**

---

## 📦 Final Submission Includes

* ✅ Public GitHub Repository
* ✅ Screenshots SS1 – SS9
* ✅ Optimized Code
* ✅ Performance Comparison

---

## 👩‍💻 Author

**Sneha Verma**
Cloud Computing Lab – Monolithic Architecture
FastAPI | Load Testing | System Design
