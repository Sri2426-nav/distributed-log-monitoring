import sqlite3
import time

def fetch_errors():
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT timestamp, service, message FROM logs WHERE level = 'ERROR' ORDER BY timestamp DESC LIMIT 5")
    errors = cursor.fetchall()
    
    if errors:
        print("\n🚨 Recent ERROR Logs:")
        for err in errors:
            print(f"[{err[0]}] {err[1]}: {err[2]}")
    else:
        print("\n✅ No recent errors.")
    
    conn.close()

if __name__ == "__main__":
    while True:
        fetch_errors()
        time.sleep(5)  # Check every 5 seconds
