# SSH Brute Force Tool using Pwntools & Paramiko

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Maintained by JOZUES](https://img.shields.io/badge/Maintained%20by-JOZUES-blue)

A simple and educational brute-force SSH login tool built using Python’s `pwntools` and `paramiko`.  
It tests a list of passwords against an SSH server to find valid credentials.

---

##  Features

- Uses `pwntools.ssh()` for simplified SSH connection
- Line-by-line wordlist scanning
- Input-based configuration (host, user, wordlist)
- Handles exceptions cleanly

---

## Requirements

```bash
pip install pwntools paramiko

python3 sshbruteforce.py
```
Then enter:

Host (e.g. 127.0.0.1)

Username (e.g. root)

Wordlist path (e.g. /usr/share/wordlists/rockyou.txt)

### Disclaimer
This tool is intended for educational and ethical testing purposes only.
Do not use it on systems you do not own or have permission to test.

### License
This project is licensed under the MIT License.
See the LICENSE file for full details.

### Author
Developed by JOZUES

Feel free to fork, contribute, and star the repo!



