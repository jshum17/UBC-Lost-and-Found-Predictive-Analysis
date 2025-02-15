import pandas as pd
import mysql.connector
import requests
from io import StringIO

CSV_URL = "https://lostandfound.ubc.ca/all-items/export.csv"

# MySQL Connection
DB_CONFIG = {
    "host": "localhost",
    "user": "root",  # MySQL username
    "password": "password",  # MySQL password
    "database": "lost_and_found_db"
}

def fetch_and_store_data():
    try:
        response = requests.get(CSV_URL)
        response.raise_for_status() 

        csv_data = StringIO(response.text)
        df = pd.read_csv(csv_data)

        df = df.fillna("")
        df["Date"] = pd.to_datetime(df["Date"])

        print("DataFrame Columns:", df.columns)
        print("DataFrame Sample Data:\n", df.head())

        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        for _, row in df.iterrows():
            sql = """
            INSERT INTO lost_items (id, item_type, status, description, date_lost, location)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE 
                id = VALUES(id),
                item_type = VALUES(item_type),
                status = VALUES(status),
                description = VALUES(description),
                date_lost = VALUES(date_lost),
                location = VALUES(location);
            """
            values = (
                row["Ticket Number"], 
                row["Item Type"], 
                row.get("Status", "Lost"), 
                row["Item Description"], 
                row["Date"], 
                row["Lost Item Location"]
            )
            cursor.execute(sql, values)
            
        conn.commit()
        cursor.close()
        conn.close()

        print("Data successfully stored in MySQL.")

    except Exception as e:
        print("Error fetching or storing data:", str(e))

if __name__ == "__main__":
    fetch_and_store_data()
