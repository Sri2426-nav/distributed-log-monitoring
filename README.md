# 📊 Distributed Log Monitoring & Alerting System

This project is a **Distributed Log Monitoring & Alerting System** built using **Python** and **Flask**. It simulates microservices sending logs, stores them in a centralized database, and monitors for error-level logs in real-time.

---

## 🚀 Project Highlights

- Simulates multiple microservices generating logs (`INFO`, `WARNING`, `ERROR`)
- Centralized **Flask API** to collect logs
- Stores logs in a **SQLite database**
- Real-time **log analyzer** that filters recent `ERROR` logs
- Automatic **alert generation** for critical issues
- Completely beginner-friendly, ideal for SDE intern/resume projects

---

## 🛠️ Technologies Used

- Python 3.10
- Flask (for REST API)
- SQLite (for log storage)
- Command Line / PowerShell (for alerts)

---

## 📂 Project Structure
distributed-log-monitoring/
├── service1.py          # Simulates log generation
├── log_collector.py     # Flask API for collecting logs
├── log_analyzer.py      # Reads logs and displays recent ERROR logs
├── alert_manager.py     # Triggers alerts when ERROR logs are found
├── logs.db              # SQLite database to store logs
├── README.md            # Project documentation

## 📎 License
---

## ▶️ How to Run the Project

1. **Start the log collector server**  
   `python log_collector.py`

2. **Run the log generator service**  
   `python service1.py`

3. **(Optional)** Open another terminal and run the log analyzer:  
   `python log_analyzer.py`

4. **Run alert manager in a separate terminal**  
   `python alert_manager.py`

💡 Use `Ctrl + C` to stop any script.

---


This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
