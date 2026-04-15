#!/usr/bin/env python3

import argparse
import psutil
import time

parser = argparse.ArgumentParser(
    prog='myscript.py',
    description='Myscript description',
    usage='%(prog)s [options..]')

parser.add_argument("-d",
                  "--disk",
                  action="store_true",
                  dest="disk",
                  help="check disk stats",
                  default=False)
parser.add_argument("-c",
                  "--cpu",
                  action="store_true",
                  dest="cpu",
                  help="check cpu stats",
                  default=False)
parser.add_argument("-p",
                  "--ports",
                  action="store_true",
                  dest="ports",
                  help="check listen ports",
                  default=False)
parser.add_argument("-r",
                  "--ram",
                  action="store_true",
                  dest="ram",
                  help="check ram stats",
                  default=False)
parser.add_argument("-o",
                  "--overview",
                  action="store_true",
                  dest="overview",
                  help="top 10 process with most CPU usage.",
                  default=False)
args = parser.parse_args()

def main():
    if args.disk:
        disk()

    if args.cpu:
        cpu()

    if args.ports:
        ports()

    if args.ram:
        ram()

    if args.overview:
        overview()

def disk():
    partitions=psutil.disk_partitions()
    for diskPart in partitions:
        diskUsage=psutil.disk_usage(diskPart.mountpoint)
        print(f"""Disk: {diskPart.device}
Total: {diskUsage.total}
Used: {diskUsage.used}
Free: {diskUsage.free}
Percent Used: {diskUsage.percent}
""")

def cpu():
    print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
    # sample over 0.5s for better user experience, sampling over 1s feels rather slow
    interval=0.5
    print(f"Usage (last {interval}s intervall): {psutil.cpu_percent(interval=interval)}%") 
    # frequency is returned as float, convert to int() for better readability
    print(f"Current CPU Frequency: {int(psutil.cpu_freq().current)}MHz")

def ports():
    print("List of Ports in state LISTEN (TCP and UDP)")
    portList= []
    for connection in psutil.net_connections(kind='inet'):
        if connection.status == 'LISTEN':
            portList.append(connection.laddr.port)
    # https://docs.python.org/3/tutorial/controlflow.html#tut-unpacking-arguments
    print(*sorted(set(portList)), sep='\n')

def ram():
    memory=psutil.virtual_memory()
    print(f"Memory Total: {memory.total}")
    print(f"Memory Used: {memory.used}")
    print(f"Memory Free: {memory.free}")
    print(f"Memory Percent Used: {memory.percent}")

def overview():
    # test over a longer interval like 5s so there is something to sort
    interval = 5

    # initialize cpu_percent run
    for proc in psutil.process_iter():
        proc.cpu_percent(None)

    # sleep for the interval and gather the cpu_percent() information
    time.sleep(interval)
    procs = {}
    for proc in psutil.process_iter(['pid', 'name']):
        cpuUsage = proc.cpu_percent()
        procs[proc.pid] = {"name": proc.name(), "cp": cpuUsage}

    # reverse sort the procs dict by the value of cp, we need a helper function which retrieves
    # the cp key from the sub-dictionary
    procsReversByCp = sorted(procs.items(), key=get_cp_value, reverse=True)
    # print the first 10 keys which had the highest cpu usage throughout the interval
    for i in range(10):
        print(f"Process: {procsReversByCp[i][1]['name']} - CPU Percentage: {procsReversByCp[i][1]['cp']}")

def get_cp_value(item):
    cp = item[1]["cp"]
    return cp


if __name__ == "__main__":
    main()
