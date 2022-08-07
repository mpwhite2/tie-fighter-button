let random = 0
let tie = game.createSprite(0, 0)
let laser = null
game.startCountdown(60000)
basic.forever(function () {
    game.createSprite(1, 3)
game.createSprite(3, 3)
game.createSprite(3, 1)
game.createSprite(1, 1)
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
        
        laser = game.createSprite(2, 2)
        basic.pause(300)
        if (laser.isTouching(tie)){
            tie.delete ()
            game.addScore (10)
            tie = game.createSprite (0,0)
            
        }
        laser.delete()
    })
// move tie
    random = randint(0, 3)
    if (random == 0) {
        tie.change(LedSpriteProperty.Y, 1)
        basic.pause(300)
    }
    if (random == 1) {
        tie.change(LedSpriteProperty.Y, -1)
        basic.pause(300)
    }
    if (random == 2) {
        tie.change(LedSpriteProperty.X, 1)
        basic.pause(300)
    }
    if (random == 3) {
        tie.change(LedSpriteProperty.X, -1)
        basic.pause(300)
    }
    input.onButtonPressed(Button.A, function() {
    tie.change (LedSpriteProperty.X,1)
})
input.onButtonPressed(Button.B, function() {
    tie.change (LedSpriteProperty.X,-1)
})
if (game.isGameOver() && input.buttonIsPressed(Button.A)) {
        control.reset()
    }
})
