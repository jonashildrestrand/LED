from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import matrix
from modes import Music
from flask_cors import CORS

app = FlaskAPI(__name__);
CORS(app)

board = matrix.Board(9,2);
modes = {
    "visualiser": Music(board),
    "none": None
}

@app.route("/get/mode", methods=['GET'])
def getMode():
    if(board.getMode()):
        return board.getMode(), 200
    return {}, 404

@app.route("/set/mode/", methods=['POST'])
def toggleMusic():
    board.setMode(modes[request.args.mode])
    return "Set mode: 2"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
