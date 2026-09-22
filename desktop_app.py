import threading
import time
import webview

from app import app


def run_flask():
    app.run(
        host='127.0.0.1',
        port=8080,
        debug=False,
        use_reloader=False
    )


flask_thread = threading.Thread(target=run_flask, daemon=True)
flask_thread.start()

time.sleep(1)

webview.create_window(
    'Customer Churn Predictor',
    'http://127.0.0.1:8080/',
    width=1200,
    height=800
)

webview.start()