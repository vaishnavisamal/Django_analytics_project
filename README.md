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


### 📊 Analytics Dashboard
![Analytics Dashboard](https://raw.githubusercontent.com/vaishnavisamal/Django_analytics_project/main/dashboard_page.png)
### 🗺️ Leaflet Map (India Boundary)
![image alt](https://github.com/vaishnavisamal/Django_analytics_project/blob/main/admin%20logi%20page.png)
### 🔌 API Response
![image alt](https://github.com/vaishnavisamal/Django_analytics_project/blob/main/admin%20page.png)



