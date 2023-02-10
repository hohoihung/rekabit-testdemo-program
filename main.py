# Turn on all LEDs

def on_button_pressed_a():
    global index
    while index < 9:
        pins.digital_write_pin(LED_pins[index], 1)
        index += 1
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    rekabit.run_motor(MotorChannel.ALL, MotorDirection.FORWARD, 128)
    rekabit.set_servo_position(ServoChannel.ALL, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_screen_down():
    control.reset()
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_button_pressed_ab():
    music.play_tone(294, music.beat(BeatFraction.QUARTER))
    rekabit.brake_motor(MotorChannel.ALL)
    rekabit.set_servo_position(ServoChannel.ALL, 90)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Turn off all LEDs

def on_button_pressed_b():
    global index2
    while index2 < 9:
        pins.digital_write_pin(LED_pins[index2], 0)
        index2 += 1
    music.play_tone(330, music.beat(BeatFraction.QUARTER))
    rekabit.run_motor(MotorChannel.ALL, MotorDirection.BACKWARD, 128)
    rekabit.set_servo_position(ServoChannel.ALL, 180)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.HEART)
index = 0
index2 = 0
index3 = 0
rekabit.clear_all_rgb_pixels()
rekabit.set_rgb_brightness(25)
# Create an array of pins associate with status indicator LEDs. View the code in Python mode.
LED_pins = [DigitalPin.P0,
    DigitalPin.P1,
    DigitalPin.P2,
    DigitalPin.P9,
    DigitalPin.P12,
    DigitalPin.P13,
    DigitalPin.P14,
    DigitalPin.P15,
    DigitalPin.P16]
while index3 < 9:
    pins.digital_write_pin(LED_pins[index3], 0)
    index3 += 1
music.start_melody(music.built_in_melody(Melodies.POWER_UP),
    MelodyOptions.ONCE_IN_BACKGROUND)
index3 = 0
# Turn on LEDs one-by-one (slow).
while index3 < 9:
    pins.digital_write_pin(LED_pins[index3], 1)
    index3 += 1
    basic.pause(100)
index3 = 0
# Turn off LEDs one-by-one (fast).
while index3 < 9:
    pins.digital_write_pin(LED_pins[index3], 0)
    index3 += 1
    basic.pause(50)

def on_forever():
    rekabit.set_all_rgb_pixels_color(0xff0000)
    basic.pause(200)
    rekabit.set_all_rgb_pixels_color(0xff8000)
    basic.pause(200)
    rekabit.set_all_rgb_pixels_color(0xffff00)
    basic.pause(200)
    rekabit.set_all_rgb_pixels_color(0x00ff00)
    basic.pause(200)
    rekabit.set_all_rgb_pixels_color(0x00ffff)
    basic.pause(200)
    rekabit.set_all_rgb_pixels_color(0x007fff)
    basic.pause(200)
    rekabit.set_all_rgb_pixels_color(0x0000ff)
    basic.pause(200)
    rekabit.set_all_rgb_pixels_color(0x7f00ff)
    basic.pause(200)
    rekabit.set_all_rgb_pixels_color(0xff00ff)
    basic.pause(200)
    rekabit.set_all_rgb_pixels_color(0xff9da5)
    basic.pause(200)
    rekabit.set_all_rgb_pixels_color(0xff0080)
    basic.pause(200)
basic.forever(on_forever)
