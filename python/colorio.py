from __future__ import print_function
import platform
import sys

color_print = sys.stdout.isatty() and platform.system() != "Windows"

def print_status(message="", type="info"):
    if type == "info":
        if color_print:
            print("\033[1;34m[*]\033[1;m {}".format(message))
        else:
            print("[*] {}".format(message))
        
    elif type == "debug":
        if color_print:
            print("\033[1;33m[#]\033[1;m {}".format(message))
        else:
            print("[#] {}".format(message))

    elif type == "maybe" or type == "unclear":
        if color_print:
            print("\033[1;33m[~]\033[1;m {}".format(message))
        else:
            print("[~] {}".format(message))
        
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
    
    else:
        raise ValueError("Invalid message type")


def take_input(message):
    # Python 2 raw_input was renamed to input in Python 3, thus this
    # workaround
    global input
    try:
        input = raw_input
    except NameError:
        pass    

    if color_print:
        result = input("\033[1;34m[?]\033[1;m {}\n"
            "\033[1;34m>\033[1;m ".format(message))
    else:
        result = input("[?] {}\n> ".format(message, prompt))
   
    return result 
