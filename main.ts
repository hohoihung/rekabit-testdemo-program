// Turn on all LEDs
input.onButtonPressed(Button.A, function () {
    index = 0
    while (index < 9) {
        pins.digitalWritePin(LED_pins[index], 1)
index += 1
    }
    music.playTone(262, music.beat(BeatFraction.Quarter))
    rekabit.runMotor(MotorChannel.All, MotorDirection.Forward, 128)
    rekabit.setServoPosition(ServoChannel.All, 0)
})
input.onGesture(Gesture.ScreenDown, function () {
    control.reset()
})
input.onButtonPressed(Button.AB, function () {
    music.playTone(294, music.beat(BeatFraction.Quarter))
    rekabit.brakeMotor(MotorChannel.All)
    rekabit.setServoPosition(ServoChannel.All, 90)
})
// Turn off all LEDs
input.onButtonPressed(Button.B, function () {
    index2 = 0
    while (index2 < 9) {
        pins.digitalWritePin(LED_pins[index2], 0)
index2 += 1
    }
    music.playTone(330, music.beat(BeatFraction.Quarter))
    rekabit.runMotor(MotorChannel.All, MotorDirection.Backward, 128)
    rekabit.setServoPosition(ServoChannel.All, 180)
})
let index3 = 0
let index2 = 0
let index = 0
basic.showIcon(IconNames.Heart)
rekabit.clearAllRgbPixels()
rekabit.setRgbBrightness(25)
// Create an array of pins associate with status indicator LEDs. View the code in Python mode.
let LED_pins = [
DigitalPin.P0,
DigitalPin.P1,
DigitalPin.P2,
DigitalPin.P9,
DigitalPin.P12,
DigitalPin.P13,
DigitalPin.P14,
DigitalPin.P15,
DigitalPin.P16
]
while (index3 < 9) {
    pins.digitalWritePin(LED_pins[index3], 0)
index3 += 1
}
music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.OnceInBackground)
index3 = 0
// Turn on LEDs one-by-one (slow).
while (index3 < 9) {
    pins.digitalWritePin(LED_pins[index3], 1)
index3 += 1
    basic.pause(100)
}
index3 = 0
// Turn off LEDs one-by-one (fast).
while (index3 < 9) {
    pins.digitalWritePin(LED_pins[index3], 0)
index3 += 1
    basic.pause(50)
}
basic.forever(function () {
    basic.showIcon(IconNames.SmallHeart)
    rekabit.setAllRgbPixelsColor(0xff0000)
    basic.pause(200)
    rekabit.setAllRgbPixelsColor(0xff8000)
    basic.pause(200)
    rekabit.setAllRgbPixelsColor(0xffff00)
    basic.pause(200)
    rekabit.setAllRgbPixelsColor(0x00ff00)
    basic.pause(200)
    rekabit.setAllRgbPixelsColor(0x00ffff)
    basic.pause(200)
    basic.showIcon(IconNames.Heart)
    rekabit.setAllRgbPixelsColor(0x007fff)
    basic.pause(200)
    rekabit.setAllRgbPixelsColor(0x0000ff)
    basic.pause(200)
    rekabit.setAllRgbPixelsColor(0x7f00ff)
    basic.pause(200)
    rekabit.setAllRgbPixelsColor(0xff00ff)
    basic.pause(200)
    rekabit.setAllRgbPixelsColor(0xff9da5)
    basic.pause(200)
    rekabit.setAllRgbPixelsColor(0xff0080)
    basic.pause(200)
})
