import sqlite3
import time

def fetch_critical_errors():
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT timestamp, service, message
        FROM logs
        WHERE level = 'ERROR'
        ORDER BY timestamp DESC
        LIMIT 1
    """)
    
    result = cursor.fetchone()
    conn.close()
    return result

last_alert = None

while True:
    error = fetch_critical_errors()
    
    if error and error != last_alert:
        print(f"\n🔔 ALERT: ERROR Detected!\nTime: {error[0]}\nService: {error[1]}\nMessage: {error[2]}\n")
        last_alert = error
    
    time.sleep(10)
