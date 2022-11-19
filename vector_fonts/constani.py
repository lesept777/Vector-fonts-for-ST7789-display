FIRST = 32
LAST = 127
WIDTH = 44
HEIGHT = 43

_font =\
b'\x01\x4d\x57\x14\x4b\x59\x50\x4a\x52\x36\x57\x35\x57\x36\x51'\
b'\x4a\x50\x4a\x20\x52\x4f\x4e\x51\x4e\x52\x4f\x52\x50\x52\x51'\
b'\x50\x53\x4f\x53\x4e\x53\x4d\x51\x4d\x50\x4d\x4f\x4e\x4e\x4f'\
b'\x4e\x0b\x4a\x5a\x4d\x33\x51\x33\x4e\x3d\x4c\x3d\x4d\x33\x20'\
b'\x52\x54\x33\x58\x33\x54\x3d\x53\x3d\x54\x33\x23\x45\x5f\x4c'\
b'\x52\x49\x52\x4b\x4a\x47\x4a\x47\x48\x4c\x48\x4d\x42\x49\x42'\
b'\x49\x3f\x4e\x3f\x50\x37\x52\x37\x50\x3f\x56\x3f\x58\x37\x5a'\
b'\x37\x59\x3f\x5d\x3f\x5d\x42\x58\x42\x57\x48\x5b\x48\x5b\x4a'\
b'\x56\x4a\x54\x52\x52\x52\x54\x4a\x4e\x4a\x4c\x52\x20\x52\x4e'\
b'\x48\x54\x48\x56\x42\x50\x42\x4e\x48\x37\x46\x5e\x50\x55\x4f'\
b'\x55\x4f\x53\x4c\x52\x48\x52\x48\x51\x4a\x4b\x4b\x4b\x4b\x50'\
b'\x4d\x51\x50\x51\x51\x48\x4e\x47\x4c\x44\x4c\x42\x4c\x40\x50'\
b'\x3c\x54\x3c\x54\x39\x56\x39\x55\x3c\x58\x3c\x5c\x3c\x5c\x3d'\
b'\x5a\x42\x59\x42\x59\x3e\x57\x3d\x55\x3d\x53\x45\x57\x47\x5a'\
b'\x4a\x5a\x4c\x5a\x4f\x55\x52\x51\x53\x50\x55\x20\x52\x56\x4d'\
b'\x56\x4c\x55\x4a\x53\x49\x51\x51\x53\x51\x56\x4f\x56\x4d\x20'\
b'\x52\x4f\x41\x4f\x42\x51\x44\x52\x45\x54\x3d\x51\x3e\x4f\x40'\
b'\x4f\x41\x5d\x40\x64\x45\x3f\x45\x41\x47\x43\x48\x43\x49\x43'\
b'\x4b\x42\x4c\x41\x4d\x3e\x4d\x3c\x4d\x39\x4d\x38\x4d\x36\x4c'\
b'\x34\x4b\x34\x4a\x34\x48\x35\x47\x37\x46\x39\x46\x3c\x45\x3e'\
b'\x45\x3f\x20\x52\x50\x39\x50\x3b\x50\x3d\x4f\x40\x4d\x42\x4c'\
b'\x44\x49\x45\x48\x45\x45\x45\x42\x41\x42\x3e\x42\x3d\x43\x3a'\
b'\x44\x38\x45\x35\x47\x34\x49\x33\x4b\x33\x4d\x33\x50\x36\x50'\
b'\x39\x20\x52\x44\x52\x5e\x33\x5f\x34\x45\x53\x44\x52\x20\x52'\
b'\x57\x4d\x57\x4f\x58\x51\x59\x51\x5a\x51\x5c\x50\x5d\x4e\x5e'\
b'\x4c\x5e\x49\x5f\x47\x5f\x46\x5f\x44\x5d\x42\x5c\x42\x5b\x42'\
b'\x59\x43\x58\x45\x57\x47\x57\x49\x57\x4c\x57\x4d\x20\x52\x62'\
b'\x47\x62\x48\x61\x4b\x60\x4e\x5f\x50\x5d\x51\x5b\x52\x59\x52'\
b'\x57\x52\x54\x4f\x54\x4c\x54\x4b\x54\x48\x55\x45\x57\x43\x58'\
b'\x42\x5b\x41\x5c\x41\x5f\x41\x62\x44\x62\x47\x50\x40\x64\x50'\
b'\x49\x50\x48\x50\x47\x50\x46\x54\x42\x56\x42\x57\x42\x59\x43'\
b'\x5a\x43\x5b\x43\x5d\x44\x5e\x44\x5f\x44\x61\x42\x62\x43\x60'\
b'\x45\x5e\x46\x5d\x46\x5c\x46\x59\x45\x59\x46\x5a\x47\x5a\x49'\
b'\x5a\x4b\x58\x4e\x54\x51\x50\x53\x4d\x53\x48\x53\x42\x4e\x42'\
b'\x4a\x42\x47\x46\x43\x4a\x42\x4a\x42\x47\x3f\x47\x3c\x47\x39'\
b'\x4d\x35\x51\x35\x54\x35\x57\x36\x57\x36\x55\x3c\x54\x3c\x54'\
b'\x37\x52\x37\x51\x37\x4e\x37\x4b\x3a\x4b\x3c\x4b\x40\x50\x41'\
b'\x50\x43\x4f\x43\x4e\x43\x4a\x43\x46\x46\x46\x49\x46\x4d\x4b'\
b'\x50\x4e\x50\x50\x50\x54\x4f\x56\x4d\x58\x4b\x58\x49\x58\x48'\
b'\x57\x46\x56\x45\x55\x44\x55\x44\x53\x44\x52\x46\x52\x46\x52'\
b'\x47\x53\x48\x53\x48\x52\x49\x50\x49\x05\x4e\x56\x51\x33\x54'\
b'\x33\x51\x3d\x50\x3d\x51\x33\x0b\x48\x5c\x51\x5a\x4a\x53\x4a'\
b'\x4a\x4a\x3b\x59\x31\x5a\x32\x4e\x3c\x4e\x4b\x4e\x54\x51\x59'\
b'\x51\x5a\x0b\x48\x5c\x53\x31\x5a\x38\x5a\x41\x5a\x50\x4b\x5a'\
b'\x4a\x59\x56\x4f\x56\x40\x56\x37\x53\x32\x53\x31\x10\x49\x5b'\
b'\x55\x34\x52\x3b\x59\x39\x59\x3c\x52\x3c\x56\x41\x53\x43\x51'\
b'\x3c\x4d\x41\x4b\x3f\x51\x3b\x4b\x39\x4c\x36\x51\x3a\x52\x34'\
b'\x55\x34\x0d\x46\x5e\x48\x47\x51\x47\x51\x3e\x53\x3e\x53\x47'\
b'\x5c\x47\x5c\x4a\x53\x4a\x53\x52\x51\x52\x51\x4a\x48\x4a\x48'\
b'\x47\x0e\x4d\x57\x4f\x57\x52\x54\x52\x52\x52\x50\x50\x4f\x50'\
b'\x4e\x52\x4c\x53\x4c\x54\x4c\x55\x4e\x55\x4f\x55\x54\x4f\x58'\
b'\x4f\x57\x05\x4a\x5a\x4d\x46\x58\x46\x57\x49\x4c\x49\x4d\x46'\
b'\x0d\x4e\x56\x52\x4e\x53\x4e\x54\x4f\x54\x50\x54\x51\x53\x53'\
b'\x52\x53\x51\x53\x50\x51\x50\x50\x50\x4f\x51\x4e\x52\x4e\x05'\
b'\x48\x5c\x4a\x57\x57\x34\x5a\x34\x4d\x57\x4a\x57\x1b\x46\x5e'\
b'\x53\x3e\x57\x3e\x5c\x43\x5c\x47\x5c\x4c\x56\x53\x51\x53\x4d'\
b'\x53\x48\x4e\x48\x4a\x48\x45\x4e\x3e\x53\x3e\x20\x52\x53\x40'\
b'\x50\x40\x4c\x46\x4c\x4a\x4c\x4d\x4f\x51\x51\x51\x54\x51\x58'\
b'\x4b\x58\x47\x58\x43\x55\x40\x53\x40\x1c\x4a\x5a\x4f\x40\x4f'\
b'\x3f\x53\x3f\x58\x3e\x58\x3e\x57\x42\x56\x46\x55\x4b\x54\x4e'\
b'\x54\x50\x54\x50\x55\x50\x58\x51\x58\x52\x54\x52\x52\x52\x50'\
b'\x52\x4c\x52\x4c\x51\x50\x50\x50\x50\x50\x50\x51\x4e\x51\x4c'\
b'\x52\x48\x53\x44\x53\x41\x4f\x40\x21\x47\x5d\x5a\x4b\x5b\x4b'\
b'\x59\x52\x59\x52\x56\x52\x51\x52\x4c\x52\x49\x52\x49\x50\x4c'\
b'\x4e\x51\x4b\x54\x48\x56\x46\x56\x44\x56\x43\x53\x41\x52\x41'\
b'\x4f\x41\x4d\x42\x4c\x41\x50\x3e\x54\x3e\x56\x3e\x5a\x41\x5a'\
b'\x44\x5a\x45\x59\x48\x56\x4a\x51\x4d\x4e\x4f\x4e\x4f\x58\x4f'\
b'\x5a\x4b\x2b\x46\x5e\x4f\x4b\x53\x4b\x58\x47\x58\x45\x58\x43'\
b'\x55\x41\x53\x41\x50\x41\x4d\x42\x4d\x41\x51\x3e\x55\x3e\x58'\
b'\x3e\x5c\x41\x5c\x43\x5c\x46\x57\x4a\x54\x4b\x54\x4b\x57\x4b'\
b'\x5b\x4e\x5b\x51\x5b\x53\x5a\x56\x57\x58\x53\x5a\x4f\x5b\x4a'\
b'\x5c\x48\x5c\x48\x5a\x4a\x5a\x4e\x5a\x51\x59\x54\x57\x56\x55'\
b'\x57\x53\x57\x51\x57\x4f\x54\x4c\x52\x4c\x50\x4c\x4f\x4d\x4f'\
b'\x4b\x27\x46\x5e\x54\x4f\x55\x48\x59\x47\x58\x4f\x5c\x4f\x5c'\
b'\x51\x5a\x51\x57\x51\x56\x54\x56\x56\x56\x59\x55\x5a\x54\x5b'\
b'\x52\x5b\x52\x5b\x52\x59\x52\x56\x53\x55\x53\x51\x4e\x51\x4d'\
b'\x51\x4a\x51\x48\x51\x48\x50\x4a\x4d\x4e\x49\x53\x44\x57\x40'\
b'\x58\x3e\x5b\x3e\x5b\x3e\x5a\x3f\x57\x42\x54\x45\x52\x48\x4f'\
b'\x4b\x4c\x4e\x4c\x4f\x54\x4f\x1e\x46\x5e\x48\x5c\x48\x5a\x4b'\
b'\x5a\x50\x59\x54\x56\x57\x53\x57\x51\x57\x4e\x52\x4a\x4d\x4a'\
b'\x4d\x49\x50\x3f\x52\x3f\x56\x3f\x5a\x3f\x5c\x3f\x5c\x3f\x5b'\
b'\x42\x51\x42\x4f\x47\x55\x47\x5b\x4c\x5b\x50\x5b\x52\x59\x55'\
b'\x57\x57\x53\x59\x4f\x5b\x4a\x5c\x48\x5c\x25\x46\x5e\x5c\x36'\
b'\x51\x38\x4d\x43\x4d\x43\x4f\x40\x53\x40\x56\x40\x5b\x44\x5b'\
b'\x48\x5b\x4c\x54\x53\x50\x53\x4c\x53\x48\x4e\x48\x49\x48\x47'\
b'\x49\x43\x4b\x3e\x4f\x3a\x53\x37\x59\x35\x5c\x35\x5c\x36\x20'\
b'\x52\x56\x48\x56\x45\x54\x42\x52\x42\x4f\x42\x4b\x47\x4b\x4b'\
b'\x4b\x4d\x4e\x51\x50\x51\x53\x51\x56\x4c\x56\x48\x18\x46\x5e'\
b'\x48\x5a\x58\x42\x4b\x42\x49\x46\x49\x46\x4a\x3f\x4a\x3f\x4c'\
b'\x3f\x51\x3f\x53\x3f\x54\x3f\x56\x3f\x5a\x3f\x5c\x3f\x5c\x3f'\
b'\x5a\x42\x57\x46\x54\x4b\x52\x50\x4f\x55\x4d\x59\x4c\x5a\x48'\
b'\x5b\x48\x5a\x34\x45\x5f\x4c\x3d\x4c\x39\x51\x35\x55\x35\x58'\
b'\x35\x5d\x38\x5d\x3b\x5d\x3d\x59\x41\x55\x43\x59\x45\x5b\x48'\
b'\x5b\x4a\x5b\x4e\x55\x53\x50\x53\x4c\x53\x47\x4f\x47\x4c\x47'\
b'\x49\x4c\x45\x50\x43\x4e\x42\x4c\x3f\x4c\x3d\x20\x52\x4b\x4b'\
b'\x4b\x4e\x4f\x51\x51\x51\x54\x51\x57\x4e\x57\x4b\x57\x49\x55'\
b'\x46\x51\x44\x4e\x45\x4b\x49\x4b\x4b\x20\x52\x59\x3b\x59\x39'\
b'\x56\x37\x54\x37\x52\x37\x4f\x3a\x4f\x3c\x4f\x3d\x52\x40\x54'\
b'\x42\x59\x3f\x59\x3b\x25\x46\x5e\x48\x5a\x53\x59\x57\x4e\x57'\
b'\x4e\x55\x51\x51\x51\x4e\x51\x49\x4c\x49\x49\x49\x45\x50\x3e'\
b'\x54\x3e\x58\x3e\x5c\x43\x5c\x47\x5c\x4a\x5b\x4e\x59\x52\x55'\
b'\x56\x51\x59\x4b\x5b\x48\x5c\x48\x5a\x20\x52\x4e\x49\x4e\x4c'\
b'\x50\x4f\x52\x4f\x55\x4f\x59\x4a\x59\x46\x59\x43\x56\x40\x54'\
b'\x40\x51\x40\x4e\x45\x4e\x49\x1b\x4c\x58\x50\x4e\x52\x4e\x53'\
b'\x4f\x53\x50\x53\x51\x52\x53\x50\x53\x4f\x53\x4e\x51\x4e\x50'\
b'\x4e\x4f\x4f\x4e\x50\x4e\x20\x52\x53\x3f\x55\x3f\x56\x40\x56'\
b'\x41\x56\x42\x54\x44\x53\x44\x52\x44\x51\x42\x51\x41\x51\x40'\
b'\x52\x3f\x53\x3f\x1c\x4c\x58\x4e\x57\x51\x54\x51\x52\x51\x50'\
b'\x4f\x4f\x4f\x4e\x51\x4c\x52\x4c\x53\x4c\x54\x4e\x54\x4f\x54'\
b'\x54\x4e\x58\x4e\x57\x20\x52\x54\x3f\x55\x3f\x56\x40\x56\x41'\
b'\x56\x42\x55\x44\x54\x44\x53\x44\x52\x42\x52\x41\x52\x40\x53'\
b'\x3f\x54\x3f\x08\x46\x5e\x48\x47\x5c\x3f\x5c\x41\x4b\x48\x5c'\
b'\x4f\x5c\x52\x48\x4a\x48\x47\x0b\x46\x5e\x48\x44\x5c\x44\x5c'\
b'\x46\x48\x46\x48\x44\x20\x52\x48\x4b\x5c\x4b\x5c\x4d\x48\x4d'\
b'\x48\x4b\x08\x46\x5e\x5c\x4a\x48\x52\x48\x4f\x59\x48\x48\x41'\
b'\x48\x3f\x5c\x47\x5c\x4a\x35\x49\x5b\x4f\x4a\x4c\x47\x4c\x45'\
b'\x4c\x45\x4d\x43\x4e\x42\x50\x41\x51\x40\x52\x3f\x54\x3e\x55'\
b'\x3c\x56\x3b\x56\x3a\x56\x38\x54\x37\x52\x37\x50\x37\x4f\x37'\
b'\x4d\x3c\x4c\x3c\x4c\x36\x50\x35\x53\x35\x56\x35\x59\x37\x59'\
b'\x3a\x59\x3b\x58\x3e\x57\x40\x55\x41\x54\x42\x53\x43\x51\x44'\
b'\x50\x45\x4f\x47\x4f\x47\x4f\x48\x50\x49\x4f\x4a\x20\x52\x4d'\
b'\x4e\x4e\x4e\x50\x4f\x50\x50\x50\x51\x4e\x53\x4d\x53\x4c\x53'\
b'\x4b\x51\x4b\x50\x4b\x4f\x4c\x4e\x4d\x4e\x4c\x40\x64\x54\x4e'\
b'\x51\x51\x4f\x51\x4d\x51\x4a\x4e\x4a\x4b\x4a\x46\x50\x40\x54'\
b'\x40\x56\x40\x58\x40\x59\x40\x5a\x40\x5b\x40\x5a\x41\x5a\x44'\
b'\x59\x46\x58\x4d\x58\x4d\x58\x4e\x58\x4f\x59\x4f\x59\x4f\x5a'\
b'\x4f\x5c\x4d\x5e\x4c\x5f\x49\x60\x46\x60\x44\x60\x3f\x5a\x3a'\
b'\x56\x3a\x4e\x3a\x45\x44\x45\x4b\x45\x50\x4c\x57\x51\x57\x59'\
b'\x57\x5f\x52\x5f\x53\x5c\x56\x54\x5a\x50\x5a\x4a\x5a\x42\x52'\
b'\x42\x4b\x42\x44\x4d\x39\x56\x39\x5b\x39\x62\x3f\x62\x44\x62'\
b'\x46\x61\x4a\x5f\x4d\x5d\x4f\x5b\x50\x58\x51\x57\x51\x56\x51'\
b'\x54\x50\x54\x4e\x20\x52\x57\x42\x55\x41\x54\x41\x52\x41\x4e'\
b'\x47\x4e\x4a\x4e\x4c\x4f\x4f\x50\x4f\x52\x4f\x54\x4d\x57\x42'\
b'\x30\x41\x63\x4c\x51\x4c\x52\x49\x52\x47\x52\x45\x52\x43\x52'\
b'\x43\x51\x45\x51\x46\x50\x47\x50\x47\x4f\x48\x4f\x48\x4e\x57'\
b'\x35\x59\x34\x5d\x4e\x5e\x4f\x5e\x50\x5e\x50\x5f\x51\x61\x51'\
b'\x61\x52\x5e\x52\x5c\x52\x59\x52\x56\x52\x56\x51\x58\x51\x59'\
b'\x50\x59\x50\x59\x4f\x59\x4f\x59\x4d\x58\x47\x4e\x47\x4b\x4d'\
b'\x4a\x4e\x4a\x50\x4a\x50\x4a\x50\x4a\x50\x4a\x51\x4c\x51\x20'\
b'\x52\x58\x45\x56\x3a\x4f\x45\x58\x45\x3e\x44\x60\x4b\x35\x4e'\
b'\x35\x51\x35\x51\x35\x55\x35\x55\x35\x5a\x35\x5e\x38\x5e\x3b'\
b'\x5e\x41\x57\x42\x5d\x44\x5d\x49\x5d\x4d\x56\x52\x50\x52\x4f'\
b'\x52\x4c\x52\x4b\x52\x48\x52\x46\x52\x46\x51\x49\x50\x49\x50'\
b'\x49\x50\x49\x4f\x4a\x4d\x4a\x4c\x4d\x3b\x4e\x3a\x4e\x38\x4e'\
b'\x37\x4e\x37\x4e\x36\x4b\x36\x4b\x35\x20\x52\x50\x43\x4d\x50'\
b'\x4e\x51\x50\x51\x54\x51\x58\x4d\x58\x49\x58\x46\x55\x43\x52'\
b'\x43\x51\x43\x50\x43\x20\x52\x50\x42\x51\x42\x52\x42\x56\x42'\
b'\x5a\x3e\x5a\x3b\x5a\x39\x57\x36\x54\x36\x53\x36\x52\x36\x50'\
b'\x42\x1a\x43\x61\x5d\x3c\x5c\x3c\x5b\x37\x59\x36\x57\x36\x51'\
b'\x36\x49\x3f\x49\x46\x49\x4b\x4f\x50\x54\x50\x57\x50\x5a\x4f'\
b'\x5b\x50\x56\x53\x51\x53\x4c\x53\x45\x4c\x45\x46\x45\x3e\x50'\
b'\x34\x58\x34\x5b\x34\x5f\x35\x5f\x35\x5d\x3c\x2d\x41\x63\x48'\
b'\x52\x45\x52\x43\x52\x43\x51\x45\x50\x46\x50\x46\x50\x46\x4f'\
b'\x47\x4d\x47\x4c\x4a\x3b\x4a\x3a\x4b\x38\x4b\x37\x4b\x37\x4a'\
b'\x36\x48\x36\x48\x35\x4b\x35\x4d\x35\x4f\x35\x53\x35\x54\x35'\
b'\x5a\x35\x61\x3a\x61\x40\x61\x48\x57\x52\x4e\x52\x4d\x52\x49'\
b'\x52\x48\x52\x20\x52\x4a\x50\x4c\x50\x4f\x50\x55\x50\x5d\x47'\
b'\x5d\x40\x5d\x3b\x58\x36\x53\x36\x52\x36\x4f\x36\x4a\x50\x3a'\
b'\x43\x61\x50\x35\x55\x35\x59\x35\x5f\x35\x5f\x35\x5c\x3b\x5b'\
b'\x3b\x5b\x37\x52\x37\x4f\x42\x52\x42\x53\x42\x56\x42\x56\x42'\
b'\x57\x42\x58\x3f\x59\x3f\x58\x42\x58\x43\x58\x44\x57\x47\x56'\
b'\x47\x56\x44\x56\x44\x55\x44\x54\x44\x51\x44\x4f\x44\x4e\x4c'\
b'\x4d\x4e\x4d\x50\x57\x50\x5a\x4b\x5b\x4b\x59\x52\x59\x52\x54'\
b'\x52\x4f\x52\x4b\x52\x48\x52\x45\x52\x45\x51\x48\x50\x49\x50'\
b'\x49\x50\x49\x4f\x49\x4d\x4a\x4c\x4d\x3b\x4d\x3a\x4d\x38\x4d'\
b'\x37\x4e\x37\x4d\x36\x4b\x36\x4b\x35\x4d\x35\x50\x35\x37\x43'\
b'\x61\x4e\x4c\x4d\x4e\x4d\x50\x4d\x50\x4d\x50\x50\x51\x50\x52'\
b'\x4d\x52\x4b\x52\x48\x52\x45\x52\x45\x51\x48\x50\x49\x50\x49'\
b'\x50\x49\x4e\x4a\x4c\x4d\x3b\x4d\x3a\x4d\x38\x4d\x37\x4e\x37'\
b'\x4d\x36\x4b\x36\x4b\x35\x4d\x35\x50\x35\x55\x35\x59\x35\x5f'\
b'\x35\x5f\x35\x5c\x3b\x5b\x3b\x5b\x37\x52\x37\x4f\x43\x51\x43'\
b'\x53\x43\x56\x43\x56\x43\x57\x42\x58\x3f\x59\x3f\x58\x42\x58'\
b'\x43\x58\x45\x57\x48\x56\x48\x56\x45\x56\x44\x56\x44\x53\x44'\
b'\x51\x44\x4f\x44\x4e\x4c\x2e\x43\x61\x5d\x3c\x5c\x3c\x5b\x37'\
b'\x59\x36\x57\x36\x51\x36\x49\x3f\x49\x46\x49\x4b\x4f\x51\x53'\
b'\x51\x54\x51\x56\x51\x57\x4b\x57\x4a\x57\x48\x58\x47\x58\x47'\
b'\x57\x47\x55\x46\x55\x45\x58\x45\x5a\x45\x5d\x45\x5f\x45\x5f'\
b'\x46\x5c\x47\x5c\x47\x5c\x47\x5c\x48\x5b\x4a\x5b\x4b\x5a\x51'\
b'\x5a\x52\x56\x53\x52\x53\x4c\x53\x45\x4c\x45\x46\x45\x3e\x4f'\
b'\x34\x58\x34\x5b\x34\x5f\x35\x5f\x35\x5d\x3c\x49\x3f\x65\x4b'\
b'\x43\x49\x4c\x49\x4e\x48\x50\x48\x50\x49\x50\x4b\x51\x4b\x52'\
b'\x48\x52\x46\x52\x43\x52\x41\x52\x41\x51\x43\x50\x44\x50\x44'\
b'\x50\x44\x4e\x45\x4c\x48\x3b\x49\x38\x49\x37\x49\x37\x48\x36'\
b'\x46\x36\x46\x35\x49\x35\x4b\x35\x4e\x35\x50\x35\x50\x36\x4e'\
b'\x36\x4d\x36\x4d\x37\x4d\x38\x4c\x3b\x4b\x42\x5a\x42\x5b\x3b'\
b'\x5c\x38\x5c\x37\x5c\x36\x5b\x36\x59\x36\x59\x35\x5c\x35\x5e'\
b'\x35\x61\x35\x63\x35\x63\x36\x61\x36\x60\x37\x60\x37\x60\x38'\
b'\x5f\x3b\x5c\x4c\x5b\x4e\x5b\x50\x5b\x50\x5c\x50\x5e\x51\x5e'\
b'\x52\x5b\x52\x59\x52\x56\x52\x54\x52\x54\x51\x56\x50\x57\x50'\
b'\x57\x50\x57\x4e\x58\x4c\x59\x43\x4b\x43\x27\x48\x5c\x52\x4c'\
b'\x52\x4d\x52\x4f\x52\x50\x52\x50\x52\x50\x55\x51\x54\x52\x52'\
b'\x52\x4f\x52\x4d\x52\x4a\x52\x4a\x51\x4d\x50\x4d\x50\x4e\x50'\
b'\x4e\x4f\x4e\x4d\x4e\x4c\x52\x3b\x52\x3a\x52\x38\x52\x37\x52'\
b'\x37\x52\x36\x4f\x36\x50\x35\x52\x35\x55\x35\x57\x35\x5a\x35'\
b'\x5a\x36\x57\x36\x57\x36\x56\x37\x56\x38\x56\x39\x56\x3b\x52'\
b'\x4c\x22\x46\x5e\x52\x35\x55\x35\x57\x35\x5a\x35\x5c\x35\x5c'\
b'\x36\x59\x36\x59\x36\x59\x37\x59\x38\x58\x39\x58\x3b\x54\x4d'\
b'\x54\x50\x53\x53\x52\x56\x50\x58\x4e\x59\x4a\x5a\x48\x5b\x48'\
b'\x5a\x4a\x59\x4d\x57\x4f\x54\x50\x50\x50\x4e\x54\x3b\x54\x3a'\
b'\x55\x38\x55\x37\x55\x37\x54\x36\x52\x36\x52\x35\x49\x41\x63'\
b'\x4e\x3b\x4b\x4c\x4b\x4d\x4a\x4f\x4a\x50\x4a\x50\x4b\x50\x4d'\
b'\x51\x4d\x52\x4a\x52\x48\x52\x45\x52\x43\x52\x43\x51\x46\x50'\
b'\x46\x50\x46\x50\x46\x4f\x47\x4d\x47\x4c\x4a\x3b\x4b\x3a\x4b'\
b'\x38\x4b\x37\x4b\x37\x4b\x36\x48\x36\x48\x35\x4b\x35\x4d\x35'\
b'\x50\x35\x52\x35\x52\x36\x50\x36\x4f\x36\x4f\x37\x4f\x38\x4f'\
b'\x39\x4e\x3b\x20\x52\x4d\x43\x57\x3a\x58\x39\x5a\x37\x5a\x37'\
b'\x5a\x36\x59\x36\x58\x36\x58\x35\x5a\x35\x5d\x35\x5f\x35\x61'\
b'\x35\x61\x36\x5f\x36\x5e\x37\x5c\x38\x5b\x39\x51\x42\x58\x4e'\
b'\x59\x4f\x5a\x50\x5b\x51\x5d\x51\x5d\x52\x5b\x52\x58\x52\x57'\
b'\x52\x56\x52\x55\x52\x55\x51\x52\x4c\x4d\x43\x28\x45\x5f\x53'\
b'\x3b\x4f\x4c\x4f\x4e\x4e\x50\x58\x50\x5c\x4b\x5d\x4a\x5b\x52'\
b'\x5b\x52\x56\x52\x52\x52\x4c\x52\x4a\x52\x47\x52\x47\x51\x4a'\
b'\x50\x4a\x50\x4a\x50\x4b\x4f\x4b\x4d\x4b\x4c\x4f\x3b\x4f\x3a'\
b'\x4f\x38\x4f\x37\x4f\x37\x4f\x36\x4c\x36\x4c\x35\x4f\x35\x52'\
b'\x35\x54\x35\x57\x35\x57\x36\x54\x36\x53\x36\x53\x37\x53\x38'\
b'\x53\x3b\x53\x3b\x3e\x3c\x68\x5e\x35\x60\x35\x62\x35\x63\x35'\
b'\x66\x35\x66\x36\x63\x36\x63\x37\x63\x37\x62\x38\x62\x3b\x5f'\
b'\x4c\x5e\x4e\x5e\x50\x5e\x50\x5e\x50\x61\x51\x61\x52\x5e\x52'\
b'\x5b\x52\x59\x52\x56\x52\x57\x51\x59\x50\x5a\x50\x5a\x50\x5a'\
b'\x4e\x5b\x4c\x5e\x39\x4f\x52\x4e\x52\x48\x39\x45\x4c\x44\x4e'\
b'\x44\x50\x44\x50\x44\x50\x46\x51\x46\x52\x44\x52\x42\x52\x41'\
b'\x52\x3e\x52\x3e\x51\x41\x50\x41\x50\x41\x50\x42\x4e\x42\x4c'\
b'\x46\x3b\x46\x38\x46\x37\x46\x37\x46\x36\x43\x36\x43\x35\x46'\
b'\x35\x48\x35\x49\x35\x4b\x35\x50\x4c\x5e\x35\x3b\x3f\x65\x4b'\
b'\x3a\x48\x4c\x47\x4d\x47\x4f\x47\x50\x47\x50\x47\x50\x4a\x51'\
b'\x4a\x52\x47\x52\x45\x52\x44\x52\x41\x52\x41\x51\x44\x50\x44'\
b'\x50\x45\x50\x45\x4f\x45\x4d\x45\x4c\x49\x3b\x49\x3a\x49\x38'\
b'\x49\x37\x49\x37\x49\x36\x46\x36\x46\x35\x48\x35\x4a\x35\x4b'\
b'\x35\x4b\x35\x4c\x35\x4d\x35\x59\x4b\x5c\x3b\x5d\x39\x5d\x38'\
b'\x5d\x37\x5d\x37\x5d\x36\x5a\x36\x5a\x35\x5c\x35\x5e\x35\x5f'\
b'\x35\x5f\x35\x62\x35\x63\x35\x63\x36\x60\x36\x60\x37\x5f\x37'\
b'\x5f\x38\x5f\x3a\x5f\x3b\x5a\x52\x59\x52\x4b\x3a\x1b\x41\x63'\
b'\x50\x53\x4a\x53\x43\x4c\x43\x47\x43\x3f\x4d\x34\x54\x34\x5a'\
b'\x34\x61\x3a\x61\x40\x61\x48\x57\x53\x50\x53\x20\x52\x5c\x40'\
b'\x5c\x3b\x58\x36\x54\x36\x4e\x36\x48\x40\x48\x47\x48\x4c\x4c'\
b'\x51\x50\x51\x56\x51\x5c\x47\x5c\x40\x35\x43\x61\x4f\x44\x50'\
b'\x44\x52\x44\x56\x44\x5a\x40\x5a\x3c\x5a\x39\x57\x36\x54\x36'\
b'\x53\x36\x52\x37\x4f\x44\x20\x52\x46\x51\x48\x50\x49\x50\x49'\
b'\x50\x49\x4f\x49\x4d\x4a\x4c\x4d\x3b\x4d\x3a\x4d\x38\x4e\x37'\
b'\x4e\x37\x4d\x36\x4b\x36\x4b\x35\x4d\x35\x4f\x35\x50\x35\x54'\
b'\x35\x55\x35\x5a\x35\x5f\x38\x5f\x3c\x5f\x41\x57\x46\x52\x46'\
b'\x50\x46\x4f\x46\x4e\x4c\x4d\x4e\x4d\x50\x4d\x50\x4d\x50\x50'\
b'\x51\x50\x52\x4d\x52\x4b\x52\x48\x52\x45\x52\x46\x51\x24\x41'\
b'\x63\x54\x34\x5a\x34\x61\x3a\x61\x40\x61\x48\x58\x52\x52\x53'\
b'\x53\x57\x5a\x57\x5d\x57\x5f\x57\x5f\x58\x5b\x5b\x59\x5b\x51'\
b'\x5b\x4f\x53\x4a\x53\x43\x4c\x43\x47\x43\x3f\x4d\x34\x54\x34'\
b'\x20\x52\x5c\x40\x5c\x3b\x58\x36\x54\x36\x4e\x36\x48\x40\x48'\
b'\x47\x48\x4c\x4c\x51\x50\x51\x56\x51\x5c\x47\x5c\x40\x55\x43'\
b'\x61\x4e\x4c\x4d\x4d\x4d\x4f\x4d\x50\x4d\x50\x4d\x50\x50\x51'\
b'\x4f\x52\x4d\x52\x4a\x52\x48\x52\x45\x52\x45\x51\x48\x50\x49'\
b'\x50\x49\x50\x49\x4f\x49\x4d\x4a\x4c\x4d\x3b\x4d\x3a\x4d\x38'\
b'\x4d\x37\x4e\x37\x4d\x36\x4b\x36\x4b\x35\x4d\x35\x50\x35\x50'\
b'\x35\x51\x35\x52\x35\x53\x35\x55\x35\x55\x35\x59\x35\x5e\x38'\
b'\x5e\x3b\x5e\x42\x56\x44\x57\x45\x58\x47\x58\x48\x58\x49\x59'\
b'\x4c\x5a\x4d\x5a\x4e\x5b\x4f\x5c\x50\x5e\x51\x5f\x51\x5f\x52'\
b'\x5d\x52\x5c\x52\x5b\x52\x59\x52\x58\x51\x57\x50\x56\x4e\x56'\
b'\x4d\x55\x4c\x55\x4a\x54\x49\x53\x47\x53\x46\x53\x45\x52\x45'\
b'\x52\x44\x51\x44\x51\x44\x4f\x44\x4e\x4c\x20\x52\x4f\x43\x51'\
b'\x43\x52\x43\x56\x43\x5a\x3f\x5a\x3c\x5a\x39\x57\x36\x54\x36'\
b'\x53\x36\x52\x36\x4f\x43\x33\x45\x5f\x5a\x36\x58\x36\x56\x36'\
b'\x53\x36\x4f\x39\x4f\x3c\x4f\x3d\x50\x3f\x51\x40\x53\x41\x54'\
b'\x42\x56\x43\x58\x44\x5a\x46\x5b\x48\x5b\x49\x5b\x4c\x59\x4f'\
b'\x57\x50\x54\x53\x4e\x53\x4a\x53\x47\x51\x47\x51\x49\x4a\x4a'\
b'\x4a\x4a\x50\x4d\x51\x4f\x51\x52\x51\x56\x4e\x56\x4b\x56\x4a'\
b'\x56\x48\x54\x46\x52\x45\x51\x45\x4f\x44\x4d\x43\x4c\x41\x4b'\
b'\x3e\x4b\x3d\x4b\x39\x51\x34\x57\x34\x5a\x34\x5d\x35\x5d\x35'\
b'\x5b\x3c\x5a\x3c\x5a\x36\x22\x43\x61\x4d\x52\x4a\x52\x47\x52'\
b'\x47\x51\x4a\x50\x4b\x50\x4b\x50\x4b\x4e\x4c\x4c\x50\x37\x49'\
b'\x37\x46\x3c\x45\x3c\x46\x35\x46\x35\x4b\x35\x50\x35\x55\x35'\
b'\x5a\x35\x5f\x35\x5f\x35\x5c\x3c\x5b\x3c\x5b\x37\x54\x37\x50'\
b'\x4c\x4f\x4e\x4f\x50\x4f\x50\x50\x50\x53\x51\x53\x52\x4f\x52'\
b'\x4d\x52\x3d\x41\x63\x44\x35\x47\x35\x49\x35\x4c\x35\x4e\x35'\
b'\x4e\x36\x4b\x36\x4b\x36\x4b\x37\x4b\x38\x4a\x39\x4a\x3b\x48'\
b'\x45\x47\x48\x47\x4a\x47\x4d\x4b\x51\x4e\x51\x50\x51\x54\x4f'\
b'\x56\x4c\x57\x48\x58\x45\x5a\x3b\x5a\x39\x5a\x38\x5a\x37\x5b'\
b'\x37\x5a\x36\x58\x36\x58\x35\x5a\x35\x5c\x35\x5e\x35\x61\x35'\
b'\x61\x36\x5e\x36\x5d\x37\x5d\x37\x5d\x38\x5d\x3a\x5d\x3b\x5a'\
b'\x45\x5a\x49\x58\x4e\x55\x51\x50\x53\x4d\x53\x49\x53\x43\x4e'\
b'\x43\x4a\x43\x48\x44\x46\x46\x3b\x46\x3a\x46\x38\x47\x37\x47'\
b'\x37\x46\x36\x44\x36\x44\x35\x2a\x41\x63\x58\x35\x5b\x35\x5d'\
b'\x35\x5f\x35\x61\x35\x61\x36\x5f\x36\x5e\x36\x5d\x37\x5d\x38'\
b'\x5c\x38\x5c\x39\x4d\x52\x4b\x52\x47\x39\x46\x37\x46\x37\x46'\
b'\x36\x45\x36\x43\x36\x43\x35\x46\x35\x48\x35\x4b\x35\x4e\x35'\
b'\x4e\x36\x4c\x36\x4b\x36\x4b\x37\x4b\x38\x4b\x38\x4b\x3a\x4e'\
b'\x4d\x59\x3a\x5a\x39\x5a\x37\x5a\x37\x5a\x37\x5a\x36\x5a\x36'\
b'\x58\x36\x58\x35\x2c\x3a\x6a\x54\x52\x51\x3c\x45\x52\x43\x52'\
b'\x40\x38\x3f\x37\x3f\x36\x3e\x36\x3c\x36\x3c\x35\x3f\x35\x41'\
b'\x35\x44\x35\x47\x35\x47\x36\x44\x36\x44\x36\x44\x37\x44\x38'\
b'\x44\x3a\x46\x4c\x52\x35\x54\x35\x57\x4c\x60\x39\x61\x38\x61'\
b'\x37\x61\x37\x61\x36\x61\x36\x61\x36\x5f\x36\x5f\x35\x61\x35'\
b'\x63\x35\x66\x35\x68\x35\x68\x36\x66\x36\x65\x36\x64\x37\x63'\
b'\x38\x56\x52\x54\x52\x46\x40\x64\x48\x35\x4a\x35\x4d\x35\x50'\
b'\x35\x53\x35\x53\x36\x51\x36\x50\x36\x50\x37\x50\x38\x51\x39'\
b'\x54\x40\x5a\x39\x5b\x37\x5b\x37\x5b\x36\x5a\x36\x59\x36\x59'\
b'\x35\x5b\x35\x5e\x35\x60\x35\x62\x35\x62\x36\x60\x36\x5f\x36'\
b'\x5e\x38\x5d\x39\x55\x42\x5a\x4e\x5b\x50\x5c\x50\x5c\x51\x5e'\
b'\x51\x5e\x52\x5c\x52\x59\x52\x56\x52\x53\x52\x53\x51\x55\x51'\
b'\x56\x50\x56\x4f\x56\x4f\x55\x4d\x52\x45\x4a\x4e\x49\x4f\x49'\
b'\x50\x49\x50\x4a\x51\x4b\x51\x4b\x52\x49\x52\x46\x52\x44\x52'\
b'\x42\x52\x42\x51\x44\x51\x45\x50\x46\x50\x46\x4f\x47\x4e\x51'\
b'\x43\x4c\x38\x4b\x37\x4a\x36\x4a\x36\x48\x36\x48\x35\x39\x42'\
b'\x62\x51\x43\x57\x3a\x58\x39\x59\x37\x59\x37\x59\x36\x58\x36'\
b'\x56\x36\x56\x35\x59\x35\x5b\x35\x5d\x35\x60\x35\x5f\x36\x5d'\
b'\x36\x5c\x36\x5b\x37\x5b\x38\x51\x45\x50\x4c\x50\x4d\x4f\x4f'\
b'\x4f\x50\x4f\x50\x50\x50\x52\x51\x52\x52\x4f\x52\x4d\x52\x4a'\
b'\x52\x48\x52\x48\x51\x4a\x50\x4b\x50\x4b\x50\x4b\x4f\x4c\x4d'\
b'\x4c\x4c\x4d\x45\x48\x39\x48\x38\x47\x36\x46\x36\x44\x36\x45'\
b'\x35\x47\x35\x4a\x35\x4c\x35\x4f\x35\x4f\x36\x4d\x36\x4d\x36'\
b'\x4c\x37\x4c\x37\x4c\x38\x4d\x39\x51\x43\x19\x43\x61\x45\x52'\
b'\x45\x51\x59\x37\x4e\x37\x4b\x3c\x4b\x3c\x4b\x35\x4b\x35\x50'\
b'\x35\x55\x35\x59\x35\x5c\x35\x5f\x35\x5f\x36\x4b\x50\x57\x50'\
b'\x5b\x4a\x5c\x4a\x5a\x52\x5a\x52\x54\x52\x4f\x52\x4b\x52\x48'\
b'\x52\x45\x52\x09\x48\x5c\x4d\x57\x52\x59\x52\x59\x4a\x59\x52'\
b'\x32\x5a\x32\x5a\x32\x55\x34\x4d\x57\x05\x4b\x59\x55\x57\x4d'\
b'\x34\x4f\x34\x57\x57\x55\x57\x09\x48\x5c\x57\x34\x52\x32\x52'\
b'\x32\x5a\x32\x52\x59\x4a\x59\x4a\x59\x4f\x57\x57\x34\x08\x47'\
b'\x5d\x53\x35\x5b\x46\x59\x46\x52\x38\x4b\x46\x49\x46\x51\x35'\
b'\x53\x35\x05\x45\x5f\x5d\x58\x47\x58\x47\x56\x5d\x56\x5d\x58'\
b'\x08\x4a\x5a\x58\x3c\x57\x3c\x53\x34\x57\x34\x58\x3c\x20\x52'\
b'\x4c\x3e\x4c\x3e\x2e\x47\x5d\x5b\x3f\x5b\x3f\x5a\x43\x59\x48'\
b'\x58\x4e\x58\x4f\x58\x4f\x58\x50\x59\x51\x5b\x51\x5b\x51\x58'\
b'\x52\x57\x52\x56\x52\x54\x51\x54\x50\x54\x4f\x54\x4f\x52\x51'\
b'\x4f\x52\x4e\x52\x4c\x52\x49\x4e\x49\x4b\x49\x46\x4f\x3e\x54'\
b'\x3e\x56\x3e\x59\x3f\x5a\x3f\x5b\x3e\x5b\x3f\x20\x52\x57\x41'\
b'\x55\x40\x54\x40\x51\x40\x4d\x46\x4d\x4a\x4d\x4d\x4e\x50\x50'\
b'\x50\x50\x50\x53\x4f\x54\x4d\x57\x41\x25\x47\x5d\x49\x51\x49'\
b'\x50\x49\x4e\x4a\x49\x4f\x35\x4b\x35\x4b\x34\x4f\x33\x53\x32'\
b'\x53\x33\x52\x34\x51\x39\x51\x3c\x50\x41\x54\x3e\x56\x3e\x58'\
b'\x3e\x5b\x42\x5b\x46\x5b\x4b\x55\x52\x50\x52\x4c\x52\x49\x51'\
b'\x20\x52\x4d\x50\x4e\x51\x50\x51\x53\x51\x57\x4a\x57\x47\x57'\
b'\x44\x56\x41\x54\x41\x52\x41\x4f\x42\x4d\x50\x1b\x47\x5d\x58'\
b'\x4e\x58\x4f\x57\x51\x53\x52\x51\x52\x4d\x52\x49\x4e\x49\x4a'\
b'\x49\x45\x50\x3e\x55\x3e\x58\x3e\x5b\x3f\x5a\x42\x59\x45\x59'\
b'\x45\x57\x40\x56\x40\x55\x40\x52\x40\x4d\x46\x4d\x4a\x4d\x4d'\
b'\x50\x50\x53\x50\x55\x50\x58\x4e\x31\x45\x5f\x55\x35\x55\x34'\
b'\x59\x33\x5c\x32\x5d\x33\x5c\x34\x5b\x39\x5b\x3c\x57\x4e\x57'\
b'\x4f\x57\x4f\x57\x50\x58\x51\x5a\x51\x5a\x51\x57\x52\x56\x52'\
b'\x54\x52\x53\x51\x53\x50\x53\x4f\x53\x4f\x51\x51\x4e\x52\x4d'\
b'\x52\x4b\x52\x47\x4e\x47\x4b\x47\x46\x4e\x3e\x53\x3e\x55\x3e'\
b'\x56\x3f\x58\x35\x55\x35\x20\x52\x56\x41\x54\x40\x53\x40\x50'\
b'\x40\x4b\x46\x4b\x4a\x4b\x4d\x4d\x50\x4f\x50\x4f\x50\x51\x4f'\
b'\x53\x4d\x56\x41\x27\x48\x5c\x4e\x49\x4d\x4a\x4d\x4a\x4d\x4d'\
b'\x50\x50\x53\x50\x55\x50\x58\x4e\x59\x4f\x57\x51\x53\x52\x51'\
b'\x52\x4d\x52\x4a\x4e\x4a\x4b\x4a\x49\x4a\x46\x4c\x43\x4e\x41'\
b'\x51\x3f\x53\x3e\x55\x3e\x58\x3e\x5a\x41\x5a\x42\x5a\x45\x53'\
b'\x49\x4e\x49\x20\x52\x4e\x47\x52\x47\x57\x44\x57\x42\x57\x41'\
b'\x55\x40\x54\x40\x52\x40\x4f\x44\x4e\x47\x25\x42\x62\x50\x41'\
b'\x4d\x40\x4d\x3f\x50\x3f\x51\x3f\x52\x39\x58\x33\x5c\x33\x5e'\
b'\x33\x60\x33\x5f\x36\x5f\x38\x5e\x39\x5c\x34\x5c\x34\x5b\x34'\
b'\x59\x34\x56\x39\x54\x3e\x54\x3f\x5a\x3f\x59\x41\x54\x41\x51'\
b'\x51\x4f\x57\x4b\x5c\x47\x5c\x46\x5c\x44\x5c\x44\x5a\x45\x58'\
b'\x45\x58\x48\x5a\x49\x5a\x4c\x5a\x4d\x54\x50\x41\x36\x46\x5e'\
b'\x55\x4f\x53\x51\x50\x52\x50\x52\x4d\x52\x4a\x4e\x4a\x4b\x4a'\
b'\x46\x50\x3e\x55\x3e\x57\x3e\x5a\x3f\x5a\x3f\x5c\x3f\x5c\x3e'\
b'\x5c\x3f\x5c\x3f\x5c\x40\x5c\x41\x5c\x42\x5b\x45\x5a\x48\x59'\
b'\x4e\x58\x52\x56\x57\x53\x5b\x50\x5c\x4e\x5c\x4b\x5c\x48\x5b'\
b'\x48\x59\x48\x57\x49\x57\x4d\x5a\x4f\x5a\x50\x5a\x52\x59\x53'\
b'\x57\x54\x53\x55\x51\x55\x4f\x20\x52\x58\x41\x57\x40\x55\x40'\
b'\x52\x40\x4e\x46\x4e\x4a\x4e\x4c\x4f\x4f\x51\x4f\x52\x4f\x56'\
b'\x4d\x58\x41\x2b\x46\x5e\x48\x52\x4e\x35\x4b\x35\x4b\x34\x4f'\
b'\x33\x52\x32\x52\x33\x52\x34\x51\x39\x50\x3c\x4f\x41\x53\x3e'\
b'\x57\x3e\x59\x3e\x5b\x41\x5b\x43\x5b\x44\x5b\x45\x59\x4f\x59'\
b'\x4f\x59\x4f\x59\x4f\x59\x50\x5a\x51\x5c\x51\x5c\x51\x59\x52'\
b'\x58\x52\x56\x52\x55\x51\x55\x50\x55\x4f\x55\x4e\x57\x45\x57'\
b'\x45\x57\x44\x57\x42\x56\x41\x54\x41\x52\x41\x4f\x43\x4c\x52'\
b'\x48\x52\x2c\x4c\x58\x52\x4f\x52\x4f\x52\x4f\x52\x50\x53\x51'\
b'\x55\x51\x55\x51\x52\x52\x50\x52\x4f\x52\x4e\x51\x4e\x50\x4e'\
b'\x4f\x4e\x4e\x50\x42\x51\x42\x51\x41\x51\x41\x51\x41\x50\x40'\
b'\x4e\x40\x4e\x3f\x51\x3e\x52\x3e\x53\x3e\x54\x3f\x54\x40\x54'\
b'\x41\x54\x41\x52\x4f\x20\x52\x56\x37\x56\x38\x55\x39\x54\x39'\
b'\x53\x39\x52\x38\x52\x37\x52\x36\x53\x35\x54\x35\x55\x35\x56'\
b'\x36\x56\x37\x26\x48\x5c\x51\x40\x51\x3f\x54\x3e\x56\x3e\x57'\
b'\x3e\x58\x3f\x58\x40\x58\x41\x58\x41\x55\x50\x54\x54\x50\x59'\
b'\x4b\x5d\x4a\x5c\x4f\x58\x50\x53\x51\x50\x54\x42\x54\x42\x54'\
b'\x41\x54\x41\x54\x41\x53\x40\x51\x40\x20\x52\x5a\x37\x5a\x38'\
b'\x58\x39\x57\x39\x56\x39\x55\x38\x55\x37\x55\x36\x56\x35\x57'\
b'\x35\x58\x35\x5a\x36\x5a\x37\x2b\x46\x5e\x48\x52\x4e\x35\x4a'\
b'\x35\x4a\x34\x4c\x34\x50\x33\x52\x32\x52\x33\x51\x34\x50\x39'\
b'\x50\x3c\x4b\x52\x48\x52\x20\x52\x5a\x52\x57\x52\x56\x52\x56'\
b'\x52\x55\x52\x54\x52\x53\x50\x50\x4b\x4e\x47\x55\x42\x56\x3f'\
b'\x57\x3f\x58\x3f\x59\x3f\x5c\x3f\x5c\x40\x5b\x40\x5a\x40\x59'\
b'\x41\x59\x41\x57\x42\x57\x42\x52\x46\x57\x4f\x58\x50\x58\x50'\
b'\x59\x51\x5a\x51\x5a\x52\x19\x4b\x59\x4f\x35\x4f\x34\x53\x33'\
b'\x57\x32\x57\x33\x56\x34\x55\x39\x55\x3c\x51\x4f\x51\x4f\x51'\
b'\x4f\x51\x50\x52\x51\x54\x51\x54\x51\x51\x52\x50\x52\x4e\x52'\
b'\x4d\x51\x4d\x50\x4d\x50\x4d\x4f\x4d\x4e\x53\x35\x4f\x35\x41'\
b'\x40\x64\x42\x52\x45\x42\x46\x41\x46\x41\x46\x41\x45\x40\x43'\
b'\x40\x43\x3f\x46\x3e\x47\x3e\x48\x3e\x49\x3f\x49\x40\x49\x40'\
b'\x49\x41\x49\x41\x4d\x3e\x51\x3e\x54\x3e\x55\x41\x59\x3e\x5d'\
b'\x3e\x5f\x3e\x61\x41\x61\x43\x61\x44\x61\x45\x5f\x4f\x5f\x4f'\
b'\x5f\x4f\x5f\x4f\x5f\x50\x60\x51\x62\x51\x62\x51\x5f\x52\x5e'\
b'\x52\x5c\x52\x5b\x51\x5b\x50\x5b\x50\x5b\x4f\x5b\x4e\x5d\x45'\
b'\x5d\x44\x5d\x44\x5d\x42\x5c\x41\x5a\x41\x58\x41\x55\x43\x55'\
b'\x44\x55\x45\x52\x52\x4e\x52\x51\x45\x51\x44\x51\x44\x51\x42'\
b'\x50\x41\x4e\x41\x4c\x41\x49\x43\x46\x52\x42\x52\x2f\x46\x5e'\
b'\x48\x52\x4b\x42\x4c\x41\x4c\x41\x4c\x41\x4b\x40\x49\x40\x49'\
b'\x3f\x4c\x3e\x4d\x3e\x4e\x3e\x4f\x3f\x4f\x40\x4f\x41\x4f\x41'\
b'\x53\x3e\x57\x3e\x59\x3e\x5b\x41\x5b\x43\x5b\x44\x5b\x45\x59'\
b'\x4f\x59\x4f\x59\x4f\x59\x4f\x59\x50\x5a\x51\x5c\x51\x5c\x51'\
b'\x59\x52\x58\x52\x56\x52\x55\x51\x55\x50\x55\x4f\x55\x4e\x57'\
b'\x45\x57\x44\x57\x44\x57\x42\x56\x41\x54\x41\x52\x41\x4f\x43'\
b'\x4c\x52\x48\x52\x1b\x47\x5d\x53\x3e\x57\x3e\x5b\x43\x5b\x47'\
b'\x5b\x4c\x56\x52\x51\x52\x4d\x52\x49\x4e\x49\x4a\x49\x45\x4e'\
b'\x3e\x53\x3e\x20\x52\x53\x40\x50\x40\x4d\x46\x4d\x4a\x4d\x4d'\
b'\x4f\x51\x51\x51\x54\x51\x57\x4b\x57\x47\x57\x44\x55\x40\x53'\
b'\x40\x3b\x44\x60\x46\x5b\x49\x5b\x49\x5a\x49\x5a\x4a\x59\x4a'\
b'\x57\x4a\x55\x4e\x42\x4e\x41\x4e\x41\x4e\x41\x4d\x40\x4b\x40'\
b'\x4c\x3f\x4e\x3e\x50\x3e\x51\x3e\x52\x3f\x52\x40\x52\x40\x52'\
b'\x41\x52\x41\x52\x41\x57\x3e\x58\x3e\x5a\x3e\x5e\x42\x5e\x46'\
b'\x5e\x4b\x57\x53\x52\x53\x50\x53\x4f\x52\x4e\x57\x4d\x58\x4d'\
b'\x59\x4d\x5a\x4d\x5a\x4d\x5b\x50\x5b\x50\x5c\x4d\x5c\x4b\x5c'\
b'\x49\x5c\x46\x5c\x46\x5b\x20\x52\x4f\x50\x50\x51\x52\x51\x55'\
b'\x51\x5a\x4a\x5a\x47\x5a\x44\x58\x41\x57\x41\x55\x41\x52\x42'\
b'\x4f\x50\x32\x47\x5d\x4f\x5b\x51\x5b\x52\x5a\x52\x5a\x52\x57'\
b'\x54\x4f\x52\x51\x51\x52\x4f\x52\x4e\x52\x4c\x52\x49\x4e\x49'\
b'\x4b\x49\x46\x4f\x3e\x54\x3e\x56\x3e\x59\x3f\x5a\x3f\x5b\x3e'\
b'\x5b\x3f\x5b\x3f\x5a\x43\x59\x48\x56\x56\x56\x59\x56\x5a\x56'\
b'\x5a\x56\x5b\x58\x5b\x58\x5c\x56\x5c\x53\x5c\x51\x5c\x4f\x5c'\
b'\x4f\x5b\x20\x52\x57\x41\x56\x40\x54\x40\x51\x40\x4d\x46\x4d'\
b'\x4a\x4d\x4d\x4e\x50\x50\x50\x50\x50\x53\x4f\x55\x4d\x57\x41'\
b'\x1c\x49\x5b\x4b\x52\x4e\x42\x4e\x41\x4e\x41\x4e\x41\x4d\x40'\
b'\x4b\x40\x4b\x3f\x4e\x3e\x50\x3e\x51\x3e\x52\x3f\x52\x40\x52'\
b'\x40\x52\x41\x56\x3e\x59\x3e\x59\x3e\x59\x42\x58\x45\x57\x45'\
b'\x57\x43\x56\x42\x54\x42\x53\x42\x51\x42\x4e\x52\x4b\x52\x31'\
b'\x48\x5c\x57\x40\x56\x40\x54\x40\x52\x40\x50\x42\x50\x43\x50'\
b'\x44\x50\x45\x52\x46\x53\x47\x54\x47\x55\x47\x57\x48\x58\x49'\
b'\x59\x4b\x59\x4c\x59\x4f\x54\x52\x50\x52\x4d\x52\x4a\x51\x4a'\
b'\x4f\x4b\x4c\x4c\x4c\x4d\x50\x4f\x51\x50\x51\x52\x51\x55\x4f'\
b'\x55\x4d\x55\x4d\x54\x4c\x53\x4b\x52\x4a\x51\x4a\x50\x49\x4e'\
b'\x49\x4d\x47\x4c\x46\x4c\x45\x4c\x42\x51\x3e\x55\x3e\x58\x3e'\
b'\x5a\x3f\x5a\x41\x59\x44\x58\x45\x57\x40\x23\x4a\x5a\x52\x41'\
b'\x51\x44\x50\x4a\x50\x4c\x4f\x4d\x4f\x4e\x4f\x4f\x51\x50\x52'\
b'\x50\x54\x50\x56\x50\x56\x51\x54\x51\x51\x52\x4f\x52\x4d\x52'\
b'\x4c\x51\x4c\x4f\x4c\x4e\x4c\x4d\x4c\x4b\x4d\x45\x4e\x41\x4c'\
b'\x40\x4c\x3f\x4f\x3f\x51\x3a\x52\x3a\x54\x39\x54\x39\x53\x3c'\
b'\x53\x3f\x58\x3f\x58\x41\x52\x41\x2f\x46\x5e\x58\x3f\x5c\x3f'\
b'\x59\x4e\x58\x4f\x58\x4f\x58\x50\x5a\x51\x5b\x51\x5b\x51\x59'\
b'\x52\x57\x52\x56\x52\x55\x51\x55\x50\x55\x4f\x55\x4f\x51\x52'\
b'\x4e\x52\x4c\x52\x49\x50\x49\x4d\x49\x4c\x49\x4b\x4b\x42\x4b'\
b'\x42\x4b\x41\x4b\x41\x4b\x41\x4a\x40\x48\x40\x48\x3f\x4b\x3e'\
b'\x4d\x3e\x4e\x3e\x4f\x3f\x4f\x40\x4f\x41\x4f\x41\x4d\x4b\x4d'\
b'\x4c\x4d\x4c\x4d\x4e\x4e\x50\x50\x50\x52\x50\x55\x4d\x58\x3f'\
b'\x2e\x46\x5e\x51\x4e\x53\x4c\x55\x49\x57\x45\x57\x41\x57\x3f'\
b'\x59\x3f\x5b\x3e\x5c\x3f\x5c\x40\x5a\x43\x59\x47\x56\x4b\x54'\
b'\x4e\x51\x51\x50\x52\x4e\x52\x4e\x50\x4d\x4b\x4d\x48\x4d\x48'\
b'\x4d\x45\x4c\x43\x4c\x41\x4b\x41\x4b\x41\x4a\x40\x4a\x40\x49'\
b'\x40\x48\x40\x48\x3f\x4b\x3e\x4d\x3e\x4e\x3e\x4f\x3f\x4f\x40'\
b'\x4f\x40\x50\x42\x50\x44\x50\x46\x51\x48\x51\x4a\x51\x4b\x51'\
b'\x4b\x51\x4d\x51\x4e\x41\x41\x63\x57\x4e\x58\x4c\x5a\x49\x5c'\
b'\x45\x5d\x41\x5d\x3f\x5f\x3f\x61\x3e\x61\x3f\x61\x40\x60\x43'\
b'\x5e\x47\x5b\x4b\x59\x4e\x56\x51\x55\x52\x54\x52\x53\x4d\x52'\
b'\x47\x50\x4c\x4b\x52\x49\x52\x49\x50\x48\x4b\x48\x48\x48\x48'\
b'\x47\x45\x47\x44\x47\x43\x46\x41\x46\x41\x46\x41\x45\x40\x45'\
b'\x40\x44\x40\x43\x40\x43\x3f\x46\x3e\x48\x3e\x49\x3e\x4a\x3f'\
b'\x4a\x40\x4a\x40\x4a\x42\x4b\x44\x4b\x46\x4c\x48\x4c\x4a\x4c'\
b'\x4b\x4c\x4d\x4c\x4e\x50\x49\x52\x45\x51\x42\x51\x3f\x53\x3f'\
b'\x54\x3f\x54\x3f\x55\x40\x55\x43\x56\x46\x56\x49\x56\x4b\x57'\
b'\x4d\x57\x4e\x49\x45\x5f\x5c\x42\x5b\x42\x5a\x42\x59\x42\x58'\
b'\x43\x57\x44\x55\x46\x54\x47\x55\x49\x56\x4d\x57\x4f\x57\x4f'\
b'\x58\x50\x59\x51\x5a\x51\x5b\x51\x5b\x51\x58\x52\x56\x52\x56'\
b'\x52\x54\x52\x54\x51\x53\x4f\x52\x4c\x51\x4b\x50\x4d\x4e\x50'\
b'\x4c\x52\x4a\x52\x49\x52\x48\x52\x47\x52\x48\x50\x48\x4e\x48'\
b'\x4e\x49\x4f\x4a\x4f\x4b\x4f\x4c\x4e\x4e\x4d\x4f\x4b\x51\x49'\
b'\x50\x48\x4f\x46\x4f\x44\x4e\x43\x4e\x42\x4d\x41\x4d\x41\x4c'\
b'\x40\x4b\x40\x4a\x40\x4a\x3f\x4d\x3e\x4e\x3e\x4f\x3e\x50\x3f'\
b'\x50\x3f\x51\x40\x51\x41\x51\x42\x53\x44\x53\x46\x54\x44\x57'\
b'\x41\x58\x3f\x5a\x3f\x5c\x3f\x5c\x3f\x5d\x3f\x5d\x40\x5c\x42'\
b'\x5c\x42\x39\x45\x5f\x58\x40\x5a\x3f\x5c\x3e\x5d\x3f\x5c\x42'\
b'\x59\x47\x57\x4c\x55\x50\x54\x52\x52\x54\x50\x59\x4f\x5a\x4f'\
b'\x5b\x4e\x5c\x4e\x5c\x4c\x5d\x4b\x5d\x49\x5d\x47\x5c\x47\x5c'\
b'\x49\x5b\x4b\x5b\x4b\x5a\x4c\x5a\x4d\x59\x4e\x57\x50\x54\x51'\
b'\x52\x50\x52\x50\x51\x50\x4e\x4f\x4a\x4e\x47\x4d\x44\x4c\x42'\
b'\x4c\x42\x4c\x41\x4b\x41\x4a\x40\x49\x40\x48\x40\x48\x3f\x4b'\
b'\x3e\x4d\x3e\x4e\x3e\x4f\x3f\x4f\x40\x4f\x40\x50\x42\x51\x44'\
b'\x52\x47\x52\x4a\x53\x4d\x53\x4f\x55\x4b\x58\x44\x58\x40\x1d'\
b'\x46\x5e\x48\x52\x4c\x4d\x52\x46\x56\x40\x4f\x40\x4c\x45\x4b'\
b'\x45\x4b\x42\x4b\x3f\x4b\x3f\x50\x3f\x54\x3f\x58\x3f\x5c\x3f'\
b'\x5c\x3f\x58\x44\x52\x4c\x4e\x50\x56\x50\x59\x4c\x5a\x4c\x59'\
b'\x4f\x59\x52\x59\x52\x55\x52\x50\x52\x4c\x52\x48\x52\x48\x52'\
b'\x2b\x49\x5b\x4b\x45\x4d\x45\x4f\x43\x4f\x41\x51\x37\x52\x34'\
b'\x55\x31\x58\x31\x58\x31\x59\x31\x59\x32\x57\x33\x55\x34\x55'\
b'\x36\x53\x3f\x52\x42\x50\x45\x4e\x45\x4e\x46\x4f\x46\x51\x48'\
b'\x51\x49\x51\x4b\x50\x4c\x4f\x53\x4e\x55\x4e\x56\x4e\x57\x50'\
b'\x58\x52\x59\x51\x5a\x4e\x5a\x4b\x58\x4b\x56\x4b\x55\x4b\x53'\
b'\x4d\x4a\x4d\x49\x4d\x49\x4d\x47\x4c\x46\x4b\x46\x4b\x45\x05'\
b'\x4f\x55\x53\x32\x53\x5d\x51\x5d\x51\x32\x53\x32\x2b\x49\x5b'\
b'\x59\x46\x57\x46\x55\x48\x55\x4a\x53\x54\x52\x57\x4f\x5a\x4c'\
b'\x5a\x4c\x5a\x4b\x5a\x4b\x59\x4d\x58\x4f\x57\x4f\x55\x51\x4c'\
b'\x52\x49\x54\x46\x56\x46\x56\x45\x55\x45\x53\x43\x53\x42\x53'\
b'\x40\x54\x3f\x55\x38\x56\x36\x56\x35\x56\x34\x54\x33\x52\x32'\
b'\x53\x31\x56\x31\x59\x33\x59\x35\x59\x36\x59\x38\x57\x41\x57'\
b'\x42\x57\x42\x57\x44\x58\x45\x59\x45\x59\x46\x17\x46\x5e\x48'\
b'\x48\x4b\x46\x4d\x46\x4f\x46\x51\x47\x53\x47\x54\x48\x56\x48'\
b'\x57\x48\x59\x48\x5c\x47\x5c\x49\x59\x4b\x57\x4b\x55\x4b\x53'\
b'\x4a\x52\x49\x50\x49\x4e\x48\x4d\x48\x4b\x48\x48\x4a\x48\x48'\
b'\x36\x46\x5e\x5c\x35\x5c\x52\x48\x52\x48\x35\x5c\x35\x20\x52'\
b'\x5a\x50\x5a\x37\x4a\x37\x4a\x50\x5a\x50\x20\x52\x51\x48\x51'\
b'\x48\x51\x45\x52\x43\x53\x42\x54\x41\x55\x3f\x55\x3f\x55\x3d'\
b'\x53\x3b\x52\x3b\x51\x3b\x4f\x3d\x4f\x3f\x4d\x3f\x4d\x3c\x50'\
b'\x39\x52\x39\x54\x39\x57\x3c\x57\x3e\x57\x40\x56\x42\x55\x43'\
b'\x53\x45\x53\x46\x53\x48\x51\x48\x20\x52\x50\x4c\x50\x4b\x51'\
b'\x4a\x52\x4a\x52\x4a\x53\x4b\x53\x4c\x53\x4d\x52\x4d\x52\x4d'\
b'\x51\x4d\x50\x4d\x50\x4c'

_index =\
b'\x00\x00\x03\x00\x2e\x00\x47\x00\x90\x00\x01\x01\xbe\x01\x61'\
b'\x02\x6e\x02\x87\x02\xa0\x02\xc3\x02\xe0\x02\xff\x02\x0c\x03'\
b'\x29\x03\x36\x03\x6f\x03\xaa\x03\xef\x03\x48\x04\x99\x04\xd8'\
b'\x04\x25\x05\x58\x05\xc3\x05\x10\x06\x49\x06\x84\x06\x97\x06'\
b'\xb0\x06\xc3\x06\x30\x07\xcb\x07\x2e\x08\xad\x08\xe4\x08\x41'\
b'\x09\xb8\x09\x29\x0a\x88\x0a\x1d\x0b\x6e\x0b\xb5\x0b\x4a\x0c'\
b'\x9d\x0c\x1c\x0d\x95\x0d\xce\x0d\x3b\x0e\x86\x0e\x33\x0f\x9c'\
b'\x0f\xe3\x0f\x60\x10\xb7\x10\x12\x11\xa1\x11\x16\x12\x4b\x12'\
b'\x60\x12\x6d\x12\x82\x12\x95\x12\xa2\x12\xb5\x12\x14\x13\x61'\
b'\x13\x9a\x13\xff\x13\x50\x14\x9d\x14\x0c\x15\x65\x15\xc0\x15'\
b'\x0f\x16\x68\x16\x9d\x16\x22\x17\x83\x17\xbc\x17\x35\x18\x9c'\
b'\x18\xd7\x18\x3c\x19\x85\x19\xe6\x19\x45\x1a\xca\x1a\x5f\x1b'\
b'\xd4\x1b\x11\x1c\x6a\x1c\x77\x1c\xd0\x1c\x01\x1d'

FONT = memoryview(_font)
INDEX = memoryview(_index)
