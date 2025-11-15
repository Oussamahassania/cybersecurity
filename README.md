
🔒 Disclaimer

This tool is made for educational and legitimate security testing purposes only.
Using it for malicious activities is prohibited.

👨‍💻 Author
Oussama Hassania
Simple mac changer Tool – Python Security Utilities

 Features:

✔ Change MAC address easily
✔ Get current MAC automatically
✔ Clean terminal interface
✔ Fully command‑line based
✔ Error handling for invalid usage
✔ Works on Linux (Kali, Ubuntu, etc.)

Requirements

                                   **The MAC address must start with 00**

Make sure you have:

Python 3.x

ifconfig installed (usually from net-tools)

Root privileges (sudo)

🛠️ Usage

                            sudo python3 macChanger.py -i wlan0 -m 11:22:33:44:55:66

| Argument              | Description                        | Required |
| --------------------- | ---------------------------------- | -------- |
| `-i` or `--interface` | Network interface (eth0, wlan0...) | Yes      |
| `-m` or `--mac`       | New MAC address                    | Yes      |


