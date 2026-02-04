from flask import Flask, jsonify
import socket
import os
import platform
from datetime import datetime

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        # 1. 基础信息
        'message': "Good job, man!",
        'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        
        # 2. 网络诊断 (在 K8s 中非常有用)
        'hostname': socket.gethostname(),
        'pod_ip': socket.gethostbyname(socket.gethostname()),
        
        # 3. 运行环境
        'os': platform.system(),
        'python_version': platform.python_version(),
        
        # 4. 环境变量 (可以确认你的 ConfigMap 或 Secret 是否生效)
        'env_app_version': os.getenv('APP_VERSION', 'unknown')
    })

@app.route('/api/v1/healthy')
def healthy():
    return jsonify({
        'status': 'up'
    }),200

if __name__ == '__main__':
    app.run(host="0.0.0.0")
