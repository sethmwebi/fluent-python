import time

from example9_24 import clock


@clock("{name}:.{elapsed}s")
def snooze(seconds):
    time.sleep(seconds)


for i in range(3):
    snooze(0.123)
