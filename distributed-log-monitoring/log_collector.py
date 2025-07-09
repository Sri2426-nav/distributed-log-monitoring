from flask import Flask, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Create database table (only once)
def init_db():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    service TEXT,
                    level TEXT,
                    message TEXT,
                    timestamp TEXT
                )''')
    conn.commit()
    conn.close()

@app.route('/log', methods=['POST'])
def receive_log():
    data = request.get_json()
    service = data.get('service')
    level = data.get('level')
    message = data.get('message')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
    c.execute("INSERT INTO logs (service, level, message, timestamp) VALUES (?, ?, ?, ?)",
              (service, level, message, timestamp))
    conn.commit()
    conn.close()

    return {'status': 'Log received'}, 200

if __name__ == '__main__':
    init_db()
    app.run(port=5000)
