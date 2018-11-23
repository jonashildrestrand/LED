from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import matrix

board = matrix.Board(9,2);
app = FlaskAPI(__name__);

@app.route("/set-color/", methods=['POST'])
def setColor():
    r = int(request.data['r']);
    g = int(request.data['g']);
    b = int(request.data['b']);

    board.fill(r,g,b);

    return "Color changed";

@app.route("/set-pixel-color/", methods=['POST'])
def setPixelColor():
    row = int(request.data['row']);
    col = int(request.data['col']);
    r = int(request.data['r']);
    g = int(request.data['g']);
    b = int(request.data['b']);

    board.setPixelColor(row, col, r, g, b);

    return "Color changed";

@app.route("/toggle-random/", methods=['POST'])
def toggleRandom():
    board.randomPixelFlow();
    return "Done";

@app.route("/music/", methods=['POST'])
def toggleMusic():
    board.music();
    return "Done";

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
