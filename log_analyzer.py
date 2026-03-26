import re
import argparse
from collections import Counter

parser = argparse.ArgumentParser(description="Log Analyzer Tool")
parser.add_argument("-t", "--threshold", type=int, required=True)
parser.add_argument("-f", "--file", required=True)
args = parser.parse_args()

ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
ip_list = []

try:
    with open(args.file, "r") as log_file:
        for line in log_file:
            matches = re.findall(ip_pattern, line)
            if matches:
                ip_list.extend(matches)
except FileNotFoundError:
    print("Error: Log file not found.")

ip_counts = Counter(ip_list)

print("--- Analysis Results ---")
for ip, count in ip_counts.items():
    if count > args.threshold:
        print(f"Suspicious activity: {ip} appeared {count} times.")

if not ip_list:
    print("No IP addresses found in the log file.")