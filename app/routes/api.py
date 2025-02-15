from flask import Blueprint, jsonify
from db.database import get_db_connection

api = Blueprint("api", __name__)

@api.route("/summary", methods=["GET"])
def get_summary():
    """Fetch lost item statistics."""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT item_type, COUNT(*) as count FROM lost_items GROUP BY item_type")
    data = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return jsonify(data)
