import pyglet
from pyglet.window import mouse
from time import sleep


window = pyglet.window.Window()
image = pyglet.resource.image('nyancat.jpg')
music = pyglet.resource.media('01_02_Blank Space.wav')
@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')
        music.play()

for i in range(3):
    x=1
    sleep(5)
    if x ==1:
        music.play()
        pyglet.app.run()



