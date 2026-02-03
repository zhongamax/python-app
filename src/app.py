from flask import Flask, jsonify
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'time': datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname()
    })

@app.route('/api/v1/healthy')
def healthy():
    return jsonify({
        'status': 'up'
    }),200

if __name__ == '__main__':
    app.run(host="0.0.0.0")

http://amax.zhong:69549779@ssl-15ez6r-xxxx-0.catspac.com:3389