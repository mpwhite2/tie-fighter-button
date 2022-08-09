random = 0
Y_Acceleration = 0
X_Acceleration = 0
laser = None
tie = game.create_sprite(0, 0)
game.start_countdown(60000)

def on_forever():
    global X_Acceleration, Y_Acceleration, random
    X_Acceleration = input.acceleration(Dimension.X)
    Y_Acceleration = input.acceleration(Dimension.Y)
    game.create_sprite(1, 3)
    game.create_sprite(3, 3)
    game.create_sprite(3, 1)
    game.create_sprite(1, 1)
    
    def on_button_pressed_ab():
        global laser, tie
        laser = game.create_sprite(2, 2)
        basic.pause(300)
        if laser.is_touching(tie):
            tie.delete()
            game.add_score(10)
            tie = game.create_sprite(0, 0)
        laser.delete()
    input.on_button_pressed(Button.AB, on_button_pressed_ab)
    
    # move tie
    random = randint(0, 3)
    if random == 0:
        tie.change(LedSpriteProperty.Y, 1)
        basic.pause(300)
    if random == 1:
        tie.change(LedSpriteProperty.Y, -1)
        basic.pause(300)
    if random == 2:
        tie.change(LedSpriteProperty.X, 1)
        basic.pause(300)
    if random == 3:
        tie.change(LedSpriteProperty.X, -1)
        basic.pause(300)
    if X_Acceleration > 120:
        tie.change(LedSpriteProperty.X, 1)
    elif X_Acceleration < 120:
        tie.change(LedSpriteProperty.X, -1)
    if Y_Acceleration > 120:
        tie.change(LedSpriteProperty.Y, 1)
    elif Y_Acceleration < 120:
        tie.change(LedSpriteProperty.Y, -1)
    if game.is_game_over() and input.button_is_pressed(Button.A):
        control.reset()
basic.forever(on_forever)
