# Smart Expense Analyzer

A full-stack expense management and analytics web application built with Python, Flask, SQLite, Pandas, HTML, CSS, JavaScript, and Chart.js.

## Features

- Add expenses through a web dashboard
- View all recorded expenses
- Delete expenses
- Store expenses persistently using SQLite
- Import expenses from CSV using Pandas
- Analyze total spending
- Analyze spending by category
- Analyze monthly spending
- Interactive spending charts
- Data-driven spending insights
- Responsive and modern dashboard UI

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite
- **Data Processing:** Pandas
- **Frontend:** HTML, CSS, JavaScript
- **Visualization:** Chart.js
- **API:** REST APIs
- **Version Control:** Git & GitHub

## Project Structure

```text
Smart-Expense-Analyzer/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   └── templates/
│       └── index.html
│
├── data/
│   └── expenses.csv
│
├── requirements.txt
├── .gitignore
└── README.md
```

## API Endpoints

| Method | Endpoint               | Purpose                  |
| ------ | ---------------------- | ------------------------ |
| GET    | `/api/expenses`        | Get all expenses         |
| POST   | `/api/expenses`        | Add an expense           |
| DELETE | `/api/expenses/<id>`   | Delete an expense        |
| POST   | `/api/expenses/import` | Import expenses from CSV |
| GET    | `/api/analytics`       | Get spending analytics   |

## How to Run

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Smart-Expense-Analyzer
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python backend\app.py
```

Open:

```text
http://127.0.0.1:5000
```

The SQLite database is created automatically when the application starts.

## CSV Format

The CSV file should contain:

```text
title,amount,category,expense_date
Lunch,150,Food,2026-10-01
Uber,220,Travel,2026-10-02
Movie,300,Entertainment,2026-10-03
Groceries,850,Food,2026-10-04
Book,450,Education,2026-10-05
```

## What I Learned

This project helped me work with:

- Flask REST API development
- SQLite database operations
- CRUD operations
- Pandas CSV processing
- SQL aggregation and analytics
- Frontend-backend integration
- JavaScript `fetch()` API calls
- Chart.js data visualization
- Git and GitHub workflow
- Building and testing a complete end-to-end application

## Future Improvements

- User authentication
- Budget tracking
- Expense filtering by date
- Export analytics reports
- More advanced spending predictions
- Personalized financial insights

## Author

**Priyanshu Singh**

B.Tech CSE — Artificial Intelligence & Machine Learning
