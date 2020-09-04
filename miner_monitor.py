from time import sleep
from subprocess import run, call, check_output
from os import system


class MinerMonitor(object):
    """Monitor the running status of Ethereum miners"""
    def __init__(self, max_temp, mining_command, time_out):
        super(MinerMonitor, self).__init__()
        self.sleep_interval = sleep_interval
        self.mining_command = mining_command
        self.time_out = time_out

    def monitor_mining(self):
        """Monitor mining status"""
        while True:
            check_output(self.mining_command, shell=True)
            
if __name__ == '__main__':
    miner_monitor = MinerMonitor(80, "mine_eth", 1200)
    miner_monitor.monitor_mining()