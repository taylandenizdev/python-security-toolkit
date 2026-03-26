Python Security Toolkit
A collection of basic security tools written in Python for educational and research purposes.

⚠️ DISCLAIMER
This toolkit is for educational purposes only. The author is NOT responsible for any misuse of these tools. Unauthorized access to computer systems or networks is illegal. Users are solely responsible for complying with local and international laws. Use these tools only on systems you own or have explicit permission to test.

Tools Included
1. Port Scanner
File: port_scanner.py

Function: Scans a range of ports on a target IP address to check for open services.

Usage: python port_scanner.py -i <IP> -s <START_PORT> -e <END_PORT>

2. Hash Cracker
File: hash_cracker.py

Function: Performs a dictionary attack (using a wordlist) against a SHA-256 hash.

Usage: Set the target_hash and file_path inside the script and run.

3. Log Analyzer
File: log_analyzer.py

Function: Parses log files to detect suspicious activity by identifying IP addresses that exceed a certain request threshold.

Usage: python log_analyzer.py -f <LOG_FILE> -t <THRESHOLD>

Installation & Requirements
Python 3.x

No external libraries required (built with standard Python modules: socket, hashlib, re, argparse, collections, threading).