# Productivity Analytics Dashboard

## Overview

Productivity Analytics Dashboard is a desktop analytics application that monitors active application usage, stores activity sessions in SQLite, performs usage analytics using Pandas, and visualizes productivity metrics through a Flask-based interactive dashboard.

## Features

- Tracks active desktop applications in real time
- Records application sessions with start time, end time, and duration
- Automatically categorizes applications into predefined categories
- Displays a live analytics dashboard with automatic refresh
- Provides daily, weekly, and monthly usage statistics
- Visualizes hourly and weekday activity patterns
- Displays top application usage
- Generates category-wise screen time analytics
- Exposes analytics through REST APIs
- Stores activity history using SQLite

---

## Technology Stack

### Backend

- Python
- Flask
- SQLite
- Pandas

### Frontend

- HTML
- CSS
- JavaScript
- Chart.js

---

## Project Structure

```text
tracker/
│
├── analytics/
│   └── statistics.py
│
├── database/
│   ├── database.py
│   ├── repository.py
│   └── activity.db
│
├── tracker/
│   ├── tracker.py
│   ├── window_detector.py
│   ├── categorizer.py
│   └── application_categories.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── dashboard.js
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Dashboard

The dashboard provides the following analytics:

- Today's screen time
- Total screen time
- Total sessions
- Application switches
- Longest session
- Top applications
- Daily activity chart
- Hourly activity chart
- Weekday activity chart
- Category-wise usage chart

The dashboard automatically refreshes to display the latest activity statistics.

---

## REST API

| Endpoint | Description |
|----------|-------------|
| `/api/dashboard` | Dashboard summary statistics |
| `/api/top-applications` | Top application usage |
| `/api/daily` | Daily screen time |
| `/api/hourly` | Hourly activity |
| `/api/weekday` | Weekday activity |
| `/api/categories` | Category-wise usage |
| `/api/category-percentage` | Category percentage breakdown |

---

## Installation

Clone the repository

```bash
git clone https://github.com/hima-12376/productivity-analytics-dashboard.git
```

Navigate to the project directory

```bash
cd productivity-analytics-dashboard
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Start the activity tracker

```bash
python main.py
```

Open another terminal and start the dashboard

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## Screenshots

Include screenshots of:

- Dashboard overview
- Analytics charts
- Category breakdown
- Top applications

---

## Future Improvements

- AI-generated productivity insights
- Export reports (PDF/CSV)
- System tray integration
- Auto-start with Windows
- User-defined application categories
- Productivity scoring

---

## Author

Hima Paul

GitHub: https://github.com/hima-12376
