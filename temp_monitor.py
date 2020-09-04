from time import sleep
import os
import subprocess

class TempMonitor(object):
    """Monitor the temperature of the miners"""
    def __init__(self, **params):
        super(TempMonitor, self).__init__()
        self.max_temp = params['max_temp']
        self.sleep_interval = params['sleep_interval']
        self.pid_command =  params['pid_command']
        with open("temperature_status.txt", "w") as f:
            f.write('0')        

    def monitor_temp(self):
        """Monitor gpu temperature"""
        while True:
            temps = subprocess.check_output("nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader", shell=True)
            print(temps.decode("utf-8").replace('\n', ' '))
            for x in temps.decode("utf-8").split('\n')[:-1]:
                if int(x) >= self.max_temp:
                    miner_pid = subprocess.check_output(self.pid_command, shell=True).decode("utf-8").replace('\n', '')
                    subprocess.run(["kill", miner_pid])
                    with open("temperature_status.txt", "w") as f:
                        f.write('1')
                    print("Miners Over Heated Shutting Them Down !")

            sleep(self.sleep_interval)
            with open("temperature_status.txt", "w") as f:
                f.write('0')


if __name__ == '__main__':
    temp_monitor = TempMonitor(max_temp = 80, sleep_interval = 1200, pid_command = 'pidof ethminer')
    temp_monitor.monitor_temp()