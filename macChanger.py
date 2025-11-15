import argparse
import re
import subprocess
import os
from time import sleep

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"


def intro():
    os.system("clear")
    print(CYAN + r"""
                                             ___                                                         
                                            (   )                                                        
 ___ .-. .-.     .---.    .--.      .--.     | | .-.     .---.   ___ .-.     .--.     .--.    ___ .-.    
(   )   '   \   / .-, \  /    \    /    \    | |/   \   / .-, \ (   )   \   /    \   /    \  (   )   \   
 |  .-.  .-. ; (__) ; | |  .-. ;  |  .-. ;   |  .-. .  (__) ; |  |  .-. .  ;  ,-. ' |  .-. ;  | ' .-. ;  
 | |  | |  | |   .'`  | |  |(___) |  |(___)  | |  | |    .'`  |  | |  | |  | |  | | |  | | |  |  / (___) 
 | |  | |  | |  / .'| | |  |      |  |       | |  | |   / .'| |  | |  | |  | |  | | |  |/  |  | |        
 | |  | |  | | | /  | | |  | ___  |  | ___   | |  | |  | /  | |  | |  | |  | |  | | |  ' _.'  | |        
 | |  | |  | | ; |  ; | |  '(   ) |  '(   )  | |  | |  ; |  ; |  | |  | |  | '  | | |  .'.-.  | |        
 | |  | |  | | ' `-'  | '  `-' |  '  `-' |   | |  | |  ' `-'  |  | |  | |  '  `-' | '  `-' /  | |        
(___)(___)(___)`.__.'_.  `.__,'    `.__,'   (___)(___) `.__.'_. (___)(___)  `.__. |  `.__.'  (___)       
                                                                            ( `-' ;                      
                                                                             `.__.                       
""" + RESET)

    print(YELLOW + "[*] Simple MAC Address Changer by Oussama" + RESET)
    print(YELLOW + "[*] GitHub: github.com/Oussamahassania " + RESET)
    print(YELLOW + "--------------------------------------------------" + RESET)
    sleep(1)

    print(GREEN + "[*] Initializing..." + RESET)
    sleep(0.5)
    print(GREEN + "[*] Loading modules..." + RESET)
    sleep(0.5)
    print(GREEN + "[*] Ready to start!" + RESET)
    print()

def get_argument():
    parser = argparse.ArgumentParser(
        description="simple mac changer ",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
     '-i',
     '--interface',
      dest='interface',
      required=True,
      help='interface like (eth0,wlan0,...)')

    parser.add_argument(
        '-m',
        '--mac',
        dest='mac',
        required=True,
        help='mac address that u want')
    args = parser.parse_args()
    if args.interface and args.mac:
        return args.interface, args.mac
    else:
        parser.error("[!] Invalid Syntax. "
                     "Use --help for more details.")

def mac_changer(interface,mac):
    print("changing the mac address for " + interface + " to " + mac)
    subprocess.call("sudo ifconfig " + interface + " down", shell=True)
    subprocess.call("sudo ifconfig " + interface + " hw ether " + mac, shell=True)
    subprocess.call("sudo ifconfig " + interface + " up", shell=True)

def get_current_mac(interface):
    output = subprocess.check_output(["ifconfig",interface])
    return (re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w"
                     ,str(output))
                     .group(0))

if __name__ == "__main__":
    intro()
    print("[* Welcome to my simple mac changer]*]")
    print("[*] Press CTRL-C to QUIT")
    TIME_TO_WAIT = 60
    interface,mac=get_argument()
    current_mac=get_current_mac(interface)
    print("[+] Current MAC:", current_mac)
    mac_changer(interface, mac)
    print("[+] New MAC:", get_current_mac(interface))