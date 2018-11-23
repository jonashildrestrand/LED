import led
import board
import neopixel
import time
import random
from threading import Thread
import alsaaudio, audioop

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

    def fill(self, r, g, b): 
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                self.matrix[i][j].setColor(r,g,b);
        return "test"

    def setPixelColor(self, row, col, r, g, b):
        self.matrix[row][col].animateInAndOut(r,g,b);

    def randomPixelFlow(self):
        print("test");
        while True:
            row = random.randint(0,1);
            col = random.randint(0,8);
            r = random.randint(0,255);
            g = random.randint(0,255);
            b = random.randint(0,255);
            self.matrix[row][col].animateInAndOut(r,g,b);

    def music(self):
        inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)
        inp.setchannels(1)
        inp.setrate(8000)
        inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
        inp.setperiodsize(160)

        prev = 0;
        while True:
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
