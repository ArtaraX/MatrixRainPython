import pygame as pg
from random import choice, randrange
import os

#VARIABLES
WIDTH = 1920
HEIGHT = 1050
FONT_SIZE = 30
background_color = (0,0,0)
# alpha_value = randrange(30, 40) # start, end, step
alpha_value = 25
# char_color = (0,255,255)

FPS = 60

x = 0
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

chars = [chr(unicode) for unicode in range(12449, 12539)]  # generate list of katakana
# chars = [chr(unicode) for unicode in range(12437, 12539)] 

pg.init()
clock = pg.time.Clock()
pg.display.set_caption("Matrix Rain")
screen = pg.display.set_mode((WIDTH, HEIGHT))
display_surface = pg.Surface((WIDTH, HEIGHT))
display_surface.set_alpha(alpha_value)
# screen.fill(background_color)

font = pg.font.Font('MS Mincho.ttf', FONT_SIZE)





pg.display.flip()


def generate_colors():
    r, g, b = randrange(255), randrange(255), randrange(255)
    return (r,g,b)

class Katakana:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.speed = FONT_SIZE
        self.value = choice(colored_chars)

    def draw(self):
        
        self.value = choice(colored_chars)
        screen.blit(self.value, (self.x, self.y))
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 20)
        


colored_chars = [font.render(char, True, generate_colors()) for char in chars]

# list of Katakana-objects
katakana_stream = [Katakana(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]



def main_loop():
    run = True
    while run:

        
        screen.blit(display_surface, (0,0)) # display_surface has an opacity to it and is repeatedly overlayed over the drawn Katakanas to create the effect of the katakanas slowly disappearing 
        display_surface.fill(background_color)
        # screen.fill(background_color)
        

        [katakana.draw() for katakana in katakana_stream] # drawing the katakana objects
        
        pg.display.update()

        pg.time.delay(120)
        pg.display.update()
        
        clock.tick(FPS) # 60fps

        for event in pg.event.get():

        
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_ESCAPE:
                    run = False
                
                
                

            if event.type == pg.QUIT:
                run = False


main_loop()





