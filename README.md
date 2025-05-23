SSH Brute Force Script (For Educational Use Only)

This Python script attempts SSH login brute-force attacks using a password list.

⚠️ Legal Notice

This tool is strictly for educational purposes.
Do NOT use it against systems you do not own or do not have explicit permission to test.
Unauthorized use of brute-force tools is illegal and unethical.

🛠 Requirements

Python 3

pwntools

paramiko

📦 Installation & Usage
```bash
git clone https://github.com/harshbansal95623/SSH-Bruetforce.git
cd SSH-Bruetforce
pip3 install -r requirements.txt
python3 ssh_brute_force.py
```

⚙️ Configuration
Before running the script, you can change the target SSH username by modifying the username variable inside ssh_brute_force.py:

```bash
username = "your_target_username"
```
Make sure to update this to the desired username for your testing environment.
