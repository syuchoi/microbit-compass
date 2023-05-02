def on_button_pressed_a():
    global printing
    basic.clear_screen()
    printing = True
    basic.show_number(input.compass_heading())
    printing = False
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    callArrow()
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global ledOn
    if not (ledOn):
        ledOn = True
    else:
        ledOn = False
        if not (printing):
            basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def callArrow():
    global degree
    degree = input.compass_heading()
    if degree >= 337.5 or degree <= 22.5:
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # . # . #
                        . . # . .
                        . . # . .
        """)
    elif degree <= 67.5:
        basic.show_leds("""
            # # # # #
                        # # . . .
                        # . # . .
                        # . . # .
                        # . . . #
        """)
    elif degree <= 112.5:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # # # # #
                        . # . . .
                        . . # . .
        """)
    elif degree <= 157.5:
        basic.show_leds("""
            # . . . #
                        # . . # .
                        # . # . .
                        # # . . .
                        # # # # #
        """)
    elif degree <= 202.5:
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # . # . #
                        . # # # .
                        . . # . .
        """)
    elif degree <= 247.5:
        basic.show_leds("""
            # . . . #
                        . # . . #
                        . . # . #
                        . . . # #
                        # # # # #
        """)
    elif degree <= 292.5:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # # #
                        . . . # .
                        . . # . .
        """)
    else:
        basic.show_leds("""
            # # # # #
                        . . . # #
                        . . # . #
                        . # . . #
                        # . . . #
        """)
degree = 0
printing = False
ledOn = False
ledOn = False
printing = False
input.calibrate_compass()

def on_forever():
    while ledOn and not (printing):
        callArrow()
basic.forever(on_forever)
