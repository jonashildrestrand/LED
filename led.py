import time

class Pixel:
    def __init__(self, control, pixel):
        self.pixel_number = pixel;
        self.control = control;
        self.pixel = self.control[self.pixel_number];

    def getPixel(self):
        return self.control[self.pixel_number];

    def getColor(self):
        pixel = self.getPixel();
        rgb = {
            "r": pixel[0],
            "g": pixel[1],
            "b": pixel[2]
        };

        return rgb;

    def setColor(self, r, g, b):
        self.control[self.pixel_number] = (r,g,b);
        self.control.show();

    def animateInAndOut(self, r, g, b):
        current = self.getColor();

        while((r != current['r']) or (g != current['g']) or (b != current['b'])):
            if(r != current['r']):
                if((r - current['r']) < 0):
                    current['r'] -= 1;
                else:
                    current['r'] += 1;

            if(g != current['g']):
                if((g - current['g']) < 0):
                    current['g'] -= 1;
                else:
                    current['g'] += 1;

            if(b != current['b']):
                if((b - current['b']) < 0):
                    current['b'] -= 1;
                else:
                    current['b'] += 1;
            
            self.setColor(current['r'], current['g'], current['b']);
            time.sleep(0.001);

        while((0 != current['r']) or (0 != current['g']) or (0 != current['b'])):
            if(0 != current['r']):
                if((0 - current['r']) < 0):
                    current['r'] -= 1;
                else:
                    current['r'] += 1;

            if(0 != current['g']):
                if((0 - current['g']) < 0):
                    current['g'] -= 1;
                else:
                    current['g'] += 1;

            if(0 != current['b']):
                if((0 - current['b']) < 0):
                    current['b'] -= 1;
                else:
                    current['b'] += 1;
            
            self.setColor(current['r'], current['g'], current['b']);
            time.sleep(0.00001);

    def animateToColor(self, r, g, b):
        current = self.getColor();

        while((r != current['r']) or (g != current['g']) or (b != current['b'])):
            if(r != current['r']):
                if((r - current['r']) < 0):
                    current['r'] -= 1;
                else:
                    current['r'] += 1;

            if(g != current['g']):
                if((g - current['g']) < 0):
                    current['g'] -= 1;
                else:
                    current['g'] += 1;

            if(b != current['b']):
                if((b - current['b']) < 0):
                    current['b'] -= 1;
                else:
                    current['b'] += 1;
            
            self.setColor(current['r'], current['g'], current['b']);
            time.sleep(0.001);

        return 0;
