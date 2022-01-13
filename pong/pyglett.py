import pyglet
import math


okno = pyglet.window.Window(width=1000, height=800)

def tik(t):
    had.x = had.x + t * 20
    


pyglet.clock.schedule_interval(tik, 1/30)

def spracuj_text(text):
    had.x = 150

obrazok = pyglet.image.load('snek.png')
obrazok2 = pyglet.image.load('snek2.jpg')
had = pyglet.sprite.Sprite(obrazok)


def vykresli():
    okno.clear()
    had.draw()

def zmen(t):
    had.image = obrazok2
    pyglet.clock.schedule_once(zmen2, 1)

def zmen2(t):
    had.image = obrazok
    pyglet.clock.schedule_once(zmen, 1)

pyglet.clock.schedule_once(zmen, 1)

def klik(x,y, tlacitko, mod):
    had.x = x
    had.y = y
    print(x, y, tlacitko, mod)



okno.push_handlers(
    on_text=spracuj_text, 
    on_draw=vykresli,
    on_mouse_press=klik,
    )
pyglet.app.run()


