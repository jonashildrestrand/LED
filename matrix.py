import led
import board
import neopixel
import time
import random
from threading import Thread
import alsaaudio, audioop
from modes import Mode

class Board:
    def __init__(self,x,y):
        self.pixel_pin = board.D18
        self.num_pixels = (x * y)
        self.ORDER = neopixel.GRB
        self.pixels = neopixel.NeoPixel(self.pixel_pin, self.num_pixels, brightness=0.5, auto_write=False, pixel_order=self.ORDER) 
        self.matrix = self.initMatrix(x,y);
    
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
        if(isinstance(mode, Mode)):
            if(isinstance(self.mode, Mode)):
                print("testing destr")
                self.mode.terminate()
            self.mode = mode
            mode.start()
