import pyglet
from pyglet.window import mouse
from time import sleep

fps = pyglet.clock.ClockDisplay()
fullscreen = False

window = pyglet.window.Window(width=800, height=800, caption='Resizable window', resizable=True)
image = pyglet.resource.image('nyancat.jpg')
imageTwo = pyglet.resource.image('black.jpg')
logo = pyglet.resource.image('CoderSchoolLogo.png')
logo.anchor_x = logo.width // 2
logo.anchor_y = logo.height // 2
music = pyglet.resource.media('01_02_Blank Space.wav')
sprite = pyglet.sprite.Sprite(img=logo, x=0, y=0)


@window.event
def on_draw():
    window.clear()
    window.set_fullscreen(fullscreen=fullscreen, width=800, height=600)

    sprite.draw()
    fps.draw()

def update(dt):
    sprite.rotation += dt * 90

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        window.clear()
        pyglet.clock.schedule_interval(update, 1 / 60.0)
        print('The left mouse button was pressed.')
        music.play()



        # logo.blit(x, y, 0)

@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.SPACE:
        global fullscreen  # provides access to the global variable
        fullscreen = not fullscreen  # swaps mode

        if fullscreen:
            # if it is in fullscreen mode, change the resolution to 800x600 pixels
            window.set_fullscreen(fullscreen=fullscreen, width=800, height=600)
        else:
            # if not, change the resolution to 300x300 pixels
            window.set_fullscreen(fullscreen=fullscreen, width=300, height=300)


pyglet.app.run()



