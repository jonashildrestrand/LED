import led
import board
import neopixel
import time
from threading import Thread
from modes import Mode

class Board:
    mode = None

    def __init__(self,x,y):
        self.pixel_pin = board.D18
        self.num_pixels = (x * y)
        self.ORDER = neopixel.GRB
        self.pixels = neopixel.NeoPixel(self.pixel_pin, self.num_pixels, brightness=0.5, auto_write=False, pixel_order=self.ORDER) 
        self.matrix = self.initMatrix(x,y);
        self.x = x;
        self.y = y;
    
    def initMatrix(self, x, y):
        matrix = [];
        for i in range(0, y):
            row = [];
            reverse = ((i % 2) == 1);
            for j in range(0, x):
                pixel = None;
                if(reverse):
                    pixel = ((i+1)*x) - (j+1);
                else:
                    pixel = (i+1) * j;
                row.append(led.Pixel(self.pixels, pixel));
            matrix.append(row);
        return matrix;

    def setMode(self, mode):
        if(isinstance(self.mode, Mode)):
            self.mode.terminate()
        if(isinstance(mode, Mode)):
            self.mode = mode
            self.mode.start()
        self.mode = None

    def getMode(self):
        if(isinstance(mode, Mode)):
            return self.mode.config