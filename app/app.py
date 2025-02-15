from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "lost_and_found_db"
}

def fetch_lost_items():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM lost_items")
        lost_items = cursor.fetchall()
        cursor.close()
        conn.close()
        return lost_items
    except Exception as e:
        return str(e)

@app.route('/api/lost-items', methods=['GET'])
def get_lost_items():
    items = fetch_lost_items()
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
