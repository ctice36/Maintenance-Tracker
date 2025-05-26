# Maintenance-Tracker
Maintenance Tracker System (Python CLI + Pandas)
# 🛠️ Maintenance Tracker System (Python CLI + Pandas)

A command-line application for tracking industrial machine maintenance using Python and pandas. Designed for small factories or workshops to keep machine records updated, ensure timely maintenance, and prevent costly downtime.

---

## 📦 Features

- ✅ Add new machines with auto-generated maintenance schedules
- 📝 Update machine maintenance status and reschedule next maintenance
- ❌ Remove outdated or retired machines
- 📋 View complete machine records with status
- ⏱️ View upcoming maintenance due within 10 days
- 💾 JSON-based persistent storage
- 🐼 Uses pandas for clean tabular data handling

---

## 📁 Project Structure
maintenance_tracker/
├── main.py # CLI entry point
├── machine.py # MachineOperation class
├── data/
│ └── Machine List.json # Saved machine records
├── README.md # This file
└── requirements.txt # Python package dependencies
---

## 💻 Requirements

- Python 3.8+
- pandas

Install with:

```bash
pip install pandas
```

🚀 How to Run
From your terminal:
python main.py

🧪 Sample Output
-----------------------------
Available operation
-----------------------------
1. Add new machine
2. Update machine upcoming maintenance date
3. Remove machine
4. View machine details
5. View upcoming maintenance date
6. Exit
-----------------------------
Select the number for the operation:


🧠 Concepts Demonstrated
- Object-Oriented Programming (Python classes)
- File handling with JSON
- Date arithmetic with datetime
- CLI interaction with error handling
- Data filtering and formatting using pandas

📌 Notes
- Machine IDs are formatted with a prefix like MS001, MS002, etc. (can be change to alphanumerical format)
- All dates follow YYYY-MM-DD format
- "Day Remaining" is dynamically calculated — never saved

📚 Future Improvements
- Export reports to Excel or CSV
- Add alert notifications for overdue maintenance
- Web-based dashboard using Flask or Streamlit
