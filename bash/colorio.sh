function print_status() {
    MESSAGE=$1
    TYPE=$2
    case $TYPE in
        debug)
            printf "\033[1;33m[#]\033[1;m $MESSAGE\n" 
        ;;
        maybe|unclear)
            printf "\033[1;33m[~]\033[1;m $MESSAGE\n" 
        ;;
        warn|error)
            printf "\033[1;31m[!]\033[1;m $MESSAGE\n" 
        ;;
        fail)
            printf "\033[1;31m[-]\033[1;m $MESSAGE\n" 
        ;;
        success)
            printf "\033[1;32m[+]\033[1;m $MESSAGE\n" 
        ;;
        alert)
            printf "\033[1;31m[ALERT]\033[1;m $MESSAGE\n" 
        ;;
        info|*)  # All other types are informational
            printf "\033[1;34m[*]\033[1;m $MESSAGE\n" 
        ;;
    esac
}

function take_input() {
    MESSAGE=$1
    printf "\033[1;34m[?]\033[1;m $MESSAGE\n" 
    printf "\033[1;34m>\033[1;m " 
    read $2
}
