import time
from example9_24 import clock


@clock("{name}({args}) dt={elapsed:0.3f}s")
def snooze(seconds):
    time.sleep(seconds)


for i in range(3):
    snooze(0.123)
