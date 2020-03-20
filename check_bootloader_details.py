import re
with open("BUILD/HANI_IOT/GCC_ARM-RELEASE/mbed-bootloader_application.map", 'r') as fd:
    s = fd.read()

regex = r"\.rodata\..*{}\s+(0x[0-9a-fA-F]+)".format("bootloader")
match = re.search(regex, s, re.MULTILINE)
offset = int(match.groups()[0], 16)
print hex(offset)