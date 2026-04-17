import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = psycopg2.connect(
            host=os.getenv['DB_HOST'],
            database=os.getenv['DB_NAME'],
            user=os.getenv['DB_USER'],
            password=os.getenv['DB_PASS']
        )
        cur = conn.cursor()
        message = "Hello, World! + Postgres is connected via Docker Compose"
        cur.execute("SELECT %s", (message,))
        conn.close()
        return jsonify({"message": result[0]})

    except Exception as e:   # ✅ aligned with try
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)