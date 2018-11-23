from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import matrix
from modes import Music
from flask_cors import CORS

board = matrix.Board(9,2);
app = FlaskAPI(__name__);
CORS(app)

@app.route("/get/mode", methods=['GET'])
def getMode():
    return board.getMode()

@app.route("/set/mode/", methods=['POST'])
def toggleMusic():
    board.setMode(Music(board))
    return "Set mode: 2"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
