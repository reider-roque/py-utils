. colorio.sh

print_status "Info" "info"
print_status "Warn" "warn"
print_status "Fail" "fail"
print_status "Success" "success"
print_status "Debug" "debug"
print_status "Maybe" "maybe"
print_status "Critical" "alert"

take_input "What's your name?" RESULT
print_status "Hello $RESULT!"
