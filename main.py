import re
#ip = re.findall(r'(\d*\.\d*\.\d*\.\d*).*\"GET', file)
def ip_checker(current_ip,ip_list):
    if (current_ip != '') and (current_ip not in ip_list):
        pattern = re.compile('\d*\.\d*\.\d*')
        ip_subnet = re.findall(pattern,current_ip)
        for n in range (len(ip_list)):
            current_subnet = re.findall(pattern,ip_list[n])
            if (ip_subnet == current_subnet):
                ip_list.insert((n+1),current_ip) #IPs from one subnet are nearby
                break
        if (current_ip not in ip_list):
            ip_list.append(current_ip)
f = open('access.log')
ip = []
line = f.readline()
while (line):
    temp_ip = re.findall(r'(\d*\.\d*\.\d*\.\d*).*', line)
    string_ip = temp_ip[0]
    ip_checker((string_ip), ip)
    line = f.readline()
for i in range (len(ip)):
    print(ip[i])




