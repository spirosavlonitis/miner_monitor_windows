from time import sleep
import os
import subprocess

class TempMonitor(object):
    """Monitor the temperature of the miners"""
    def __init__(self, **params):
        super(TempMonitor, self).__init__()
        self.max_temp = params['max_temp']
        self.sleep_interval = params['sleep_interval']

    def monitor_temp(self):
        """Monitor gpu temperature"""
        while True:
            temps = subprocess.check_output("nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader", shell=True)
            print(temps)
            sleep(self.sleep_interval)


if __name__ == '__main__':
    temp_monitor = TempMonitor(max_temp = 80, sleep_interval = 1200)
    temp_monitor.monitor_temp()