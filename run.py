import pyglet

window = pyglet.window.Window()
image = pyglet.resource.image('nyancat.jpg')

@window.event
def on_draw():
    window.clear()
    image.blit(0, 0)


music = pyglet.resource.media('01_02_Blank Space.wav')
music.play()

pyglet.app.run()