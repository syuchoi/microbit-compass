input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    printing = true
    basic.showNumber(input.compassHeading())
    printing = false
})
input.onButtonPressed(Button.AB, function () {
    callArrow()
    basic.pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    if (!(ledOn)) {
        ledOn = true
    } else {
        ledOn = false
        if (!(printing)) {
            basic.clearScreen()
        }
    }
})
function callArrow () {
    degree = input.compassHeading()
    if (degree >= 337.5 || degree <= 22.5) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # . # . #
            . . # . .
            . . # . .
            `)
    } else if (degree <= 67.5) {
        basic.showLeds(`
            # # # # #
            # # . . .
            # . # . .
            # . . # .
            # . . . #
            `)
    } else if (degree <= 112.5) {
        basic.showLeds(`
            . . # . .
            . # . . .
            # # # # #
            . # . . .
            . . # . .
            `)
    } else if (degree <= 157.5) {
        basic.showLeds(`
            # . . . #
            # . . # .
            # . # . .
            # # . . .
            # # # # #
            `)
    } else if (degree <= 202.5) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            . # # # .
            . . # . .
            `)
    } else if (degree <= 247.5) {
        basic.showLeds(`
            # . . . #
            . # . . #
            . . # . #
            . . . # #
            # # # # #
            `)
    } else if (degree <= 292.5) {
        basic.showLeds(`
            . . # . .
            . . . # .
            # # # # #
            . . . # .
            . . # . .
            `)
    } else {
        basic.showLeds(`
            # # # # #
            . . . # #
            . . # . #
            . # . . #
            # . . . #
            `)
    }
}
let degree = 0
let printing = false
let ledOn = false
ledOn = false
printing = false
input.calibrateCompass()
basic.forever(function () {
    while (ledOn && !(printing)) {
        callArrow()
    }
})
