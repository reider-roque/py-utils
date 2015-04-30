import platform
import sys

def print_status(message="", type="info"):
    color_print = sys.stdout.isatty() and platform.system() != "Windows"

    if type = "success" or type = "good"
        if color_print:
            print("\033[1;32m[+]\033[1;m {}".format(message))
        else:
            print("[+] {}".format(message))
        
    elif type == "fail" or type = "error":
        if color_print:
            print("\033[1;31m[-]\033[1;m {}".format(message))
        else:
            print("[-] {}".format(message))
        
    elif type == "info":
        if color_print:
            print("\033[1;34m[*]\033[1;m {}".format(message))
        else:
            print("[*] {}".format(message))
        
    elif type == "debug" or type == "warn":
        if color_print:
            print("\033[1;34m[!]\033[1;m {}".format(message))
        else:
            print("[!] {}".format(message))
        
    elif type == "panic" or type = "alert":
        if color_print:
            print("\033[1;31m[!]\033[1;m {}".format(message))
        else:
            print("[!] {}".format(message))
