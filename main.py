laser = None
tie = None

def on_forever():
    game.create_sprite(1, 3)
    game.create_sprite(3, 3)
    game.create_sprite(3, 1)
    game.create_sprite(1, 1)
    
    def on_button_pressed_ab():
        global laser
        laser = game.create_sprite(2, 2)
        basic.pause(300)
        laser.delete()
    input.on_button_pressed(Button.AB, on_button_pressed_ab)
    
basic.forever(on_forever)
