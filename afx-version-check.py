import sys

import ctypes  # An included library with Python install.   

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

            check = "Unknown"
            currBuffer = buffer[32 : 39]

            # At 40 is the build number stored
            currBuild = ord(buffer[39:40])

            if (currBuffer) == b'\x00\x5E\x00\x04\x0B\x39\x86': check = "2023 23.3.0"
            if (currBuffer) == b'\x00\x5E\x00\x03\x0B\x39\x0E': check = "2023 23.2.1"
            if (currBuffer) == b'\x00\x5E\x00\x01\x0B\x38\x06': check = "2023 XXX"

            if (currBuffer) == b'\x00\x5D\x00\x2B\x0B\x33\x06': check = "2022 22.6.0"
            if (currBuffer) == b'\x00\x5D\x00\x28\x0B\x32\x86': check = "2022 22.5.0"
            if (currBuffer) == b'\x00\x5D\x00\x1D\x0B\x70\x06': check = "2022 22.0.0"

            if (currBuffer) == b'\x00\x5D\x00\x1D\x0B\x12\x06': check = "2021 18.4.0"
            if (currBuffer) == b'\x00\x5D\x00\x1B\x0B\x11\x0E': check = "2021 18.2.1"

            if (currBuffer) == b'\x00\x5D\x00\x0B\x0B\x08\x26': check = "2020 17.0.4"
            if (currBuffer) == b'\x00\x5D\x00\x0A\x0B\x08\x16': check = "2020 17.0.2"

            if (currBuffer) == b'\x00\x5D\x00\x05\x0B\x00\x9E': check = "16.1.3"
            if (currBuffer) == b'\x00\x5D\x00\x05\x0B\x00\x96': check = "16.1.2"
            if (currBuffer) == b'\x00\x5D\x00\x04\x0B\x00\x0E': check = "16.0.1"
            if (currBuffer) == b'\x00\x5D\x00\x04\x0B\x00\x06': check = "16.0.0"
            if (currBuffer) == b'\x00\x5D\x00\x05\x0B\x00\x9E': check = "16x"
            
            if (currBuffer) == b'\x00\x5C\x00\x06\x07\x38\x06': check = "15.0.0"
            if (currBuffer) == b'\x00\x5C\x00\x0e\x07\x38\x96': check = "15x"
            
            print("After Effects",check,"(Build",currBuild,")")
            input("Press Enter to continue...")
            break
        else:
            count += 1
            buffer = f.read(BUFFER_SIZE)
    else:  # while...else
        # executed if no break
        print("After Effects Build not found.")
        input("Press Enter to continue...")
