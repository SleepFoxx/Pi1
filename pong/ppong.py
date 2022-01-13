import OpenGl as gl
import pyglet 
import math 

sirka = 1000
vyska = 700

velkost_lopty = 20
rychlost = 200

dlzka_palky = 10
sirka_palky = 100
rychlost_palky = rychlost * 1.5 



ciara_hruba = 20

velkost_fontu = 42
odsadenie_textu = 30 

pozicia_palok = [vyska //2, vyska //2]
pozicia_lopty = [0,0]
rychlost_lopty = [0,0]
stisknutie_klavesy = set()
skore = [0,0]


def vykresli_obdlznik(x1, y1, x2, y2):
    gl.glBegin(gl.GL_TRIANGLES_FAN)
    gl.glVertex2f(int(x1), int(y1))
    gl.glVertex2f(int(x1), int(y2))
    gl.glVertex2f(int(x2), int(y2))
    gl.glVertex2f(int(x2), int(y1))
    gl.glEnd()

def nakresli_text(text, x, y, pozicia_x):
    napis = pyglet.text.Label(text, font_size=velkost_fontu,x=x,y=y, pozicia_x=pozicia_x)





def vykresli():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(1,1,1)


vykresli_obdlznik(
    pozicia_lopty[0] - velkost_lopty //2,
    pozicia_lopty[1] - velkost_lopty //2,
    pozicia_lopty[0] + velkost_lopty //2,
    pozicia_lopty[1] + velkost_lopty //2
)

#text
nakresli_text(str(skore[0]), x=obsadenie_textu)


#palka
for x, y in [(0, pozicia_palok[0]), (sirka, pozicia_palok[1])]:
    vykresli_obdlznik(
        sirka // 2 - 1,
        y,
        sirka // 2 + 1,
        y + ciara_hruba
    )


#poliaca ciara
for y in range(ciara_hruba // 2, vyska, ciara_hruba * 2):
    vykresli_obdlznik(
        sirka // 2 - 1,
        y,
        sirka // 2 + 1,
        y + ciara_hruba 
    )

    #skore
    nakresli_text(str(skore[0]),x=obsadenie_textu,y=vyska - obsadenie_textu - velkost_fontu, pozicia_x='left')
    nakresli_text(str(skore[1]),x=sirka_obsadenie_textu,y=vyska - obsadenie_textu - velkost_fontu, pozicia_x='right')




okno = pyglet.window.Window(width=sirka, height=vyska)
okno,push_handlers(
    on_draw=vykresli,
)
pyglet.app.run()