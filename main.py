from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

connection = psycopg2.connect(
    dbname="microservices",
    user="postgres",
    password="Admin*2023",
    host="192.168.1.121",
    port="5432"
)


@app.route('/doctors', methods=['GET'])
def get_doctors():
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    return jsonify(doctors)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
