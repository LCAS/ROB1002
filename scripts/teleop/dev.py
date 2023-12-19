from flask import Flask, render_template, send_from_directory, Response, redirect
from flask_sock import Sock
import socket 
import numpy as np

app = Flask(__name__)
sock = Sock(app)

import time

@app.route('/')
def index():
    hostname = (socket.gethostname().split(".")[0]).upper()
    return render_template('index.html', hostname=hostname)

@app.route("/manifest.json")
def manifest():
    return send_from_directory('./static', 'manifest.json')

@app.route("/app.js")
def script():
    return send_from_directory('./static', 'app.js')

@sock.route('/command')
def command(sock):
    
    speed = 0.5
    
    while True:
        cmd = sock.receive().split(':')

        if cmd[0] == "left":
            print("curve_forward_left" + speed)

        elif cmd[0] == "right":
            print("curve_forward_right" + speed)

        elif cmd[0] == "up":
            print("forward" + speed)

        elif cmd[0] == "down":
            print("backward" + speed)

        elif cmd[0] == "stop":
            print("stop")

        elif cmd[0] == "speed":
            speed = float(cmd[1])

        else: 
            print("send either `up` `down` `left` `right` or `stop` to move your robot!")

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return redirect('https://placehold.co/600x400/EEE/31343C')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port =5000, debug=False, threaded=True)
    print("Trilobot stopped.")