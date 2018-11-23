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
    if board.getMode() is not None:
        return board.getMode().config, 200
    else:
        return {}, 404

@app.route("/set/mode", methods=['POST'])
def toggleMusic():
    mode = request.form.get('mode')
    if mode in modes:
        board.setMode(modes[mode])
        return {}, 200
    return {}, 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
