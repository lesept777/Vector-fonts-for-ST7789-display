FIRST = 32
LAST = 127
WIDTH = 32
HEIGHT = 36

_font =\
b'\x01\x4f\x55\x13\x4e\x56\x53\x39\x53\x4b\x51\x4b\x50\x39\x53'\
b'\x39\x20\x52\x52\x52\x51\x52\x50\x51\x50\x50\x50\x50\x51\x4e'\
b'\x52\x4e\x53\x4e\x54\x50\x54\x50\x54\x51\x53\x52\x52\x52\x0b'\
b'\x4c\x58\x51\x39\x50\x41\x4e\x41\x4e\x39\x51\x39\x20\x52\x56'\
b'\x39\x56\x41\x54\x41\x53\x39\x56\x39\x23\x46\x5e\x5c\x40\x5b'\
b'\x42\x57\x42\x56\x47\x5b\x47\x5a\x49\x55\x49\x54\x50\x52\x50'\
b'\x53\x49\x4f\x49\x4d\x50\x4b\x50\x4d\x49\x48\x49\x48\x47\x4d'\
b'\x47\x4e\x42\x49\x42\x4a\x40\x4f\x40\x50\x39\x52\x39\x51\x40'\
b'\x55\x40\x57\x39\x59\x39\x57\x40\x5c\x40\x20\x52\x55\x42\x50'\
b'\x42\x4f\x47\x54\x47\x55\x42\x30\x49\x5b\x53\x52\x53\x56\x51'\
b'\x56\x51\x52\x4d\x52\x4b\x50\x4b\x4d\x4c\x4e\x4f\x50\x51\x50'\
b'\x51\x47\x4d\x45\x4b\x42\x4b\x40\x4b\x3d\x4e\x39\x51\x39\x51'\
b'\x36\x53\x36\x53\x39\x56\x39\x58\x3a\x58\x3d\x56\x3b\x53\x3b'\
b'\x53\x45\x56\x46\x59\x49\x59\x4c\x59\x4e\x56\x51\x53\x52\x20'\
b'\x52\x51\x44\x51\x3b\x50\x3c\x4e\x3e\x4e\x3f\x4e\x41\x4f\x43'\
b'\x51\x44\x20\x52\x53\x48\x53\x4f\x56\x4f\x56\x4c\x56\x49\x53'\
b'\x48\x3d\x43\x61\x4a\x46\x48\x46\x45\x42\x45\x3f\x45\x3c\x48'\
b'\x39\x4b\x39\x4d\x39\x50\x3c\x50\x3f\x50\x42\x4d\x46\x4a\x46'\
b'\x20\x52\x4b\x3b\x49\x3b\x47\x3d\x47\x3f\x47\x41\x49\x44\x4b'\
b'\x44\x4c\x44\x4e\x41\x4e\x3f\x4e\x3d\x4c\x3b\x4b\x3b\x20\x52'\
b'\x5b\x39\x4b\x52\x49\x52\x59\x39\x5b\x39\x20\x52\x59\x52\x57'\
b'\x52\x54\x4f\x54\x4c\x54\x49\x57\x45\x5a\x45\x5c\x45\x5f\x49'\
b'\x5f\x4c\x5f\x4f\x5c\x52\x59\x52\x20\x52\x5a\x47\x58\x47\x56'\
b'\x4a\x56\x4c\x56\x4e\x58\x50\x59\x50\x5b\x50\x5d\x4e\x5d\x4c'\
b'\x5d\x4a\x5b\x47\x5a\x47\x6d\x43\x61\x5c\x52\x5b\x52\x5a\x52'\
b'\x58\x51\x57\x4f\x57\x4f\x56\x4f\x54\x51\x52\x52\x4f\x52\x4e'\
b'\x52\x4c\x52\x49\x51\x46\x50\x45\x4d\x45\x4b\x45\x49\x48\x45'\
b'\x4b\x44\x4a\x43\x49\x42\x49\x41\x48\x3f\x48\x3e\x48\x3d\x49'\
b'\x3b\x4b\x39\x4d\x39\x4f\x39\x50\x39\x52\x39\x54\x3b\x55\x3d'\
b'\x55\x3e\x55\x40\x52\x43\x50\x44\x51\x44\x53\x46\x55\x47\x56'\
b'\x49\x57\x4a\x58\x48\x5a\x43\x5a\x41\x5a\x40\x59\x3f\x59\x3e'\
b'\x5c\x3e\x5c\x3f\x5c\x40\x5c\x41\x5c\x42\x5c\x46\x5b\x49\x59'\
b'\x4b\x58\x4c\x59\x4d\x5a\x4f\x5b\x4f\x5c\x50\x5d\x50\x5d\x50'\
b'\x5e\x4f\x5f\x4f\x5f\x52\x5e\x52\x5d\x52\x5c\x52\x20\x52\x4e'\
b'\x50\x4f\x50\x51\x4f\x53\x4e\x55\x4d\x55\x4c\x54\x4b\x52\x48'\
b'\x51\x47\x4e\x45\x4d\x45\x4c\x45\x4a\x46\x49\x48\x48\x4a\x48'\
b'\x4b\x48\x4c\x49\x4e\x4a\x4f\x4c\x50\x4e\x50\x20\x52\x52\x3e'\
b'\x52\x3d\x51\x3c\x50\x3b\x4f\x3b\x4f\x3b\x4d\x3b\x4b\x3d\x4b'\
b'\x3e\x4b\x3f\x4b\x40\x4c\x41\x4d\x42\x4e\x42\x50\x42\x52\x40'\
b'\x52\x3e\x05\x4e\x56\x54\x39\x53\x41\x51\x41\x50\x39\x54\x39'\
b'\x0b\x4c\x58\x56\x58\x53\x58\x4e\x52\x4e\x48\x4e\x3f\x53\x39'\
b'\x56\x39\x51\x40\x51\x48\x51\x51\x56\x58\x0b\x4c\x58\x51\x58'\
b'\x4e\x58\x53\x51\x53\x48\x53\x40\x4e\x39\x51\x39\x56\x3f\x56'\
b'\x48\x56\x52\x51\x58\x10\x4a\x5a\x58\x3f\x53\x40\x57\x44\x55'\
b'\x45\x52\x41\x4f\x45\x4d\x44\x51\x40\x4c\x3f\x4d\x3d\x51\x3e'\
b'\x51\x39\x53\x39\x53\x3e\x57\x3d\x58\x3f\x0d\x48\x5c\x5a\x49'\
b'\x53\x49\x53\x50\x51\x50\x51\x49\x4a\x49\x4a\x46\x51\x46\x51'\
b'\x3f\x53\x3f\x53\x46\x5a\x46\x5a\x49\x05\x4e\x56\x54\x4e\x52'\
b'\x57\x50\x57\x52\x4e\x54\x4e\x05\x4b\x59\x57\x49\x4d\x49\x4d'\
b'\x47\x57\x47\x57\x49\x0d\x4e\x56\x52\x52\x51\x52\x50\x51\x50'\
b'\x50\x50\x50\x51\x4e\x52\x4e\x53\x4e\x54\x50\x54\x50\x54\x51'\
b'\x53\x52\x52\x52\x05\x49\x5b\x59\x39\x4d\x56\x4b\x56\x57\x39'\
b'\x59\x39\x16\x48\x5c\x52\x52\x4e\x52\x4a\x4c\x4a\x46\x4a\x3f'\
b'\x4e\x39\x52\x39\x5a\x39\x5a\x45\x5a\x4c\x56\x52\x52\x52\x20'\
b'\x52\x52\x3b\x4d\x3b\x4d\x46\x4d\x50\x52\x50\x57\x50\x57\x46'\
b'\x57\x3b\x52\x3b\x0b\x49\x5b\x59\x52\x4b\x52\x4b\x4f\x51\x4f'\
b'\x51\x3c\x4b\x3e\x4b\x3b\x54\x38\x54\x4f\x59\x4f\x59\x52\x19'\
b'\x48\x5c\x59\x52\x4a\x52\x4a\x4f\x52\x48\x54\x45\x57\x42\x57'\
b'\x40\x57\x3d\x54\x3b\x52\x3b\x4f\x3b\x4c\x3e\x4c\x3b\x4f\x39'\
b'\x52\x39\x56\x39\x5a\x3c\x5a\x3f\x5a\x42\x57\x46\x54\x4a\x4e'\
b'\x4f\x4e\x4f\x59\x4f\x59\x52\x23\x49\x5b\x4b\x51\x4b\x4e\x4d'\
b'\x50\x51\x50\x53\x50\x56\x4d\x56\x4b\x56\x46\x4f\x46\x4d\x46'\
b'\x4d\x44\x4f\x44\x55\x44\x55\x3f\x55\x3b\x51\x3b\x4e\x3b\x4c'\
b'\x3d\x4c\x3a\x4e\x39\x51\x39\x55\x39\x58\x3c\x58\x3f\x58\x43'\
b'\x53\x45\x53\x45\x56\x45\x59\x48\x59\x4b\x59\x4e\x54\x52\x50'\
b'\x52\x4d\x52\x4b\x51\x16\x47\x5d\x5b\x4b\x58\x4b\x58\x52\x55'\
b'\x52\x55\x4b\x49\x4b\x49\x49\x54\x39\x58\x39\x58\x49\x5b\x49'\
b'\x5b\x4b\x20\x52\x55\x49\x55\x3e\x55\x3d\x55\x3c\x55\x3c\x55'\
b'\x3c\x54\x3e\x4c\x49\x55\x49\x1b\x49\x5b\x4b\x51\x4b\x4e\x4e'\
b'\x50\x50\x50\x53\x50\x56\x4d\x56\x4b\x56\x48\x53\x45\x50\x45'\
b'\x4f\x45\x4c\x46\x4c\x39\x58\x39\x58\x3c\x4e\x3c\x4e\x43\x50'\
b'\x43\x51\x43\x55\x43\x59\x47\x59\x4a\x59\x4e\x54\x52\x50\x52'\
b'\x4d\x52\x4b\x51\x26\x48\x5c\x58\x39\x58\x3c\x56\x3b\x54\x3b'\
b'\x51\x3b\x4d\x41\x4d\x46\x4d\x46\x4f\x42\x53\x42\x56\x42\x5a'\
b'\x47\x5a\x4a\x5a\x4e\x56\x52\x52\x52\x4e\x52\x4a\x4c\x4a\x47'\
b'\x4a\x40\x50\x39\x54\x39\x57\x39\x58\x39\x20\x52\x52\x45\x50'\
b'\x45\x4d\x48\x4d\x4a\x4d\x4c\x50\x50\x52\x50\x54\x50\x57\x4d'\
b'\x57\x4a\x57\x48\x54\x45\x52\x45\x08\x48\x5c\x5a\x3a\x50\x52'\
b'\x4d\x52\x57\x3c\x4a\x3c\x4a\x39\x5a\x39\x5a\x3a\x2f\x48\x5c'\
b'\x50\x45\x50\x45\x4b\x43\x4b\x3f\x4b\x3c\x4f\x39\x52\x39\x55'\
b'\x39\x59\x3c\x59\x3e\x59\x43\x54\x45\x54\x45\x5a\x47\x5a\x4c'\
b'\x5a\x4f\x55\x52\x51\x52\x4e\x52\x4a\x4f\x4a\x4c\x4a\x47\x50'\
b'\x45\x20\x52\x56\x3f\x56\x3d\x54\x3b\x52\x3b\x50\x3b\x4e\x3d'\
b'\x4e\x3f\x4e\x42\x52\x44\x56\x42\x56\x3f\x20\x52\x52\x46\x4d'\
b'\x48\x4d\x4c\x4d\x4e\x50\x50\x52\x50\x54\x50\x57\x4e\x57\x4c'\
b'\x57\x48\x52\x46\x27\x48\x5c\x4b\x52\x4b\x4f\x4e\x50\x50\x50'\
b'\x53\x50\x57\x4b\x57\x45\x57\x46\x57\x45\x55\x49\x51\x49\x4e'\
b'\x49\x4a\x44\x4a\x41\x4a\x3d\x4f\x39\x52\x39\x56\x39\x5a\x3e'\
b'\x5a\x44\x5a\x4b\x55\x52\x50\x52\x4d\x52\x4b\x52\x20\x52\x52'\
b'\x3b\x50\x3b\x4d\x3e\x4d\x41\x4d\x43\x50\x46\x52\x46\x54\x46'\
b'\x57\x43\x57\x41\x57\x3f\x54\x3b\x52\x3b\x1b\x4e\x56\x52\x44'\
b'\x51\x44\x50\x42\x50\x42\x50\x41\x51\x40\x52\x40\x53\x40\x54'\
b'\x41\x54\x42\x54\x42\x53\x44\x52\x44\x20\x52\x52\x52\x51\x52'\
b'\x50\x51\x50\x50\x50\x50\x51\x4e\x52\x4e\x53\x4e\x54\x50\x54'\
b'\x50\x54\x51\x53\x52\x52\x52\x13\x4d\x57\x53\x44\x52\x44\x51'\
b'\x42\x51\x42\x51\x41\x52\x40\x53\x40\x53\x40\x55\x41\x55\x42'\
b'\x55\x42\x53\x44\x53\x44\x20\x52\x54\x4e\x51\x57\x4f\x57\x51'\
b'\x4e\x54\x4e\x09\x48\x5c\x5a\x50\x4a\x48\x4a\x47\x5a\x3f\x5a'\
b'\x41\x4e\x48\x4e\x48\x5a\x4d\x5a\x50\x0b\x48\x5c\x5a\x45\x4a'\
b'\x45\x4a\x43\x5a\x43\x5a\x45\x20\x52\x5a\x4c\x4a\x4c\x4a\x4a'\
b'\x5a\x4a\x5a\x4c\x09\x48\x5c\x5a\x48\x4a\x50\x4a\x4d\x56\x48'\
b'\x56\x48\x4a\x41\x4a\x3f\x5a\x47\x5a\x48\x37\x4a\x5a\x50\x4b'\
b'\x4f\x4b\x4f\x49\x4f\x48\x4f\x47\x50\x46\x51\x44\x53\x43\x54'\
b'\x41\x55\x3f\x55\x3e\x55\x3e\x55\x3c\x53\x3b\x52\x3b\x51\x3b'\
b'\x4e\x3b\x4c\x3d\x4c\x3a\x4f\x39\x52\x39\x53\x39\x55\x39\x57'\
b'\x3b\x58\x3d\x58\x3e\x58\x3f\x57\x41\x56\x43\x54\x45\x53\x46'\
b'\x52\x48\x52\x48\x52\x49\x52\x4b\x52\x4b\x50\x4b\x20\x52\x51'\
b'\x52\x50\x52\x50\x52\x4f\x51\x4f\x50\x4f\x50\x50\x4f\x50\x4e'\
b'\x51\x4e\x52\x4e\x53\x4f\x53\x50\x53\x50\x53\x51\x53\x52\x52'\
b'\x52\x51\x52\x41\x42\x62\x55\x4b\x55\x4b\x54\x4f\x50\x4f\x4e'\
b'\x4f\x4b\x4b\x4b\x48\x4b\x44\x4f\x3f\x52\x3f\x53\x3f\x55\x40'\
b'\x56\x41\x56\x41\x56\x41\x56\x3f\x58\x3f\x57\x49\x57\x49\x57'\
b'\x4d\x59\x4d\x5b\x4d\x5e\x49\x5e\x45\x5e\x41\x58\x3b\x52\x3b'\
b'\x4d\x3b\x46\x42\x46\x47\x46\x4d\x4d\x53\x52\x53\x57\x53\x5a'\
b'\x52\x5a\x54\x57\x55\x52\x55\x4c\x55\x44\x4e\x44\x47\x44\x41'\
b'\x4c\x39\x52\x39\x58\x39\x60\x40\x60\x45\x60\x4a\x5c\x4f\x59'\
b'\x4f\x55\x4f\x55\x4b\x20\x52\x52\x41\x50\x41\x4d\x45\x4d\x48'\
b'\x4d\x4a\x4f\x4d\x51\x4d\x53\x4d\x55\x48\x55\x45\x55\x41\x52'\
b'\x41\x13\x45\x5f\x5d\x52\x5a\x52\x57\x4b\x4d\x4b\x4a\x52\x47'\
b'\x52\x50\x39\x54\x39\x5d\x52\x20\x52\x56\x48\x52\x3e\x52\x3d'\
b'\x52\x3c\x52\x3c\x52\x3d\x51\x3e\x4e\x48\x56\x48\x25\x48\x5c'\
b'\x4a\x52\x4a\x39\x51\x39\x55\x39\x58\x3c\x58\x3f\x58\x41\x56'\
b'\x44\x54\x45\x54\x45\x57\x45\x5a\x48\x5a\x4b\x5a\x4e\x55\x52'\
b'\x52\x52\x4a\x52\x20\x52\x4d\x3c\x4d\x44\x50\x44\x53\x44\x55'\
b'\x41\x55\x3f\x55\x3c\x51\x3c\x4d\x3c\x20\x52\x4d\x46\x4d\x4f'\
b'\x51\x4f\x54\x4f\x57\x4d\x57\x4b\x57\x46\x51\x46\x4d\x46\x17'\
b'\x47\x5d\x5b\x51\x59\x52\x54\x52\x4f\x52\x49\x4c\x49\x46\x49'\
b'\x40\x50\x39\x55\x39\x59\x39\x5b\x3a\x5b\x3d\x59\x3b\x55\x3b'\
b'\x51\x3b\x4c\x41\x4c\x46\x4c\x4a\x51\x50\x55\x50\x59\x50\x5b'\
b'\x4e\x5b\x51\x13\x46\x5e\x48\x52\x48\x39\x4f\x39\x5c\x39\x5c'\
b'\x45\x5c\x4b\x55\x52\x4f\x52\x48\x52\x20\x52\x4b\x3c\x4b\x4f'\
b'\x4f\x4f\x54\x4f\x59\x4a\x59\x45\x59\x3c\x4f\x3c\x4b\x3c\x0d'\
b'\x49\x5b\x59\x52\x4b\x52\x4b\x39\x58\x39\x58\x3c\x4e\x3c\x4e'\
b'\x44\x57\x44\x57\x47\x4e\x47\x4e\x4f\x59\x4f\x59\x52\x0b\x4a'\
b'\x5a\x58\x3c\x4f\x3c\x4f\x44\x58\x44\x58\x47\x4f\x47\x4f\x52'\
b'\x4c\x52\x4c\x39\x58\x39\x58\x3c\x1b\x46\x5e\x5c\x50\x58\x52'\
b'\x54\x52\x4e\x52\x48\x4c\x48\x46\x48\x40\x4f\x39\x55\x39\x59'\
b'\x39\x5c\x3a\x5c\x3d\x59\x3b\x54\x3b\x50\x3b\x4b\x41\x4b\x46'\
b'\x4b\x4a\x50\x50\x54\x50\x57\x50\x59\x4f\x59\x48\x54\x48\x54'\
b'\x45\x5c\x45\x5c\x50\x0d\x47\x5d\x5b\x52\x58\x52\x58\x47\x4c'\
b'\x47\x4c\x52\x49\x52\x49\x39\x4c\x39\x4c\x44\x58\x44\x58\x39'\
b'\x5b\x39\x5b\x52\x0d\x4c\x58\x56\x39\x56\x3b\x53\x3b\x53\x4f'\
b'\x56\x4f\x56\x52\x4e\x52\x4e\x4f\x51\x4f\x51\x3b\x4e\x3b\x4e'\
b'\x39\x56\x39\x0e\x4b\x59\x57\x49\x57\x4d\x53\x52\x50\x52\x4e'\
b'\x52\x4d\x52\x4d\x4f\x4e\x50\x50\x50\x54\x50\x54\x49\x54\x39'\
b'\x57\x39\x57\x49\x12\x47\x5d\x5b\x52\x57\x52\x4d\x47\x4c\x46'\
b'\x4c\x46\x4c\x46\x4c\x52\x49\x52\x49\x39\x4c\x39\x4c\x45\x4c'\
b'\x45\x4d\x44\x4d\x44\x56\x39\x5a\x39\x4f\x45\x5b\x52\x07\x4a'\
b'\x5a\x58\x52\x4c\x52\x4c\x39\x4e\x39\x4e\x4f\x58\x4f\x58\x52'\
b'\x1d\x43\x61\x5f\x52\x5c\x52\x5c\x41\x5c\x3f\x5c\x3c\x5c\x3c'\
b'\x5c\x3e\x5b\x3f\x53\x52\x51\x52\x49\x3f\x48\x3e\x48\x3c\x48'\
b'\x3c\x48\x3e\x48\x41\x48\x52\x45\x52\x45\x39\x49\x39\x51\x4a'\
b'\x52\x4c\x52\x4d\x52\x4d\x53\x4b\x53\x4a\x5b\x39\x5f\x39\x5f'\
b'\x52\x15\x46\x5e\x5c\x52\x58\x52\x4c\x3e\x4b\x3d\x4b\x3c\x4b'\
b'\x3c\x4b\x3d\x4b\x40\x4b\x52\x48\x52\x48\x39\x4c\x39\x58\x4d'\
b'\x59\x4e\x59\x4e\x59\x4e\x59\x4d\x59\x4b\x59\x39\x5c\x39\x5c'\
b'\x52\x1b\x44\x60\x52\x52\x4d\x52\x46\x4b\x46\x46\x46\x40\x4d'\
b'\x39\x52\x39\x57\x39\x5e\x40\x5e\x45\x5e\x4b\x57\x52\x52\x52'\
b'\x20\x52\x52\x3b\x4e\x3b\x49\x41\x49\x46\x49\x4a\x4e\x50\x52'\
b'\x50\x56\x50\x5b\x4a\x5b\x46\x5b\x41\x56\x3b\x52\x3b\x16\x48'\
b'\x5c\x4d\x49\x4d\x52\x4a\x52\x4a\x39\x51\x39\x55\x39\x5a\x3d'\
b'\x5a\x40\x5a\x44\x55\x49\x51\x49\x4d\x49\x20\x52\x4d\x3c\x4d'\
b'\x46\x50\x46\x53\x46\x57\x43\x57\x41\x57\x3c\x51\x3c\x4d\x3c'\
b'\x3c\x44\x60\x51\x52\x50\x52\x4e\x52\x4c\x51\x4a\x50\x49\x4f'\
b'\x46\x4b\x46\x46\x46\x40\x49\x3c\x4c\x39\x52\x39\x57\x39\x5a'\
b'\x3c\x5e\x40\x5e\x45\x5e\x48\x5c\x4c\x5a\x4f\x57\x51\x55\x52'\
b'\x56\x53\x57\x54\x59\x56\x5b\x56\x5c\x56\x5c\x56\x5d\x56\x5d'\
b'\x56\x5e\x56\x5e\x56\x5e\x58\x5e\x59\x5d\x59\x5c\x59\x5c\x59'\
b'\x5b\x59\x5a\x59\x57\x58\x55\x56\x53\x54\x51\x52\x20\x52\x52'\
b'\x3b\x4e\x3b\x4b\x3e\x49\x41\x49\x46\x49\x4a\x4b\x4d\x4e\x50'\
b'\x52\x50\x56\x50\x58\x4d\x5a\x4a\x5a\x46\x5a\x41\x58\x3e\x56'\
b'\x3b\x52\x3b\x2b\x47\x5d\x5b\x52\x57\x52\x53\x4b\x53\x4a\x52'\
b'\x49\x50\x48\x4f\x47\x4e\x47\x4c\x47\x4c\x52\x49\x52\x49\x39'\
b'\x50\x39\x52\x39\x55\x3a\x57\x3b\x58\x3e\x58\x40\x58\x41\x57'\
b'\x43\x56\x45\x54\x46\x53\x46\x53\x46\x53\x47\x54\x47\x55\x48'\
b'\x56\x4a\x56\x4a\x5b\x52\x20\x52\x4c\x3c\x4c\x45\x50\x45\x51'\
b'\x45\x53\x44\x54\x43\x55\x41\x55\x40\x55\x3e\x52\x3c\x50\x3c'\
b'\x4c\x3c\x37\x48\x5c\x4a\x51\x4a\x4e\x4b\x4e\x4d\x4f\x4f\x4f'\
b'\x50\x50\x51\x50\x54\x50\x57\x4e\x57\x4c\x57\x4b\x56\x49\x54'\
b'\x48\x52\x47\x51\x46\x4f\x46\x4d\x44\x4b\x43\x4a\x41\x4a\x3f'\
b'\x4a\x3e\x4c\x3b\x4e\x39\x52\x39\x53\x39\x57\x39\x59\x39\x59'\
b'\x3d\x56\x3b\x53\x3b\x52\x3b\x50\x3c\x4e\x3d\x4e\x3e\x4e\x3f'\
b'\x4e\x40\x4e\x41\x50\x42\x52\x44\x53\x44\x54\x45\x57\x46\x59'\
b'\x48\x5a\x4a\x5a\x4c\x5a\x4e\x58\x50\x56\x52\x52\x52\x51\x52'\
b'\x50\x52\x4e\x52\x4d\x52\x4b\x51\x4a\x51\x09\x47\x5d\x5b\x3c'\
b'\x53\x3c\x53\x52\x51\x52\x51\x3c\x49\x3c\x49\x39\x5b\x39\x5b'\
b'\x3c\x0f\x47\x5d\x5b\x48\x5b\x52\x52\x52\x49\x52\x49\x48\x49'\
b'\x39\x4c\x39\x4c\x48\x4c\x50\x52\x50\x58\x50\x58\x48\x58\x39'\
b'\x5b\x39\x5b\x48\x0d\x45\x5f\x5d\x39\x54\x52\x50\x52\x47\x39'\
b'\x4a\x39\x51\x4d\x52\x4e\x52\x4f\x52\x4f\x52\x4e\x53\x4d\x5a'\
b'\x39\x5d\x39\x1d\x40\x64\x62\x39\x5b\x52\x58\x52\x53\x40\x52'\
b'\x3f\x52\x3d\x52\x3d\x52\x3e\x52\x40\x4c\x52\x49\x52\x42\x39'\
b'\x45\x39\x4a\x4c\x4b\x4d\x4b\x4f\x4b\x4f\x4b\x4e\x4b\x4c\x51'\
b'\x39\x54\x39\x59\x4c\x59\x4d\x59\x4f\x59\x4f\x5a\x4e\x5a\x4c'\
b'\x5f\x39\x62\x39\x17\x46\x5e\x5c\x52\x58\x52\x53\x48\x52\x48'\
b'\x52\x47\x52\x47\x52\x48\x51\x48\x4c\x52\x48\x52\x50\x45\x49'\
b'\x39\x4c\x39\x51\x42\x52\x43\x52\x44\x52\x44\x53\x42\x53\x42'\
b'\x59\x39\x5c\x39\x54\x45\x5c\x52\x0f\x46\x5e\x5c\x39\x53\x49'\
b'\x53\x52\x50\x52\x50\x49\x48\x39\x4c\x39\x51\x44\x51\x44\x52'\
b'\x46\x52\x46\x52\x45\x53\x44\x59\x39\x5c\x39\x0b\x46\x5e\x5c'\
b'\x3a\x4d\x4f\x5b\x4f\x5b\x52\x48\x52\x48\x51\x57\x3c\x4a\x3c'\
b'\x4a\x39\x5c\x39\x5c\x3a\x09\x4d\x57\x55\x58\x4f\x58\x4f\x39'\
b'\x55\x39\x55\x3b\x51\x3b\x51\x56\x55\x56\x55\x58\x05\x49\x5b'\
b'\x59\x56\x57\x56\x4b\x39\x4e\x39\x59\x56\x09\x4d\x57\x55\x58'\
b'\x4f\x58\x4f\x56\x53\x56\x53\x3b\x4f\x3b\x4f\x39\x55\x39\x55'\
b'\x58\x09\x48\x5c\x5a\x47\x58\x47\x52\x3c\x52\x3c\x4c\x47\x4a'\
b'\x47\x51\x39\x52\x39\x5a\x47\x05\x49\x5b\x59\x57\x4b\x57\x4b'\
b'\x55\x59\x55\x59\x57\x05\x4d\x57\x55\x3d\x53\x3d\x4f\x37\x52'\
b'\x37\x55\x3d\x23\x49\x5b\x59\x52\x56\x52\x56\x4f\x56\x4f\x54'\
b'\x52\x51\x52\x4e\x52\x4b\x50\x4b\x4d\x4b\x48\x51\x47\x56\x47'\
b'\x56\x42\x53\x42\x4f\x42\x4d\x44\x4d\x41\x4f\x40\x53\x40\x59'\
b'\x40\x59\x46\x59\x52\x20\x52\x56\x49\x52\x4a\x50\x4a\x4e\x4b'\
b'\x4e\x4d\x4e\x4e\x50\x50\x51\x50\x53\x50\x56\x4d\x56\x4b\x56'\
b'\x49\x21\x48\x5c\x4d\x4f\x4d\x4f\x4d\x52\x4a\x52\x4a\x38\x4d'\
b'\x38\x4d\x43\x4d\x43\x4f\x40\x53\x40\x56\x40\x5a\x45\x5a\x49'\
b'\x5a\x4d\x56\x52\x52\x52\x4f\x52\x4d\x4f\x20\x52\x4d\x48\x4d'\
b'\x4b\x4d\x4d\x50\x50\x52\x50\x54\x50\x57\x4c\x57\x48\x57\x46'\
b'\x55\x42\x52\x42\x50\x42\x4d\x46\x4d\x48\x17\x49\x5b\x59\x51'\
b'\x57\x52\x54\x52\x50\x52\x4b\x4d\x4b\x49\x4b\x45\x50\x40\x55'\
b'\x40\x57\x40\x59\x41\x59\x44\x57\x42\x54\x42\x52\x42\x4e\x46'\
b'\x4e\x49\x4e\x4c\x52\x50\x54\x50\x57\x50\x59\x4e\x59\x51\x21'\
b'\x48\x5c\x5a\x52\x57\x52\x57\x4f\x57\x4f\x55\x52\x51\x52\x4e'\
b'\x52\x4a\x4e\x4a\x49\x4a\x45\x4e\x40\x52\x40\x56\x40\x57\x43'\
b'\x57\x43\x57\x38\x5a\x38\x5a\x52\x20\x52\x57\x4a\x57\x47\x57'\
b'\x45\x55\x42\x52\x42\x50\x42\x4d\x46\x4d\x49\x4d\x4c\x50\x50'\
b'\x52\x50\x54\x50\x57\x4d\x57\x4a\x1d\x48\x5c\x5a\x4a\x4d\x4a'\
b'\x4d\x4d\x50\x50\x53\x50\x56\x50\x59\x4e\x59\x51\x56\x52\x52'\
b'\x52\x4f\x52\x4a\x4e\x4a\x49\x4a\x45\x4f\x40\x52\x40\x56\x40'\
b'\x5a\x44\x5a\x48\x5a\x4a\x20\x52\x57\x47\x57\x45\x54\x42\x52'\
b'\x42\x50\x42\x4e\x45\x4d\x47\x57\x47\x16\x4b\x59\x57\x3a\x57'\
b'\x3a\x55\x3a\x52\x3a\x52\x3d\x52\x40\x57\x40\x57\x43\x52\x43'\
b'\x52\x52\x50\x52\x50\x43\x4d\x43\x4d\x40\x50\x40\x50\x3d\x50'\
b'\x3a\x53\x37\x55\x37\x57\x37\x57\x37\x57\x3a\x29\x48\x5c\x5a'\
b'\x51\x5a\x5a\x51\x5a\x4d\x5a\x4b\x59\x4b\x56\x4e\x58\x51\x58'\
b'\x57\x58\x57\x51\x57\x4f\x57\x4f\x55\x52\x51\x52\x4e\x52\x4a'\
b'\x4e\x4a\x4a\x4a\x45\x4e\x40\x52\x40\x56\x40\x57\x43\x57\x43'\
b'\x57\x40\x5a\x40\x5a\x51\x20\x52\x57\x4a\x57\x47\x57\x45\x54'\
b'\x42\x52\x42\x50\x42\x4d\x46\x4d\x49\x4d\x4c\x50\x50\x52\x50'\
b'\x54\x50\x57\x4d\x57\x4a\x13\x49\x5b\x59\x52\x57\x52\x57\x48'\
b'\x57\x42\x52\x42\x50\x42\x4d\x45\x4d\x48\x4d\x52\x4b\x52\x4b'\
b'\x38\x4d\x38\x4d\x43\x4e\x43\x50\x40\x53\x40\x59\x40\x59\x47'\
b'\x59\x52\x13\x4e\x56\x52\x3c\x51\x3c\x50\x3b\x50\x3a\x50\x39'\
b'\x51\x38\x52\x38\x53\x38\x54\x39\x54\x3a\x54\x3b\x53\x3c\x52'\
b'\x3c\x20\x52\x53\x52\x51\x52\x51\x40\x53\x40\x53\x52\x1c\x4b'\
b'\x59\x56\x51\x56\x56\x53\x5a\x50\x5a\x4e\x5a\x4d\x5a\x4d\x57'\
b'\x4e\x58\x50\x58\x54\x58\x54\x52\x54\x40\x56\x40\x56\x51\x20'\
b'\x52\x55\x3c\x54\x3c\x53\x3b\x53\x3a\x53\x39\x54\x38\x55\x38'\
b'\x56\x38\x57\x39\x57\x3a\x57\x3b\x56\x3c\x55\x3c\x0e\x49\x5b'\
b'\x59\x52\x55\x52\x4e\x49\x4d\x49\x4d\x52\x4b\x52\x4b\x38\x4d'\
b'\x38\x4d\x48\x4e\x48\x55\x40\x59\x40\x50\x49\x59\x52\x05\x4f'\
b'\x55\x53\x52\x51\x52\x51\x38\x53\x38\x53\x52\x21\x43\x61\x5f'\
b'\x52\x5c\x52\x5c\x48\x5c\x45\x5a\x42\x58\x42\x56\x42\x53\x45'\
b'\x53\x48\x53\x52\x51\x52\x51\x47\x51\x42\x4d\x42\x4b\x42\x48'\
b'\x45\x48\x48\x48\x52\x45\x52\x45\x40\x48\x40\x48\x43\x48\x43'\
b'\x4a\x40\x4e\x40\x50\x40\x52\x42\x53\x43\x55\x40\x59\x40\x5f'\
b'\x40\x5f\x47\x5f\x52\x14\x49\x5b\x59\x52\x57\x52\x57\x48\x57'\
b'\x42\x52\x42\x50\x42\x4d\x45\x4d\x48\x4d\x52\x4b\x52\x4b\x40'\
b'\x4d\x40\x4d\x43\x4e\x43\x50\x40\x53\x40\x56\x40\x59\x44\x59'\
b'\x47\x59\x52\x1b\x47\x5d\x52\x52\x4e\x52\x49\x4d\x49\x49\x49'\
b'\x45\x4e\x40\x52\x40\x56\x40\x5b\x45\x5b\x49\x5b\x4d\x56\x52'\
b'\x52\x52\x20\x52\x52\x42\x4f\x42\x4c\x46\x4c\x49\x4c\x4c\x4f'\
b'\x50\x52\x50\x55\x50\x58\x4c\x58\x49\x58\x46\x55\x42\x52\x42'\
b'\x21\x48\x5c\x4d\x4f\x4d\x4f\x4d\x5a\x4a\x5a\x4a\x40\x4d\x40'\
b'\x4d\x43\x4d\x43\x4f\x40\x53\x40\x56\x40\x5a\x45\x5a\x49\x5a'\
b'\x4d\x56\x52\x52\x52\x4f\x52\x4d\x4f\x20\x52\x4d\x48\x4d\x4b'\
b'\x4d\x4d\x50\x50\x52\x50\x54\x50\x57\x4c\x57\x48\x57\x46\x55'\
b'\x42\x52\x42\x50\x42\x4d\x46\x4d\x48\x21\x48\x5c\x5a\x5a\x57'\
b'\x5a\x57\x4f\x57\x4f\x55\x52\x51\x52\x4e\x52\x4a\x4e\x4a\x49'\
b'\x4a\x45\x4e\x40\x52\x40\x56\x40\x57\x43\x57\x43\x57\x40\x5a'\
b'\x40\x5a\x5a\x20\x52\x57\x4a\x57\x47\x57\x45\x54\x42\x52\x42'\
b'\x50\x42\x4d\x46\x4d\x49\x4d\x4d\x50\x50\x52\x50\x54\x50\x57'\
b'\x4d\x57\x4a\x12\x4b\x59\x57\x43\x56\x42\x54\x42\x53\x42\x50'\
b'\x46\x50\x49\x50\x52\x4d\x52\x4d\x40\x50\x40\x50\x44\x50\x44'\
b'\x51\x42\x53\x40\x55\x40\x56\x40\x57\x40\x57\x43\x30\x4a\x5a'\
b'\x4c\x51\x4c\x4e\x4e\x50\x51\x50\x55\x50\x55\x4d\x55\x4d\x54'\
b'\x4c\x53\x4b\x52\x4a\x51\x4a\x50\x4a\x4e\x49\x4d\x47\x4c\x46'\
b'\x4c\x45\x4c\x44\x4d\x42\x4f\x40\x52\x40\x53\x40\x55\x40\x57'\
b'\x41\x57\x43\x55\x42\x53\x42\x52\x42\x50\x42\x50\x43\x4f\x44'\
b'\x4f\x45\x4f\x45\x50\x46\x51\x47\x52\x48\x53\x48\x54\x48\x56'\
b'\x49\x57\x4b\x58\x4c\x58\x4d\x58\x4f\x57\x50\x55\x52\x52\x52'\
b'\x51\x52\x4e\x52\x4c\x51\x16\x4b\x59\x57\x52\x56\x52\x55\x52'\
b'\x50\x52\x50\x4d\x50\x43\x4d\x43\x4d\x40\x50\x40\x50\x3c\x53'\
b'\x3b\x53\x40\x57\x40\x57\x43\x53\x43\x53\x4d\x53\x4e\x54\x50'\
b'\x55\x50\x56\x50\x57\x4f\x57\x52\x13\x49\x5b\x59\x52\x57\x52'\
b'\x57\x4f\x56\x4f\x55\x52\x51\x52\x4b\x52\x4b\x4b\x4b\x40\x4d'\
b'\x40\x4d\x4a\x4d\x50\x52\x50\x54\x50\x57\x4d\x57\x4a\x57\x40'\
b'\x59\x40\x59\x52\x0d\x48\x5c\x5a\x40\x53\x52\x50\x52\x4a\x40'\
b'\x4d\x40\x51\x4d\x52\x4f\x52\x50\x52\x50\x52\x4e\x53\x4d\x57'\
b'\x40\x5a\x40\x1d\x44\x60\x5e\x40\x59\x52\x56\x52\x52\x45\x52'\
b'\x44\x52\x44\x52\x44\x52\x44\x52\x45\x4e\x52\x4b\x52\x46\x40'\
b'\x49\x40\x4c\x4e\x4c\x4e\x4c\x4f\x4d\x4f\x4d\x4e\x4d\x4e\x51'\
b'\x40\x54\x40\x57\x4e\x58\x4e\x58\x4f\x58\x4f\x58\x4f\x58\x4e'\
b'\x5c\x40\x5e\x40\x15\x48\x5c\x5a\x40\x54\x49\x5a\x52\x56\x52'\
b'\x53\x4c\x52\x4c\x52\x4b\x52\x4b\x52\x4b\x51\x4c\x4e\x52\x4a'\
b'\x52\x50\x49\x4b\x40\x4e\x40\x51\x46\x52\x47\x52\x48\x52\x48'\
b'\x57\x40\x5a\x40\x16\x48\x5c\x5a\x40\x52\x55\x50\x5a\x4c\x5a'\
b'\x4b\x5a\x4a\x5a\x4a\x58\x4b\x58\x4c\x58\x4e\x58\x4f\x55\x51'\
b'\x52\x4a\x40\x4d\x40\x52\x4e\x52\x4e\x52\x4f\x52\x4f\x52\x4f'\
b'\x52\x4e\x57\x40\x5a\x40\x0b\x49\x5b\x59\x41\x4f\x50\x59\x50'\
b'\x59\x52\x4b\x52\x4b\x51\x55\x43\x4c\x43\x4c\x40\x59\x40\x59'\
b'\x41\x1a\x4c\x58\x56\x58\x51\x58\x51\x52\x51\x4d\x51\x4a\x4e'\
b'\x49\x4e\x47\x51\x47\x51\x44\x51\x3e\x51\x39\x56\x39\x56\x3b'\
b'\x53\x3b\x53\x3f\x53\x44\x53\x47\x51\x48\x51\x48\x53\x49\x53'\
b'\x4d\x53\x52\x53\x54\x55\x55\x56\x55\x56\x58\x05\x4f\x55\x53'\
b'\x5a\x51\x5a\x51\x37\x53\x37\x53\x5a\x1a\x4c\x58\x56\x49\x53'\
b'\x4a\x53\x4d\x53\x52\x53\x58\x4e\x58\x4e\x55\x4f\x55\x51\x54'\
b'\x51\x52\x51\x4d\x51\x49\x53\x48\x53\x48\x51\x47\x51\x44\x51'\
b'\x3f\x51\x3b\x4e\x3b\x4e\x39\x53\x39\x53\x3e\x53\x44\x53\x47'\
b'\x56\x47\x56\x49\x16\x47\x5d\x5b\x45\x5a\x47\x58\x4a\x56\x4a'\
b'\x54\x4a\x51\x48\x4f\x47\x4e\x47\x4c\x47\x4c\x4a\x49\x4a\x49'\
b'\x48\x4c\x45\x4e\x45\x50\x45\x52\x46\x55\x48\x56\x48\x57\x48'\
b'\x58\x46\x58\x45\x5b\x45\x13\x44\x60\x49\x36\x5b\x36\x5e\x36'\
b'\x5e\x3a\x5e\x52\x5e\x55\x5b\x55\x49\x55\x46\x55\x46\x52\x46'\
b'\x3a\x46\x36\x49\x36\x20\x52\x5b\x52\x5b\x3a\x49\x3a\x49\x52'\
b'\x5b\x52'

_index =\
b'\x00\x00\x03\x00\x2c\x00\x45\x00\x8e\x00\xf1\x00\x6e\x01\x4b'\
b'\x02\x58\x02\x71\x02\x8a\x02\xad\x02\xca\x02\xd7\x02\xe4\x02'\
b'\x01\x03\x0e\x03\x3d\x03\x56\x03\x8b\x03\xd4\x03\x03\x04\x3c'\
b'\x04\x8b\x04\x9e\x04\xff\x04\x50\x05\x89\x05\xb2\x05\xc7\x05'\
b'\xe0\x05\xf5\x05\x66\x06\xeb\x06\x14\x07\x61\x07\x92\x07\xbb'\
b'\x07\xd8\x07\xf1\x07\x2a\x08\x47\x08\x64\x08\x83\x08\xaa\x08'\
b'\xbb\x08\xf8\x08\x25\x09\x5e\x09\x8d\x09\x08\x0a\x61\x0a\xd2'\
b'\x0a\xe7\x0a\x08\x0b\x25\x0b\x62\x0b\x93\x0b\xb4\x0b\xcd\x0b'\
b'\xe2\x0b\xef\x0b\x04\x0c\x19\x0c\x26\x0c\x33\x0c\x7c\x0c\xc1'\
b'\x0c\xf2\x0c\x37\x0d\x74\x0d\xa3\x0d\xf8\x0d\x21\x0e\x4a\x0e'\
b'\x85\x0e\xa4\x0e\xb1\x0e\xf6\x0e\x21\x0f\x5a\x0f\x9f\x0f\xe4'\
b'\x0f\x0b\x10\x6e\x10\x9d\x10\xc6\x10\xe3\x10\x20\x11\x4d\x11'\
b'\x7c\x11\x95\x11\xcc\x11\xd9\x11\x10\x12\x3f\x12'

FONT = memoryview(_font)
INDEX = memoryview(_index)
