import os
import sys
import time
from datetime import datetime
from random import random
from threading import Thread

# DATASET FOR CAR
object_distances = [random() for _ in range(10000000)]  # Random Data


def process(alive_alert):  # CRITICAL PROCESS
    """
    The critical process(feature). This process is active all the time except the times of failure.

    Parameters
    ----------
    :param alive_alert: monitoring function for the process

    """
    heartbeat_interval = .5  # Send Heartbeat every half second
    last_beat = 0  # Last time a beat was sent
    i = 0  # index of array
    while True:
        t = time.time()
        if last_beat < t - heartbeat_interval:
            alive_alert(t)  # Send heartbeat before processing
            last_beat = t

        str(object_distances[i])  # Simulate Converting data into usable data for processing, will unexpectedly run out
        i += 1  # Loop Through Data


class Monitoring:  # MONITORING
    """
    Monitoring keeps track of active process and updates the heartbeat status.

    """
    def __init__(self):
        self.last_check_in = 0
        self.checkingInterval = .75

    def start_critical_process(self):  # For restarting Threads if they die
        """
        Method to start/restart the critical process based on it's activity status
        """
        p = Thread(target=process, args=[self.alive_alert])
        p.start()

    def alive_alert(self, t):  # Where the process sends the heartbeat to
        """
        Update the heartbeat status

        Parameters
        ----------
        :param t: time when last heartbeat was detected
        """
        self.last_check_in = t

    def monitoring(self):  # Monitoring for the last beat
        """
        Monitor the heartbeat of active process. Restart if process is not active

        """
        while True:
            if self.last_check_in > time.time() - self.checkingInterval:  # Process is alive if it has given a heartbeat in the last .75 seconds
                sys.stdout.write("\rProcess is Alive - " + str(datetime.fromtimestamp(self.last_check_in)))
                sys.stdout.flush()
            else:  # Process is dead if >.75 seconds passed from last heart beat
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the Terminal
                sys.stdout.write("Process is Dead\n")  # Announce Process is Dead
                sys.stdout.write("Restarting in 1 Second\n")  # Announce Restarting
                time.sleep(1)  # Sleep for 1 Second
                self.start_critical_process()  # Restart Process
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear Terminal
                sys.stdout.flush()  # Flush Changes


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear Terminal
    monitor = Monitoring()  # Create Monitoring Process
    monitor.start_critical_process()  # Start the First Process
    monitor.monitoring()  # Start Monitoring
