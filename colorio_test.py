from print_status import print_status
from print_status import take_input

print_status("Info", "info")
print_status("Warn", "warn")
print_status("Fail", "fail")
print_status("Success", "success")
print_status("Debug", "debug")
print_status("Maybe", "maybe")
print_status("Critical", "alert")

try:
    print_status("Invalid", "invalid")
except ValueError as e:
    print("Exception: " + e.args[0])

user_input = take_input("What's your name?")
print_status("Hello {}!".format(user_input))
