from time import sleep


class MinerMonitor(object):
    """Monitor the status of Ethereum miners"""
    def __init__(self, check_interval, max_temp, pid_command, mining_command, time_out):
        super(MinerMonitor, self).__init__()
        self.check_interval = check_interval
        self.max_temp = max_temp
        self.pid_command = pid_command
        self.mining_command = mining_command
        self.time_out = time_out

    def monitor_mining(self):
        """Monitor mining status"""

        while True:
            self.check_status()     # check mininer status
            sleep(self.check_interval)

    def check_status(self):
        """Check the status of the mining program"""
        print(self.pid_command)


if __name__ == '__main__':
    miner_monitor = MinerMonitor(300, 80, "pid_command", "mining_command", 1200)
    miner_monitor.monitor_mining()