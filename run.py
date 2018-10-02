import pyglet
from pyglet.window import mouse
from time import sleep


window = pyglet.window.Window()
image = pyglet.resource.image('nyancat.jpg')
imageTwo = pyglet.resource.image('black.jpg')
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

pyglet.app.run()



