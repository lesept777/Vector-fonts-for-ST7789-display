WIDTH = 40
HEIGHT = 45
FIRST = 0x20
LAST = 0x7f

_font =\
b'\x01\x4d\x57\x19\x4d\x57\x54\x3b\x54\x3f\x54\x45\x53\x48\x51'\
b'\x48\x50\x45\x50\x3f\x50\x3b\x50\x32\x54\x32\x54\x3b\x20\x52'\
b'\x55\x50\x55\x51\x53\x53\x52\x53\x51\x53\x4f\x51\x4f\x50\x4f'\
b'\x4e\x51\x4c\x52\x4c\x53\x4c\x55\x4e\x55\x50\x17\x4a\x5a\x50'\
b'\x2f\x50\x31\x50\x33\x50\x38\x4f\x3b\x4d\x3b\x4c\x38\x4c\x33'\
b'\x4c\x31\x4c\x2f\x50\x2f\x20\x52\x58\x2f\x58\x31\x58\x33\x58'\
b'\x38\x57\x3b\x55\x3b\x54\x38\x54\x33\x54\x31\x54\x2f\x58\x2f'\
b'\x23\x43\x61\x50\x3a\x57\x3a\x59\x32\x5d\x32\x5b\x3a\x5f\x3a'\
b'\x5f\x3e\x5a\x3e\x59\x46\x5f\x46\x5f\x4a\x58\x4a\x57\x52\x53'\
b'\x52\x54\x4a\x4d\x4a\x4b\x52\x47\x52\x49\x4a\x45\x4a\x45\x46'\
b'\x4a\x46\x4b\x3e\x45\x3e\x45\x3a\x4c\x3a\x4d\x32\x51\x32\x50'\
b'\x3a\x20\x52\x4d\x46\x55\x46\x57\x3e\x4f\x3e\x4d\x46\x35\x46'\
b'\x5e\x51\x4e\x55\x4e\x58\x4b\x58\x4a\x58\x48\x56\x46\x54\x45'\
b'\x52\x44\x50\x43\x4f\x43\x4c\x42\x4a\x40\x49\x3d\x49\x3c\x49'\
b'\x38\x4c\x34\x50\x33\x50\x2e\x54\x2e\x54\x33\x56\x33\x5a\x34'\
b'\x5b\x35\x5a\x38\x59\x38\x55\x37\x53\x37\x50\x37\x4d\x39\x4d'\
b'\x3b\x4d\x3c\x4e\x3e\x50\x3f\x52\x40\x53\x40\x55\x41\x58\x42'\
b'\x5b\x44\x5c\x47\x5c\x49\x5c\x4d\x58\x51\x54\x51\x54\x57\x50'\
b'\x57\x50\x51\x4d\x51\x49\x50\x48\x4f\x49\x4c\x4a\x4d\x4e\x4e'\
b'\x51\x4e\x4d\x3e\x66\x40\x3a\x40\x38\x42\x35\x44\x32\x46\x31'\
b'\x48\x31\x49\x31\x4c\x32\x4e\x35\x4f\x38\x4f\x3a\x4f\x3c\x4e'\
b'\x3f\x4c\x41\x49\x42\x48\x42\x46\x42\x44\x41\x42\x3f\x40\x3c'\
b'\x40\x3a\x20\x52\x4c\x3a\x4c\x37\x4a\x34\x48\x34\x46\x34\x44'\
b'\x37\x44\x3a\x44\x3c\x46\x3f\x48\x3f\x4a\x3f\x4c\x3c\x4c\x3a'\
b'\x20\x52\x55\x4a\x55\x48\x56\x45\x58\x43\x5b\x42\x5c\x42\x5e'\
b'\x42\x60\x43\x62\x45\x64\x48\x64\x4a\x64\x4c\x62\x4f\x60\x52'\
b'\x5e\x53\x5c\x53\x5b\x53\x58\x52\x56\x4f\x55\x4c\x55\x4a\x20'\
b'\x52\x60\x4a\x60\x48\x5e\x45\x5c\x45\x5a\x45\x58\x48\x58\x4a'\
b'\x58\x4d\x5a\x50\x5c\x50\x5e\x50\x60\x4d\x60\x4a\x20\x52\x5d'\
b'\x32\x4b\x52\x47\x52\x59\x32\x5d\x32\x4c\x42\x62\x44\x49\x44'\
b'\x48\x45\x45\x47\x43\x49\x41\x4b\x40\x47\x3d\x47\x39\x47\x37'\
b'\x49\x34\x4b\x32\x4e\x31\x50\x31\x51\x31\x54\x32\x56\x34\x57'\
b'\x37\x57\x38\x57\x3a\x56\x3c\x54\x3f\x52\x40\x51\x41\x58\x49'\
b'\x5a\x46\x5a\x42\x5e\x43\x5e\x45\x5c\x49\x5b\x4b\x5c\x4d\x5f'\
b'\x50\x60\x52\x5c\x52\x5b\x51\x59\x4f\x58\x4e\x57\x50\x52\x52'\
b'\x4e\x52\x4b\x52\x47\x51\x45\x4e\x44\x4b\x44\x49\x20\x52\x48'\
b'\x49\x48\x4a\x49\x4c\x4a\x4e\x4d\x4f\x4e\x4f\x51\x4f\x55\x4d'\
b'\x56\x4c\x4d\x43\x4c\x43\x4a\x44\x49\x46\x48\x48\x48\x49\x20'\
b'\x52\x53\x38\x53\x37\x51\x35\x50\x35\x4e\x35\x4b\x37\x4b\x39'\
b'\x4b\x3c\x4f\x3f\x50\x3e\x51\x3d\x53\x3b\x53\x3a\x53\x38\x0b'\
b'\x4e\x56\x54\x2f\x54\x31\x54\x33\x54\x38\x53\x3b\x51\x3b\x50'\
b'\x38\x50\x33\x50\x31\x50\x2f\x54\x2f\x0f\x4a\x5a\x51\x44\x51'\
b'\x4a\x54\x54\x58\x58\x54\x5b\x51\x56\x4c\x4b\x4c\x44\x4c\x3e'\
b'\x51\x32\x54\x2e\x58\x30\x54\x34\x51\x3e\x51\x44\x0f\x4a\x5a'\
b'\x53\x44\x53\x3e\x50\x34\x4c\x30\x50\x2e\x53\x32\x58\x3e\x58'\
b'\x44\x58\x4b\x53\x56\x50\x5b\x4c\x58\x50\x54\x53\x4a\x53\x44'\
b'\x2e\x47\x5d\x54\x32\x54\x34\x53\x38\x53\x3a\x55\x39\x58\x37'\
b'\x5a\x36\x5a\x36\x5b\x3a\x5b\x3a\x59\x3b\x55\x3b\x54\x3c\x55'\
b'\x3d\x58\x3f\x59\x41\x59\x41\x56\x44\x56\x43\x54\x42\x53\x3e'\
b'\x52\x3d\x51\x3e\x50\x42\x4e\x43\x4e\x44\x4b\x41\x4b\x41\x4c'\
b'\x3f\x4f\x3d\x50\x3c\x4f\x3b\x4b\x3b\x49\x3a\x49\x3a\x4a\x36'\
b'\x4a\x36\x4c\x37\x4f\x39\x51\x3a\x51\x38\x50\x34\x50\x32\x50'\
b'\x32\x54\x32\x54\x32\x0d\x45\x5f\x47\x42\x50\x42\x50\x39\x54'\
b'\x39\x54\x42\x5d\x42\x5d\x46\x54\x46\x54\x50\x50\x50\x50\x46'\
b'\x47\x46\x47\x42\x0f\x4d\x57\x55\x4d\x55\x4d\x55\x4e\x55\x4e'\
b'\x55\x51\x54\x57\x52\x59\x4f\x58\x50\x56\x51\x51\x51\x4f\x51'\
b'\x4e\x51\x4d\x51\x4d\x55\x4d\x05\x4a\x5a\x4c\x42\x58\x42\x58'\
b'\x46\x4c\x46\x4c\x42\x0d\x4d\x57\x55\x50\x55\x51\x53\x53\x52'\
b'\x53\x51\x53\x4f\x51\x4f\x50\x4f\x4e\x51\x4c\x52\x4c\x53\x4c'\
b'\x55\x4e\x55\x50\x05\x46\x5e\x4c\x5b\x48\x5b\x58\x2e\x5c\x2e'\
b'\x4c\x5b\x23\x45\x5f\x47\x42\x47\x3a\x4d\x31\x52\x31\x57\x31'\
b'\x5d\x3a\x5d\x42\x5d\x4a\x57\x53\x52\x53\x4d\x53\x47\x4a\x47'\
b'\x42\x20\x52\x58\x42\x58\x3f\x58\x3b\x56\x37\x54\x35\x52\x35'\
b'\x50\x35\x4e\x37\x4c\x3b\x4c\x3f\x4c\x42\x4c\x45\x4c\x49\x4e'\
b'\x4d\x50\x4f\x52\x4f\x54\x4f\x56\x4d\x58\x49\x58\x45\x58\x42'\
b'\x0e\x4a\x5a\x4c\x39\x4e\x38\x53\x34\x55\x32\x58\x32\x58\x52'\
b'\x54\x52\x54\x38\x54\x38\x52\x3a\x50\x3b\x4e\x3c\x4d\x3c\x4c'\
b'\x39\x2e\x46\x5e\x5b\x3a\x5b\x3c\x5a\x3f\x57\x42\x55\x45\x53'\
b'\x46\x52\x47\x50\x49\x4f\x4b\x4d\x4e\x4d\x4e\x5c\x4e\x5c\x52'\
b'\x49\x52\x49\x52\x49\x51\x49\x51\x49\x4f\x4a\x4b\x4c\x48\x4f'\
b'\x45\x51\x43\x52\x42\x54\x40\x55\x3e\x56\x3c\x56\x3a\x56\x39'\
b'\x56\x37\x54\x36\x52\x35\x51\x35\x50\x35\x4d\x36\x4c\x37\x4a'\
b'\x38\x4a\x38\x48\x35\x48\x35\x4a\x33\x4c\x32\x4f\x31\x51\x31'\
b'\x56\x31\x5b\x36\x5b\x3a\x3a\x46\x5e\x50\x4f\x54\x4f\x58\x4c'\
b'\x58\x49\x58\x47\x56\x45\x54\x43\x50\x43\x4f\x43\x4e\x43\x4e'\
b'\x3f\x4f\x3f\x50\x3f\x53\x3f\x55\x3e\x56\x3b\x56\x3a\x56\x39'\
b'\x55\x37\x54\x36\x52\x35\x51\x35\x4e\x35\x4b\x36\x4a\x37\x49'\
b'\x34\x49\x33\x4b\x32\x4d\x32\x4f\x31\x51\x31\x53\x31\x57\x32'\
b'\x59\x35\x5b\x38\x5b\x3a\x5b\x3c\x58\x40\x56\x41\x57\x41\x59'\
b'\x42\x5b\x45\x5c\x47\x5c\x49\x5c\x4b\x5b\x4f\x58\x51\x53\x53'\
b'\x50\x53\x4f\x53\x4c\x52\x4a\x52\x48\x51\x48\x51\x49\x4d\x4a'\
b'\x4e\x4d\x4f\x50\x4f\x19\x45\x5f\x47\x47\x48\x45\x4b\x3f\x4f'\
b'\x3a\x53\x34\x55\x32\x59\x32\x59\x46\x5d\x46\x5d\x4a\x59\x4a'\
b'\x59\x52\x55\x52\x55\x4a\x47\x4a\x47\x47\x20\x52\x55\x37\x54'\
b'\x39\x51\x3c\x4e\x40\x4c\x44\x4b\x46\x55\x46\x55\x37\x29\x46'\
b'\x5e\x4e\x3e\x55\x3f\x5c\x44\x5c\x49\x5c\x4b\x5a\x4f\x57\x51'\
b'\x53\x53\x50\x53\x4f\x53\x4c\x52\x4a\x52\x49\x51\x48\x51\x49'\
b'\x4d\x4a\x4e\x4d\x4f\x50\x4f\x52\x4f\x55\x4e\x57\x4c\x57\x4a'\
b'\x57\x49\x57\x47\x56\x45\x53\x43\x4e\x42\x4a\x42\x4a\x40\x4b'\
b'\x3c\x4b\x38\x4b\x34\x4b\x32\x5b\x32\x5b\x36\x4f\x36\x4f\x36'\
b'\x4f\x39\x4f\x3b\x4e\x3e\x4e\x3e\x31\x46\x5e\x48\x45\x48\x40'\
b'\x4a\x39\x4f\x34\x56\x32\x5a\x32\x5a\x35\x58\x35\x53\x37\x50'\
b'\x39\x4d\x3d\x4d\x40\x4e\x3f\x51\x3e\x52\x3e\x55\x3e\x59\x40'\
b'\x5b\x43\x5c\x46\x5c\x48\x5c\x4a\x5b\x4e\x59\x51\x55\x53\x52'\
b'\x53\x4d\x53\x48\x4b\x48\x45\x20\x52\x52\x42\x50\x42\x4e\x42'\
b'\x4c\x43\x4c\x44\x4c\x45\x4c\x45\x4c\x47\x4d\x4b\x4e\x4e\x50'\
b'\x4f\x52\x4f\x54\x4f\x56\x4e\x57\x4c\x58\x49\x58\x48\x58\x45'\
b'\x55\x42\x52\x42\x10\x46\x5e\x4d\x52\x4d\x4e\x4f\x46\x52\x3e'\
b'\x56\x38\x57\x36\x48\x36\x48\x32\x5c\x32\x5c\x36\x5b\x37\x57'\
b'\x3d\x54\x45\x51\x4e\x51\x52\x4d\x52\x4b\x46\x5e\x5c\x4a\x5c'\
b'\x4c\x5b\x4f\x59\x51\x55\x53\x52\x53\x4f\x53\x4b\x51\x49\x4e'\
b'\x48\x4b\x48\x4a\x48\x49\x48\x46\x4a\x44\x4c\x42\x4d\x42\x48'\
b'\x3f\x48\x3a\x48\x38\x4a\x35\x4c\x33\x50\x31\x52\x31\x55\x31'\
b'\x58\x33\x5b\x35\x5c\x38\x5c\x3a\x5c\x3b\x5b\x3d\x5a\x3f\x58'\
b'\x41\x57\x42\x5c\x44\x5c\x4a\x20\x52\x4c\x4a\x4c\x4b\x4c\x4d'\
b'\x4e\x4e\x50\x4f\x52\x4f\x54\x4f\x56\x4e\x57\x4d\x58\x4b\x58'\
b'\x4a\x58\x48\x57\x46\x55\x45\x52\x43\x50\x43\x4e\x44\x4c\x48'\
b'\x4c\x4a\x20\x52\x57\x3a\x57\x39\x57\x37\x56\x36\x53\x35\x52'\
b'\x35\x51\x35\x4e\x36\x4d\x37\x4d\x39\x4d\x3a\x4d\x3b\x4d\x3d'\
b'\x4f\x3f\x51\x40\x53\x40\x55\x3f\x57\x3c\x57\x3a\x31\x46\x5e'\
b'\x5c\x3f\x5c\x48\x53\x52\x4a\x52\x49\x4e\x4c\x4e\x51\x4d\x55'\
b'\x4b\x57\x47\x57\x44\x56\x45\x53\x45\x52\x45\x4f\x45\x4b\x44'\
b'\x49\x41\x48\x3e\x48\x3c\x48\x3a\x49\x36\x4b\x33\x4f\x31\x52'\
b'\x31\x54\x31\x58\x33\x5b\x37\x5c\x3c\x5c\x3f\x20\x52\x52\x42'\
b'\x54\x42\x57\x41\x58\x41\x58\x40\x58\x3f\x58\x3f\x58\x3d\x57'\
b'\x39\x56\x36\x54\x35\x52\x35\x50\x35\x4e\x36\x4d\x38\x4c\x3a'\
b'\x4c\x3c\x4c\x3f\x4f\x42\x52\x42\x1b\x4d\x57\x55\x50\x55\x51'\
b'\x53\x53\x52\x53\x51\x53\x4f\x51\x4f\x50\x4f\x4e\x51\x4c\x52'\
b'\x4c\x53\x4c\x55\x4e\x55\x50\x20\x52\x55\x3d\x55\x3e\x53\x40'\
b'\x52\x40\x51\x40\x4f\x3e\x4f\x3d\x4f\x3c\x51\x3a\x52\x3a\x53'\
b'\x3a\x55\x3c\x55\x3d\x1d\x4c\x58\x55\x4d\x55\x4d\x55\x4e\x55'\
b'\x4e\x55\x51\x53\x57\x52\x59\x4e\x58\x50\x56\x50\x51\x50\x4f'\
b'\x50\x4e\x50\x4d\x50\x4d\x55\x4d\x20\x52\x56\x3d\x56\x3e\x54'\
b'\x40\x52\x40\x51\x40\x4f\x3e\x4f\x3d\x4f\x3c\x51\x3a\x52\x3a'\
b'\x54\x3a\x56\x3c\x56\x3d\x08\x45\x5f\x4c\x44\x5d\x4b\x5b\x4e'\
b'\x47\x46\x47\x42\x5b\x3a\x5d\x3d\x4c\x44\x0b\x45\x5f\x47\x47'\
b'\x5d\x47\x5d\x4b\x47\x4b\x47\x47\x20\x52\x47\x3d\x5d\x3d\x5d'\
b'\x41\x47\x41\x47\x3d\x08\x45\x5f\x47\x3d\x49\x3a\x5d\x42\x5d'\
b'\x46\x49\x4e\x47\x4b\x58\x44\x47\x3d\x31\x48\x5c\x51\x35\x4e'\
b'\x35\x4b\x36\x4a\x33\x4b\x32\x4f\x31\x51\x31\x54\x31\x57\x33'\
b'\x59\x35\x5a\x38\x5a\x39\x5a\x3a\x59\x3d\x57\x3f\x55\x41\x53'\
b'\x43\x52\x45\x52\x47\x52\x47\x52\x48\x52\x48\x4f\x48\x4e\x47'\
b'\x4e\x46\x4e\x45\x50\x42\x51\x40\x53\x3e\x55\x3c\x56\x3a\x56'\
b'\x39\x56\x37\x53\x35\x51\x35\x20\x52\x54\x50\x54\x51\x52\x53'\
b'\x51\x53\x4f\x53\x4e\x51\x4e\x50\x4e\x4e\x4f\x4c\x51\x4c\x52'\
b'\x4c\x54\x4e\x54\x50\x59\x3d\x67\x5c\x50\x5a\x50\x59\x4f\x58'\
b'\x4e\x57\x4f\x54\x50\x53\x50\x50\x50\x4d\x4e\x4a\x4c\x49\x48'\
b'\x49\x45\x49\x43\x4a\x3f\x4d\x3c\x51\x3a\x53\x3a\x55\x3a\x59'\
b'\x3b\x5a\x3c\x5a\x4a\x5a\x4b\x5b\x4c\x5c\x4c\x5d\x4c\x5f\x4b'\
b'\x60\x48\x61\x45\x61\x43\x61\x40\x5f\x3b\x5b\x37\x56\x35\x52'\
b'\x35\x4f\x35\x49\x37\x45\x3b\x43\x41\x43\x45\x43\x49\x45\x4f'\
b'\x4a\x53\x50\x56\x53\x56\x56\x56\x59\x55\x5a\x55\x5a\x58\x5a'\
b'\x58\x55\x59\x53\x59\x4f\x59\x48\x57\x42\x52\x3f\x4a\x3f\x45'\
b'\x3f\x40\x42\x39\x48\x34\x4e\x31\x52\x31\x56\x31\x5d\x34\x62'\
b'\x38\x65\x3f\x65\x43\x65\x46\x64\x4b\x61\x4e\x5e\x50\x5c\x50'\
b'\x20\x52\x53\x4c\x54\x4c\x56\x4c\x56\x4b\x56\x4b\x56\x4a\x56'\
b'\x49\x56\x3e\x56\x3e\x54\x3e\x53\x3e\x50\x3e\x4d\x42\x4d\x45'\
b'\x4d\x48\x50\x4c\x53\x4c\x1c\x41\x63\x5c\x52\x5b\x50\x5a\x4c'\
b'\x59\x4a\x4b\x4a\x48\x52\x43\x52\x45\x4d\x48\x44\x4b\x3d\x4e'\
b'\x35\x50\x32\x54\x32\x56\x35\x59\x3d\x5c\x44\x5f\x4d\x61\x52'\
b'\x5c\x52\x20\x52\x58\x46\x56\x42\x53\x3b\x52\x37\x50\x3b\x4d'\
b'\x42\x4c\x46\x58\x46\x3e\x44\x60\x4f\x52\x4e\x52\x4c\x52\x49'\
b'\x52\x47\x52\x46\x51\x46\x32\x47\x32\x49\x32\x4c\x32\x4e\x32'\
b'\x4f\x32\x52\x32\x57\x32\x5a\x34\x5c\x38\x5c\x3a\x5c\x3d\x5a'\
b'\x40\x58\x41\x5a\x42\x5e\x45\x5e\x49\x5e\x4d\x57\x52\x4f\x52'\
b'\x20\x52\x4b\x43\x4b\x4e\x4b\x4e\x4c\x4e\x4d\x4e\x4e\x4f\x4f'\
b'\x4f\x51\x4f\x55\x4e\x57\x4d\x59\x4a\x59\x49\x59\x47\x58\x45'\
b'\x56\x44\x52\x43\x51\x43\x4b\x43\x20\x52\x4b\x3f\x4f\x3f\x51'\
b'\x3f\x54\x3f\x56\x3e\x57\x3c\x57\x3a\x57\x39\x56\x37\x54\x36'\
b'\x51\x35\x4f\x35\x4d\x35\x4c\x35\x4b\x36\x4b\x3f\x29\x44\x60'\
b'\x55\x53\x51\x53\x4c\x50\x48\x4c\x46\x46\x46\x42\x46\x3e\x48'\
b'\x38\x4c\x33\x52\x31\x55\x31\x57\x31\x5a\x32\x5c\x33\x5e\x33'\
b'\x5e\x33\x5d\x37\x5c\x37\x5b\x36\x59\x36\x57\x35\x55\x35\x53'\
b'\x35\x4f\x37\x4c\x3a\x4a\x3f\x4a\x42\x4a\x45\x4c\x4a\x4e\x4d'\
b'\x52\x4f\x55\x4f\x58\x4f\x5c\x4d\x5d\x4d\x5e\x51\x5e\x51\x5c'\
b'\x52\x5a\x52\x57\x53\x55\x53\x21\x43\x61\x5f\x42\x5f\x46\x5d'\
b'\x4c\x58\x50\x51\x52\x4d\x52\x4b\x52\x47\x52\x45\x51\x45\x32'\
b'\x47\x32\x4b\x32\x4d\x32\x51\x32\x58\x34\x5d\x38\x5f\x3e\x5f'\
b'\x42\x20\x52\x4e\x4e\x54\x4e\x5a\x48\x5a\x42\x5a\x3c\x54\x36'\
b'\x4e\x36\x4c\x36\x4a\x36\x49\x36\x49\x4e\x4a\x4e\x4c\x4e\x4e'\
b'\x4e\x0d\x46\x5e\x48\x52\x48\x32\x5b\x32\x5b\x36\x4c\x36\x4c'\
b'\x3f\x5a\x3f\x5a\x43\x4c\x43\x4c\x4e\x5c\x4e\x5c\x52\x48\x52'\
b'\x0b\x46\x5e\x48\x52\x48\x32\x5c\x32\x5c\x36\x4d\x36\x4d\x3f'\
b'\x5a\x3f\x5a\x43\x4d\x43\x4d\x52\x48\x52\x29\x43\x61\x5a\x42'\
b'\x5f\x42\x5f\x51\x5e\x51\x5c\x52\x59\x52\x56\x53\x54\x53\x51'\
b'\x53\x4b\x50\x48\x4c\x45\x46\x45\x42\x45\x3e\x48\x38\x4c\x33'\
b'\x52\x31\x55\x31\x57\x31\x5a\x32\x5d\x33\x5e\x33\x5e\x33\x5d'\
b'\x37\x5c\x36\x57\x35\x55\x35\x53\x35\x4e\x37\x4c\x3a\x4a\x3f'\
b'\x4a\x42\x4a\x45\x4b\x4a\x4e\x4d\x52\x4f\x55\x4f\x57\x4f\x5a'\
b'\x4e\x5a\x4e\x5a\x42\x0d\x44\x60\x5a\x32\x5e\x32\x5e\x52\x5a'\
b'\x52\x5a\x43\x4a\x43\x4a\x52\x46\x52\x46\x32\x4a\x32\x4a\x3f'\
b'\x5a\x3f\x5a\x32\x05\x4e\x56\x50\x32\x54\x32\x54\x52\x50\x52'\
b'\x50\x32\x15\x47\x5d\x5b\x48\x5b\x4a\x5b\x4e\x58\x51\x54\x53'\
b'\x51\x53\x4f\x53\x4d\x52\x4b\x51\x49\x51\x49\x50\x4a\x4d\x4b'\
b'\x4d\x4e\x4f\x51\x4f\x54\x4f\x57\x4b\x57\x47\x57\x32\x5b\x32'\
b'\x5b\x48\x1c\x44\x60\x5d\x32\x5c\x34\x58\x37\x54\x3b\x50\x3f'\
b'\x4f\x41\x51\x42\x55\x46\x59\x4b\x5d\x50\x5e\x52\x59\x52\x58'\
b'\x50\x54\x4b\x50\x47\x4c\x44\x4a\x43\x4a\x52\x46\x52\x46\x32'\
b'\x4a\x32\x4a\x40\x4c\x3f\x50\x3b\x53\x37\x57\x33\x58\x32\x5d'\
b'\x32\x07\x46\x5e\x5c\x4e\x5c\x52\x48\x52\x48\x32\x4d\x32\x4d'\
b'\x4e\x5c\x4e\x2b\x3f\x65\x50\x4e\x50\x4c\x4e\x49\x4c\x45\x4a'\
b'\x41\x49\x3d\x47\x3a\x47\x39\x46\x3f\x46\x4c\x45\x52\x41\x52'\
b'\x41\x4e\x42\x45\x42\x3d\x43\x35\x43\x32\x47\x32\x48\x34\x4b'\
b'\x3a\x4e\x40\x51\x46\x52\x48\x53\x46\x56\x40\x59\x3a\x5c\x34'\
b'\x5d\x32\x61\x32\x62\x41\x63\x52\x5f\x52\x5e\x4c\x5e\x3f\x5d'\
b'\x39\x5d\x3a\x5b\x3d\x5a\x41\x58\x45\x56\x49\x54\x4c\x54\x4e'\
b'\x50\x4e\x15\x43\x61\x5b\x52\x5a\x50\x57\x4c\x54\x47\x51\x43'\
b'\x4e\x3e\x4b\x3a\x4a\x39\x4a\x52\x45\x52\x45\x32\x49\x32\x4b'\
b'\x34\x50\x3a\x55\x41\x59\x47\x5a\x4a\x5a\x32\x5f\x32\x5f\x52'\
b'\x5b\x52\x2b\x41\x63\x43\x42\x43\x3e\x45\x38\x49\x33\x4f\x31'\
b'\x52\x31\x55\x31\x5b\x33\x5f\x38\x61\x3e\x61\x42\x61\x46\x5f'\
b'\x4c\x5b\x51\x55\x53\x52\x53\x4f\x53\x49\x51\x45\x4c\x43\x46'\
b'\x43\x42\x20\x52\x47\x42\x47\x45\x49\x4a\x4c\x4d\x50\x4f\x52'\
b'\x4f\x54\x4f\x58\x4d\x5b\x4a\x5d\x45\x5d\x42\x5d\x3f\x5b\x3a'\
b'\x58\x37\x54\x35\x52\x35\x50\x35\x4c\x37\x49\x3a\x47\x3f\x47'\
b'\x42\x20\x45\x5f\x4f\x32\x56\x32\x5d\x37\x5d\x3c\x5d\x3f\x5b'\
b'\x43\x58\x45\x52\x46\x4f\x46\x4b\x46\x4b\x52\x47\x52\x47\x32'\
b'\x49\x32\x4d\x32\x4f\x32\x20\x52\x50\x36\x4d\x36\x4b\x36\x4b'\
b'\x42\x4f\x42\x51\x42\x55\x42\x57\x40\x59\x3e\x59\x3c\x59\x3a'\
b'\x57\x38\x55\x36\x51\x36\x50\x36\x36\x41\x63\x43\x42\x43\x3e'\
b'\x45\x38\x49\x33\x4f\x31\x52\x31\x55\x31\x5b\x33\x5f\x38\x61'\
b'\x3e\x61\x42\x61\x46\x5f\x4b\x5c\x4f\x58\x52\x55\x52\x55\x53'\
b'\x57\x55\x5a\x56\x5d\x57\x5f\x57\x5e\x5b\x5c\x5a\x57\x59\x54'\
b'\x57\x51\x55\x51\x53\x4e\x52\x49\x50\x45\x4c\x43\x46\x43\x42'\
b'\x20\x52\x47\x42\x47\x45\x49\x4a\x4c\x4d\x50\x4f\x52\x4f\x54'\
b'\x4f\x58\x4d\x5b\x4a\x5d\x45\x5d\x42\x5d\x3f\x5b\x3a\x58\x37'\
b'\x54\x35\x52\x35\x50\x35\x4c\x37\x49\x3a\x47\x3f\x47\x42\x2c'\
b'\x44\x60\x56\x45\x56\x46\x59\x49\x5b\x4c\x5d\x50\x5e\x52\x59'\
b'\x52\x58\x50\x56\x4d\x54\x49\x52\x46\x51\x45\x50\x45\x4f\x45'\
b'\x4e\x45\x4a\x45\x4a\x52\x46\x52\x46\x32\x48\x32\x4c\x32\x4e'\
b'\x32\x55\x32\x5c\x37\x5c\x3c\x5c\x3f\x59\x43\x56\x45\x20\x52'\
b'\x4f\x36\x4c\x36\x4a\x36\x4a\x42\x4e\x42\x50\x42\x54\x41\x56'\
b'\x40\x57\x3e\x57\x3c\x57\x3a\x56\x38\x54\x36\x51\x36\x4f\x36'\
b'\x32\x45\x5f\x51\x4f\x58\x4f\x58\x4a\x58\x49\x57\x46\x55\x45'\
b'\x52\x44\x50\x43\x4f\x43\x4c\x41\x49\x3f\x48\x3c\x48\x3a\x48'\
b'\x36\x4e\x31\x53\x31\x56\x31\x5a\x32\x5b\x33\x5a\x37\x59\x36'\
b'\x55\x35\x53\x35\x51\x35\x4f\x36\x4e\x37\x4d\x38\x4d\x3a\x4d'\
b'\x3b\x4e\x3d\x4f\x3e\x52\x3f\x53\x40\x55\x41\x59\x42\x5b\x45'\
b'\x5d\x48\x5d\x4a\x5d\x4e\x57\x53\x51\x53\x4f\x53\x4c\x52\x49'\
b'\x51\x48\x51\x47\x50\x49\x4d\x4a\x4d\x4e\x4f\x51\x4f\x09\x44'\
b'\x60\x5e\x32\x5e\x36\x54\x36\x54\x52\x50\x52\x50\x36\x46\x36'\
b'\x46\x32\x5e\x32\x19\x44\x60\x52\x53\x4f\x53\x4a\x51\x47\x4d'\
b'\x46\x49\x46\x46\x46\x32\x4a\x32\x4a\x46\x4a\x4a\x4f\x4f\x52'\
b'\x4f\x54\x4f\x57\x4e\x59\x4b\x5a\x48\x5a\x46\x5a\x32\x5e\x32'\
b'\x5e\x46\x5e\x49\x5d\x4d\x5a\x51\x55\x53\x52\x53\x14\x41\x63'\
b'\x61\x32\x5f\x37\x5c\x40\x59\x47\x56\x4f\x54\x52\x50\x52\x4e'\
b'\x4f\x4b\x47\x48\x40\x45\x37\x43\x32\x48\x32\x4b\x39\x50\x47'\
b'\x52\x4d\x55\x47\x59\x39\x5c\x32\x61\x32\x22\x3c\x68\x52\x3c'\
b'\x50\x42\x4c\x4d\x4a\x52\x46\x52\x43\x4b\x3f\x3b\x3e\x32\x43'\
b'\x32\x43\x36\x45\x3d\x46\x44\x48\x4a\x48\x4c\x4a\x48\x4e\x3c'\
b'\x50\x36\x54\x36\x56\x3c\x5a\x48\x5c\x4c\x5d\x4a\x5e\x44\x60'\
b'\x3d\x61\x36\x62\x32\x66\x32\x65\x3b\x61\x4b\x5e\x52\x5a\x52'\
b'\x58\x4d\x54\x42\x52\x3c\x19\x42\x62\x5b\x52\x5a\x51\x58\x4d'\
b'\x56\x4a\x53\x46\x52\x44\x51\x46\x4e\x4a\x4c\x4d\x4a\x51\x49'\
b'\x52\x44\x52\x46\x4e\x4c\x46\x4f\x41\x45\x32\x4a\x32\x52\x3e'\
b'\x5a\x32\x5f\x32\x55\x41\x58\x45\x5d\x4e\x60\x52\x5b\x52\x12'\
b'\x42\x62\x50\x52\x50\x45\x4d\x40\x47\x37\x44\x32\x4a\x32\x4b'\
b'\x36\x50\x3e\x52\x41\x54\x3e\x59\x36\x5b\x32\x60\x32\x5d\x37'\
b'\x57\x40\x54\x45\x54\x52\x50\x52\x17\x44\x60\x5d\x36\x5c\x37'\
b'\x59\x3a\x56\x3e\x53\x43\x50\x47\x4d\x4c\x4c\x4e\x5e\x4e\x5e'\
b'\x52\x46\x52\x46\x4f\x47\x4d\x4a\x49\x4d\x44\x50\x3f\x53\x3b'\
b'\x56\x37\x58\x36\x47\x36\x47\x32\x5d\x32\x5d\x36\x09\x4b\x59'\
b'\x4d\x2e\x57\x2e\x57\x31\x51\x31\x51\x57\x57\x57\x57\x5b\x4d'\
b'\x5b\x4d\x2e\x05\x46\x5e\x48\x2e\x4c\x2e\x5c\x5b\x58\x5b\x48'\
b'\x2e\x09\x4b\x59\x57\x5b\x4d\x5b\x4d\x57\x53\x57\x53\x31\x4d'\
b'\x31\x4d\x2e\x57\x2e\x57\x5b\x08\x45\x5f\x54\x32\x5d\x42\x59'\
b'\x43\x52\x36\x4b\x43\x47\x42\x50\x32\x54\x32\x05\x44\x60\x46'\
b'\x57\x5e\x57\x5e\x5b\x46\x5b\x46\x57\x05\x4c\x58\x50\x2e\x56'\
b'\x35\x54\x37\x4e\x31\x50\x2e\x39\x47\x5d\x52\x4f\x54\x4f\x56'\
b'\x4f\x57\x4f\x57\x47\x57\x47\x55\x47\x53\x47\x52\x47\x50\x47'\
b'\x4e\x48\x4d\x4a\x4d\x4b\x4d\x4d\x50\x4f\x52\x4f\x20\x52\x52'\
b'\x39\x55\x39\x58\x3b\x5a\x3d\x5b\x41\x5b\x43\x5b\x52\x5b\x52'\
b'\x59\x52\x56\x52\x53\x53\x52\x53\x50\x53\x4d\x52\x4a\x50\x49'\
b'\x4d\x49\x4b\x49\x49\x4a\x46\x4d\x44\x51\x43\x53\x43\x53\x43'\
b'\x55\x44\x56\x44\x57\x44\x57\x44\x57\x43\x57\x42\x57\x40\x55'\
b'\x3e\x53\x3d\x52\x3d\x50\x3d\x4c\x3e\x4c\x3e\x4b\x3a\x4c\x3a'\
b'\x50\x39\x52\x39\x25\x45\x5f\x4c\x3b\x4d\x3b\x50\x39\x52\x39'\
b'\x54\x39\x58\x3b\x5b\x3f\x5d\x43\x5d\x46\x5d\x49\x5b\x4e\x58'\
b'\x51\x53\x53\x51\x53\x4e\x53\x49\x52\x47\x51\x47\x2f\x4c\x2e'\
b'\x4c\x3b\x20\x52\x4c\x4e\x4c\x4e\x4f\x4f\x50\x4f\x54\x4f\x58'\
b'\x4a\x58\x46\x58\x44\x57\x41\x56\x3f\x53\x3d\x51\x3d\x4f\x3d'\
b'\x4d\x3e\x4c\x3f\x4c\x4e\x23\x47\x5d\x55\x53\x52\x53\x4d\x51'\
b'\x4a\x4d\x49\x49\x49\x46\x49\x43\x4b\x3f\x4d\x3b\x52\x39\x54'\
b'\x39\x56\x39\x59\x3a\x5b\x3b\x5a\x3e\x59\x3e\x56\x3d\x55\x3d'\
b'\x51\x3d\x4d\x42\x4d\x46\x4d\x48\x4e\x4b\x50\x4e\x53\x4f\x55'\
b'\x4f\x57\x4f\x5a\x4e\x5b\x4e\x5b\x51\x5b\x52\x59\x52\x58\x52'\
b'\x56\x53\x55\x53\x25\x45\x5f\x58\x3f\x57\x3e\x55\x3d\x53\x3d'\
b'\x51\x3d\x4e\x3f\x4d\x41\x4c\x44\x4c\x46\x4c\x4a\x50\x4f\x54'\
b'\x4f\x55\x4f\x58\x4e\x58\x4e\x58\x3f\x20\x52\x58\x2f\x5d\x2e'\
b'\x5d\x51\x5b\x52\x56\x53\x53\x53\x51\x53\x4c\x51\x49\x4e\x47'\
b'\x49\x47\x46\x47\x43\x49\x3f\x4c\x3b\x50\x39\x52\x39\x54\x39'\
b'\x57\x3b\x58\x3b\x58\x2f\x27\x46\x5e\x48\x46\x48\x43\x49\x3e'\
b'\x4c\x3b\x50\x39\x52\x39\x57\x39\x5c\x3f\x5c\x46\x5c\x46\x5c'\
b'\x47\x5c\x47\x4c\x47\x4c\x4b\x50\x4f\x54\x4f\x56\x4f\x59\x4e'\
b'\x5a\x4e\x5b\x51\x5a\x52\x56\x53\x54\x53\x50\x53\x4c\x51\x49'\
b'\x4d\x48\x49\x48\x46\x20\x52\x58\x44\x58\x41\x55\x3d\x52\x3d'\
b'\x51\x3d\x4f\x3e\x4d\x40\x4c\x42\x4c\x44\x58\x44\x15\x49\x5b'\
b'\x54\x2e\x56\x2e\x59\x2f\x59\x2f\x58\x33\x58\x32\x56\x32\x54'\
b'\x32\x51\x32\x4f\x35\x4f\x38\x4f\x3a\x58\x3a\x58\x3e\x4f\x3e'\
b'\x4f\x52\x4b\x52\x4b\x38\x4b\x33\x4f\x2e\x54\x2e\x31\x46\x5e'\
b'\x58\x50\x58\x50\x54\x51\x52\x51\x50\x51\x4c\x50\x49\x4d\x48'\
b'\x48\x48\x45\x48\x43\x49\x3e\x4c\x3b\x51\x39\x53\x39\x56\x39'\
b'\x5b\x3a\x5c\x3b\x5c\x50\x5c\x56\x57\x5b\x51\x5b\x4f\x5b\x4a'\
b'\x5a\x49\x59\x4a\x56\x4b\x56\x4f\x57\x51\x57\x55\x57\x58\x54'\
b'\x58\x51\x58\x50\x20\x52\x58\x3e\x57\x3e\x55\x3d\x53\x3d\x50'\
b'\x3d\x4c\x42\x4c\x46\x4c\x48\x4d\x4b\x4f\x4d\x51\x4d\x53\x4d'\
b'\x54\x4d\x57\x4c\x58\x4c\x58\x3e\x1b\x46\x5e\x48\x52\x48\x2f'\
b'\x4d\x2e\x4d\x3a\x4e\x3a\x51\x39\x52\x39\x55\x39\x59\x3b\x5b'\
b'\x3e\x5c\x42\x5c\x45\x5c\x52\x57\x52\x57\x45\x57\x43\x57\x40'\
b'\x55\x3e\x53\x3d\x51\x3d\x51\x3d\x4f\x3d\x4e\x3e\x4d\x3e\x4d'\
b'\x3e\x4d\x52\x48\x52\x13\x4d\x57\x54\x52\x50\x52\x50\x3a\x54'\
b'\x3a\x54\x52\x20\x52\x52\x36\x51\x36\x4f\x34\x4f\x33\x4f\x32'\
b'\x51\x30\x52\x30\x53\x30\x55\x32\x55\x33\x55\x34\x53\x36\x52'\
b'\x36\x1f\x4a\x5a\x4f\x5b\x4e\x5b\x4d\x5a\x4c\x5a\x4d\x57\x4d'\
b'\x57\x4e\x57\x4f\x57\x51\x57\x53\x54\x53\x52\x53\x3a\x57\x3a'\
b'\x57\x52\x57\x56\x53\x5b\x4f\x5b\x20\x52\x55\x36\x54\x36\x52'\
b'\x34\x52\x33\x52\x32\x54\x30\x55\x30\x56\x30\x58\x32\x58\x33'\
b'\x58\x34\x56\x36\x55\x36\x1c\x46\x5e\x51\x45\x52\x46\x55\x49'\
b'\x58\x4d\x5b\x50\x5c\x52\x57\x52\x56\x50\x53\x4d\x51\x4a\x4e'\
b'\x47\x4c\x46\x4c\x52\x48\x52\x48\x2f\x4c\x2e\x4c\x44\x4e\x43'\
b'\x50\x40\x53\x3d\x55\x3b\x56\x3a\x5b\x3a\x5a\x3b\x57\x3e\x55'\
b'\x41\x52\x44\x51\x45\x0d\x4c\x58\x55\x52\x51\x52\x4e\x4f\x4e'\
b'\x4c\x4e\x2f\x52\x2e\x52\x4b\x52\x4c\x53\x4d\x54\x4e\x55\x4f'\
b'\x56\x4f\x55\x52\x2f\x40\x64\x42\x3b\x43\x3a\x48\x39\x4b\x39'\
b'\x4d\x39\x51\x3b\x52\x3c\x52\x3c\x53\x3b\x55\x3a\x58\x39\x59'\
b'\x39\x5c\x39\x60\x3b\x62\x3e\x62\x42\x62\x45\x62\x52\x5e\x52'\
b'\x5e\x45\x5e\x43\x5e\x40\x5c\x3e\x5a\x3d\x59\x3d\x57\x3d\x54'\
b'\x3e\x53\x3f\x54\x40\x54\x43\x54\x45\x54\x52\x50\x52\x50\x45'\
b'\x50\x43\x4f\x40\x4e\x3e\x4c\x3d\x4b\x3d\x4a\x3d\x49\x3d\x47'\
b'\x3d\x46\x3e\x46\x3e\x46\x52\x42\x52\x42\x3b\x19\x46\x5e\x48'\
b'\x3b\x4a\x3a\x4f\x39\x52\x39\x55\x39\x59\x3b\x5b\x3e\x5c\x42'\
b'\x5c\x45\x5c\x52\x57\x52\x57\x45\x57\x43\x57\x40\x55\x3e\x53'\
b'\x3d\x51\x3d\x51\x3d\x4f\x3d\x4e\x3d\x4d\x3e\x4d\x3e\x4d\x52'\
b'\x48\x52\x48\x3b\x23\x45\x5f\x5d\x46\x5d\x49\x5c\x4d\x59\x51'\
b'\x54\x53\x52\x53\x50\x53\x4b\x51\x48\x4d\x47\x49\x47\x46\x47'\
b'\x43\x48\x3f\x4b\x3b\x50\x39\x52\x39\x54\x39\x59\x3b\x5c\x3f'\
b'\x5d\x43\x5d\x46\x20\x52\x59\x46\x59\x42\x55\x3d\x52\x3d\x4f'\
b'\x3d\x4b\x42\x4b\x46\x4b\x4a\x4f\x4f\x52\x4f\x55\x4f\x59\x4a'\
b'\x59\x46\x25\x45\x5f\x58\x46\x58\x42\x54\x3d\x50\x3d\x4f\x3d'\
b'\x4c\x3e\x4c\x3e\x4c\x4d\x4d\x4e\x4f\x4f\x51\x4f\x53\x4f\x56'\
b'\x4d\x57\x4b\x58\x48\x58\x46\x20\x52\x5d\x46\x5d\x49\x5b\x4d'\
b'\x58\x51\x54\x53\x52\x53\x50\x53\x4d\x51\x4c\x51\x4c\x5b\x47'\
b'\x5b\x47\x3b\x49\x3a\x4e\x39\x51\x39\x53\x39\x58\x3b\x5b\x3e'\
b'\x5d\x43\x5d\x46\x25\x45\x5f\x4c\x46\x4c\x48\x4d\x4b\x4e\x4d'\
b'\x51\x4f\x53\x4f\x55\x4f\x57\x4e\x58\x4d\x58\x3e\x58\x3e\x55'\
b'\x3d\x54\x3d\x50\x3d\x4c\x42\x4c\x46\x20\x52\x47\x46\x47\x43'\
b'\x49\x3e\x4c\x3b\x51\x39\x53\x39\x56\x39\x5b\x3a\x5d\x3b\x5d'\
b'\x5b\x58\x5b\x58\x51\x57\x51\x54\x53\x52\x53\x50\x53\x4c\x51'\
b'\x49\x4d\x47\x49\x47\x46\x13\x49\x5b\x54\x39\x55\x39\x56\x3a'\
b'\x57\x3a\x59\x3a\x59\x3a\x58\x3e\x58\x3e\x55\x3d\x53\x3d\x52'\
b'\x3d\x50\x3e\x4f\x3e\x4f\x52\x4b\x52\x4b\x3b\x4d\x3a\x51\x39'\
b'\x54\x39\x2f\x48\x5c\x51\x4f\x54\x4f\x56\x4e\x56\x4c\x56\x4a'\
b'\x54\x49\x51\x47\x4f\x47\x4d\x46\x4b\x44\x4a\x42\x4a\x40\x4a'\
b'\x3d\x4f\x39\x53\x39\x54\x39\x56\x3a\x57\x3a\x59\x3a\x59\x3a'\
b'\x58\x3e\x58\x3e\x55\x3d\x53\x3d\x51\x3d\x4e\x3e\x4e\x40\x4e'\
b'\x41\x4f\x42\x50\x43\x52\x44\x53\x44\x55\x45\x58\x46\x59\x48'\
b'\x5a\x4a\x5a\x4c\x5a\x4f\x56\x53\x51\x53\x4e\x53\x4a\x51\x4a'\
b'\x51\x4a\x4e\x4b\x4e\x4e\x4f\x51\x4f\x19\x49\x5b\x4f\x3a\x58'\
b'\x3a\x58\x3e\x4f\x3e\x4f\x49\x4f\x4a\x50\x4d\x51\x4e\x52\x4f'\
b'\x54\x4f\x56\x4f\x58\x4e\x58\x4e\x59\x51\x59\x52\x55\x53\x53'\
b'\x53\x51\x53\x4e\x51\x4c\x4f\x4b\x4b\x4b\x49\x4b\x33\x4f\x33'\
b'\x4f\x3a\x17\x46\x5e\x5c\x51\x5a\x52\x55\x53\x52\x53\x4f\x53'\
b'\x4c\x51\x49\x4e\x48\x4a\x48\x47\x48\x3a\x4d\x3a\x4d\x47\x4d'\
b'\x4b\x4f\x4f\x53\x4f\x53\x4f\x55\x4f\x56\x4e\x57\x4e\x57\x4e'\
b'\x57\x3a\x5c\x3a\x5c\x51\x14\x45\x5f\x5d\x3a\x5b\x41\x56\x4d'\
b'\x54\x52\x50\x52\x4e\x4d\x49\x41\x47\x3a\x4c\x3a\x4c\x3c\x4e'\
b'\x41\x50\x46\x51\x4b\x52\x4d\x53\x4b\x55\x46\x56\x41\x58\x3c'\
b'\x58\x3a\x5d\x3a\x26\x3f\x65\x57\x52\x56\x4f\x53\x46\x52\x42'\
b'\x51\x46\x4e\x4f\x4d\x52\x49\x52\x47\x4d\x43\x41\x41\x3a\x46'\
b'\x3a\x46\x3c\x47\x41\x49\x46\x4a\x4b\x4b\x4d\x4c\x4b\x4d\x46'\
b'\x4f\x41\x50\x3c\x50\x3a\x54\x3a\x54\x3c\x56\x41\x57\x46\x58'\
b'\x4b\x59\x4d\x5a\x4b\x5b\x46\x5d\x41\x5e\x3c\x5f\x3a\x63\x3a'\
b'\x61\x41\x5d\x4d\x5b\x52\x57\x52\x19\x45\x5f\x58\x52\x58\x51'\
b'\x56\x4e\x55\x4c\x53\x49\x52\x48\x51\x49\x4f\x4c\x4d\x4f\x4c'\
b'\x51\x4b\x52\x47\x52\x49\x4f\x4d\x48\x4f\x45\x47\x3a\x4c\x3a'\
b'\x52\x42\x58\x3a\x5c\x3a\x55\x45\x57\x48\x5b\x4f\x5d\x52\x58'\
b'\x52\x22\x45\x5f\x48\x56\x48\x57\x4a\x57\x4b\x57\x4d\x57\x50'\
b'\x55\x51\x52\x4e\x4d\x49\x40\x48\x3a\x4c\x3a\x4d\x3c\x4e\x41'\
b'\x50\x46\x52\x4b\x53\x4d\x55\x49\x57\x3f\x59\x3a\x5d\x3a\x5b'\
b'\x41\x57\x4d\x55\x53\x54\x55\x52\x58\x50\x5a\x4d\x5b\x4b\x5b'\
b'\x4a\x5b\x49\x5b\x48\x5a\x47\x5a\x47\x5a\x48\x56\x13\x47\x5d'\
b'\x5b\x3d\x5a\x3e\x57\x42\x53\x47\x4f\x4c\x4e\x4e\x5b\x4e\x5b'\
b'\x52\x49\x52\x49\x4f\x4a\x4d\x4d\x48\x51\x43\x54\x3f\x55\x3e'\
b'\x49\x3e\x49\x3a\x5b\x3a\x5b\x3d\x2a\x49\x5b\x4b\x43\x4d\x43'\
b'\x4e\x42\x4f\x40\x50\x3f\x50\x3e\x50\x36\x50\x34\x50\x31\x53'\
b'\x2f\x56\x2e\x58\x2e\x59\x2e\x59\x31\x56\x31\x54\x33\x54\x36'\
b'\x54\x3d\x54\x40\x52\x43\x51\x44\x52\x45\x54\x48\x54\x4b\x54'\
b'\x53\x54\x55\x56\x57\x59\x57\x59\x5b\x58\x5b\x56\x5b\x53\x5a'\
b'\x50\x57\x50\x55\x50\x53\x50\x4a\x50\x49\x4f\x48\x4e\x47\x4d'\
b'\x46\x4b\x46\x4b\x43\x05\x4e\x56\x50\x2e\x54\x2e\x54\x5b\x50'\
b'\x5b\x50\x2e\x2a\x49\x5b\x59\x46\x57\x46\x56\x47\x55\x48\x54'\
b'\x49\x54\x4a\x54\x53\x54\x55\x54\x57\x51\x5a\x4e\x5b\x4c\x5b'\
b'\x4b\x5b\x4b\x57\x4e\x57\x50\x55\x50\x53\x50\x4b\x50\x48\x52'\
b'\x45\x53\x44\x52\x43\x50\x40\x50\x3d\x50\x36\x50\x33\x4e\x31'\
b'\x4b\x31\x4b\x2e\x4c\x2e\x4e\x2e\x51\x2f\x54\x31\x54\x34\x54'\
b'\x36\x54\x3e\x54\x3f\x55\x40\x56\x42\x57\x43\x59\x43\x59\x46'\
b'\x23\x45\x5f\x5d\x42\x5d\x42\x5c\x45\x5b\x47\x58\x48\x57\x48'\
b'\x55\x48\x53\x47\x52\x46\x51\x45\x4e\x44\x4d\x44\x4c\x44\x4b'\
b'\x45\x4b\x46\x4a\x47\x4a\x48\x47\x47\x47\x46\x48\x44\x49\x42'\
b'\x4c\x40\x4d\x40\x4f\x40\x51\x41\x52\x42\x53\x43\x56\x44\x57'\
b'\x44\x58\x44\x59\x44\x59\x43\x5a\x41\x5a\x41\x5d\x42\x19\x4d'\
b'\x57\x54\x3b\x54\x3f\x54\x45\x53\x48\x51\x48\x50\x45\x50\x3f'\
b'\x50\x3b\x50\x32\x54\x32\x54\x3b\x20\x52\x55\x50\x55\x51\x53'\
b'\x53\x52\x53\x51\x53\x4f\x51\x4f\x50\x4f\x4e\x51\x4c\x52\x4c'\
b'\x53\x4c\x55\x4e\x55\x50'

_index =\
b'\x00\x00\x03\x00\x38\x00\x69\x00\xb2\x00\x1f\x01\xbc\x01\x57'\
b'\x02\x70\x02\x91\x02\xb2\x02\x11\x03\x2e\x03\x4f\x03\x5c\x03'\
b'\x79\x03\x86\x03\xcf\x03\xee\x03\x4d\x04\xc4\x04\xf9\x04\x4e'\
b'\x05\xb3\x05\xd6\x05\x6f\x06\xd4\x06\x0d\x07\x4a\x07\x5d\x07'\
b'\x76\x07\x89\x07\xee\x07\xa3\x08\xde\x08\x5d\x09\xb2\x09\xf7'\
b'\x09\x14\x0a\x2d\x0a\x82\x0a\x9f\x0a\xac\x0a\xd9\x0a\x14\x0b'\
b'\x25\x0b\x7e\x0b\xab\x0b\x04\x0c\x47\x0c\xb6\x0c\x11\x0d\x78'\
b'\x0d\x8d\x0d\xc2\x0d\xed\x0d\x34\x0e\x69\x0e\x90\x0e\xc1\x0e'\
b'\xd6\x0e\xe3\x0e\xf8\x0e\x0b\x0f\x18\x0f\x25\x0f\x9a\x0f\xe7'\
b'\x0f\x30\x10\x7d\x10\xce\x10\xfb\x10\x60\x11\x99\x11\xc2\x11'\
b'\x03\x12\x3e\x12\x5b\x12\xbc\x12\xf1\x12\x3a\x13\x87\x13\xd4'\
b'\x13\xfd\x13\x5e\x14\x93\x14\xc4\x14\xef\x14\x3e\x15\x73\x15'\
b'\xba\x15\xe3\x15\x3a\x16\x47\x16\x9e\x16\xe7\x16'


FONT = memoryview(_font)
INDEX = memoryview(_index)
