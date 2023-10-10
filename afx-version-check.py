import sys
import json

import ctypes  # An included library with Python install.   

BUFFER_SIZE = 40  
filename = sys.argv[1]
assert BUFFER_SIZE % 2 == 0
START_HEADER = b'\x68\x65\x61\x64'

with open('ae-builds.json', 'r') as json_file:
    json_data = json.load(json_file)

hex_version_map = {bytes.fromhex(item['hex']): item['version'] for item in json_data}

with open(filename, 'rb') as f:
    count = 0
    buffer = f.read(BUFFER_SIZE)
    while buffer:
        p = buffer.find(START_HEADER)
        if p != -1:
            print("After Effects Version:")

            check = "Unknown"
            currBuffer = buffer[32:39]

            if currBuffer in hex_version_map:
                check = hex_version_map[currBuffer]

            # At 40 is the build number stored
            currBuild = ord(buffer[39:40])
            
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
