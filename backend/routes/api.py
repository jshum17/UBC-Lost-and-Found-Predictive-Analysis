from flask import Blueprint, jsonify
from db.database import get_db_connection

api = Blueprint("api", __name__)


@api.route('/lost_items', methods=['GET'])
def get_lost_items():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM lost_items;")
        lost_items = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(lost_items)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@api.route("/summary", methods=["GET"])
def get_summary():
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)

            cursor.execute("SELECT item_type, COUNT(*) as count FROM lost_items GROUP BY item_type")
            data = cursor.fetchall()

            cursor.close()
            conn.close()
            return jsonify(data)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
