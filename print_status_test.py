from print_status import print_status

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
    print("Exception: " + e.message)
