FIRST = 32
LAST = 127
WIDTH = 35
HEIGHT = 31

_font =\
b'\x01\x4e\x56\x1c\x4b\x59\x51\x4b\x51\x4b\x51\x47\x52\x3e\x54'\
b'\x3a\x55\x3a\x56\x3a\x57\x3c\x57\x3d\x57\x3d\x57\x3f\x55\x42'\
b'\x53\x47\x51\x4b\x20\x52\x50\x4d\x51\x4d\x52\x4f\x52\x50\x52'\
b'\x51\x51\x52\x50\x52\x4e\x52\x4d\x51\x4d\x50\x4d\x4f\x4e\x4d'\
b'\x50\x4d\x1d\x49\x5b\x54\x46\x53\x46\x53\x3f\x54\x3d\x54\x3d'\
b'\x54\x3c\x56\x3a\x57\x3a\x58\x3a\x59\x3b\x59\x3c\x59\x3d\x59'\
b'\x3d\x59\x3e\x58\x3f\x54\x46\x20\x52\x4c\x46\x4b\x46\x4b\x3f'\
b'\x4b\x3d\x4d\x3a\x4f\x3a\x50\x3a\x51\x3b\x51\x3c\x51\x3d\x4f'\
b'\x3f\x4c\x46\x23\x48\x5c\x4b\x52\x4c\x4b\x4a\x4b\x4a\x49\x4d'\
b'\x49\x4e\x44\x4a\x44\x4a\x42\x4e\x42\x50\x3a\x52\x3a\x50\x42'\
b'\x55\x42\x57\x3a\x59\x3a\x58\x42\x5a\x42\x5a\x44\x57\x44\x56'\
b'\x49\x5a\x49\x5a\x4b\x56\x4b\x54\x52\x52\x52\x54\x4b\x4f\x4b'\
b'\x4d\x52\x4b\x52\x20\x52\x4f\x49\x54\x49\x55\x44\x50\x44\x4f'\
b'\x49\x41\x48\x5c\x54\x44\x57\x47\x57\x48\x58\x49\x58\x4b\x58'\
b'\x4f\x54\x53\x50\x53\x50\x53\x4f\x52\x4f\x55\x4d\x55\x4e\x52'\
b'\x4d\x52\x4b\x52\x4a\x51\x4c\x4b\x4c\x4b\x4c\x4e\x4d\x50\x4e'\
b'\x51\x51\x48\x4f\x45\x4d\x42\x4d\x41\x4d\x3f\x4f\x3c\x52\x3a'\
b'\x54\x3a\x54\x3a\x55\x3a\x55\x39\x56\x39\x56\x3b\x58\x3b\x5a'\
b'\x3c\x58\x41\x58\x41\x58\x40\x58\x3f\x58\x3e\x57\x3d\x57\x3c'\
b'\x56\x3c\x54\x44\x20\x52\x55\x3c\x53\x3c\x52\x3d\x51\x3e\x51'\
b'\x3f\x51\x41\x52\x43\x55\x3c\x20\x52\x50\x51\x50\x51\x51\x51'\
b'\x52\x51\x54\x4f\x54\x4d\x54\x4c\x53\x4a\x52\x49\x50\x51\x4f'\
b'\x44\x60\x5e\x3a\x48\x53\x46\x53\x5c\x3a\x5e\x3a\x20\x52\x4a'\
b'\x47\x48\x47\x46\x45\x46\x42\x46\x3f\x49\x3d\x4a\x3a\x4d\x3a'\
b'\x4f\x3a\x51\x3d\x51\x3f\x51\x42\x4d\x47\x4a\x47\x20\x52\x4a'\
b'\x46\x4b\x46\x4b\x46\x4c\x45\x4c\x44\x4c\x44\x4d\x40\x4e\x3e'\
b'\x4e\x3d\x4e\x3c\x4d\x3b\x4d\x3b\x4c\x3b\x4c\x3c\x4c\x3c\x4b'\
b'\x3d\x4b\x3e\x4a\x42\x49\x44\x49\x45\x49\x45\x4a\x46\x4a\x46'\
b'\x20\x52\x57\x53\x55\x53\x53\x51\x53\x4e\x53\x4b\x57\x47\x5a'\
b'\x47\x5b\x47\x5e\x49\x5e\x4b\x5e\x4e\x59\x53\x57\x53\x20\x52'\
b'\x57\x52\x58\x52\x58\x52\x58\x51\x59\x50\x59\x50\x5a\x4c\x5b'\
b'\x4a\x5b\x49\x5b\x48\x5a\x47\x5a\x47\x59\x47\x58\x49\x57\x4b'\
b'\x56\x4f\x56\x51\x56\x51\x57\x52\x57\x52\x56\x44\x60\x4f\x45'\
b'\x4f\x44\x4f\x43\x4f\x42\x4f\x3f\x53\x3a\x56\x3a\x58\x3a\x5a'\
b'\x3c\x5a\x3e\x5a\x40\x59\x41\x57\x43\x54\x45\x55\x48\x56\x4a'\
b'\x56\x4c\x57\x4b\x58\x48\x58\x48\x58\x47\x58\x46\x57\x46\x57'\
b'\x46\x5e\x46\x5d\x46\x5c\x47\x5b\x48\x59\x4a\x58\x4b\x57\x4d'\
b'\x58\x4f\x59\x4f\x5a\x50\x5b\x50\x5c\x50\x5c\x4f\x5d\x4f\x5e'\
b'\x4f\x5d\x51\x5a\x53\x58\x53\x57\x53\x55\x51\x53\x50\x52\x51'\
b'\x4e\x53\x4c\x53\x4a\x53\x46\x50\x46\x4e\x46\x4c\x48\x4a\x4c'\
b'\x47\x4f\x45\x20\x52\x53\x43\x55\x42\x55\x41\x56\x40\x56\x3e'\
b'\x56\x3d\x56\x3c\x55\x3c\x55\x3c\x54\x3c\x54\x3c\x53\x3d\x53'\
b'\x3f\x53\x40\x53\x42\x53\x43\x20\x52\x4f\x47\x4d\x48\x4c\x4a'\
b'\x4c\x4c\x4c\x4d\x4e\x50\x50\x50\x50\x50\x52\x50\x53\x4f\x52'\
b'\x4d\x50\x49\x4f\x47\x0c\x4d\x57\x50\x46\x4f\x46\x4f\x3f\x4f'\
b'\x3d\x51\x3a\x53\x3a\x54\x3a\x55\x3b\x55\x3c\x55\x3d\x54\x3f'\
b'\x50\x46\x12\x49\x5b\x59\x3a\x58\x3b\x56\x3d\x54\x3f\x52\x43'\
b'\x4f\x4d\x4f\x52\x4f\x54\x50\x58\x50\x59\x4b\x53\x4b\x4c\x4b'\
b'\x49\x4d\x45\x4f\x41\x52\x3e\x55\x3c\x59\x3a\x13\x49\x5b\x4b'\
b'\x59\x4c\x58\x4e\x56\x50\x53\x53\x4d\x54\x4a\x55\x45\x55\x41'\
b'\x55\x3f\x54\x3b\x54\x3a\x59\x40\x59\x47\x59\x4a\x57\x4e\x55'\
b'\x52\x52\x55\x4f\x57\x4b\x59\x4d\x49\x5b\x52\x41\x52\x40\x51'\
b'\x3f\x50\x3d\x50\x3c\x50\x3c\x51\x3a\x52\x3a\x53\x3a\x54\x3b'\
b'\x54\x3c\x54\x3d\x53\x3f\x52\x40\x52\x41\x53\x41\x54\x40\x55'\
b'\x3f\x56\x3e\x57\x3e\x58\x3e\x59\x3f\x59\x40\x59\x41\x58\x42'\
b'\x57\x42\x56\x42\x55\x42\x55\x42\x54\x42\x54\x42\x53\x42\x53'\
b'\x42\x54\x43\x56\x44\x57\x45\x57\x45\x57\x46\x57\x47\x56\x48'\
b'\x55\x48\x54\x48\x53\x46\x53\x45\x53\x44\x53\x43\x52\x42\x51'\
b'\x43\x51\x44\x51\x45\x51\x46\x50\x48\x4f\x48\x4e\x48\x4d\x47'\
b'\x4d\x46\x4d\x45\x4e\x44\x50\x43\x51\x42\x52\x42\x50\x42\x4f'\
b'\x42\x4f\x42\x4e\x42\x4d\x42\x4c\x42\x4b\x41\x4b\x40\x4b\x3f'\
b'\x4c\x3e\x4d\x3e\x4e\x3e\x50\x40\x50\x40\x51\x41\x52\x41\x0d'\
b'\x47\x5d\x49\x45\x51\x45\x51\x3d\x53\x3d\x53\x45\x5b\x45\x5b'\
b'\x48\x53\x48\x53\x50\x51\x50\x51\x48\x49\x48\x49\x45\x14\x4c'\
b'\x58\x4f\x58\x4e\x57\x51\x55\x52\x55\x52\x54\x52\x53\x52\x53'\
b'\x50\x51\x50\x51\x50\x50\x50\x50\x50\x4e\x52\x4d\x53\x4d\x54'\
b'\x4d\x56\x4f\x56\x50\x56\x52\x52\x56\x4f\x58\x05\x4a\x5a\x4e'\
b'\x49\x58\x49\x56\x4c\x4c\x4c\x4e\x49\x0d\x4d\x57\x52\x4d\x53'\
b'\x4d\x55\x4f\x55\x50\x55\x51\x53\x52\x52\x52\x51\x52\x4f\x51'\
b'\x4f\x50\x4f\x4f\x51\x4d\x52\x4d\x05\x47\x5d\x5b\x3a\x4c\x53'\
b'\x49\x53\x58\x3a\x5b\x3a\x30\x48\x5c\x55\x3a\x56\x3a\x59\x3c'\
b'\x5a\x40\x5a\x41\x5a\x44\x58\x4a\x56\x4e\x54\x50\x53\x51\x51'\
b'\x52\x4f\x52\x4e\x52\x4c\x51\x4a\x4e\x4a\x4c\x4a\x48\x4c\x44'\
b'\x4d\x41\x50\x3c\x53\x3a\x55\x3a\x20\x52\x55\x3c\x54\x3c\x54'\
b'\x3c\x53\x3d\x52\x3f\x51\x43\x4f\x48\x4e\x4c\x4e\x4d\x4e\x4e'\
b'\x4e\x50\x4e\x50\x4f\x51\x4f\x51\x50\x51\x50\x51\x51\x50\x52'\
b'\x4e\x53\x4a\x55\x43\x56\x3f\x56\x3d\x56\x3d\x55\x3c\x55\x3c'\
b'\x1c\x49\x5b\x59\x3a\x54\x4e\x53\x4f\x53\x50\x53\x50\x54\x51'\
b'\x55\x51\x56\x51\x56\x52\x4b\x52\x4b\x51\x4d\x51\x4e\x51\x4f'\
b'\x50\x4f\x4e\x53\x42\x53\x40\x53\x40\x54\x3f\x54\x3f\x54\x3e'\
b'\x53\x3d\x52\x3d\x51\x3d\x50\x3d\x50\x3d\x59\x3a\x59\x3a\x20'\
b'\x48\x5c\x56\x52\x4a\x52\x4a\x51\x4e\x4d\x52\x49\x54\x46\x56'\
b'\x43\x56\x41\x56\x40\x54\x3e\x52\x3e\x50\x3e\x4e\x40\x4e\x40'\
b'\x4f\x3e\x50\x3c\x52\x3a\x55\x3a\x57\x3a\x5a\x3d\x5a\x3f\x5a'\
b'\x41\x59\x45\x56\x47\x54\x49\x4f\x4e\x53\x4e\x55\x4e\x57\x4d'\
b'\x58\x4c\x59\x4c\x56\x52\x35\x48\x5c\x4e\x45\x4e\x45\x51\x44'\
b'\x52\x44\x54\x43\x56\x41\x56\x3f\x56\x3e\x54\x3d\x53\x3d\x52'\
b'\x3d\x50\x3e\x50\x3f\x4f\x3e\x50\x3c\x53\x3a\x55\x3a\x57\x3a'\
b'\x5a\x3d\x5a\x3f\x5a\x40\x59\x42\x57\x43\x56\x44\x54\x44\x56'\
b'\x45\x57\x46\x58\x47\x58\x4a\x58\x4e\x55\x50\x52\x52\x4e\x52'\
b'\x4c\x52\x4b\x52\x4a\x51\x4a\x50\x4a\x50\x4b\x4f\x4c\x4f\x4c'\
b'\x4f\x4d\x4f\x4d\x4f\x50\x51\x51\x51\x52\x51\x53\x50\x54\x4e'\
b'\x54\x4c\x54\x4a\x52\x47\x50\x46\x4e\x45\x11\x48\x5c\x51\x4d'\
b'\x4a\x4d\x4a\x4a\x58\x3a\x5a\x3a\x56\x4a\x58\x4a\x58\x4d\x55'\
b'\x4d\x53\x52\x50\x52\x51\x4d\x20\x52\x52\x4a\x55\x40\x4c\x4a'\
b'\x52\x4a\x23\x48\x5c\x51\x3b\x5a\x3b\x59\x3f\x51\x3f\x50\x41'\
b'\x52\x41\x56\x43\x58\x47\x58\x49\x58\x4b\x55\x50\x50\x52\x4e'\
b'\x52\x4c\x52\x4a\x51\x4a\x50\x4a\x4f\x4b\x4e\x4c\x4e\x4c\x4e'\
b'\x4d\x4f\x4d\x4f\x4f\x50\x4f\x51\x50\x51\x52\x51\x53\x4f\x54'\
b'\x4e\x54\x4c\x54\x4a\x52\x46\x50\x45\x4f\x45\x4d\x45\x51\x3b'\
b'\x2d\x48\x5c\x5a\x3a\x5a\x3b\x57\x3c\x55\x3d\x53\x40\x51\x44'\
b'\x53\x43\x54\x43\x56\x43\x58\x46\x58\x49\x58\x4c\x56\x4f\x54'\
b'\x52\x50\x52\x4d\x52\x4a\x4f\x4a\x4b\x4a\x48\x4d\x41\x52\x3d'\
b'\x55\x3b\x57\x3a\x5a\x3a\x20\x52\x50\x45\x4f\x48\x4f\x4b\x4e'\
b'\x4d\x4e\x4f\x4e\x50\x4f\x51\x50\x51\x51\x51\x51\x51\x52\x50'\
b'\x53\x4e\x54\x4a\x54\x48\x54\x46\x53\x46\x53\x45\x52\x45\x51'\
b'\x45\x50\x45\x0c\x48\x5c\x4e\x3b\x5a\x3b\x5a\x3c\x4c\x52\x4b'\
b'\x52\x56\x3f\x50\x3f\x4e\x3f\x4c\x40\x4b\x41\x4a\x41\x4e\x3b'\
b'\x3e\x48\x5c\x50\x46\x4f\x45\x4e\x42\x4e\x41\x4e\x3e\x51\x3a'\
b'\x54\x3a\x57\x3a\x5a\x3d\x5a\x3f\x5a\x41\x59\x43\x57\x44\x57'\
b'\x44\x55\x45\x57\x48\x58\x4a\x58\x4b\x58\x4e\x54\x52\x50\x52'\
b'\x4d\x52\x4a\x4f\x4a\x4d\x4a\x4b\x4c\x49\x4d\x47\x4e\x47\x50'\
b'\x46\x20\x52\x54\x44\x55\x44\x55\x43\x56\x41\x56\x3e\x56\x3d'\
b'\x55\x3b\x54\x3b\x53\x3b\x53\x3c\x52\x3d\x52\x3f\x52\x40\x53'\
b'\x43\x54\x44\x20\x52\x51\x47\x50\x47\x4f\x48\x4f\x49\x4e\x4c'\
b'\x4e\x4e\x4e\x50\x4f\x51\x50\x51\x51\x51\x52\x50\x53\x4f\x53'\
b'\x4d\x53\x4b\x52\x49\x51\x47\x2c\x48\x5c\x4a\x52\x4a\x52\x4d'\
b'\x51\x51\x4d\x53\x49\x51\x49\x50\x49\x4e\x49\x4c\x47\x4c\x44'\
b'\x4c\x41\x4e\x3e\x50\x3a\x54\x3a\x57\x3a\x5a\x3e\x5a\x41\x5a'\
b'\x45\x57\x4c\x52\x50\x4f\x51\x4d\x52\x4a\x52\x20\x52\x54\x48'\
b'\x55\x45\x56\x41\x56\x3f\x56\x3e\x56\x3d\x55\x3b\x54\x3b\x53'\
b'\x3b\x53\x3c\x52\x3d\x51\x3f\x50\x43\x50\x45\x50\x46\x51\x47'\
b'\x51\x48\x52\x48\x53\x48\x54\x48\x1b\x4c\x58\x54\x42\x55\x42'\
b'\x56\x44\x56\x45\x56\x46\x55\x48\x54\x48\x52\x48\x51\x46\x51'\
b'\x45\x51\x44\x52\x42\x54\x42\x20\x52\x50\x4d\x52\x4d\x53\x4f'\
b'\x53\x50\x53\x51\x52\x52\x50\x52\x4f\x52\x4e\x51\x4e\x50\x4e'\
b'\x4f\x4f\x4d\x50\x4d\x22\x4b\x59\x54\x42\x55\x42\x57\x44\x57'\
b'\x45\x57\x46\x55\x48\x54\x48\x53\x48\x51\x46\x51\x45\x51\x44'\
b'\x53\x42\x54\x42\x20\x52\x4d\x58\x4d\x57\x50\x55\x50\x55\x51'\
b'\x54\x51\x53\x51\x53\x4f\x51\x4f\x51\x4e\x50\x4e\x50\x4e\x4e'\
b'\x50\x4d\x51\x4d\x52\x4d\x54\x4f\x54\x50\x54\x52\x51\x56\x4d'\
b'\x58\x08\x47\x5d\x5b\x4f\x49\x47\x49\x46\x5b\x3e\x5b\x41\x4d'\
b'\x47\x5b\x4c\x5b\x4f\x0b\x47\x5d\x49\x43\x5b\x43\x5b\x45\x49'\
b'\x45\x49\x43\x20\x52\x49\x48\x5b\x48\x5b\x4a\x49\x4a\x49\x48'\
b'\x08\x47\x5d\x49\x3e\x5b\x46\x5b\x47\x49\x4f\x49\x4c\x57\x46'\
b'\x49\x41\x49\x3e\x34\x49\x5b\x4f\x4b\x4e\x4b\x4e\x4a\x4f\x47'\
b'\x52\x44\x53\x42\x54\x40\x55\x3f\x55\x3e\x55\x3d\x53\x3b\x52'\
b'\x3b\x52\x3b\x51\x3c\x51\x3c\x51\x3d\x51\x3d\x52\x3e\x52\x3f'\
b'\x52\x40\x50\x41\x4f\x41\x4e\x41\x4d\x40\x4d\x3f\x4d\x3d\x50'\
b'\x3a\x53\x3a\x54\x3a\x57\x3c\x59\x3e\x59\x3f\x59\x41\x58\x42'\
b'\x57\x44\x51\x48\x4f\x4a\x4f\x4b\x20\x52\x4e\x4d\x4f\x4d\x51'\
b'\x4f\x51\x50\x51\x51\x4f\x52\x4e\x52\x4d\x52\x4b\x51\x4b\x50'\
b'\x4b\x4f\x4d\x4d\x4e\x4d\x5a\x41\x63\x55\x42\x5a\x42\x56\x4d'\
b'\x56\x4f\x56\x4f\x56\x50\x57\x51\x57\x51\x59\x51\x5c\x4e\x5f'\
b'\x49\x5f\x46\x5f\x41\x59\x3b\x54\x3b\x50\x3b\x49\x3f\x45\x47'\
b'\x45\x4b\x45\x51\x4c\x59\x52\x59\x57\x59\x5e\x53\x60\x4f\x61'\
b'\x4f\x5f\x54\x57\x5a\x52\x5a\x4b\x5a\x43\x51\x43\x4b\x43\x46'\
b'\x47\x3e\x4f\x3a\x53\x3a\x57\x3a\x5d\x3d\x60\x43\x60\x46\x60'\
b'\x49\x5d\x4f\x58\x52\x55\x52\x54\x52\x52\x50\x52\x4f\x52\x4e'\
b'\x52\x4d\x51\x4f\x50\x50\x4f\x51\x4e\x52\x4d\x52\x4d\x52\x4b'\
b'\x52\x4a\x50\x4a\x4e\x4a\x4c\x4b\x49\x4d\x45\x4f\x43\x51\x42'\
b'\x52\x42\x52\x42\x53\x42\x55\x43\x55\x44\x55\x42\x20\x52\x53'\
b'\x43\x52\x43\x52\x44\x51\x45\x50\x47\x4e\x4b\x4e\x4d\x4e\x4e'\
b'\x4f\x4f\x4f\x4f\x4f\x4f\x50\x4e\x51\x4e\x53\x4b\x54\x47\x54'\
b'\x45\x54\x44\x54\x43\x53\x43\x53\x43\x28\x45\x5f\x57\x4b\x50'\
b'\x4b\x4e\x4c\x4c\x4e\x4c\x4f\x4c\x4f\x4c\x50\x4c\x50\x4c\x51'\
b'\x4c\x51\x4d\x51\x4d\x52\x47\x52\x47\x51\x48\x51\x48\x51\x49'\
b'\x50\x4b\x4e\x5b\x3a\x5c\x3a\x5b\x4d\x5b\x4f\x5b\x4f\x5b\x50'\
b'\x5c\x51\x5d\x51\x5d\x52\x53\x52\x53\x51\x55\x51\x55\x51\x56'\
b'\x51\x56\x4f\x57\x4e\x57\x4b\x20\x52\x57\x49\x57\x42\x51\x49'\
b'\x57\x49\x36\x44\x60\x4d\x3b\x56\x3b\x59\x3b\x5a\x3b\x5c\x3c'\
b'\x5e\x3e\x5e\x3f\x5e\x41\x5c\x43\x59\x45\x56\x46\x59\x47\x5c'\
b'\x49\x5c\x4b\x5c\x4d\x59\x50\x55\x52\x50\x52\x46\x52\x47\x51'\
b'\x48\x51\x49\x51\x4a\x50\x4a\x4e\x4e\x40\x4f\x3e\x4f\x3d\x4f'\
b'\x3c\x4e\x3c\x4c\x3c\x4d\x3b\x20\x52\x52\x45\x54\x45\x57\x44'\
b'\x58\x40\x58\x3f\x58\x3e\x57\x3c\x55\x3c\x54\x3c\x52\x45\x20'\
b'\x52\x51\x46\x4e\x51\x4f\x51\x50\x51\x54\x51\x57\x4c\x57\x4a'\
b'\x57\x49\x55\x47\x54\x46\x51\x46\x23\x45\x5f\x5d\x3a\x5c\x42'\
b'\x5b\x42\x5b\x3f\x58\x3c\x56\x3c\x54\x3c\x4f\x40\x4d\x44\x4c'\
b'\x47\x4c\x4b\x4c\x4d\x4f\x51\x51\x51\x54\x51\x57\x4f\x59\x4d'\
b'\x59\x4d\x57\x50\x53\x53\x50\x53\x4c\x53\x47\x4d\x47\x49\x47'\
b'\x46\x4b\x3f\x52\x3a\x56\x3a\x57\x3a\x5a\x3b\x5b\x3b\x5b\x3b'\
b'\x5c\x3b\x5d\x3a\x5d\x3a\x29\x43\x61\x45\x52\x45\x51\x47\x51'\
b'\x49\x50\x49\x4e\x4d\x40\x4e\x3e\x4e\x3d\x4e\x3c\x4d\x3c\x4b'\
b'\x3c\x4b\x3b\x53\x3b\x59\x3b\x5f\x40\x5f\x45\x5f\x48\x5e\x4a'\
b'\x5b\x4e\x54\x52\x4f\x52\x45\x52\x20\x52\x54\x3c\x4e\x4e\x4e'\
b'\x4f\x4e\x50\x4e\x50\x4f\x50\x4f\x51\x50\x51\x52\x51\x54\x4f'\
b'\x57\x4d\x59\x47\x59\x44\x59\x41\x58\x3e\x56\x3d\x55\x3c\x54'\
b'\x3c\x32\x44\x60\x54\x3c\x51\x45\x52\x45\x55\x45\x58\x43\x59'\
b'\x41\x5a\x41\x57\x4a\x57\x4a\x57\x4a\x57\x49\x57\x48\x56\x47'\
b'\x55\x47\x54\x46\x52\x46\x51\x46\x4f\x4e\x4e\x4f\x4e\x50\x4e'\
b'\x50\x4f\x50\x4f\x51\x51\x51\x54\x51\x59\x4e\x5b\x4c\x5c\x4c'\
b'\x59\x52\x46\x52\x46\x51\x47\x51\x49\x50\x4a\x4e\x4e\x3f\x4e'\
b'\x3e\x4e\x3d\x4e\x3c\x4e\x3c\x4c\x3c\x4c\x3b\x5e\x3b\x5d\x41'\
b'\x5c\x41\x5c\x3f\x5c\x3e\x5b\x3d\x59\x3c\x56\x3c\x54\x3c\x2d'\
b'\x43\x61\x54\x3c\x51\x45\x54\x45\x55\x45\x56\x44\x58\x43\x59'\
b'\x41\x59\x41\x57\x4a\x56\x4a\x56\x4a\x56\x49\x56\x48\x55\x47'\
b'\x54\x46\x51\x46\x4f\x4d\x4e\x4f\x4e\x4f\x4e\x50\x4e\x50\x4f'\
b'\x51\x50\x51\x51\x51\x51\x52\x45\x52\x46\x51\x47\x51\x49\x50'\
b'\x49\x4e\x4e\x40\x4e\x3e\x4e\x3d\x4e\x3c\x4d\x3c\x4c\x3c\x4c'\
b'\x3b\x5f\x3b\x5d\x41\x5c\x41\x5c\x3f\x5b\x3d\x59\x3c\x57\x3c'\
b'\x54\x3c\x31\x44\x60\x5e\x3a\x5c\x42\x5c\x42\x5b\x3f\x59\x3c'\
b'\x56\x3c\x54\x3c\x4f\x3f\x4c\x46\x4c\x4a\x4c\x4e\x4f\x51\x51'\
b'\x51\x52\x51\x53\x51\x55\x4b\x55\x49\x55\x49\x55\x48\x54\x47'\
b'\x53\x47\x53\x47\x5d\x47\x5d\x47\x5c\x47\x5b\x48\x5a\x48\x5a'\
b'\x49\x5a\x4a\x58\x51\x54\x53\x50\x53\x4d\x53\x49\x50\x46\x4c'\
b'\x46\x48\x46\x42\x4c\x3e\x51\x3a\x56\x3a\x57\x3a\x58\x3a\x59'\
b'\x3b\x5a\x3b\x5b\x3b\x5c\x3b\x5d\x3b\x5d\x3a\x5e\x3a\x36\x40'\
b'\x64\x4e\x46\x56\x46\x58\x3f\x59\x3e\x59\x3d\x59\x3c\x58\x3c'\
b'\x56\x3c\x56\x3b\x62\x3b\x61\x3c\x60\x3c\x5e\x3d\x5d\x3f\x59'\
b'\x4e\x59\x4f\x59\x50\x59\x51\x59\x51\x5a\x51\x5b\x51\x5b\x52'\
b'\x50\x52\x50\x51\x52\x51\x53\x50\x54\x4e\x56\x47\x4e\x47\x4c'\
b'\x4e\x4b\x4f\x4b\x50\x4b\x51\x4c\x51\x4e\x51\x4e\x52\x42\x52'\
b'\x43\x51\x44\x51\x46\x50\x46\x4e\x4b\x3f\x4b\x3e\x4b\x3d\x4b'\
b'\x3c\x4a\x3c\x48\x3c\x49\x3b\x54\x3b\x54\x3c\x52\x3c\x51\x3d'\
b'\x50\x3f\x4e\x46\x1a\x47\x5d\x4f\x3c\x4f\x3b\x5b\x3b\x5b\x3c'\
b'\x59\x3c\x57\x3d\x57\x3f\x53\x4e\x52\x4f\x52\x50\x52\x51\x53'\
b'\x51\x53\x51\x55\x51\x55\x52\x49\x52\x49\x51\x4b\x51\x4d\x50'\
b'\x4d\x4e\x52\x3f\x52\x3e\x52\x3d\x52\x3c\x51\x3c\x4f\x3c\x26'\
b'\x45\x5f\x51\x3c\x51\x3b\x5d\x3b\x5c\x3c\x5b\x3c\x59\x3d\x59'\
b'\x3f\x56\x48\x55\x4c\x53\x50\x4f\x53\x4c\x53\x4a\x53\x47\x51'\
b'\x47\x4f\x47\x4e\x49\x4c\x4a\x4c\x4b\x4c\x4c\x4d\x4c\x4e\x4c'\
b'\x4f\x4b\x50\x4b\x50\x4b\x51\x4b\x51\x4b\x51\x4c\x51\x4c\x51'\
b'\x4d\x51\x4f\x4f\x50\x49\x53\x3f\x54\x3e\x54\x3d\x54\x3c\x53'\
b'\x3c\x51\x3c\x3d\x42\x62\x5b\x52\x51\x52\x51\x51\x52\x51\x53'\
b'\x50\x53\x50\x53\x4f\x53\x4d\x50\x45\x4e\x4e\x4d\x4f\x4d\x50'\
b'\x4d\x50\x4e\x51\x50\x51\x50\x52\x44\x52\x45\x51\x46\x51\x47'\
b'\x51\x48\x4f\x49\x4d\x4c\x40\x4d\x3e\x4d\x3d\x4d\x3c\x4c\x3c'\
b'\x4b\x3c\x4b\x3b\x56\x3b\x55\x3c\x54\x3c\x54\x3c\x53\x3c\x53'\
b'\x3d\x52\x3e\x52\x40\x50\x45\x56\x40\x58\x3e\x58\x3e\x58\x3d'\
b'\x58\x3d\x58\x3c\x58\x3c\x57\x3c\x57\x3b\x60\x3b\x5f\x3c\x5e'\
b'\x3c\x5e\x3c\x5d\x3c\x5b\x3d\x5a\x3e\x58\x40\x54\x43\x57\x4c'\
b'\x58\x50\x5a\x51\x5b\x51\x5b\x52\x1d\x45\x5f\x5a\x52\x47\x52'\
b'\x48\x51\x49\x51\x4b\x50\x4b\x4e\x50\x3f\x50\x3e\x50\x3d\x50'\
b'\x3c\x4f\x3c\x4e\x3c\x4e\x3b\x59\x3b\x59\x3c\x57\x3c\x56\x3d'\
b'\x55\x3f\x51\x4d\x50\x4f\x50\x50\x50\x50\x51\x51\x52\x51\x55'\
b'\x51\x5a\x4e\x5c\x4c\x5d\x4c\x5a\x52\x2b\x3e\x66\x4f\x3b\x51'\
b'\x4b\x5b\x3b\x64\x3b\x63\x3c\x62\x3c\x60\x3d\x5f\x3f\x5b\x4e'\
b'\x5b\x4f\x5b\x50\x5b\x51\x5c\x51\x5d\x51\x5d\x52\x52\x52\x52'\
b'\x51\x54\x51\x55\x50\x56\x4e\x5a\x3f\x4d\x52\x4c\x52\x4a\x3f'\
b'\x46\x4e\x46\x4f\x46\x4f\x46\x50\x47\x51\x48\x51\x48\x52\x40'\
b'\x52\x41\x51\x42\x51\x43\x51\x44\x50\x45\x4e\x4a\x3d\x49\x3c'\
b'\x48\x3c\x46\x3c\x47\x3b\x4f\x3b\x25\x41\x63\x51\x3b\x58\x4a'\
b'\x5b\x3f\x5c\x3e\x5c\x3d\x5c\x3d\x5b\x3c\x59\x3c\x59\x3b\x61'\
b'\x3b\x61\x3c\x5f\x3c\x5d\x3d\x5d\x3f\x57\x52\x56\x52\x4d\x3f'\
b'\x49\x4e\x48\x4f\x48\x4f\x48\x50\x4a\x51\x4b\x51\x4b\x52\x43'\
b'\x52\x43\x51\x44\x51\x45\x51\x46\x51\x47\x4f\x47\x4e\x4c\x3d'\
b'\x4b\x3c\x4a\x3c\x49\x3c\x49\x3b\x51\x3b\x25\x44\x60\x4e\x53'\
b'\x4c\x53\x48\x50\x46\x4c\x46\x4a\x46\x47\x4b\x3f\x52\x3a\x56'\
b'\x3a\x58\x3a\x5c\x3c\x5e\x40\x5e\x42\x5e\x46\x58\x4f\x55\x51'\
b'\x52\x53\x4e\x53\x20\x52\x55\x3c\x54\x3c\x52\x3d\x50\x3f\x4e'\
b'\x43\x4c\x4b\x4c\x4d\x4c\x4f\x4e\x51\x4f\x51\x51\x51\x52\x50'\
b'\x55\x4d\x58\x44\x58\x40\x58\x3e\x56\x3c\x55\x3c\x2d\x44\x60'\
b'\x51\x47\x4f\x4e\x4f\x4f\x4f\x50\x4f\x51\x50\x51\x52\x51\x52'\
b'\x52\x46\x52\x46\x51\x48\x51\x49\x51\x49\x50\x4a\x50\x4a\x4e'\
b'\x4f\x3f\x4f\x3e\x4f\x3d\x4f\x3c\x4e\x3c\x4c\x3c\x4d\x3b\x56'\
b'\x3b\x5a\x3b\x5b\x3c\x5e\x3d\x5e\x40\x5e\x43\x59\x48\x54\x48'\
b'\x53\x48\x51\x47\x20\x52\x52\x46\x53\x46\x53\x46\x56\x46\x58'\
b'\x42\x58\x40\x58\x3e\x57\x3c\x55\x3c\x55\x3c\x54\x3c\x52\x46'\
b'\x3c\x44\x60\x4f\x53\x4c\x55\x4e\x55\x4f\x55\x50\x55\x56\x56'\
b'\x57\x56\x59\x56\x5a\x56\x5b\x55\x5c\x54\x5d\x55\x5b\x57\x56'\
b'\x59\x53\x59\x51\x59\x4b\x58\x4a\x58\x49\x58\x47\x58\x47\x58'\
b'\x4d\x53\x4b\x52\x4a\x51\x48\x50\x46\x4c\x46\x4a\x46\x47\x4b'\
b'\x3f\x52\x3a\x56\x3a\x58\x3a\x5c\x3c\x5e\x40\x5e\x42\x5e\x45'\
b'\x5b\x4c\x56\x51\x53\x52\x51\x52\x4f\x53\x20\x52\x55\x3c\x54'\
b'\x3c\x52\x3d\x50\x3f\x4e\x43\x4c\x4b\x4c\x4d\x4c\x4f\x4e\x51'\
b'\x4f\x51\x51\x51\x52\x50\x55\x4d\x58\x44\x58\x40\x58\x3e\x56'\
b'\x3c\x55\x3c\x33\x44\x60\x51\x47\x4f\x4e\x4f\x4f\x4f\x50\x4f'\
b'\x51\x50\x51\x52\x51\x51\x52\x46\x52\x46\x51\x48\x51\x4a\x50'\
b'\x4a\x4e\x4f\x3f\x4f\x3e\x4f\x3d\x4f\x3c\x4e\x3c\x4d\x3c\x4d'\
b'\x3b\x56\x3b\x5a\x3b\x5e\x3e\x5e\x40\x5e\x42\x5c\x44\x5b\x45'\
b'\x57\x46\x59\x4d\x5a\x50\x5c\x51\x5d\x51\x5d\x52\x56\x52\x53'\
b'\x47\x52\x47\x52\x47\x51\x47\x20\x52\x52\x46\x52\x46\x53\x46'\
b'\x55\x46\x58\x42\x58\x40\x58\x3e\x57\x3c\x55\x3c\x55\x3c\x54'\
b'\x3c\x52\x46\x36\x45\x5f\x5d\x3a\x5b\x42\x5a\x42\x5a\x40\x59'\
b'\x3f\x59\x3e\x56\x3c\x55\x3c\x54\x3c\x52\x3e\x52\x3f\x52\x40'\
b'\x53\x43\x56\x45\x58\x47\x59\x4a\x59\x4c\x59\x4e\x57\x51\x53'\
b'\x53\x51\x53\x4f\x53\x4b\x52\x4a\x52\x4a\x52\x49\x52\x48\x53'\
b'\x47\x53\x49\x4a\x4a\x4a\x4a\x4c\x4c\x4f\x4e\x51\x50\x51\x52'\
b'\x51\x54\x4f\x54\x4d\x54\x4c\x53\x4a\x4e\x45\x4d\x43\x4d\x42'\
b'\x4d\x41\x4d\x3e\x51\x3a\x54\x3a\x56\x3a\x58\x3b\x59\x3b\x5a'\
b'\x3b\x5b\x3b\x5b\x3b\x5c\x3a\x5d\x3a\x1b\x45\x5f\x4a\x3b\x5d'\
b'\x3b\x5b\x41\x5a\x41\x5a\x41\x5a\x40\x5a\x3e\x58\x3d\x56\x3c'\
b'\x51\x4e\x50\x4f\x50\x50\x50\x51\x51\x51\x53\x51\x53\x52\x47'\
b'\x52\x48\x51\x49\x51\x4b\x50\x4c\x4e\x51\x3c\x4e\x3c\x4a\x3f'\
b'\x49\x41\x48\x41\x4a\x3b\x31\x44\x60\x57\x3b\x5e\x3b\x5e\x3c'\
b'\x5d\x3c\x5c\x3c\x5b\x3d\x5a\x3f\x57\x4a\x56\x4f\x51\x53\x4d'\
b'\x53\x4b\x53\x48\x51\x46\x50\x46\x4e\x46\x4d\x46\x4c\x46\x49'\
b'\x49\x3f\x4a\x3e\x4a\x3d\x4a\x3c\x49\x3c\x47\x3c\x47\x3b\x52'\
b'\x3b\x52\x3c\x51\x3c\x4f\x3d\x4e\x3f\x4b\x49\x4b\x4c\x4b\x4d'\
b'\x4b\x4f\x4d\x51\x4f\x51\x51\x51\x53\x4f\x54\x4e\x55\x4d\x56'\
b'\x4a\x59\x3f\x59\x3e\x59\x3e\x59\x3c\x59\x3c\x58\x3c\x56\x3c'\
b'\x57\x3b\x1e\x45\x5f\x48\x53\x49\x3f\x49\x3e\x49\x3d\x49\x3c'\
b'\x48\x3c\x47\x3c\x47\x3b\x50\x3b\x50\x3c\x4f\x3c\x4e\x3d\x4e'\
b'\x3f\x4d\x4b\x56\x41\x58\x3f\x59\x3d\x59\x3d\x59\x3c\x58\x3c'\
b'\x57\x3c\x57\x3b\x5d\x3b\x5d\x3c\x5d\x3c\x5c\x3c\x5b\x3d\x5a'\
b'\x3f\x49\x53\x48\x53\x31\x41\x63\x43\x53\x44\x3f\x45\x3e\x45'\
b'\x3d\x45\x3c\x44\x3c\x43\x3c\x43\x3b\x4c\x3b\x4c\x3c\x4c\x3c'\
b'\x4b\x3c\x4a\x3d\x49\x3e\x49\x4a\x4f\x41\x50\x3e\x50\x3e\x50'\
b'\x3d\x50\x3c\x4f\x3c\x4e\x3c\x4e\x3b\x57\x3b\x57\x3c\x56\x3c'\
b'\x55\x3d\x55\x3e\x54\x4a\x5a\x41\x5c\x3f\x5d\x3e\x5d\x3d\x5d'\
b'\x3d\x5d\x3c\x5c\x3c\x5b\x3c\x5b\x3b\x61\x3b\x61\x3c\x60\x3c'\
b'\x60\x3c\x5f\x3d\x5e\x3e\x4f\x53\x4e\x53\x4f\x43\x44\x53\x43'\
b'\x53\x3a\x42\x62\x50\x47\x4d\x3f\x4c\x3d\x4b\x3c\x49\x3c\x49'\
b'\x3b\x53\x3b\x53\x3c\x52\x3c\x51\x3c\x51\x3d\x51\x3e\x52\x3f'\
b'\x54\x44\x57\x41\x59\x3f\x5a\x3e\x5a\x3d\x5a\x3d\x5a\x3c\x5a'\
b'\x3c\x59\x3c\x59\x3b\x60\x3b\x60\x3c\x5f\x3c\x5f\x3c\x5e\x3d'\
b'\x5b\x3f\x55\x45\x58\x4d\x59\x50\x5b\x51\x5c\x51\x5c\x52\x51'\
b'\x52\x52\x51\x53\x51\x54\x51\x54\x50\x54\x4f\x53\x4d\x51\x49'\
b'\x4c\x4d\x4a\x4e\x4a\x50\x4a\x50\x4a\x51\x4b\x51\x4c\x51\x4c'\
b'\x52\x44\x52\x44\x51\x45\x51\x45\x51\x47\x50\x49\x4e\x50\x47'\
b'\x2d\x45\x5f\x4d\x48\x4b\x3f\x4b\x3d\x4a\x3c\x49\x3c\x48\x3c'\
b'\x48\x3b\x53\x3b\x53\x3c\x52\x3c\x50\x3d\x50\x3e\x50\x3e\x50'\
b'\x40\x52\x47\x56\x41\x57\x3f\x58\x3e\x58\x3d\x58\x3d\x57\x3c'\
b'\x56\x3c\x56\x3b\x5d\x3b\x5d\x3c\x5c\x3c\x5b\x3d\x59\x3f\x52'\
b'\x48\x51\x4e\x50\x4f\x50\x50\x50\x50\x51\x51\x52\x51\x53\x51'\
b'\x53\x52\x47\x52\x47\x51\x49\x51\x4a\x51\x4b\x50\x4b\x50\x4b'\
b'\x4e\x4d\x48\x13\x44\x60\x5e\x3c\x4d\x51\x4e\x51\x52\x51\x57'\
b'\x4e\x59\x4b\x5a\x4b\x58\x52\x46\x52\x46\x51\x57\x3c\x55\x3c'\
b'\x51\x3c\x4d\x3e\x4c\x41\x4b\x41\x4d\x3b\x5e\x3b\x5e\x3c\x15'\
b'\x48\x5c\x4a\x58\x53\x3b\x5a\x3b\x5a\x3c\x59\x3c\x58\x3c\x57'\
b'\x3c\x56\x3d\x56\x3f\x4f\x54\x4f\x56\x4f\x57\x4f\x57\x4f\x57'\
b'\x4f\x58\x4f\x58\x50\x58\x51\x58\x52\x58\x51\x58\x4a\x58\x05'\
b'\x4e\x56\x52\x3a\x54\x53\x52\x53\x50\x3a\x52\x3a\x15\x48\x5c'\
b'\x5a\x3b\x51\x58\x4a\x58\x4a\x58\x4b\x58\x4c\x58\x4d\x57\x4e'\
b'\x56\x4e\x55\x55\x3f\x55\x3d\x55\x3c\x55\x3c\x55\x3c\x55\x3c'\
b'\x55\x3c\x54\x3c\x53\x3c\x52\x3c\x53\x3b\x5a\x3b\x08\x48\x5c'\
b'\x4a\x47\x51\x3a\x53\x3a\x5a\x47\x57\x47\x52\x3e\x4d\x47\x4a'\
b'\x47\x05\x47\x5d\x49\x57\x5b\x57\x5b\x5a\x49\x5a\x49\x57\x05'\
b'\x4d\x57\x4f\x3a\x54\x3a\x55\x40\x54\x40\x4f\x3a\x3b\x48\x5c'\
b'\x5a\x42\x57\x4e\x56\x4f\x56\x4f\x56\x50\x56\x50\x57\x50\x57'\
b'\x50\x57\x50\x58\x4f\x58\x4f\x59\x4e\x5a\x4e\x58\x50\x56\x52'\
b'\x54\x52\x53\x52\x52\x51\x52\x51\x52\x50\x53\x4e\x53\x4d\x51'\
b'\x50\x4f\x52\x4e\x52\x4d\x52\x4b\x52\x4a\x50\x4a\x4e\x4a\x4c'\
b'\x4d\x46\x4f\x44\x51\x42\x53\x42\x54\x42\x55\x43\x55\x45\x56'\
b'\x43\x5a\x42\x20\x52\x55\x46\x55\x44\x54\x44\x54\x43\x53\x43'\
b'\x53\x43\x52\x44\x51\x45\x4e\x4b\x4e\x4e\x4e\x4f\x4f\x4f\x4f'\
b'\x4f\x50\x4f\x51\x4e\x52\x4d\x53\x4b\x55\x48\x55\x46\x2a\x48'\
b'\x5c\x55\x3a\x52\x45\x53\x43\x55\x42\x56\x42\x58\x42\x5a\x45'\
b'\x5a\x47\x5a\x4c\x57\x4f\x54\x52\x50\x52\x4d\x52\x4a\x51\x4f'\
b'\x3f\x50\x3d\x50\x3d\x50\x3d\x4f\x3c\x4f\x3c\x4e\x3c\x4e\x3b'\
b'\x54\x3a\x55\x3a\x20\x52\x4e\x51\x4f\x52\x50\x52\x50\x52\x51'\
b'\x51\x52\x51\x54\x4e\x56\x49\x56\x47\x56\x46\x55\x45\x54\x45'\
b'\x53\x45\x52\x46\x51\x47\x50\x49\x4e\x51\x2a\x49\x5b\x57\x4e'\
b'\x58\x4e\x56\x50\x54\x51\x52\x52\x50\x52\x4e\x52\x4c\x51\x4b'\
b'\x4f\x4b\x4e\x4b\x4b\x4e\x45\x53\x42\x55\x42\x57\x42\x59\x44'\
b'\x59\x45\x59\x46\x58\x48\x57\x48\x56\x48\x55\x47\x55\x46\x55'\
b'\x45\x56\x45\x56\x44\x56\x44\x56\x43\x56\x43\x56\x43\x55\x43'\
b'\x54\x43\x53\x44\x51\x46\x4f\x4a\x4f\x4c\x4f\x4e\x51\x50\x52'\
b'\x50\x53\x50\x56\x4f\x57\x4e\x40\x47\x5d\x5b\x3a\x56\x4d\x55'\
b'\x4f\x55\x50\x55\x50\x55\x50\x56\x50\x56\x50\x56\x50\x57\x4f'\
b'\x58\x4e\x58\x4e\x56\x52\x53\x52\x52\x52\x51\x51\x51\x51\x51'\
b'\x50\x51\x4e\x52\x4d\x50\x50\x4e\x52\x4d\x52\x4c\x52\x4b\x52'\
b'\x49\x50\x49\x4e\x49\x4c\x4b\x47\x4e\x44\x51\x42\x52\x42\x53'\
b'\x42\x54\x43\x54\x43\x56\x3f\x56\x3e\x56\x3d\x56\x3d\x55\x3c'\
b'\x55\x3c\x55\x3c\x54\x3c\x55\x3b\x5a\x3a\x5b\x3a\x20\x52\x54'\
b'\x45\x54\x44\x53\x43\x52\x43\x52\x43\x51\x44\x50\x45\x4d\x4b'\
b'\x4d\x4e\x4d\x4e\x4e\x4f\x4e\x4f\x4f\x4f\x4f\x4f\x51\x4d\x54'\
b'\x47\x54\x45\x2c\x49\x5b\x4f\x4c\x4f\x4d\x4f\x4d\x4f\x4f\x51'\
b'\x50\x52\x50\x53\x50\x56\x4f\x57\x4e\x58\x4e\x56\x50\x52\x52'\
b'\x50\x52\x4d\x52\x4b\x50\x4b\x4e\x4b\x4b\x4e\x46\x54\x42\x56'\
b'\x42\x58\x42\x59\x44\x59\x45\x59\x46\x59\x47\x58\x49\x55\x4b'\
b'\x53\x4b\x51\x4b\x4f\x4c\x20\x52\x50\x4b\x51\x4b\x53\x4a\x54'\
b'\x48\x55\x45\x55\x44\x55\x44\x55\x43\x55\x43\x54\x43\x53\x44'\
b'\x51\x47\x50\x4b\x3a\x44\x60\x55\x45\x53\x4d\x52\x52\x4f\x57'\
b'\x4b\x5a\x49\x5a\x48\x5a\x46\x58\x46\x58\x46\x57\x47\x56\x48'\
b'\x56\x49\x56\x4a\x57\x4a\x57\x4a\x58\x49\x58\x49\x58\x4a\x59'\
b'\x4a\x59\x4a\x59\x4a\x59\x4b\x58\x4c\x58\x4c\x56\x4c\x56\x4d'\
b'\x52\x51\x45\x4e\x45\x4f\x43\x50\x43\x51\x42\x52\x41\x54\x3d'\
b'\x58\x3a\x5b\x3a\x5c\x3a\x5e\x3c\x5e\x3d\x5e\x3e\x5d\x3f\x5c'\
b'\x3f\x5b\x3f\x5a\x3e\x5a\x3d\x5a\x3d\x5b\x3c\x5b\x3c\x5b\x3b'\
b'\x5b\x3b\x5a\x3b\x59\x3b\x58\x3c\x57\x3e\x56\x43\x58\x43\x57'\
b'\x45\x55\x45\x58\x46\x5e\x57\x43\x5c\x43\x5b\x45\x59\x45\x5a'\
b'\x46\x5a\x47\x5a\x49\x58\x4b\x55\x4d\x53\x4d\x52\x4d\x51\x4d'\
b'\x50\x4c\x4f\x4d\x4f\x4d\x4e\x4e\x4e\x4e\x4e\x4e\x4f\x4e\x4f'\
b'\x4f\x50\x4f\x53\x50\x55\x50\x56\x51\x58\x53\x58\x54\x58\x56'\
b'\x54\x5a\x50\x5a\x4b\x5a\x49\x58\x48\x57\x48\x56\x48\x55\x4a'\
b'\x53\x4d\x52\x4c\x52\x4c\x51\x4b\x51\x4b\x50\x4b\x4f\x4d\x4d'\
b'\x4f\x4c\x4d\x4c\x4c\x49\x4c\x48\x4c\x47\x4e\x44\x51\x42\x53'\
b'\x42\x55\x42\x56\x43\x57\x43\x57\x43\x20\x52\x54\x43\x53\x43'\
b'\x52\x44\x51\x44\x50\x48\x50\x4a\x50\x4b\x51\x4c\x52\x4c\x52'\
b'\x4c\x53\x4b\x54\x4a\x55\x46\x55\x45\x55\x44\x54\x43\x54\x43'\
b'\x20\x52\x4e\x53\x4c\x53\x4b\x55\x4b\x56\x4b\x57\x4d\x59\x50'\
b'\x59\x52\x59\x54\x57\x54\x56\x54\x55\x52\x54\x50\x53\x4f\x53'\
b'\x4e\x53\x37\x47\x5d\x54\x3a\x50\x4a\x52\x46\x53\x45\x55\x43'\
b'\x57\x42\x58\x42\x59\x42\x5a\x44\x5a\x45\x5a\x46\x5a\x47\x58'\
b'\x4e\x57\x4f\x57\x4f\x57\x50\x58\x50\x58\x50\x58\x50\x58\x50'\
b'\x59\x4f\x59\x4e\x5a\x4e\x5a\x4e\x5b\x4e\x59\x50\x56\x52\x55'\
b'\x52\x54\x52\x53\x51\x53\x50\x53\x50\x53\x4e\x56\x47\x56\x46'\
b'\x56\x46\x56\x46\x55\x45\x55\x45\x55\x45\x54\x46\x51\x48\x4f'\
b'\x4d\x4e\x52\x49\x52\x4f\x3f\x4f\x3e\x4f\x3d\x4f\x3d\x4f\x3c'\
b'\x4f\x3c\x4e\x3c\x4e\x3b\x53\x3a\x54\x3a\x2c\x4b\x59\x54\x3a'\
b'\x55\x3a\x57\x3c\x57\x3d\x57\x3e\x55\x3f\x54\x3f\x53\x3f\x52'\
b'\x3e\x52\x3d\x52\x3c\x53\x3a\x54\x3a\x20\x52\x55\x42\x52\x4e'\
b'\x52\x4f\x52\x50\x52\x50\x52\x50\x52\x50\x52\x50\x53\x50\x53'\
b'\x4f\x54\x4e\x55\x4e\x52\x52\x50\x52\x4e\x52\x4d\x51\x4d\x50'\
b'\x4d\x50\x4d\x4f\x50\x47\x50\x45\x50\x45\x50\x44\x50\x44\x4f'\
b'\x44\x4f\x44\x4e\x44\x4f\x43\x54\x42\x55\x42\x34\x48\x5c\x57'\
b'\x3a\x59\x3a\x5a\x3c\x5a\x3d\x5a\x3e\x59\x3f\x57\x3f\x56\x3f'\
b'\x55\x3e\x55\x3d\x55\x3c\x56\x3a\x57\x3a\x20\x52\x59\x42\x55'\
b'\x50\x54\x54\x53\x56\x52\x58\x4f\x5a\x4d\x5a\x4b\x5a\x4a\x58'\
b'\x4a\x58\x4a\x57\x4b\x56\x4c\x56\x4d\x56\x4d\x57\x4d\x57\x4d'\
b'\x58\x4d\x58\x4d\x58\x4d\x58\x4d\x59\x4d\x59\x4d\x59\x4e\x59'\
b'\x4f\x58\x4f\x57\x50\x54\x53\x47\x54\x45\x54\x45\x54\x44\x53'\
b'\x44\x52\x44\x52\x44\x52\x44\x52\x43\x58\x42\x59\x42\x34\x47'\
b'\x5d\x54\x3a\x50\x4a\x54\x47\x55\x46\x55\x45\x56\x45\x56\x44'\
b'\x56\x44\x56\x44\x55\x43\x54\x43\x54\x43\x5b\x43\x5b\x43\x59'\
b'\x44\x59\x44\x58\x44\x57\x45\x56\x46\x55\x46\x55\x47\x56\x4c'\
b'\x56\x4f\x57\x4f\x57\x4f\x57\x4f\x58\x4f\x58\x4e\x59\x4e\x59'\
b'\x4d\x59\x4e\x58\x50\x56\x51\x55\x52\x55\x52\x54\x52\x53\x51'\
b'\x52\x4e\x51\x4a\x4f\x4c\x4d\x52\x49\x52\x4f\x3f\x4f\x3e\x4f'\
b'\x3d\x4f\x3d\x4f\x3c\x4e\x3c\x4d\x3c\x4d\x3b\x53\x3a\x54\x3a'\
b'\x1f\x4b\x59\x57\x3a\x52\x4e\x51\x4f\x51\x50\x51\x50\x51\x50'\
b'\x52\x50\x52\x50\x52\x50\x53\x4f\x54\x4e\x55\x4e\x53\x51\x51'\
b'\x52\x50\x52\x4f\x52\x4e\x52\x4d\x51\x4d\x50\x4d\x50\x4d\x4e'\
b'\x52\x3f\x52\x3d\x52\x3d\x52\x3d\x52\x3c\x51\x3c\x50\x3c\x51'\
b'\x3b\x56\x3a\x57\x3a\x52\x44\x60\x4e\x42\x4c\x4a\x4e\x46\x4f'\
b'\x45\x51\x43\x53\x42\x54\x42\x55\x42\x56\x44\x56\x44\x56\x45'\
b'\x56\x47\x55\x4a\x57\x46\x58\x45\x59\x43\x5b\x43\x5b\x42\x5c'\
b'\x42\x5d\x42\x5e\x43\x5e\x44\x5e\x45\x5e\x47\x5c\x4e\x5b\x4f'\
b'\x5b\x4f\x5b\x50\x5c\x50\x5c\x50\x5c\x50\x5c\x50\x5d\x4f\x5d'\
b'\x4e\x5e\x4e\x5e\x4e\x5e\x4e\x5d\x50\x5a\x52\x59\x52\x58\x52'\
b'\x57\x51\x57\x50\x57\x50\x57\x4e\x59\x47\x5a\x46\x5a\x46\x5a'\
b'\x46\x59\x45\x59\x45\x59\x45\x59\x45\x59\x46\x57\x47\x55\x4b'\
b'\x54\x4d\x53\x4e\x52\x52\x4e\x52\x51\x47\x51\x46\x51\x46\x51'\
b'\x46\x51\x45\x51\x45\x50\x45\x4f\x47\x4d\x4a\x4b\x4d\x4a\x52'\
b'\x46\x52\x49\x47\x49\x45\x49\x45\x49\x44\x49\x44\x48\x44\x47'\
b'\x44\x48\x43\x4d\x42\x4e\x42\x36\x47\x5d\x52\x42\x50\x4a\x52'\
b'\x46\x53\x45\x55\x43\x57\x42\x58\x42\x59\x42\x5a\x44\x5a\x45'\
b'\x5a\x46\x5a\x47\x58\x4e\x57\x4f\x57\x4f\x57\x50\x58\x50\x58'\
b'\x50\x58\x50\x58\x50\x59\x4f\x59\x4e\x5a\x4e\x5a\x4e\x5b\x4e'\
b'\x58\x52\x55\x52\x54\x52\x53\x51\x53\x50\x53\x50\x53\x4e\x56'\
b'\x47\x56\x46\x56\x46\x56\x46\x56\x45\x55\x45\x55\x45\x54\x46'\
b'\x51\x48\x4f\x4d\x4e\x52\x49\x52\x4d\x47\x4d\x45\x4d\x45\x4d'\
b'\x44\x4d\x44\x4c\x44\x4b\x44\x4c\x43\x51\x42\x52\x42\x24\x48'\
b'\x5c\x55\x42\x56\x42\x59\x43\x5a\x46\x5a\x47\x5a\x4a\x57\x4f'\
b'\x52\x52\x4f\x52\x4d\x52\x4a\x50\x4a\x4e\x4a\x4b\x4c\x47\x4f'\
b'\x44\x53\x42\x55\x42\x20\x52\x54\x43\x53\x43\x53\x44\x51\x45'\
b'\x4e\x4d\x4e\x50\x4e\x51\x4f\x52\x50\x52\x51\x52\x51\x51\x52'\
b'\x51\x54\x4c\x56\x47\x56\x45\x56\x44\x55\x43\x54\x43\x38\x46'\
b'\x5e\x4e\x43\x54\x42\x55\x42\x54\x45\x56\x43\x58\x42\x59\x42'\
b'\x5b\x42\x5c\x45\x5c\x46\x5c\x4b\x59\x4f\x56\x52\x52\x52\x52'\
b'\x52\x51\x52\x50\x52\x4f\x55\x4f\x57\x4f\x57\x4f\x58\x50\x59'\
b'\x51\x59\x51\x59\x48\x59\x48\x59\x49\x59\x4a\x57\x4b\x55\x4f'\
b'\x47\x50\x45\x50\x45\x50\x44\x4f\x44\x4f\x44\x4e\x44\x4e\x43'\
b'\x20\x52\x51\x50\x51\x51\x52\x52\x53\x52\x53\x52\x54\x51\x56'\
b'\x4f\x57\x4c\x58\x49\x58\x47\x58\x46\x57\x45\x56\x45\x56\x45'\
b'\x55\x45\x54\x45\x53\x47\x51\x50\x39\x48\x5c\x5a\x43\x55\x54'\
b'\x55\x56\x54\x56\x54\x57\x54\x57\x54\x58\x55\x58\x55\x59\x57'\
b'\x59\x56\x59\x4d\x59\x4d\x59\x4e\x59\x4f\x58\x50\x57\x51\x55'\
b'\x53\x4d\x51\x50\x4f\x52\x4e\x52\x4d\x52\x4c\x52\x4b\x52\x4a'\
b'\x50\x4a\x4e\x4a\x4c\x4c\x47\x4f\x44\x51\x43\x52\x42\x53\x42'\
b'\x54\x42\x55\x43\x55\x45\x56\x43\x5a\x43\x20\x52\x53\x43\x53'\
b'\x43\x52\x44\x51\x45\x50\x48\x4e\x4b\x4e\x4e\x4e\x4e\x4f\x4f'\
b'\x4f\x4f\x4f\x4f\x50\x4f\x51\x4f\x52\x4d\x55\x48\x55\x46\x55'\
b'\x44\x54\x43\x53\x43\x23\x49\x5b\x53\x42\x50\x4c\x54\x45\x55'\
b'\x43\x56\x42\x57\x42\x58\x42\x59\x43\x59\x44\x59\x46\x58\x47'\
b'\x57\x48\x57\x48\x56\x48\x55\x46\x55\x46\x55\x46\x55\x46\x55'\
b'\x46\x54\x47\x53\x48\x51\x4c\x50\x4e\x4f\x52\x4b\x52\x4e\x47'\
b'\x4e\x45\x4e\x45\x4e\x45\x4e\x44\x4e\x44\x4d\x44\x4d\x43\x52'\
b'\x42\x53\x42\x35\x49\x5b\x59\x42\x58\x47\x57\x47\x57\x45\x55'\
b'\x43\x53\x43\x53\x43\x52\x44\x52\x45\x52\x45\x52\x46\x53\x47'\
b'\x56\x4a\x57\x4c\x57\x4d\x57\x4f\x55\x51\x53\x52\x51\x52\x50'\
b'\x52\x4f\x52\x4e\x52\x4d\x52\x4d\x52\x4c\x52\x4c\x52\x4b\x52'\
b'\x4c\x4d\x4d\x4d\x4d\x4f\x4f\x51\x50\x52\x51\x52\x52\x52\x53'\
b'\x50\x53\x50\x53\x4f\x52\x4d\x51\x4c\x4f\x4a\x4e\x48\x4e\x48'\
b'\x4e\x46\x4e\x45\x51\x42\x53\x42\x54\x42\x56\x43\x56\x43\x57'\
b'\x43\x57\x43\x58\x42\x59\x42\x1f\x4b\x59\x56\x3e\x55\x43\x57'\
b'\x43\x57\x45\x54\x45\x51\x4f\x51\x4f\x51\x50\x51\x50\x51\x50'\
b'\x52\x50\x52\x50\x52\x50\x53\x50\x54\x4e\x55\x4f\x54\x51\x51'\
b'\x52\x4f\x52\x4e\x52\x4d\x51\x4d\x50\x4d\x4f\x4d\x4e\x50\x45'\
b'\x4e\x45\x4e\x43\x50\x43\x53\x40\x55\x3e\x56\x3e\x35\x48\x5c'\
b'\x52\x42\x4e\x4e\x4e\x4f\x4e\x4f\x4e\x4f\x4e\x4f\x4e\x4f\x4f'\
b'\x4f\x4f\x4f\x51\x4e\x53\x4c\x55\x48\x56\x43\x5a\x43\x57\x4e'\
b'\x57\x4f\x57\x50\x57\x50\x57\x50\x57\x50\x57\x50\x58\x50\x58'\
b'\x4f\x59\x4e\x5a\x4e\x57\x52\x55\x52\x54\x52\x52\x51\x52\x51'\
b'\x52\x50\x53\x4e\x54\x4b\x51\x4f\x50\x50\x4f\x51\x4d\x52\x4c'\
b'\x52\x4b\x52\x4a\x51\x4a\x50\x4a\x4f\x4a\x4e\x4c\x47\x4c\x45'\
b'\x4c\x45\x4c\x44\x4c\x44\x4b\x44\x4b\x44\x4b\x43\x51\x42\x52'\
b'\x42\x25\x49\x5b\x4f\x52\x4e\x52\x4e\x51\x4e\x50\x4e\x4e\x4d'\
b'\x47\x4d\x46\x4d\x45\x4c\x45\x4c\x44\x4b\x44\x4b\x44\x4b\x44'\
b'\x4b\x44\x50\x42\x52\x47\x52\x4e\x55\x4c\x56\x49\x56\x48\x56'\
b'\x47\x55\x45\x55\x45\x55\x44\x55\x43\x56\x42\x57\x42\x58\x42'\
b'\x59\x43\x59\x44\x59\x45\x59\x46\x58\x48\x56\x4b\x55\x4d\x53'\
b'\x4f\x4f\x52\x2c\x45\x5f\x55\x42\x56\x4e\x59\x4c\x5a\x49\x5a'\
b'\x48\x5a\x47\x5a\x47\x59\x45\x59\x45\x59\x45\x59\x44\x59\x43'\
b'\x5a\x42\x5b\x42\x5c\x42\x5c\x43\x5d\x44\x5d\x45\x5d\x47\x59'\
b'\x4d\x53\x52\x52\x52\x51\x48\x4a\x52\x49\x52\x49\x4e\x49\x4a'\
b'\x49\x47\x49\x46\x49\x45\x48\x44\x48\x44\x47\x44\x47\x44\x47'\
b'\x44\x4d\x42\x4d\x44\x4d\x45\x4e\x47\x4e\x49\x4e\x4a\x4e\x4c'\
b'\x54\x42\x55\x42\x42\x46\x5e\x4c\x43\x51\x42\x53\x45\x54\x48'\
b'\x55\x45\x56\x44\x57\x43\x59\x42\x5a\x42\x5b\x42\x5c\x43\x5c'\
b'\x44\x5c\x45\x5b\x46\x5a\x46\x59\x46\x58\x46\x58\x46\x57\x46'\
b'\x56\x46\x55\x47\x54\x49\x56\x4e\x56\x4f\x57\x50\x57\x50\x58'\
b'\x50\x58\x50\x59\x4f\x5a\x4e\x5a\x4e\x59\x51\x57\x52\x56\x52'\
b'\x55\x52\x54\x52\x53\x52\x52\x4f\x51\x4d\x4f\x4f\x4d\x52\x4b'\
b'\x52\x4a\x52\x49\x52\x48\x51\x48\x51\x48\x50\x49\x4f\x4a\x4f'\
b'\x4b\x4f\x4b\x4f\x4c\x4f\x4d\x4f\x4d\x4f\x4d\x4f\x4e\x4f\x4f'\
b'\x4e\x4f\x4d\x51\x4c\x4f\x46\x4e\x45\x4d\x44\x4d\x44\x4c\x44'\
b'\x4b\x44\x4c\x43\x3a\x47\x5d\x4d\x44\x52\x42\x53\x43\x53\x44'\
b'\x53\x45\x54\x47\x54\x4b\x54\x50\x56\x4e\x58\x4a\x59\x48\x59'\
b'\x47\x59\x47\x57\x46\x57\x45\x57\x44\x57\x43\x58\x42\x59\x42'\
b'\x5a\x42\x5b\x44\x5b\x45\x5b\x46\x5a\x49\x58\x4c\x55\x51\x52'\
b'\x55\x50\x57\x4e\x59\x4c\x59\x4c\x5a\x4b\x5a\x4a\x5a\x49\x58'\
b'\x49\x57\x49\x56\x4a\x55\x4b\x55\x4c\x55\x4d\x56\x4d\x57\x4e'\
b'\x57\x4e\x57\x4e\x57\x4f\x56\x50\x55\x50\x53\x50\x52\x50\x51'\
b'\x50\x4e\x4f\x48\x4f\x46\x4f\x45\x4e\x44\x4d\x44\x4d\x44\x4d'\
b'\x44\x4d\x44\x29\x49\x5b\x59\x43\x4f\x4e\x51\x4e\x51\x4f\x52'\
b'\x50\x52\x53\x53\x54\x54\x54\x54\x54\x54\x54\x54\x53\x54\x53'\
b'\x54\x52\x54\x52\x54\x51\x54\x50\x55\x4f\x56\x4f\x57\x4f\x58'\
b'\x50\x58\x51\x58\x53\x55\x55\x53\x55\x51\x55\x4f\x53\x4e\x52'\
b'\x4e\x52\x4d\x52\x4d\x52\x4c\x52\x4c\x52\x4b\x52\x55\x46\x51'\
b'\x46\x50\x46\x4e\x47\x4e\x48\x4d\x48\x4e\x43\x59\x43\x2a\x49'\
b'\x5b\x59\x3a\x59\x3b\x57\x3b\x55\x3d\x54\x3f\x54\x44\x53\x46'\
b'\x51\x48\x50\x49\x4f\x49\x4d\x4a\x4f\x4a\x50\x4b\x51\x4c\x51'\
b'\x4e\x51\x4f\x4e\x55\x4e\x56\x4e\x57\x4f\x58\x51\x58\x50\x59'\
b'\x4f\x59\x4e\x59\x4c\x58\x4b\x56\x4b\x55\x4b\x53\x4e\x4e\x4e'\
b'\x4d\x4e\x4c\x4d\x4a\x4b\x4a\x4c\x49\x4d\x49\x4f\x47\x50\x45'\
b'\x50\x40\x51\x3e\x54\x3c\x57\x3a\x59\x3a\x05\x4f\x55\x51\x5a'\
b'\x51\x3a\x53\x3a\x53\x5a\x51\x5a\x2a\x49\x5b\x4b\x59\x4b\x58'\
b'\x4d\x58\x4f\x57\x50\x54\x50\x50\x51\x4d\x53\x4b\x54\x4b\x55'\
b'\x4a\x57\x4a\x55\x49\x54\x48\x53\x47\x53\x45\x53\x44\x56\x3f'\
b'\x56\x3e\x56\x3d\x55\x3b\x53\x3b\x54\x3a\x55\x3a\x56\x3b\x58'\
b'\x3b\x59\x3d\x59\x3f\x59\x40\x56\x45\x56\x47\x56\x48\x57\x49'\
b'\x59\x49\x58\x4a\x57\x4a\x55\x4c\x54\x4e\x54\x53\x53\x55\x50'\
b'\x58\x4d\x59\x4b\x59\x1c\x47\x5d\x5a\x46\x5b\x46\x5b\x49\x59'\
b'\x4b\x57\x4b\x56\x4b\x54\x4b\x50\x49\x4e\x48\x4d\x48\x4c\x48'\
b'\x4a\x4a\x4a\x4b\x49\x4b\x49\x49\x4b\x46\x4d\x46\x4e\x46\x4f'\
b'\x46\x51\x47\x54\x48\x55\x49\x56\x49\x57\x49\x57\x49\x59\x49'\
b'\x5a\x47\x5a\x46\x0b\x47\x5d\x49\x52\x49\x3c\x5b\x3c\x5b\x52'\
b'\x49\x52\x20\x52\x4a\x51\x5a\x51\x5a\x3d\x4a\x3d\x4a\x51'

_index =\
b'\x00\x00\x03\x00\x3e\x00\x7b\x00\xc4\x00\x49\x01\xea\x01\x99'\
b'\x02\xb4\x02\xdb\x02\x04\x03\xa1\x03\xbe\x03\xe9\x03\xf6\x03'\
b'\x13\x04\x20\x04\x83\x04\xbe\x04\x01\x05\x6e\x05\x93\x05\xdc'\
b'\x05\x39\x06\x54\x06\xd3\x06\x2e\x07\x67\x07\xae\x07\xc1\x07'\
b'\xda\x07\xed\x07\x58\x08\x0f\x09\x62\x09\xd1\x09\x1a\x0a\x6f'\
b'\x0a\xd6\x0a\x33\x0b\x98\x0b\x07\x0c\x3e\x0c\x8d\x0c\x0a\x0d'\
b'\x47\x0d\xa0\x0d\xed\x0d\x3a\x0e\x97\x0e\x12\x0f\x7b\x0f\xea'\
b'\x0f\x23\x10\x88\x10\xc7\x10\x2c\x11\xa3\x11\x00\x12\x29\x12'\
b'\x56\x12\x63\x12\x90\x12\xa3\x12\xb0\x12\xbd\x12\x36\x13\x8d'\
b'\x13\xe4\x13\x67\x14\xc2\x14\x39\x15\xec\x15\x5d\x16\xb8\x16'\
b'\x23\x17\x8e\x17\xcf\x17\x76\x18\xe5\x18\x30\x19\xa3\x19\x18'\
b'\x1a\x61\x1a\xce\x1a\x0f\x1b\x7c\x1b\xc9\x1b\x24\x1c\xab\x1c'\
b'\x22\x1d\x77\x1d\xce\x1d\xdb\x1d\x32\x1e\x6d\x1e'

FONT = memoryview(_font)
INDEX = memoryview(_index)

