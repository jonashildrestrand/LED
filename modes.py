from abc import ABC, abstractmethod
from threading import Thread
import alsaaudio, audioop
import random
import time

# Abstract class
class Mode(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def terminate(self):
        pass

    @abstractmethod
    def __del__(self):
        pass

# Music mode
class Music(Mode):
    loop = True
    thread = None
    config = {
        "name": "Visualiser",
        "sensitivity": 60,
        "rgb": {
            "min": {
                "r": 200,
                "g": 50,
                "b": 0
            },
            "max": {
                "r": 255,
                "g": 255,
                "b": 0
            }
        }
    }

    def __init__(self, board):
        self.board = board;
        print("music init")
        super().__init__()

    def start(self):
        print("start music mode")
        self.thread = Thread(target=self.update)
        self.thread.start()

    def setMatrix(self, matrix, pixels):
        print("set matrix")
        self.matrix = matrix
        self.pixels = pixels;

    def terminate(self):
        self.loop = False

    def update(self):
        print("starting music")
        inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
        inp.setchannels(1)
        inp.setrate(8000)
        inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        inp.setperiodsize(160)

        prev = 0;
        while self.loop:
            l,data = inp.read()
            if l:
                vol = audioop.max(data, 2);
                if(vol > self.config['sensitivity']):
                    row = random.randint(0,self.board.y-1);
                    col = random.randint(0,self.board.x-1);
                    r = random.randint(self.config['rgb']['min']['r'],self.config['rgb']['max']['r']);
                    g = random.randint(self.config['rgb']['min']['g'],self.config['rgb']['max']['g']);
                    b = random.randint(self.config['rgb']['min']['b'],self.config['rgb']['max']['b']);
                    Thread(target = self.board.matrix[row][col].setColor, args = (r,g,b)).start();

                if(vol < self.config['sensitivity']and prev > self.config['sensitivity']):
                    self.board.pixels.fill((0,0,0));
                    self.board.pixels.show()
                prev = vol;
            time.sleep(.01)

    def __del__(self):
        print("destruct music")
