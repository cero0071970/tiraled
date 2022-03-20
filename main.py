from machine import Pin, PWM, DAC
import time

pwm25 = PWM(Pin(25))
pwm25.deinit()
pwm25 = PWM(Pin(25))
pwm25.duty(1022)
pwm25.init()
pwm25.freq(1)
time.sleep(2)

pwm25.deinit()
pwm25 = PWM(Pin(25))
pwm25.init()
pwm25.duty(512)
pwm25.freq(1)
time.sleep(5)

pwm25.deinit()
pwm25 = PWM(Pin(25))
pwm25.init()
pwm25.duty(512)
pwm25.freq(4)

time.sleep(5)

pwm25.deinit()


dacG = DAC(Pin(25))
dacR = DAC(Pin(26))
i = 0
while True:
    time.sleep(0.1)
    i  =i+1
    dacG.write(i)
    dacR.write(255- i)
    if i == 255:
        i=0

