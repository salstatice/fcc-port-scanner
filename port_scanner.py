import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    start, end = port_range

    try:
        ip_address = socket.gethostbyname(target)
    except socket.gaierror:
        if target[0].isdigit():
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"

    for port in range(start, end + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        if (s.connect_ex((ip_address, port)) == 0):
            open_ports.append(port)
        s.close()
        

    if verbose:
        ip = ' ('+ip_address+')'
        try:
            url = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            url = ip_address
            ip = ''
        title = "Open ports for {}{}".format(url, ip)
        headers = f"{'PORT':<9}SERVICE"
        script = [title, headers]
        for port in open_ports:
            service_name = ports_and_services.get(port, '')
            script.append(f"{port:<9}{service_name}")
        return '\n'.join(script)
    else:
        return(open_ports)