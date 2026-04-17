    from flask import Flask, jsonify
    import psycopg2
    import os

    app = Flask(__name__)

    @app.route('/')
    def home():
        try:
            conn = psycopg2.connect(
                host=os.getenv('POSTGRES_HOST', 'postgres'),  # 👈 key fix
                database=os.getenv('POSTGRES_DB', 'flask_db'),
                user=os.getenv('POSTGRES_USER', 'postgres'),
                password=os.getenv('POSTGRES_PASSWORD', 'postgres')
            )
            cur = conn.cursor()
            cur.execute('SELECT * FROM todos')
            todos = cur.fetchall()
            cur.close()
            conn.close()
            return jsonify(todos)
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5001, debug=True)