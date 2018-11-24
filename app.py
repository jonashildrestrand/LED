from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
import matrix
from modes import Mode, Music
from flask_cors import CORS

app = FlaskAPI(__name__);
CORS(app)

board = matrix.Board(9,4);

state = {
    "current": 0,
    "modes": [
        None,
        Music(board)
    ]
}

def stateToJson():
    json = {
        'current': state['current'],
        'modes': []
    }

    for mode in state['modes']:
        if(mode is None):
            json['modes'].append(None)
        elif(isinstance(mode, Mode)):
            json['modes'].append(mode.config)
    return json

@app.route("/get/modes", methods=['GET'])
def getModes():
    return stateToJson(), 200

@app.route("/get/mode", methods=['GET'])
def getMode():
    if board.getMode() is not None:
        return board.getMode(), 200
    else:
        return {}, 404

@app.route("/set/mode", methods=['POST'])
def toggleMusic():
    print(request.data.get('mode'))
    mode = request.data.get('mode')

    try:
        state['current'] = mode
        board.setMode(state['modes'][mode])
        return stateToJson(), 200
    except KeyError:
        return {}, 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
