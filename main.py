import sys
import threading
import time
from datetime import datetime


class Monitoring():  # MONITORING
    def __init__(self):
        self.last_check_in = 0

    def alive_alert(self, t):
        self.last_check_in = t

    def monitoring(self):
        while True:
            if self.last_check_in > time.time() - 1:
                sys.stdout.write("\rProcess is Alive - " + str(datetime.fromtimestamp(self.last_check_in)))
                sys.stdout.flush()
            else:
                sys.stdout.write("\rProcess is Dead")
                sys.stdout.flush()
                # PUT ALERTING FUNCTIONALITY HERE


def process(alive_alert):  # CRITICAL PROCESS
    heartbeat_interval = .5
    last_beat = 0

    while True:
        t = time.time()
        if last_beat < t - heartbeat_interval:
            alive_alert(t)
            last_beat = t

        # PUT CRASHING HERE


monitor = Monitoring()  # Create Monitoring Process

# Put Critical Process into Thread and give place to call for heartbeat
p = threading.Thread(target=process, args=[monitor.alive_alert])
p.start()

# Start Monitoring
monitor.monitoring()
