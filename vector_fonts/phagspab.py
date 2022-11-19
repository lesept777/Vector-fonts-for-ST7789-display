FIRST = 32
LAST = 127
WIDTH = 35
HEIGHT = 35

_font =\
b'\x01\x4e\x56\x13\x4d\x57\x55\x39\x54\x4a\x50\x4a\x4f\x39\x55'\
b'\x39\x20\x52\x52\x52\x51\x52\x4f\x51\x4f\x50\x4f\x4e\x51\x4d'\
b'\x52\x4d\x53\x4d\x55\x4e\x55\x50\x55\x51\x53\x52\x52\x52\x0b'\
b'\x4a\x5a\x58\x39\x57\x41\x54\x41\x53\x39\x58\x39\x20\x52\x51'\
b'\x39\x50\x41\x4d\x41\x4c\x39\x51\x39\x23\x46\x5e\x5c\x40\x5b'\
b'\x43\x58\x43\x57\x47\x5b\x47\x5a\x4a\x56\x4a\x55\x50\x52\x50'\
b'\x53\x4a\x4f\x4a\x4e\x50\x4a\x50\x4b\x4a\x48\x4a\x49\x47\x4c'\
b'\x47\x4d\x43\x4a\x43\x4a\x40\x4e\x40\x4f\x3a\x52\x3a\x51\x40'\
b'\x55\x40\x56\x3a\x5a\x3a\x59\x40\x5c\x40\x20\x52\x54\x43\x50'\
b'\x43\x50\x47\x53\x47\x54\x43\x2e\x48\x5c\x53\x52\x53\x56\x51'\
b'\x56\x51\x52\x4d\x52\x4a\x50\x4a\x4c\x4b\x4c\x4f\x4e\x51\x4e'\
b'\x51\x48\x4d\x46\x4a\x43\x4a\x40\x4a\x3e\x4e\x3a\x51\x39\x51'\
b'\x36\x53\x36\x53\x39\x57\x3a\x59\x3b\x59\x3f\x56\x3e\x53\x3d'\
b'\x53\x44\x57\x45\x5a\x49\x5a\x4b\x5a\x4e\x57\x51\x53\x52\x20'\
b'\x52\x51\x43\x51\x3d\x4e\x3e\x4e\x40\x4e\x42\x51\x43\x20\x52'\
b'\x53\x49\x53\x4e\x56\x4d\x56\x4b\x56\x4a\x53\x49\x36\x42\x62'\
b'\x4a\x46\x48\x46\x44\x43\x44\x40\x44\x3d\x48\x39\x4b\x39\x4d'\
b'\x39\x50\x3c\x50\x3f\x50\x42\x4d\x46\x4a\x46\x20\x52\x4a\x3c'\
b'\x48\x3c\x48\x40\x48\x43\x4a\x43\x4d\x43\x4d\x3f\x4d\x3c\x4a'\
b'\x3c\x20\x52\x5c\x39\x4c\x52\x48\x52\x58\x39\x5c\x39\x20\x52'\
b'\x59\x52\x57\x52\x54\x4f\x54\x4c\x54\x49\x57\x46\x5a\x46\x5d'\
b'\x46\x60\x49\x60\x4c\x60\x4f\x5c\x52\x59\x52\x20\x52\x5a\x49'\
b'\x57\x49\x57\x4c\x57\x4f\x5a\x4f\x5c\x4f\x5c\x4c\x5c\x4a\x5b'\
b'\x49\x5a\x49\x6f\x42\x62\x5c\x52\x5b\x52\x5a\x52\x58\x51\x57'\
b'\x50\x56\x4f\x56\x50\x54\x51\x52\x52\x4f\x52\x4d\x52\x4b\x52'\
b'\x48\x51\x45\x50\x44\x4d\x44\x4b\x44\x49\x45\x47\x47\x45\x49'\
b'\x44\x4a\x44\x49\x43\x48\x42\x48\x41\x47\x40\x47\x3f\x47\x3d'\
b'\x48\x3b\x4a\x3a\x4d\x39\x4e\x39\x50\x39\x53\x3a\x54\x3b\x56'\
b'\x3d\x56\x3e\x56\x40\x53\x43\x51\x44\x52\x44\x54\x45\x55\x47'\
b'\x56\x48\x57\x49\x58\x47\x5a\x43\x5a\x41\x5a\x41\x59\x3f\x59'\
b'\x3f\x5e\x3f\x5e\x3f\x5e\x40\x5e\x41\x5e\x43\x5e\x46\x5c\x49'\
b'\x5a\x4b\x59\x4c\x5a\x4d\x5c\x4e\x5d\x4e\x5e\x4e\x5f\x4e\x60'\
b'\x4e\x60\x52\x5f\x52\x5d\x52\x5c\x52\x20\x52\x4e\x4e\x4f\x4e'\
b'\x50\x4e\x52\x4d\x53\x4c\x54\x4c\x53\x4b\x51\x49\x50\x47\x4e'\
b'\x46\x4d\x46\x4c\x46\x4b\x47\x4a\x48\x4a\x4a\x4a\x4b\x4a\x4b'\
b'\x4a\x4d\x4b\x4e\x4d\x4e\x4e\x4e\x20\x52\x51\x3f\x51\x3e\x50'\
b'\x3e\x50\x3d\x4f\x3d\x4e\x3d\x4e\x3d\x4d\x3d\x4c\x3e\x4c\x3e'\
b'\x4c\x3f\x4c\x40\x4d\x41\x4e\x42\x4e\x42\x50\x41\x50\x40\x51'\
b'\x3f\x51\x3f\x05\x4e\x56\x54\x39\x54\x41\x50\x41\x50\x39\x54'\
b'\x39\x0b\x4b\x59\x57\x58\x53\x58\x4d\x51\x4d\x49\x4d\x40\x53'\
b'\x39\x57\x39\x52\x40\x52\x49\x52\x51\x57\x58\x0b\x4b\x59\x51'\
b'\x58\x4d\x58\x52\x51\x52\x49\x52\x40\x4d\x39\x51\x39\x57\x40'\
b'\x57\x49\x57\x51\x51\x58\x10\x49\x5b\x59\x40\x54\x41\x57\x44'\
b'\x54\x46\x52\x42\x50\x46\x4d\x44\x50\x41\x4b\x40\x4c\x3d\x51'\
b'\x3e\x50\x39\x54\x39\x53\x3e\x58\x3d\x59\x40\x0d\x48\x5c\x5a'\
b'\x4a\x54\x4a\x54\x50\x50\x50\x50\x4a\x4a\x4a\x4a\x46\x50\x46'\
b'\x50\x40\x54\x40\x54\x46\x5a\x46\x5a\x4a\x05\x4d\x57\x55\x4e'\
b'\x53\x56\x4f\x56\x50\x4e\x55\x4e\x05\x4b\x59\x57\x4b\x4d\x4b'\
b'\x4d\x47\x57\x47\x57\x4b\x0d\x4d\x57\x52\x52\x51\x52\x4f\x51'\
b'\x4f\x50\x4f\x4e\x51\x4d\x52\x4d\x53\x4d\x55\x4e\x55\x50\x55'\
b'\x51\x53\x52\x52\x52\x05\x48\x5c\x5a\x39\x4e\x56\x4a\x56\x56'\
b'\x39\x5a\x39\x15\x47\x5d\x52\x52\x49\x52\x49\x46\x49\x40\x4e'\
b'\x39\x52\x39\x5b\x39\x5b\x46\x5b\x4c\x56\x52\x52\x52\x20\x52'\
b'\x52\x3d\x4f\x3d\x4f\x46\x4f\x4e\x52\x4e\x55\x4e\x55\x46\x55'\
b'\x3d\x52\x3d\x0b\x48\x5c\x5a\x52\x4a\x52\x4a\x4e\x4f\x4e\x4f'\
b'\x3e\x4a\x40\x4a\x3b\x55\x39\x55\x4e\x5a\x4e\x5a\x52\x17\x48'\
b'\x5c\x50\x4d\x50\x4e\x5a\x4e\x5a\x52\x4a\x52\x4a\x4e\x51\x47'\
b'\x53\x45\x55\x42\x55\x41\x55\x3d\x51\x3d\x4e\x3d\x4b\x40\x4b'\
b'\x3b\x4e\x39\x52\x39\x56\x39\x5a\x3d\x5a\x40\x5a\x44\x55\x49'\
b'\x50\x4d\x24\x48\x5c\x4a\x51\x4a\x4c\x4d\x4e\x50\x4e\x52\x4e'\
b'\x54\x4d\x54\x4b\x54\x49\x51\x48\x4f\x48\x4d\x48\x4d\x43\x4f'\
b'\x43\x54\x43\x54\x40\x54\x3d\x50\x3d\x4d\x3d\x4b\x3f\x4b\x3a'\
b'\x4e\x39\x51\x39\x55\x39\x59\x3c\x59\x3f\x59\x44\x54\x45\x54'\
b'\x45\x57\x46\x5a\x49\x5a\x4b\x5a\x4e\x55\x52\x50\x52\x4d\x52'\
b'\x4a\x51\x16\x47\x5d\x5b\x4d\x58\x4d\x58\x52\x53\x52\x53\x4d'\
b'\x49\x4d\x49\x49\x53\x39\x58\x39\x58\x49\x5b\x49\x5b\x4d\x20'\
b'\x52\x53\x3f\x53\x3f\x53\x40\x52\x41\x4d\x49\x53\x49\x53\x41'\
b'\x53\x40\x53\x3f\x1a\x48\x5c\x4a\x51\x4a\x4d\x4d\x4e\x50\x4e'\
b'\x52\x4e\x54\x4c\x54\x4b\x54\x47\x4f\x47\x4d\x47\x4b\x47\x4b'\
b'\x39\x59\x39\x59\x3e\x50\x3e\x50\x43\x51\x43\x52\x43\x55\x43'\
b'\x5a\x47\x5a\x4a\x5a\x4e\x55\x52\x50\x52\x4d\x52\x4a\x51\x25'\
b'\x47\x5d\x59\x3a\x59\x3e\x57\x3d\x55\x3d\x52\x3d\x4f\x41\x4f'\
b'\x45\x4f\x45\x51\x42\x54\x42\x57\x42\x5b\x46\x5b\x4a\x5b\x4e'\
b'\x56\x52\x52\x52\x4e\x52\x49\x4c\x49\x47\x49\x41\x4f\x39\x54'\
b'\x39\x57\x39\x59\x3a\x20\x52\x52\x46\x51\x46\x4f\x48\x4f\x4a'\
b'\x4f\x4c\x51\x4e\x52\x4e\x54\x4e\x55\x4c\x55\x4a\x55\x46\x52'\
b'\x46\x08\x47\x5d\x5b\x3c\x52\x52\x4c\x52\x55\x3e\x49\x3e\x49'\
b'\x39\x5b\x39\x5b\x3c\x30\x47\x5d\x4e\x45\x4e\x45\x4a\x43\x4a'\
b'\x40\x4a\x3d\x4f\x39\x52\x39\x56\x39\x5a\x3d\x5a\x3f\x5a\x43'\
b'\x55\x45\x55\x45\x58\x46\x5b\x49\x5b\x4b\x5b\x4f\x56\x52\x52'\
b'\x52\x4e\x52\x49\x4f\x49\x4c\x49\x47\x4e\x45\x20\x52\x55\x40'\
b'\x55\x3e\x53\x3d\x52\x3d\x51\x3d\x4f\x3f\x4f\x40\x4f\x42\x52'\
b'\x43\x55\x42\x55\x40\x20\x52\x52\x47\x4e\x49\x4e\x4b\x4e\x4d'\
b'\x51\x4f\x52\x4f\x54\x4f\x56\x4d\x56\x4b\x56\x49\x52\x47\x26'\
b'\x47\x5d\x4b\x51\x4b\x4d\x4d\x4e\x4f\x4e\x52\x4e\x55\x4a\x55'\
b'\x47\x55\x47\x54\x49\x50\x49\x4d\x49\x49\x45\x49\x42\x49\x3e'\
b'\x4e\x39\x52\x39\x56\x39\x5b\x3f\x5b\x45\x5b\x4b\x55\x52\x50'\
b'\x52\x4d\x52\x4b\x51\x20\x52\x52\x3d\x50\x3d\x4f\x3f\x4f\x41'\
b'\x4f\x43\x50\x45\x52\x45\x53\x45\x55\x43\x55\x42\x55\x40\x53'\
b'\x3d\x52\x3d\x1b\x4d\x57\x52\x46\x51\x46\x4f\x44\x4f\x43\x4f'\
b'\x42\x51\x40\x52\x40\x53\x40\x55\x42\x55\x43\x55\x44\x53\x46'\
b'\x52\x46\x20\x52\x52\x52\x51\x52\x4f\x51\x4f\x50\x4f\x4e\x51'\
b'\x4d\x52\x4d\x53\x4d\x55\x4e\x55\x50\x55\x51\x53\x52\x52\x52'\
b'\x13\x4c\x58\x52\x46\x51\x46\x4f\x44\x4f\x43\x4f\x42\x51\x40'\
b'\x53\x40\x54\x40\x56\x42\x56\x43\x56\x44\x54\x46\x52\x46\x20'\
b'\x52\x55\x4e\x53\x56\x4e\x56\x50\x4e\x55\x4e\x09\x48\x5c\x5a'\
b'\x51\x4a\x4a\x4a\x47\x5a\x3f\x5a\x43\x4f\x48\x4f\x48\x5a\x4d'\
b'\x5a\x51\x0b\x48\x5c\x5a\x46\x4a\x46\x4a\x43\x5a\x43\x5a\x46'\
b'\x20\x52\x5a\x4d\x4a\x4d\x4a\x4a\x5a\x4a\x5a\x4d\x09\x48\x5c'\
b'\x5a\x49\x4a\x51\x4a\x4d\x55\x48\x55\x48\x4a\x43\x4a\x3f\x5a'\
b'\x47\x5a\x49\x3f\x49\x5b\x4f\x4b\x4e\x4a\x4e\x49\x4e\x49\x4e'\
b'\x48\x4f\x47\x4f\x46\x50\x45\x51\x44\x51\x44\x52\x43\x53\x42'\
b'\x53\x41\x53\x40\x53\x3f\x53\x3f\x52\x3e\x51\x3e\x51\x3e\x4f'\
b'\x3e\x4c\x3f\x4b\x40\x4b\x3b\x4d\x3a\x50\x39\x51\x39\x53\x39'\
b'\x56\x3a\x58\x3b\x59\x3e\x59\x3f\x59\x40\x58\x42\x57\x44\x56'\
b'\x45\x55\x46\x55\x46\x54\x47\x53\x48\x53\x49\x53\x49\x53\x4a'\
b'\x53\x4b\x53\x4b\x4f\x4b\x20\x52\x51\x52\x50\x52\x4f\x52\x4e'\
b'\x51\x4e\x50\x4e\x4e\x4f\x4e\x50\x4d\x51\x4d\x52\x4d\x53\x4e'\
b'\x54\x4e\x54\x50\x54\x51\x53\x52\x53\x52\x51\x52\x41\x42\x62'\
b'\x54\x4c\x54\x4c\x53\x4f\x50\x4f\x4e\x4f\x4b\x4c\x4b\x48\x4b'\
b'\x45\x4f\x40\x52\x40\x54\x40\x55\x42\x55\x42\x55\x40\x59\x40'\
b'\x58\x47\x58\x49\x58\x4c\x59\x4c\x5b\x4c\x5d\x48\x5d\x45\x5d'\
b'\x41\x57\x3c\x53\x3c\x4e\x3c\x48\x43\x48\x48\x48\x4d\x4d\x52'\
b'\x52\x52\x56\x52\x59\x51\x59\x54\x56\x55\x52\x55\x4b\x55\x44'\
b'\x4e\x44\x48\x44\x42\x4c\x39\x53\x39\x59\x39\x60\x40\x60\x45'\
b'\x60\x4a\x5c\x4f\x58\x4f\x57\x4f\x55\x4d\x54\x4c\x20\x52\x52'\
b'\x43\x51\x43\x4f\x46\x4f\x48\x4f\x4a\x50\x4c\x51\x4c\x53\x4c'\
b'\x55\x48\x55\x46\x55\x44\x53\x43\x52\x43\x13\x44\x60\x5e\x52'\
b'\x58\x52\x56\x4d\x4e\x4d\x4c\x52\x46\x52\x4f\x39\x55\x39\x5e'\
b'\x52\x20\x52\x55\x48\x52\x40\x52\x3f\x52\x3e\x52\x3e\x52\x3f'\
b'\x51\x40\x4f\x48\x55\x48\x26\x47\x5d\x49\x52\x49\x39\x52\x39'\
b'\x56\x39\x5a\x3d\x5a\x3f\x5a\x41\x58\x44\x55\x45\x55\x45\x58'\
b'\x45\x5b\x48\x5b\x4b\x5b\x4e\x56\x52\x52\x52\x49\x52\x20\x52'\
b'\x4e\x3e\x4e\x43\x51\x43\x52\x43\x54\x42\x54\x40\x54\x3e\x50'\
b'\x3e\x4e\x3e\x20\x52\x4e\x47\x4e\x4e\x51\x4e\x53\x4e\x55\x4c'\
b'\x55\x4b\x55\x49\x53\x47\x51\x47\x4e\x47\x17\x46\x5e\x5c\x51'\
b'\x59\x52\x55\x52\x4f\x52\x48\x4c\x48\x46\x48\x40\x50\x39\x56'\
b'\x39\x59\x39\x5c\x3a\x5c\x3f\x59\x3e\x56\x3e\x52\x3e\x4e\x42'\
b'\x4e\x46\x4e\x49\x52\x4e\x56\x4e\x59\x4e\x5c\x4c\x5c\x51\x14'\
b'\x45\x5f\x47\x52\x47\x39\x50\x39\x5d\x39\x5d\x45\x5d\x4b\x56'\
b'\x52\x50\x52\x47\x52\x20\x52\x4d\x3e\x4d\x4e\x4f\x4e\x53\x4e'\
b'\x57\x49\x57\x46\x57\x42\x53\x3e\x4f\x3e\x4d\x3e\x0d\x49\x5b'\
b'\x59\x52\x4b\x52\x4b\x39\x59\x39\x59\x3e\x50\x3e\x50\x43\x58'\
b'\x43\x58\x48\x50\x48\x50\x4e\x59\x4e\x59\x52\x0b\x49\x5b\x59'\
b'\x3e\x50\x3e\x50\x44\x58\x44\x58\x48\x50\x48\x50\x52\x4b\x52'\
b'\x4b\x39\x59\x39\x59\x3e\x1b\x45\x5f\x5d\x50\x59\x52\x54\x52'\
b'\x4e\x52\x47\x4c\x47\x46\x47\x40\x4f\x39\x55\x39\x59\x39\x5c'\
b'\x3a\x5c\x3f\x59\x3e\x55\x3e\x51\x3e\x4d\x42\x4d\x46\x4d\x4a'\
b'\x51\x4e\x54\x4e\x56\x4e\x57\x4d\x57\x48\x52\x48\x52\x44\x5d'\
b'\x44\x5d\x50\x0d\x45\x5f\x5d\x52\x57\x52\x57\x48\x4d\x48\x4d'\
b'\x52\x47\x52\x47\x39\x4d\x39\x4d\x43\x57\x43\x57\x39\x5d\x39'\
b'\x5d\x52\x0d\x4b\x59\x57\x39\x57\x3e\x55\x3e\x55\x4e\x57\x4e'\
b'\x57\x52\x4d\x52\x4d\x4e\x4f\x4e\x4f\x3e\x4d\x3e\x4d\x39\x57'\
b'\x39\x0e\x4a\x5a\x58\x48\x58\x4d\x54\x52\x4f\x52\x4d\x52\x4c'\
b'\x52\x4c\x4d\x4d\x4e\x4f\x4e\x53\x4e\x53\x48\x53\x39\x58\x39'\
b'\x58\x48\x12\x46\x5e\x5c\x52\x55\x52\x4e\x47\x4e\x47\x4d\x46'\
b'\x4d\x46\x4d\x52\x48\x52\x48\x39\x4d\x39\x4d\x45\x4d\x45\x4e'\
b'\x45\x4e\x44\x55\x39\x5b\x39\x53\x45\x5c\x52\x07\x49\x5b\x59'\
b'\x52\x4b\x52\x4b\x39\x50\x39\x50\x4e\x59\x4e\x59\x52\x1d\x42'\
b'\x62\x60\x52\x5b\x52\x5b\x43\x5b\x41\x5b\x3e\x5b\x3e\x5a\x40'\
b'\x5a\x41\x54\x52\x50\x52\x4a\x42\x49\x41\x49\x3e\x49\x3e\x49'\
b'\x42\x49\x44\x49\x52\x44\x52\x44\x39\x4c\x39\x51\x48\x52\x4a'\
b'\x52\x4c\x52\x4c\x53\x49\x53\x48\x58\x39\x60\x39\x60\x52\x15'\
b'\x45\x5f\x5d\x52\x57\x52\x4d\x43\x4c\x41\x4c\x41\x4c\x41\x4c'\
b'\x42\x4c\x45\x4c\x52\x47\x52\x47\x39\x4d\x39\x57\x48\x57\x49'\
b'\x58\x4a\x58\x4a\x58\x4a\x58\x47\x58\x39\x5d\x39\x5d\x52\x1b'\
b'\x44\x60\x52\x52\x4d\x52\x46\x4c\x46\x46\x46\x40\x4d\x39\x52'\
b'\x39\x58\x39\x5e\x40\x5e\x46\x5e\x4b\x57\x52\x52\x52\x20\x52'\
b'\x52\x3e\x4f\x3e\x4c\x42\x4c\x46\x4c\x49\x4f\x4e\x52\x4e\x55'\
b'\x4e\x58\x4a\x58\x46\x58\x42\x55\x3e\x52\x3e\x14\x47\x5d\x4f'\
b'\x4a\x4f\x52\x49\x52\x49\x39\x52\x39\x5b\x39\x5b\x41\x5b\x45'\
b'\x56\x4a\x51\x4a\x4f\x4a\x20\x52\x4f\x3e\x4f\x45\x51\x45\x55'\
b'\x45\x55\x42\x55\x3e\x51\x3e\x4f\x3e\x37\x43\x61\x51\x3e\x4e'\
b'\x3e\x4d\x40\x4b\x42\x4b\x46\x4b\x49\x4d\x4c\x4e\x4e\x51\x4e'\
b'\x54\x4e\x56\x4c\x57\x4a\x57\x46\x57\x42\x56\x40\x54\x3e\x51'\
b'\x3e\x20\x52\x56\x52\x56\x52\x58\x54\x5a\x54\x5b\x55\x5c\x55'\
b'\x5d\x55\x5d\x55\x5e\x55\x5f\x54\x5f\x54\x5f\x59\x5e\x59\x5c'\
b'\x59\x5b\x59\x59\x59\x57\x58\x54\x56\x52\x54\x50\x52\x4e\x52'\
b'\x4a\x50\x47\x4d\x45\x49\x45\x46\x45\x40\x48\x3d\x4c\x39\x51'\
b'\x39\x57\x39\x5a\x3d\x5d\x40\x5d\x46\x5d\x4a\x5b\x4d\x59\x50'\
b'\x56\x52\x26\x46\x5e\x5c\x52\x56\x52\x52\x4c\x52\x4b\x51\x4a'\
b'\x50\x49\x4f\x49\x4f\x49\x4d\x49\x4d\x52\x48\x52\x48\x39\x50'\
b'\x39\x59\x39\x59\x40\x59\x41\x59\x44\x57\x45\x55\x47\x54\x47'\
b'\x54\x47\x54\x47\x55\x48\x56\x49\x57\x4a\x58\x4b\x5c\x52\x20'\
b'\x52\x4d\x3e\x4d\x44\x50\x44\x51\x44\x52\x43\x54\x42\x54\x41'\
b'\x54\x3e\x50\x3e\x4d\x3e\x37\x48\x5c\x4a\x51\x4a\x4c\x4b\x4d'\
b'\x4f\x4e\x50\x4e\x51\x4e\x53\x4e\x54\x4d\x55\x4c\x55\x4c\x55'\
b'\x4b\x54\x4a\x52\x49\x50\x48\x4f\x47\x4c\x46\x4a\x43\x4a\x40'\
b'\x4a\x3e\x4b\x3c\x4e\x3a\x51\x39\x53\x39\x55\x39\x58\x3a\x59'\
b'\x3a\x59\x3f\x59\x3f\x57\x3e\x56\x3e\x54\x3d\x54\x3d\x53\x3d'\
b'\x51\x3e\x50\x3e\x4f\x3f\x4f\x40\x4f\x41\x50\x41\x51\x42\x53'\
b'\x43\x54\x44\x56\x44\x58\x46\x5a\x47\x5a\x4a\x5a\x4b\x5a\x4d'\
b'\x59\x50\x56\x52\x53\x52\x51\x52\x4f\x52\x4b\x52\x4a\x51\x09'\
b'\x46\x5e\x5c\x3e\x55\x3e\x55\x52\x4f\x52\x4f\x3e\x48\x3e\x48'\
b'\x39\x5c\x39\x5c\x3e\x0f\x46\x5e\x5c\x47\x5c\x52\x52\x52\x48'\
b'\x52\x48\x48\x48\x39\x4d\x39\x4d\x48\x4d\x4e\x52\x4e\x57\x4e'\
b'\x57\x48\x57\x39\x5c\x39\x5c\x47\x0d\x44\x60\x5e\x39\x55\x52'\
b'\x4f\x52\x46\x39\x4c\x39\x52\x4b\x52\x4c\x52\x4d\x52\x4d\x52'\
b'\x4c\x53\x4a\x58\x39\x5e\x39\x1d\x3f\x65\x63\x39\x5d\x52\x57'\
b'\x52\x53\x42\x52\x41\x52\x40\x52\x40\x52\x41\x52\x42\x4e\x52'\
b'\x47\x52\x41\x39\x47\x39\x4a\x4a\x4a\x4b\x4b\x4d\x4b\x4d\x4b'\
b'\x4b\x4b\x4a\x50\x39\x55\x39\x5a\x4a\x5a\x4b\x5a\x4d\x5a\x4d'\
b'\x5a\x4b\x5a\x4a\x5e\x39\x63\x39\x17\x45\x5f\x5d\x52\x57\x52'\
b'\x53\x4a\x52\x4a\x52\x48\x52\x48\x52\x49\x51\x4a\x4d\x52\x47'\
b'\x52\x4e\x46\x47\x39\x4e\x39\x52\x41\x52\x42\x52\x43\x52\x43'\
b'\x53\x42\x53\x41\x57\x39\x5d\x39\x56\x46\x5d\x52\x0f\x45\x5f'\
b'\x5d\x39\x55\x49\x55\x52\x4f\x52\x4f\x49\x47\x39\x4e\x39\x52'\
b'\x43\x52\x43\x52\x45\x52\x45\x52\x43\x53\x43\x57\x39\x5d\x39'\
b'\x0b\x46\x5e\x5c\x52\x48\x52\x48\x4f\x55\x3e\x49\x3e\x49\x39'\
b'\x5c\x39\x5c\x3d\x50\x4e\x5c\x4e\x5c\x52\x09\x4c\x58\x56\x58'\
b'\x4e\x58\x4e\x39\x56\x39\x56\x3d\x52\x3d\x52\x54\x56\x54\x56'\
b'\x58\x05\x48\x5c\x5a\x56\x55\x56\x4a\x39\x4f\x39\x5a\x56\x09'\
b'\x4c\x58\x56\x58\x4e\x58\x4e\x54\x52\x54\x52\x3d\x4e\x3d\x4e'\
b'\x39\x56\x39\x56\x58\x09\x47\x5d\x5b\x48\x57\x48\x52\x3e\x52'\
b'\x3e\x4d\x48\x49\x48\x50\x39\x53\x39\x5b\x48\x05\x49\x5b\x59'\
b'\x57\x4b\x57\x4b\x55\x59\x55\x59\x57\x05\x4b\x59\x57\x3e\x53'\
b'\x3e\x4d\x38\x52\x38\x57\x3e\x23\x48\x5c\x5a\x52\x55\x52\x55'\
b'\x4f\x55\x4f\x53\x52\x50\x52\x4d\x52\x4a\x50\x4a\x4d\x4a\x48'\
b'\x50\x47\x55\x47\x55\x44\x52\x44\x4f\x44\x4c\x46\x4c\x42\x4d'\
b'\x41\x51\x40\x52\x40\x5a\x40\x5a\x48\x5a\x52\x20\x52\x55\x4b'\
b'\x55\x4a\x52\x4a\x4f\x4a\x4f\x4c\x4f\x4d\x50\x4f\x51\x4f\x53'\
b'\x4f\x55\x4c\x55\x4b\x21\x47\x5d\x4e\x50\x4e\x50\x4e\x52\x49'\
b'\x52\x49\x38\x4e\x38\x4e\x43\x4e\x43\x50\x40\x54\x40\x57\x40'\
b'\x5b\x45\x5b\x49\x5b\x4d\x57\x52\x53\x52\x50\x52\x4e\x50\x20'\
b'\x52\x4e\x49\x4e\x4a\x4e\x4c\x50\x4e\x52\x4e\x54\x4e\x56\x4b'\
b'\x56\x49\x56\x47\x54\x44\x52\x44\x50\x44\x4e\x47\x4e\x49\x17'\
b'\x49\x5b\x59\x51\x57\x52\x54\x52\x50\x52\x4b\x4e\x4b\x4a\x4b'\
b'\x45\x50\x40\x55\x40\x58\x40\x59\x41\x59\x45\x57\x44\x55\x44'\
b'\x53\x44\x50\x47\x50\x49\x50\x4c\x53\x4e\x55\x4e\x57\x4e\x59'\
b'\x4d\x59\x51\x21\x47\x5d\x5b\x52\x56\x52\x56\x50\x56\x50\x54'\
b'\x52\x50\x52\x4d\x52\x49\x4e\x49\x4a\x49\x45\x4d\x40\x51\x40'\
b'\x54\x40\x56\x42\x56\x42\x56\x38\x5b\x38\x5b\x52\x20\x52\x56'\
b'\x49\x56\x48\x56\x46\x54\x44\x52\x44\x50\x44\x4e\x47\x4e\x49'\
b'\x4e\x4c\x50\x4e\x52\x4e\x54\x4e\x56\x4c\x56\x49\x1b\x48\x5c'\
b'\x5a\x4b\x4f\x4b\x4f\x4f\x54\x4f\x57\x4f\x59\x4d\x59\x51\x56'\
b'\x52\x53\x52\x4e\x52\x4a\x4e\x4a\x4a\x4a\x45\x4f\x40\x52\x40'\
b'\x56\x40\x5a\x45\x5a\x49\x5a\x4b\x20\x52\x55\x47\x55\x44\x52'\
b'\x44\x51\x44\x4f\x46\x4f\x47\x55\x47\x16\x4a\x5a\x58\x3c\x57'\
b'\x3c\x56\x3c\x54\x3c\x54\x3f\x54\x41\x58\x41\x58\x44\x54\x44'\
b'\x54\x52\x4e\x52\x4e\x44\x4c\x44\x4c\x41\x4e\x41\x4e\x3e\x4e'\
b'\x3b\x52\x38\x56\x38\x57\x38\x58\x38\x58\x3c\x2b\x47\x5d\x5b'\
b'\x50\x5b\x55\x55\x5a\x50\x5a\x4d\x5a\x4b\x59\x4b\x55\x4d\x56'\
b'\x50\x56\x53\x56\x56\x53\x56\x51\x56\x4f\x56\x4f\x54\x52\x50'\
b'\x52\x4d\x52\x49\x4e\x49\x4a\x49\x45\x4d\x40\x51\x40\x54\x40'\
b'\x56\x43\x56\x43\x56\x41\x5b\x41\x5b\x50\x20\x52\x56\x4a\x56'\
b'\x48\x56\x47\x54\x44\x52\x44\x50\x44\x4e\x47\x4e\x4a\x4e\x4c'\
b'\x50\x4e\x52\x4e\x54\x4e\x56\x4c\x56\x4a\x13\x48\x5c\x5a\x52'\
b'\x55\x52\x55\x48\x55\x44\x52\x44\x51\x44\x4f\x46\x4f\x48\x4f'\
b'\x52\x4a\x52\x4a\x38\x4f\x38\x4f\x43\x4f\x43\x51\x40\x54\x40'\
b'\x5a\x40\x5a\x47\x5a\x52\x13\x4d\x57\x52\x3e\x51\x3e\x4f\x3c'\
b'\x4f\x3b\x4f\x3a\x51\x38\x52\x38\x53\x38\x55\x3a\x55\x3b\x55'\
b'\x3c\x53\x3e\x52\x3e\x20\x52\x55\x52\x4f\x52\x4f\x41\x55\x41'\
b'\x55\x52\x1c\x4b\x59\x54\x3e\x53\x3e\x51\x3c\x51\x3b\x51\x3a'\
b'\x53\x38\x54\x38\x55\x38\x57\x3a\x57\x3b\x57\x3c\x55\x3e\x54'\
b'\x3e\x20\x52\x57\x52\x57\x56\x53\x5a\x4f\x5a\x4e\x5a\x4d\x5a'\
b'\x4d\x55\x4e\x56\x4f\x56\x51\x56\x51\x52\x51\x41\x57\x41\x57'\
b'\x52\x0e\x47\x5d\x5b\x52\x54\x52\x4f\x49\x4f\x49\x4f\x52\x49'\
b'\x52\x49\x38\x4f\x38\x4f\x49\x4f\x49\x54\x41\x5a\x41\x54\x49'\
b'\x5b\x52\x05\x4d\x57\x55\x52\x4f\x52\x4f\x38\x55\x38\x55\x52'\
b'\x20\x42\x62\x60\x52\x5b\x52\x5b\x48\x5b\x44\x58\x44\x56\x44'\
b'\x55\x46\x55\x48\x55\x52\x4f\x52\x4f\x48\x4f\x44\x4d\x44\x4b'\
b'\x44\x4a\x46\x4a\x48\x4a\x52\x44\x52\x44\x41\x4a\x41\x4a\x43'\
b'\x4a\x43\x4a\x42\x4d\x40\x4f\x40\x53\x40\x54\x43\x56\x40\x5a'\
b'\x40\x60\x40\x60\x47\x60\x52\x13\x48\x5c\x5a\x52\x55\x52\x55'\
b'\x48\x55\x44\x52\x44\x51\x44\x4f\x46\x4f\x48\x4f\x52\x4a\x52'\
b'\x4a\x41\x4f\x41\x4f\x43\x4f\x43\x51\x40\x55\x40\x5a\x40\x5a'\
b'\x47\x5a\x52\x18\x47\x5d\x52\x52\x4e\x52\x49\x4e\x49\x49\x49'\
b'\x45\x4e\x40\x52\x40\x57\x40\x5b\x45\x5b\x49\x5b\x4d\x56\x52'\
b'\x52\x52\x20\x52\x52\x44\x50\x44\x4e\x47\x4e\x49\x4e\x4e\x52'\
b'\x4e\x56\x4e\x56\x49\x56\x44\x52\x44\x20\x47\x5d\x4e\x50\x4e'\
b'\x50\x4e\x5a\x49\x5a\x49\x41\x4e\x41\x4e\x43\x4e\x43\x50\x40'\
b'\x54\x40\x57\x40\x5b\x45\x5b\x49\x5b\x4d\x57\x52\x53\x52\x50'\
b'\x52\x4e\x50\x20\x52\x4e\x49\x4e\x4a\x4e\x4c\x50\x4e\x52\x4e'\
b'\x54\x4e\x56\x4b\x56\x49\x56\x44\x52\x44\x50\x44\x4e\x47\x4e'\
b'\x49\x21\x47\x5d\x5b\x5a\x56\x5a\x56\x50\x56\x50\x54\x52\x50'\
b'\x52\x4d\x52\x49\x4e\x49\x4a\x49\x45\x4d\x40\x51\x40\x54\x40'\
b'\x56\x43\x56\x43\x56\x41\x5b\x41\x5b\x5a\x20\x52\x56\x4a\x56'\
b'\x48\x56\x47\x54\x44\x52\x44\x50\x44\x4e\x47\x4e\x4a\x4e\x4c'\
b'\x50\x4e\x52\x4e\x54\x4e\x56\x4c\x56\x4a\x11\x4a\x5a\x58\x45'\
b'\x57\x45\x55\x45\x54\x45\x52\x47\x52\x4a\x52\x52\x4c\x52\x4c'\
b'\x41\x52\x41\x52\x44\x52\x44\x53\x40\x56\x40\x57\x40\x58\x40'\
b'\x58\x45\x34\x49\x5b\x4b\x52\x4b\x4d\x4d\x4e\x4f\x4f\x50\x4f'\
b'\x52\x4f\x54\x4e\x54\x4d\x54\x4d\x53\x4c\x52\x4b\x50\x4b\x50'\
b'\x4b\x4f\x4a\x4d\x49\x4c\x48\x4b\x47\x4b\x46\x4b\x44\x4d\x42'\
b'\x4f\x41\x51\x40\x53\x40\x54\x40\x56\x40\x58\x41\x58\x45\x57'\
b'\x44\x54\x44\x53\x44\x53\x44\x52\x44\x51\x44\x51\x45\x51\x45'\
b'\x51\x46\x51\x46\x52\x47\x53\x47\x54\x47\x55\x48\x57\x49\x58'\
b'\x4a\x59\x4c\x59\x4d\x59\x4e\x57\x50\x55\x52\x52\x52\x51\x52'\
b'\x4e\x52\x4b\x52\x15\x4a\x5a\x58\x52\x57\x52\x54\x52\x4f\x52'\
b'\x4f\x4c\x4f\x44\x4c\x44\x4c\x41\x4f\x41\x4f\x3d\x54\x3b\x54'\
b'\x41\x58\x41\x58\x44\x54\x44\x54\x4c\x54\x4e\x56\x4e\x57\x4e'\
b'\x58\x4e\x58\x52\x13\x48\x5c\x5a\x52\x55\x52\x55\x4f\x55\x4f'\
b'\x53\x52\x50\x52\x4a\x52\x4a\x4b\x4a\x41\x4f\x41\x4f\x4b\x4f'\
b'\x4e\x52\x4e\x53\x4e\x55\x4c\x55\x4b\x55\x41\x5a\x41\x5a\x52'\
b'\x0d\x47\x5d\x5b\x41\x55\x52\x4f\x52\x49\x41\x4e\x41\x51\x4b'\
b'\x52\x4d\x52\x4e\x52\x4e\x52\x4d\x53\x4b\x56\x41\x5b\x41\x1d'\
b'\x42\x62\x60\x41\x5b\x52\x55\x52\x52\x48\x52\x47\x52\x46\x52'\
b'\x46\x52\x47\x52\x48\x4f\x52\x49\x52\x44\x41\x4a\x41\x4c\x4c'\
b'\x4c\x4d\x4c\x4e\x4d\x4e\x4d\x4d\x4d\x4c\x50\x41\x55\x41\x58'\
b'\x4c\x58\x4c\x58\x4e\x58\x4e\x58\x4d\x58\x4c\x5b\x41\x60\x41'\
b'\x17\x46\x5e\x5c\x41\x56\x49\x5b\x52\x55\x52\x53\x4d\x52\x4d'\
b'\x52\x4c\x52\x4c\x52\x4c\x51\x4d\x4f\x52\x48\x52\x4e\x49\x49'\
b'\x41\x4f\x41\x52\x45\x52\x46\x52\x47\x52\x47\x53\x46\x53\x45'\
b'\x56\x41\x5c\x41\x16\x46\x5e\x5c\x41\x54\x53\x52\x5a\x4d\x5a'\
b'\x4b\x5a\x49\x5a\x49\x55\x4b\x56\x4c\x56\x4e\x56\x4f\x54\x50'\
b'\x52\x48\x41\x4e\x41\x52\x4b\x52\x4c\x52\x4d\x52\x4d\x52\x4c'\
b'\x53\x4b\x56\x41\x5c\x41\x0b\x48\x5c\x5a\x52\x4a\x52\x4a\x50'\
b'\x53\x44\x4b\x44\x4b\x41\x5a\x41\x5a\x43\x51\x4e\x5a\x4e\x5a'\
b'\x52\x1c\x4b\x59\x57\x58\x53\x58\x50\x55\x50\x51\x50\x4d\x50'\
b'\x4a\x4d\x4a\x4d\x47\x50\x47\x50\x44\x50\x40\x50\x3c\x53\x39'\
b'\x57\x39\x57\x3d\x54\x3d\x54\x40\x54\x43\x54\x47\x51\x48\x51'\
b'\x49\x54\x4a\x54\x4e\x54\x51\x54\x53\x55\x54\x57\x54\x57\x58'\
b'\x05\x4e\x56\x54\x5a\x50\x5a\x50\x37\x54\x37\x54\x5a\x1c\x4b'\
b'\x59\x57\x4a\x54\x4a\x54\x4d\x54\x51\x54\x55\x51\x58\x4d\x58'\
b'\x4d\x54\x4f\x54\x50\x53\x50\x51\x50\x4e\x50\x4a\x53\x49\x53'\
b'\x49\x50\x47\x50\x43\x50\x40\x50\x3d\x4d\x3d\x4d\x39\x51\x39'\
b'\x54\x3c\x54\x40\x54\x44\x54\x47\x57\x47\x57\x4a\x16\x47\x5d'\
b'\x5b\x45\x5b\x48\x58\x4b\x56\x4b\x54\x4b\x51\x4a\x4f\x48\x4f'\
b'\x48\x4d\x48\x4c\x4b\x49\x4b\x49\x48\x4c\x45\x4e\x45\x50\x45'\
b'\x52\x46\x55\x48\x56\x48\x56\x48\x58\x46\x58\x45\x5b\x45\x13'\
b'\x44\x60\x49\x37\x5b\x37\x5e\x37\x5e\x3a\x5e\x52\x5e\x55\x5b'\
b'\x55\x49\x55\x46\x55\x46\x52\x46\x3a\x46\x37\x49\x37\x20\x52'\
b'\x5b\x52\x5b\x3a\x49\x3a\x49\x52\x5b\x52'

_index =\
b'\x00\x00\x03\x00\x2c\x00\x45\x00\x8e\x00\xed\x00\x5c\x01\x3d'\
b'\x02\x4a\x02\x63\x02\x7c\x02\x9f\x02\xbc\x02\xc9\x02\xd6\x02'\
b'\xf3\x02\x00\x03\x2d\x03\x46\x03\x77\x03\xc2\x03\xf1\x03\x28'\
b'\x04\x75\x04\x88\x04\xeb\x04\x3a\x05\x73\x05\x9c\x05\xb1\x05'\
b'\xca\x05\xdf\x05\x60\x06\xe5\x06\x0e\x07\x5d\x07\x8e\x07\xb9'\
b'\x07\xd6\x07\xef\x07\x28\x08\x45\x08\x62\x08\x81\x08\xa8\x08'\
b'\xb9\x08\xf6\x08\x23\x09\x5c\x09\x87\x09\xf8\x09\x47\x0a\xb8'\
b'\x0a\xcd\x0a\xee\x0a\x0b\x0b\x48\x0b\x79\x0b\x9a\x0b\xb3\x0b'\
b'\xc8\x0b\xd5\x0b\xea\x0b\xff\x0b\x0c\x0c\x19\x0c\x62\x0c\xa7'\
b'\x0c\xd8\x0c\x1d\x0d\x56\x0d\x85\x0d\xde\x0d\x07\x0e\x30\x0e'\
b'\x6b\x0e\x8a\x0e\x97\x0e\xda\x0e\x03\x0f\x36\x0f\x79\x0f\xbe'\
b'\x0f\xe3\x0f\x4e\x10\x7b\x10\xa4\x10\xc1\x10\xfe\x10\x2f\x11'\
b'\x5e\x11\x77\x11\xb2\x11\xbf\x11\xfa\x11\x29\x12'

FONT = memoryview(_font)
INDEX = memoryview(_index)
