# SSH Brute Force Script (For Educational Use Only)

This Python script attempts SSH login brute-force attacks using a password list.

## ⚠️ Legal Notice

This tool is **strictly for educational purposes**. Do not use it against systems you do not own or have explicit permission to test. Unauthorized use of brute-force tools is illegal and unethical.

## 🛠 Requirements

- Python 3
- `pwntools`
- `paramiko`

🚀 Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
(Optional) Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
Install the required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
📖 Usage
Make sure you have a password list file (e.g., ssh_common-password.txt) in the project directory.

Run the script:

bash
Copy
Edit
python3 ssh_brute_force.py
Modify the script variables (host, username, etc.) as needed before running.
