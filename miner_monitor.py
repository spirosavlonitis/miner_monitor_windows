from time import sleep
from subprocess import run, call, check_output
from os import system


class MinerMonitor(object):
    """Monitor the running status of Ethereum miners"""
    def __init__(self, **params):
        super(MinerMonitor, self).__init__()
        self.mining_command = params['mining_command']
        self.sleep_interval = params['sleep_interval']


    def monitor_mining(self):
        """Monitor mining status"""
        while True:
            check_output(self.mining_command, shell=True)
            print("Miners Down waiting %.2f minutes" % (self.sleep_interval / 60))
            sleep(self.sleep_interval)
            
if __name__ == '__main__':
    miner_monitor = MinerMonitor(mining_command = '.\\eth.bat', sleep_interval = 60)
    miner_monitor.monitor_mining()