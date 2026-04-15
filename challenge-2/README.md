# Solution
Invocation with help output, implemented via standard lib argparse:

```
./myscript.py -h
usage: myscript.py [options..]

Myscript description

options:
  -h, --help      show this help message and exit
  -d, --disk      check disk stats
  -c, --cpu       check cpu stats
  -p, --ports     check listen ports
  -r, --ram       check ram stats
  -o, --overview  top 10 process with most CPU usage.
```

Feature invocation:

```
./myscript.py -d -c -p -r -o
Disk: /dev/mapper/lintilla--vg-root
Total: 982141468672
Used: 337632505856
Free: 594543480832
Percent Used: 36.2

Disk: /dev/nvme0n1p2
Total: 477210624
Used: 205620224
Free: 246005760
Percent Used: 45.5

Disk: /dev/nvme0n1p1
Total: 535805952
Used: 5029888
Free: 530776064
Percent Used: 0.9

Physical Cores: 4
Usage (last 0.5s intervall): 1.0%
Current CPU Frequency: 1334MHz
List of Ports in state LISTEN (TCP and UDP)
22
25
53
631
8000
Memory Total: 22968070144
Memory Used: 7471312896
Memory Free: 1606373376
Memory Percent Used: 32.5
Process: offlineimap - CPU Percentage: 28.3
Process: firefox - CPU Percentage: 12.3
Process: xfce4-terminal - CPU Percentage: 7.2
Process: emacs - CPU Percentage: 4.5
Process: halloy - CPU Percentage: 4.1
Process: sway - CPU Percentage: 2.9
Process: python3 - CPU Percentage: 2.9
Process: python3 - CPU Percentage: 1.8
Process: waybar - CPU Percentage: 1.4
Process: Isolated Web Co - CPU Percentage: 0.8
```

Implementation relies on the psutil and time packages (time only required for the overview
implementation).
Most values (e.g. the bytes for the disk usage and memory) are returned as-is. If
readability for human users is a goal one could add functionality to convert that to
more convenient units.

The process overview uses a 5s sample interval to generate some meaningful output
on my local system.
