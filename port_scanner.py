import socket
import argparse
import threading

parser = argparse.ArgumentParser(description="Port Scanner Tool")
parser.add_argument("-i", "--ip", required=True)
parser.add_argument("-s", "--start", type=int, required=True)
parser.add_argument("-e", "--end", type=int, required=True)
args = parser.parse_args()

target_ip = args.ip

def port_scan(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_obj:
            socket_obj.settimeout(0.5)
            result = socket_obj.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
    except:
        pass

threads = []

for target_port in range(args.start, args.end + 1):
    t = threading.Thread(target=port_scan, args=(target_ip, target_port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nScanning completed.")