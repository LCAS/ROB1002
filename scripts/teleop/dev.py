from flask import Flask, render_template, send_from_directory, redirect
from flask_sock import Sock
import socket 

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
    cmd = sock.receive().split(':')

    if cmd[0] == "stop":
        print("🛑 Trilobot Stopped")
    
    elif cmd[0] == "left":
        print("curve_forward_left" + str(speed))

    elif cmd[0] == "right":
        print("curve_forward_right" + str(speed))

    elif cmd[0] == "up":
        print("forward" + str(speed))

    elif cmd[0] == "down":
        print("backward" + str(speed))

    elif cmd[0] == "speed":
        speed = float(cmd[1])
        msg = "speed:" + str(speed)
        print("🏎️  " + msg)
        sock.send(msg)

    else: 
        print("send either `up` `down` `left` `right` or `stop` to move your robot!")

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return redirect('https://placehold.co/640x480/EEE/31343C')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port =5000, debug=False, threaded=False)
    print("Trilobot stopped.")
