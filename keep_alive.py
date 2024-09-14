from flask import Flask
from threading import Thread, Event

app = Flask(__name__)
stop_event = Event()

@app.route('/')
def index():
    return "Alive"

def run():
    while not stop_event.is_set():
        app.run(host='0.0.0.0', port=8080, threaded=True, use_reloader=False)
        stop_event.wait(1)

def keep_alive():
    server_thread = Thread(target=run)
    server_thread.start()
    return server_thread

def stop_keep_alive(server_thread):
    stop_event.set()
    server_thread.join(timeout=1)  # Ensure the thread is joined after stopping
