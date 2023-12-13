from flask import Flask, render_template, send_from_directory
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/manifest.json")
def manifest():
    return send_from_directory('./static', 'manifest.json')

@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        sock.send(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port =5000, debug=True, threaded=True)