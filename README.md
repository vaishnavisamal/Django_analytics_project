# 📊 Django Analytics + 🌍 Leaflet Map Project

A simple **Analytics Tracking System** built with **Django + Django REST Framework**, along with a **Leaflet map** that displays **India’s boundary using GeoJSON**.

This project demonstrates backend analytics aggregation and frontend map integration — perfect for interviews 💼✨

---
## 🧩 Project Overview

### 🔧 Backend (Django + DRF)
- Track basic user events (logins, button clicks)
- Aggregate analytics using Django ORM
- Secure APIs with authentication

### 🗺️ Frontend (Leaflet)
- Interactive map centered on **India**
- India boundary loaded using a public GeoJSON file
- Simple dashboard displaying analytics data from backend APIs

---
## 🏗️ Features

### ✅ Backend Features
- User event tracking
- Analytics summary APIs
- Button click aggregation
- Authentication & validation
- Clean REST API responses

### ✅ Frontend Features
- Leaflet map integration
- India boundary visualization
- Analytics dashboard UI

---
## 📂 Project Structure


---

## 🧠 Database Models

### 👤 UserProfile
- `user` (OneToOne with Django User)
- `city`
- `state`

### 📌 EventLog
- `user` (ForeignKey)
- `event_type` → (`login`, `button_click`)
- `button_name` (nullable)
- `timestamp` (auto-generated)

---

## 🔌 API Endpoints

### 📥 Log Event
**POST** `/api/events/`
```json
{
  "event_type": "button_click",
  "button_name": "Subscribe"
}

**screenshots 📸**
<img width="1918" height="847" alt="image" src="https://github.com/user-attachments/assets/bacc5928-8598-46b6-9218-27d91c9575da" />
<img width="1902" height="856" alt="image" src="https://github.com/user-attachments/assets/3dffe881-1820-40bb-9ffc-70e8c6481d36" />
<img width="1815" height="728" alt="image" src="https://github.com/user-attachments/assets/b806f260-d145-4211-9058-6b20ed00798e" />



