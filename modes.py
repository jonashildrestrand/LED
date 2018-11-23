from abc import ABC, abstractmethod
from threading import Thread
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

    def __init__(self, matrix):
        self.matrix = matrix;
        super().__init__()

    def start(self):
        self.thread = Thread(target=self.update)
        self.thread.start()

    def terminate(self):
        self.loop = False

    def update(self):
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
                #print(data);
                print(audioop.max(data,2))
                if(vol > 60 and prev > 50):
                    row = random.randint(0,1);
                    col = random.randint(0,8);
                    r = random.randint(200,255);
                    g = random.randint(0,50);
                    b = random.randint(0,50);
                    Thread(target = self.matrix[row][col].setColor, args = (r,g,b)).start();

                if(vol < 60 and prev > 60):
                    self.fill(0,0,0);

                prev = vol;


            time.sleep(.01)


    def __del__(self):
        print("destruct music")
