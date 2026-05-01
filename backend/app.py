from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# Veritabanı bağlantı bilgilerin
db_config = {
    'host': 'db',
    'user': 'burak',
    'password': '516191011be',
    'database': 'burak'
}

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        
        # Gelen verilerin kontrolü
        if not data or 'name' not in data or 'email' not in data or 'message' not in data:
            return jsonify({"error": "Eksik veri gönderildi"}), 400

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Veritabanına kayıt
        cursor.execute(
            'INSERT INTO messages (name, email, message) VALUES (%s, %s, %s)',
            (data['name'], data['email'], data['message'])
        )
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({"status": "success", "message": "Mesaj başarıyla kaydedildi"}), 200
    
    except Exception as e:
        print(f"Hata: {str(e)}") # Loglarda hatayı görmek için
        return jsonify({"error": str(e)}), 500

@app.route('/get-messages', methods=['GET'])
def get_messages():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM messages ORDER BY id DESC')
        messages = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(messages), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Docker konteynırında çalışması için 0.0.0.0 şart
    app.run(host='0.0.0.0', port=5000)
