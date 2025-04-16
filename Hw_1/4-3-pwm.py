import RPi.GPIO as gp
pin = 16
gp.setmode(gp.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
gp.setup(dac, gp.OUT)
gp.setup(pin, gp.OUT)
pwm = gp.PWM(pin, 1000)
pwm.start(0)
try:
    while True:
        d = float(input("Введите цикл от 0 до 100:"))
        pwm.ChangeDutyCycle(d)
        v = 3.3 * d / 100
        print(f" предполагаемое напряжение: {v:.2f}")
finally:
    pwm.stop()
    gp.cleanup()
