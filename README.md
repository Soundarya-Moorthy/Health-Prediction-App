# AI Health Prediction Application

## Overview

A Flask-based web application that manages patient records and predicts possible health conditions using Google Gemini AI based on blood test values.

## Features

- CRUD Operations
- SQLite Database
- SQLAlchemy ORM
- Google Gemini AI Integration
- Health Risk Prediction
- Search Patients
- Filter by Risk Level
- Responsive Bootstrap UI

## Technologies

- Python
- Flask
- HTML
- CSS
- Bootstrap
- SQLAlchemy
- SQLite
- Google Gemini API

## Installation

pip install -r requirements.txt

Create .env

GEMINI_API_KEY=your_api_key

Run

python app.py

## Screenshots

### 1. Home Page

Displays the dashboard with all patient records, search functionality, risk filter, and CRUD actions.

> **Screenshot:** `screenshots/1. Home Page.png`

---

### 2. Add Patient Page

Patient registration form with mandatory field validation for Name, Date of Birth, Email, Glucose, Haemoglobin, and Cholesterol.

> **Screenshot:** `screenshots/2. Add Page.png`

---

### 3. Adding Patient Details

Demonstrates entering valid patient information before submission.

> **Screenshot:** `screenshots/3. Adding Details.png`

---

### 4. Patient Added Successfully

Shows the newly created patient record along with the AI-generated health prediction, risk level, and recommendation.

> **Screenshot:** `screenshots/4. Added Successfully.png`

---

### 5. Filter Based on Risk

Illustrates selecting a risk category (Low, Medium, or High) using the filter.

> **Screenshot:** `screenshots/5. Filter Based on Risk.png`

---

### 6. Filter Results

Displays only the patients matching the selected risk level.

> **Screenshot:** `screenshots/6. Filtering Result.png`

---

### 7. Search by Patient Name

Demonstrates searching for a patient using the search bar.

> **Screenshot:** `screenshots/7. Search based on Name.png`

---

### 8. Search Results

Shows the filtered patient records matching the search query.

> **Screenshot:** `screenshots/8. Search Results.png`

---

### 9. Edit Patient Details

Displays the edit form for updating patient information and regenerating the AI prediction.

> **Screenshot:** `screenshots/9. Edit Page.png`

---

### 10. Delete Confirmation

Shows the Bootstrap confirmation dialog before deleting a patient record.

> **Screenshot:** `screenshots/10. Delete Confirmation.png`
