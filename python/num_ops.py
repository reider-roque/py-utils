def binify(num_or_chr):
    try:
        num = ord(num_or_chr)
    except:
        num = num_or_chr

    bin_str = bin(num)
    bin_str = bin_str.split("b")[1]
    bin_str = bin_str.zfill(8)

    return bin_str

def hexlify(data): 
    return "".join("\\x{:02x}".format(ord(c)) for c in data)

def hexlify_nasm(data): 
    return "".join("0x{:02x},".format(ord(c)) for c in data)[:-1]

def unhexlify(data):
    return "".join([chr(int(num, 16)) for num in data[2:].split("\\x")])
