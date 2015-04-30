import platform
import sys

def print_status(message="", type="info"):
    color_print = sys.stdout.isatty() and platform.system() != "Windows"
        
    if type == "info":
        if color_print:
            print("\033[1;34m[*]\033[1;m {}".format(message))
        else:
            print("[*] {}".format(message))
        
    elif type == "debug":
        if color_print:
            print("\033[1;33m[?]\033[1;m {}".format(message))
        else:
            print("[?] {}".format(message))
        
    elif type == "warn" or type == "error":
        if color_print:
            print("\033[1;31m[!]\033[1;m {}".format(message))
        else:
            print("[!] {}".format(message))
        
    elif type == "fail":
        if color_print:
            print("\033[1;31m[-]\033[1;m {}".format(message))
        else:
            print("[-] {}".format(message))

    elif type == "maybe":
        if color_print:
            print("\033[1;32m[~]\033[1;m {}".format(message))
        else:
            print("[~] {}".format(message))

    elif type == "success":
        if color_print:
            print("\033[1;32m[+]\033[1;m {}".format(message))
        else:
            print("[+] {}".format(message))
        
    elif type == "alert" or type == "panic":
        if color_print:
            print("\033[1;31m[ALERT]\033[1;m {}".format(message))
        else:
            print("[ALERT] {}".format(message))
