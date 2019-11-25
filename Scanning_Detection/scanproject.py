# Imports
import os
from collections import Counter
import operator

# Initializations
file_names = []
port = ''
port_list = []
max_port = 0
temp_dict = {}
hacker_dict = {}
hacker_time = ''
count = 0

path = os.getcwd()  # Current directory
for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith('.log'):  # Check files with .log
            print(name)
            file_names.append(os.path.join(root, name))
            with open(os.path.join(root, name), 'r+') as file:
                for lines in file:
                    line = lines.split()
                    if not line:
                        break
                    count += lines.count('\n')
                    if line[1] == 'IP':
                        ip_port = line[2]
                        time = line[0]
                        ip = ip_port[:13]
                        port = ip_port[-5:]
                        if port.isdigit():
                            ip_time = {ip: time}  # dict with ip and time
                            ip_port = {ip: port}  # dict with ip and port
                            for ip, port in ip_port.items():
                                port_list.append(port)
                                z = Counter(port_list)
                                max_port = max(z.items(), key=operator.itemgetter(1))[0]

                                if ip not in temp_dict:
                                    temp_dict.setdefault(port, ip)
                            hacker_dict = {v: k for k, v in temp_dict.items() if k == max_port}
                            for k, v in ip_time.items():
                                for k2 in hacker_dict:
                                    if k == k2:
                                        hacker_time = ip_time[k]

                # print(f'scanned from {hacker_dict} at {hacker_time}')  # Printing hacker's IP and time
                data = f'     scanned from {hacker_dict}  at {hacker_time}'
                with open('report.txt', 'a+') as result_file:
                    result_file.write( name + '      --> \n')
                    result_file.write(data + '\n')
