# ssh-brute-py

# 🚨 SSH Brute Force Tool using Pwntools & Paramiko

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple and educational brute-force SSH login tool built using Python’s `pwntools` and `paramiko`.  
It tests a list of passwords against an SSH server to find valid credentials.

---

## ⚙️ Features

- Uses `pwntools.ssh()` for simplified SSH connection
- Line-by-line wordlist scanning
- Input-based configuration (host, user, wordlist)
- Handles exceptions cleanly

---

## 🐍 Requirements

```bash
pip install pwntools paramiko
