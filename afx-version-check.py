import sys, binascii

def is_set(x, n):
    # Check if a bit is set at a given position
    return x & 1 << n != 0

def hex_to_binary(hex_string):
    # Create a 64-bit string
    value = int(hex_string, 16)
    return bin(value)[2:].zfill(64)

def is_beta(myInt):
    if not is_set(myInt, 0) and not is_set(myInt, 1):
        return True
    return False

def patch(binary_str):
    patch = binary_str[58:61]
    patch = int(patch, 2)

    return patch

def minor(binary_str):
    minor = binary_str[54:57]
    minor = int(minor, 2)

    return minor

def major(binary_str):
    major_partB = binary_str[50:53]
    major_partA = binary_str[43:46]
    major = int(major_partA + major_partB, 2)

    return major

def systemos(binary_str):
    if (binary_str[46:50] == '1110'):
        return 'Mac Arm 64'
    if (binary_str[46:50] == '1100'):
        return 'Win'
    if (binary_str[46:50] == '1101'):
        return 'Mac'

    return 'unknown'

def hex_to_version(hex_string):
    binary_string = hex_to_binary(hex_string)
    myInt = int(hex_string, 16)

    beta = ''
    if is_beta(myInt):
        beta = ' BETA'

    return 'v' + str(major(binary_string)) + '.' + str(minor(binary_string)) + "." + str(patch(binary_string)) + beta + ' (' + str(systemos(binary_string)) + ')'

BUFFER_SIZE = 40  
filename = sys.argv[1]
assert BUFFER_SIZE % 2 == 0
START_HEADER = b'\x68\x65\x61\x64'

with open(filename, 'rb') as f:
    count = 0
    buffer = f.read(BUFFER_SIZE)
    while buffer:
        p = buffer.find(START_HEADER)
        if p != -1:
            print("After Effects Version:")

            version = "Unknown"
            currBuffer = buffer[32:39]
            converted = binascii.hexlify(bytearray(currBuffer))
            hexstring = converted.decode("utf-8")

            version = hex_to_version(hexstring)

            # At 40 the build number is stored
            currBuild = ord(buffer[39:40])
            
            print("After Effects",version,"(Build",currBuild,")")
            input("Press Enter to continue...")
            break
        else:
            count += 1
            buffer = f.read(BUFFER_SIZE)
    else:  # while...else
        # executed if no break
        print("After Effects Build not found.")
        input("Press Enter to continue...")
