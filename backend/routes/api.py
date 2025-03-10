from flask import Blueprint, jsonify
import pandas as pd
import torch
from db.database import get_db_connection
from models.lstm import forecast_daily, load_model
import joblib

api = Blueprint("api", __name__)

# Load preprocessing objects and models
scaler = joblib.load('models/scaler.pkl')
day_encoder = joblib.load('models/day_encoder.pkl')
weekend_encoder = joblib.load('models/weekend_encoder.pkl')

input_size_daily = 9  # Count + 7 day encodings + 1 weekend
hidden_size = 100
num_layers = 1
output_size = 1

model_daily = load_model('models/lstm_daily_model.pth', input_size_daily, hidden_size, num_layers, output_size)

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

@api.route('/count<int:year>', methods=['GET'])
def get_counts_by_year(year):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT MONTH(date_lost) as month, COUNT(*) as count
            FROM lost_items
            WHERE date_lost >= %s AND date_lost <= %s
            GROUP BY MONTH(date_lost)
            ORDER BY MONTH(date_lost);
            """,
            (f"{year}-01-01", f"{year}-12-31")
        )
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

def get_daily_counts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT date_lost FROM lost_items;")
    lost_items = cursor.fetchall()
    cursor.close()
    conn.close()
    df = pd.DataFrame(lost_items)
    df['date_lost'] = pd.to_datetime(df['date_lost'])
    df.set_index('date_lost', inplace=True)
    daily_counts = df.resample('D').size().fillna(0).to_frame(name='Count')
    daily_counts = daily_counts.reset_index().rename(columns={'date_lost': 'Date'})
    return daily_counts

@api.route('/forecast/daily', methods=['GET'])
def get_daily_forecast():
    try:
        daily_counts = get_daily_counts()
        recent_data = daily_counts.set_index('Date').tail(7)
        if len(recent_data) < 7:
            return jsonify({"error": "Insufficient data for forecast (need at least 7 days)"}), 400
        forecast = forecast_daily(model_daily, recent_data, scaler, day_encoder, weekend_encoder, forecast_days=7)
        forecast_json = {
            'dates': forecast.index.strftime('%Y-%m-%d').tolist(),
            'counts': forecast.tolist()
        }
        return jsonify(forecast_json)
    except Exception as e:
        return jsonify({"error": str(e)}), 500