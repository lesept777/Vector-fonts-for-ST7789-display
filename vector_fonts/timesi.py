FIRST = 32
LAST = 127
WIDTH = 36
HEIGHT = 34

_font =\
b'\x01\x4e\x56\x24\x4c\x58\x51\x4c\x50\x4c\x51\x49\x51\x45\x52'\
b'\x42\x53\x3d\x53\x3c\x53\x3a\x54\x39\x55\x39\x55\x39\x56\x39'\
b'\x56\x3a\x56\x3a\x56\x3b\x56\x3c\x55\x3f\x53\x44\x52\x47\x52'\
b'\x47\x52\x48\x51\x4c\x20\x52\x4f\x4f\x50\x4f\x51\x50\x51\x51'\
b'\x51\x52\x50\x53\x4f\x53\x4f\x53\x4e\x52\x4e\x51\x4e\x50\x4f'\
b'\x4f\x4f\x4f\x23\x4a\x5a\x53\x43\x53\x3e\x54\x3c\x54\x3c\x54'\
b'\x3b\x54\x3a\x55\x39\x56\x39\x56\x39\x57\x39\x58\x3a\x58\x3a'\
b'\x58\x3b\x57\x3b\x57\x3d\x56\x3e\x54\x43\x53\x43\x20\x52\x4c'\
b'\x43\x4d\x3e\x4d\x3c\x4d\x3b\x4e\x3a\x4f\x39\x50\x39\x50\x39'\
b'\x51\x3a\x51\x3a\x51\x3b\x51\x3b\x51\x3c\x50\x3e\x4d\x43\x4c'\
b'\x43\x23\x47\x5d\x4b\x53\x4c\x4a\x49\x4a\x49\x49\x4d\x49\x4e'\
b'\x43\x49\x43\x49\x41\x4e\x41\x50\x39\x52\x39\x50\x41\x56\x41'\
b'\x58\x39\x59\x39\x58\x41\x5b\x41\x5b\x43\x57\x43\x56\x49\x5b'\
b'\x49\x5b\x4a\x56\x4a\x54\x53\x53\x53\x54\x4a\x4e\x4a\x4c\x53'\
b'\x4b\x53\x20\x52\x4e\x49\x54\x49\x56\x43\x50\x43\x4e\x49\x45'\
b'\x48\x5c\x56\x3b\x54\x43\x57\x46\x58\x48\x59\x49\x59\x4b\x59'\
b'\x4d\x56\x51\x52\x52\x4f\x52\x4f\x54\x4e\x54\x4e\x52\x4d\x52'\
b'\x4b\x51\x4a\x50\x4b\x4b\x4c\x4b\x4c\x4c\x4c\x4d\x4c\x4e\x4d'\
b'\x51\x4f\x51\x52\x46\x4f\x44\x4d\x41\x4d\x3f\x4d\x3d\x52\x39'\
b'\x54\x39\x54\x39\x55\x39\x56\x38\x57\x38\x57\x3a\x58\x3a\x59'\
b'\x3b\x5a\x3c\x59\x40\x58\x40\x58\x3f\x58\x3f\x58\x3d\x58\x3c'\
b'\x57\x3b\x56\x3b\x20\x52\x55\x3a\x54\x3a\x54\x3a\x52\x3a\x50'\
b'\x3d\x50\x3e\x50\x3f\x51\x41\x53\x43\x55\x3a\x20\x52\x50\x51'\
b'\x50\x51\x50\x51\x52\x51\x54\x50\x56\x4d\x56\x4c\x56\x4b\x55'\
b'\x48\x53\x47\x50\x51\x46\x42\x62\x60\x39\x46\x53\x44\x53\x5e'\
b'\x39\x60\x39\x20\x52\x4b\x39\x4d\x39\x50\x3c\x50\x3e\x50\x41'\
b'\x4b\x46\x49\x46\x47\x46\x44\x43\x44\x41\x44\x3e\x49\x39\x4b'\
b'\x39\x20\x52\x4b\x3a\x4b\x3a\x4a\x3a\x49\x3c\x47\x41\x47\x43'\
b'\x47\x44\x48\x45\x48\x45\x49\x45\x4a\x45\x4b\x44\x4d\x3e\x4d'\
b'\x3c\x4d\x3b\x4c\x3a\x4b\x3a\x20\x52\x5b\x46\x5d\x46\x60\x49'\
b'\x60\x4b\x60\x4d\x5e\x51\x5a\x53\x59\x53\x57\x53\x55\x50\x55'\
b'\x4e\x55\x4b\x59\x46\x5b\x46\x20\x52\x5c\x47\x5b\x47\x5a\x47'\
b'\x59\x48\x57\x4e\x57\x50\x57\x51\x58\x52\x59\x52\x59\x52\x5a'\
b'\x52\x5b\x50\x5d\x4b\x5d\x49\x5d\x48\x5c\x47\x5c\x47\x4e\x43'\
b'\x61\x57\x45\x5e\x45\x5e\x46\x5d\x46\x5b\x47\x59\x49\x58\x4c'\
b'\x56\x4d\x59\x51\x5b\x51\x5d\x51\x5e\x50\x5f\x50\x5e\x51\x5b'\
b'\x53\x5a\x53\x58\x53\x55\x51\x54\x50\x52\x51\x4e\x53\x4c\x53'\
b'\x49\x53\x45\x4f\x45\x4c\x45\x49\x48\x47\x4a\x45\x4f\x43\x4f'\
b'\x43\x4f\x41\x4f\x41\x4f\x3d\x53\x39\x56\x39\x58\x39\x5a\x3b'\
b'\x5a\x3c\x5a\x3e\x57\x42\x53\x43\x54\x49\x56\x4c\x59\x49\x59'\
b'\x47\x59\x46\x58\x46\x57\x46\x57\x45\x20\x52\x52\x42\x55\x41'\
b'\x56\x40\x57\x3e\x57\x3d\x57\x3b\x56\x3a\x55\x3a\x54\x3a\x52'\
b'\x3c\x52\x3f\x52\x40\x52\x41\x52\x42\x20\x52\x50\x44\x4c\x46'\
b'\x49\x49\x49\x4c\x49\x4e\x4c\x51\x4e\x51\x4f\x51\x52\x50\x53'\
b'\x4f\x52\x4d\x50\x47\x50\x44\x10\x4e\x56\x50\x43\x50\x3e\x50'\
b'\x3c\x51\x3b\x51\x3a\x52\x39\x53\x39\x54\x39\x54\x3a\x54\x3a'\
b'\x54\x3b\x54\x3b\x54\x3c\x53\x3e\x50\x43\x50\x43\x12\x49\x5b'\
b'\x4f\x5a\x4f\x5a\x4d\x56\x4c\x53\x4b\x50\x4b\x4e\x4b\x48\x4e'\
b'\x43\x51\x3e\x59\x38\x59\x39\x56\x3b\x53\x3e\x51\x42\x4d\x4d'\
b'\x4d\x52\x4d\x55\x4f\x5a\x12\x49\x5b\x55\x39\x55\x38\x57\x3c'\
b'\x58\x3f\x59\x42\x59\x44\x59\x4a\x56\x4f\x53\x55\x4b\x5a\x4b'\
b'\x59\x4e\x57\x51\x54\x53\x50\x57\x45\x57\x41\x57\x3d\x55\x39'\
b'\x54\x49\x5b\x52\x3f\x52\x3e\x51\x3d\x51\x3b\x51\x3a\x51\x39'\
b'\x51\x38\x52\x38\x53\x38\x53\x39\x53\x3a\x53\x3b\x53\x3e\x52'\
b'\x3f\x53\x3e\x54\x3e\x55\x3c\x57\x3b\x57\x3b\x58\x3b\x59\x3c'\
b'\x59\x3d\x59\x3d\x57\x3f\x55\x3f\x54\x3f\x53\x40\x54\x40\x55'\
b'\x40\x57\x41\x59\x42\x59\x43\x59\x43\x58\x44\x57\x44\x57\x44'\
b'\x55\x43\x54\x42\x54\x41\x52\x40\x52\x41\x53\x43\x53\x45\x53'\
b'\x46\x53\x46\x53\x47\x52\x47\x51\x47\x51\x47\x51\x46\x51\x46'\
b'\x51\x45\x51\x42\x52\x41\x52\x40\x51\x41\x50\x42\x4e\x43\x4e'\
b'\x44\x4d\x44\x4d\x44\x4c\x44\x4b\x43\x4b\x43\x4b\x42\x4c\x41'\
b'\x4d\x41\x4d\x41\x4f\x40\x50\x40\x51\x40\x50\x3f\x4f\x3f\x4d'\
b'\x3f\x4c\x3e\x4b\x3e\x4b\x3d\x4b\x3c\x4c\x3b\x4d\x3b\x4d\x3b'\
b'\x4f\x3c\x51\x3e\x52\x3f\x0d\x46\x5e\x51\x4f\x51\x46\x48\x46'\
b'\x48\x45\x51\x45\x51\x3c\x53\x3c\x53\x45\x5c\x45\x5c\x46\x53'\
b'\x46\x53\x4f\x51\x4f\x16\x4d\x57\x4f\x56\x51\x55\x52\x55\x52'\
b'\x54\x52\x53\x52\x53\x52\x53\x52\x52\x51\x52\x51\x51\x51\x51'\
b'\x51\x51\x51\x50\x52\x4f\x53\x4f\x54\x4f\x55\x50\x55\x51\x55'\
b'\x52\x52\x56\x50\x57\x4f\x56\x05\x4b\x59\x57\x49\x56\x4b\x4d'\
b'\x4b\x4e\x49\x57\x49\x0d\x4e\x56\x52\x4f\x53\x4f\x54\x50\x54'\
b'\x51\x54\x51\x53\x52\x52\x52\x51\x52\x50\x51\x50\x51\x50\x50'\
b'\x51\x4f\x52\x4f\x05\x48\x5c\x5a\x38\x4c\x53\x4a\x53\x58\x38'\
b'\x5a\x38\x28\x48\x5c\x55\x39\x57\x39\x5a\x3d\x5a\x41\x5a\x45'\
b'\x58\x4c\x56\x4f\x54\x51\x52\x52\x51\x52\x4f\x52\x4d\x52\x4a'\
b'\x4f\x4a\x4a\x4a\x46\x4c\x42\x4d\x3d\x50\x3b\x52\x39\x55\x39'\
b'\x20\x52\x55\x3a\x54\x3a\x51\x3b\x4f\x41\x4e\x45\x4d\x4a\x4d'\
b'\x4e\x4d\x50\x4e\x52\x4f\x52\x51\x52\x51\x51\x53\x4f\x55\x4a'\
b'\x57\x43\x57\x3e\x57\x3c\x56\x3a\x55\x3a\x1d\x49\x5b\x59\x39'\
b'\x53\x4d\x52\x4f\x52\x50\x52\x50\x53\x51\x55\x51\x55\x52\x4b'\
b'\x52\x4c\x51\x4d\x51\x4e\x51\x4e\x51\x4f\x50\x4f\x4f\x50\x4d'\
b'\x54\x3f\x55\x3d\x55\x3d\x55\x3d\x55\x3c\x55\x3c\x54\x3b\x53'\
b'\x3b\x53\x3b\x52\x3b\x52\x3b\x58\x39\x59\x39\x1f\x48\x5c\x56'\
b'\x52\x4a\x52\x4a\x51\x53\x49\x56\x44\x57\x42\x57\x40\x57\x3e'\
b'\x55\x3c\x53\x3c\x51\x3c\x4f\x3e\x4e\x3e\x4f\x3b\x53\x39\x55'\
b'\x39\x57\x39\x5a\x3c\x5a\x3e\x5a\x40\x5a\x41\x59\x43\x57\x46'\
b'\x53\x4a\x4d\x4f\x53\x4f\x55\x4f\x57\x4e\x57\x4d\x58\x4d\x56'\
b'\x52\x30\x48\x5c\x4f\x45\x4f\x44\x53\x43\x55\x41\x57\x40\x57'\
b'\x3e\x57\x3d\x55\x3b\x54\x3b\x52\x3b\x50\x3d\x4f\x3d\x50\x3b'\
b'\x53\x39\x55\x39\x57\x39\x5a\x3b\x5a\x3d\x5a\x3f\x57\x42\x54'\
b'\x43\x56\x44\x58\x47\x58\x49\x58\x4b\x55\x50\x51\x52\x4e\x52'\
b'\x4c\x52\x4b\x52\x4a\x51\x4a\x50\x4a\x50\x4b\x4f\x4c\x4f\x4c'\
b'\x4f\x4d\x4f\x4d\x4f\x4f\x50\x51\x51\x51\x51\x53\x51\x55\x4d'\
b'\x55\x4b\x55\x49\x54\x46\x50\x45\x4f\x45\x11\x48\x5c\x5a\x39'\
b'\x56\x4a\x59\x4a\x58\x4c\x55\x4c\x53\x52\x51\x52\x52\x4c\x4a'\
b'\x4c\x4a\x49\x59\x39\x5a\x39\x20\x52\x56\x3e\x4c\x4a\x53\x4a'\
b'\x56\x3e\x24\x48\x5c\x52\x39\x5a\x39\x59\x3c\x52\x3c\x51\x3f'\
b'\x54\x40\x55\x41\x58\x43\x58\x47\x58\x4a\x56\x4e\x53\x51\x52'\
b'\x51\x50\x52\x4d\x52\x4c\x52\x4a\x52\x4a\x51\x4a\x50\x4a\x50'\
b'\x4b\x4f\x4b\x4f\x4c\x4f\x4e\x50\x4e\x50\x4f\x50\x4f\x51\x50'\
b'\x51\x52\x51\x55\x4d\x55\x49\x55\x47\x53\x44\x50\x42\x4e\x42'\
b'\x52\x39\x26\x47\x5d\x5b\x39\x5b\x3a\x57\x3a\x52\x3f\x4f\x43'\
b'\x51\x42\x53\x42\x55\x42\x58\x45\x58\x48\x58\x4c\x53\x52\x4f'\
b'\x52\x4c\x52\x49\x4e\x49\x4b\x49\x48\x4d\x40\x53\x3b\x56\x3a'\
b'\x58\x39\x5b\x39\x20\x52\x4f\x44\x4c\x4a\x4c\x4d\x4c\x4f\x4e'\
b'\x52\x4f\x52\x51\x52\x55\x4c\x55\x48\x55\x45\x53\x43\x51\x43'\
b'\x51\x43\x50\x43\x4f\x44\x0c\x48\x5c\x4d\x39\x5a\x39\x5a\x3a'\
b'\x4c\x52\x4a\x52\x56\x3c\x51\x3c\x4e\x3c\x4c\x3d\x4b\x3f\x4b'\
b'\x3f\x4d\x39\x36\x48\x5c\x55\x44\x56\x46\x58\x49\x58\x4b\x58'\
b'\x4e\x54\x52\x50\x52\x4d\x52\x4a\x4f\x4a\x4c\x4a\x4a\x4d\x46'\
b'\x51\x45\x4f\x43\x4e\x40\x4e\x3f\x4e\x3c\x52\x39\x54\x39\x57'\
b'\x39\x5a\x3c\x5a\x3e\x5a\x40\x58\x43\x55\x44\x20\x52\x54\x43'\
b'\x56\x43\x58\x40\x58\x3e\x58\x3c\x56\x3a\x54\x3a\x53\x3a\x51'\
b'\x3c\x51\x3d\x51\x3f\x51\x40\x52\x41\x54\x43\x20\x52\x52\x45'\
b'\x4f\x46\x4c\x4b\x4c\x4d\x4c\x4f\x4f\x52\x51\x52\x53\x52\x55'\
b'\x4f\x55\x4d\x55\x4b\x54\x48\x52\x45\x29\x47\x5d\x49\x52\x49'\
b'\x52\x4b\x51\x4d\x51\x4f\x4f\x53\x4b\x55\x49\x53\x49\x52\x4a'\
b'\x51\x4a\x4f\x4a\x4c\x46\x4c\x43\x4c\x3f\x51\x39\x55\x39\x57'\
b'\x39\x5b\x3d\x5b\x40\x5b\x44\x57\x4b\x51\x50\x4e\x51\x4c\x52'\
b'\x49\x52\x20\x52\x55\x47\x58\x42\x58\x3e\x58\x3c\x56\x3a\x55'\
b'\x3a\x53\x3a\x4f\x40\x4f\x44\x4f\x46\x51\x48\x53\x48\x53\x48'\
b'\x54\x48\x55\x47\x1b\x4c\x58\x54\x42\x55\x42\x56\x43\x56\x43'\
b'\x56\x44\x55\x45\x54\x45\x53\x45\x52\x44\x52\x43\x52\x43\x53'\
b'\x42\x54\x42\x20\x52\x50\x4f\x51\x4f\x52\x50\x52\x51\x52\x51'\
b'\x51\x52\x50\x52\x4f\x52\x4e\x51\x4e\x51\x4e\x50\x4f\x4f\x50'\
b'\x4f\x25\x4b\x59\x55\x42\x55\x42\x57\x43\x57\x43\x57\x44\x55'\
b'\x45\x55\x45\x54\x45\x53\x44\x53\x43\x53\x43\x54\x42\x55\x42'\
b'\x20\x52\x4d\x56\x4f\x55\x50\x54\x50\x53\x50\x53\x50\x53\x50'\
b'\x52\x4f\x51\x4f\x51\x4f\x51\x4f\x51\x4f\x50\x50\x4f\x51\x4f'\
b'\x52\x4f\x53\x50\x53\x51\x53\x52\x51\x54\x50\x55\x50\x56\x4e'\
b'\x57\x4d\x56\x08\x46\x5e\x48\x45\x5c\x3d\x5c\x3e\x4b\x46\x5c'\
b'\x4d\x5c\x4f\x48\x46\x48\x45\x0b\x46\x5e\x48\x42\x5c\x42\x5c'\
b'\x43\x48\x43\x48\x42\x20\x52\x48\x48\x5c\x48\x5c\x49\x48\x49'\
b'\x48\x48\x08\x46\x5e\x5c\x46\x48\x4f\x48\x4d\x59\x46\x48\x3e'\
b'\x48\x3d\x5c\x45\x5c\x46\x32\x49\x5b\x4e\x4c\x4e\x4c\x4e\x4a'\
b'\x4f\x46\x54\x41\x55\x3f\x56\x3e\x56\x3d\x56\x3c\x54\x3a\x52'\
b'\x3a\x51\x3a\x50\x3a\x4f\x3b\x4f\x3b\x4f\x3c\x50\x3d\x50\x3d'\
b'\x50\x3e\x4f\x3f\x4e\x3f\x4e\x3f\x4d\x3e\x4d\x3d\x4d\x3b\x50'\
b'\x39\x52\x39\x55\x39\x59\x3c\x59\x3e\x59\x40\x58\x41\x57\x42'\
b'\x51\x46\x4f\x49\x4e\x4c\x20\x52\x4d\x4f\x4e\x4f\x4f\x50\x4f'\
b'\x51\x4f\x51\x4e\x53\x4d\x53\x4c\x53\x4b\x51\x4b\x51\x4b\x50'\
b'\x4c\x4f\x4d\x4f\x58\x40\x64\x5a\x41\x58\x48\x57\x4c\x56\x4e'\
b'\x56\x4f\x56\x4f\x57\x50\x58\x50\x59\x50\x5d\x4d\x5f\x48\x5f'\
b'\x44\x5f\x41\x5c\x3c\x57\x39\x53\x39\x4f\x39\x48\x3e\x44\x46'\
b'\x44\x4a\x44\x4f\x48\x55\x4e\x59\x52\x59\x57\x59\x5f\x54\x61'\
b'\x4f\x62\x4f\x60\x54\x58\x5a\x52\x5a\x4e\x5a\x46\x56\x42\x4e'\
b'\x42\x4a\x42\x45\x47\x3d\x4f\x38\x53\x38\x57\x38\x5d\x3b\x60'\
b'\x41\x60\x45\x60\x48\x5d\x4e\x59\x51\x56\x51\x55\x51\x54\x50'\
b'\x54\x4f\x54\x4e\x54\x4c\x51\x50\x4e\x51\x4d\x51\x4b\x51\x49'\
b'\x4f\x49\x4d\x49\x4b\x4d\x44\x50\x42\x52\x41\x53\x41\x55\x41'\
b'\x56\x42\x57\x43\x57\x41\x5a\x41\x20\x52\x54\x41\x52\x41\x51'\
b'\x43\x4f\x45\x4d\x48\x4c\x4b\x4c\x4d\x4c\x4e\x4e\x4f\x4e\x4f'\
b'\x4f\x4f\x52\x4e\x54\x4a\x55\x49\x56\x46\x56\x44\x56\x43\x55'\
b'\x41\x54\x41\x29\x45\x5f\x5c\x39\x5a\x4d\x5a\x4f\x5a\x4f\x5a'\
b'\x50\x5a\x50\x5a\x51\x5c\x51\x5d\x51\x5d\x52\x53\x52\x53\x51'\
b'\x54\x51\x55\x51\x56\x51\x56\x50\x57\x50\x57\x4f\x57\x4d\x57'\
b'\x4a\x50\x4a\x4e\x4d\x4d\x4e\x4c\x4f\x4c\x50\x4c\x50\x4d\x51'\
b'\x4e\x51\x4e\x52\x47\x52\x47\x51\x48\x51\x4b\x50\x4d\x4d\x5b'\
b'\x39\x5c\x39\x20\x52\x58\x3f\x51\x49\x57\x49\x58\x3f\x3d\x45'\
b'\x5f\x4d\x3a\x4d\x39\x56\x39\x58\x39\x5c\x3b\x5d\x3d\x5d\x3f'\
b'\x5d\x41\x5a\x44\x57\x45\x59\x46\x5b\x49\x5b\x4a\x5b\x4c\x59'\
b'\x4f\x56\x51\x54\x52\x53\x52\x50\x52\x47\x52\x47\x51\x48\x51'\
b'\x49\x51\x49\x51\x4a\x50\x4a\x50\x4b\x4d\x4f\x3e\x50\x3c\x50'\
b'\x3c\x50\x3b\x4f\x3a\x4e\x3a\x4d\x3a\x4d\x3a\x20\x52\x51\x44'\
b'\x52\x44\x52\x44\x56\x44\x5a\x41\x5a\x3f\x5a\x3d\x58\x3b\x55'\
b'\x3b\x54\x3b\x53\x3b\x51\x44\x20\x52\x4d\x50\x4f\x51\x50\x51'\
b'\x53\x51\x57\x4d\x57\x4a\x57\x48\x55\x46\x52\x46\x51\x46\x50'\
b'\x46\x4d\x50\x29\x44\x60\x5e\x39\x5c\x41\x5b\x41\x5b\x3f\x5b'\
b'\x3e\x5b\x3c\x59\x3b\x57\x3a\x56\x3a\x53\x3a\x50\x3c\x4d\x3e'\
b'\x4b\x42\x4a\x46\x4a\x49\x4a\x4d\x4e\x51\x52\x51\x54\x51\x58'\
b'\x4f\x5a\x4c\x5b\x4c\x59\x50\x54\x53\x50\x53\x4d\x53\x49\x50'\
b'\x46\x4b\x46\x49\x46\x45\x4a\x3d\x52\x39\x56\x39\x58\x39\x5a'\
b'\x3a\x5b\x3a\x5b\x3a\x5c\x3a\x5c\x3a\x5d\x39\x5e\x39\x31\x42'\
b'\x62\x4b\x3a\x4b\x39\x53\x39\x58\x39\x5d\x3c\x60\x41\x60\x43'\
b'\x60\x46\x5e\x4a\x5c\x4d\x58\x50\x53\x52\x4f\x52\x44\x52\x45'\
b'\x51\x46\x51\x47\x51\x47\x51\x48\x50\x48\x4f\x49\x4d\x4d\x3e'\
b'\x4e\x3d\x4e\x3c\x4e\x3b\x4d\x3a\x4b\x3a\x4b\x3a\x20\x52\x51'\
b'\x3b\x4c\x4d\x4b\x4f\x4b\x50\x4b\x50\x4c\x51\x4c\x51\x4d\x51'\
b'\x4e\x51\x50\x51\x55\x50\x57\x4e\x59\x4d\x5c\x47\x5c\x43\x5c'\
b'\x3f\x58\x3b\x54\x3b\x53\x3b\x51\x3b\x39\x44\x60\x53\x3b\x50'\
b'\x44\x52\x44\x55\x44\x57\x43\x58\x41\x58\x41\x56\x4a\x55\x4a'\
b'\x55\x49\x55\x48\x55\x47\x55\x46\x54\x46\x52\x46\x50\x46\x4d'\
b'\x4e\x4d\x4f\x4d\x50\x4d\x50\x4d\x51\x4e\x51\x4f\x51\x51\x51'\
b'\x55\x51\x59\x4e\x5a\x4b\x5b\x4b\x59\x52\x46\x52\x46\x51\x47'\
b'\x51\x48\x51\x49\x51\x49\x50\x4a\x4f\x4a\x4d\x4f\x3e\x4f\x3c'\
b'\x4f\x3c\x4f\x3b\x4e\x3a\x4d\x3a\x4c\x3a\x4c\x39\x5e\x39\x5d'\
b'\x3f\x5c\x3f\x5c\x3f\x5c\x3e\x5c\x3d\x5c\x3c\x5b\x3b\x5a\x3b'\
b'\x59\x3b\x56\x3b\x53\x3b\x31\x43\x61\x52\x3b\x4f\x44\x52\x44'\
b'\x55\x44\x57\x43\x58\x41\x59\x41\x56\x4a\x55\x4a\x56\x49\x56'\
b'\x48\x56\x47\x54\x46\x52\x46\x4f\x46\x4d\x4d\x4c\x4f\x4c\x50'\
b'\x4c\x50\x4d\x51\x4f\x51\x4f\x52\x45\x52\x45\x51\x47\x51\x47'\
b'\x51\x48\x51\x48\x50\x49\x4f\x49\x4d\x4e\x3e\x4e\x3d\x4e\x3c'\
b'\x4e\x3b\x4e\x3a\x4d\x3a\x4c\x3a\x4c\x39\x5f\x39\x5d\x40\x5c'\
b'\x40\x5d\x3f\x5d\x3e\x5d\x3d\x5b\x3b\x5a\x3b\x59\x3b\x57\x3b'\
b'\x52\x3b\x38\x44\x60\x5e\x39\x5c\x41\x5b\x41\x5c\x3f\x5c\x3f'\
b'\x5c\x3d\x58\x3a\x56\x3a\x50\x3a\x4d\x3f\x4a\x44\x4a\x49\x4a'\
b'\x4c\x4d\x51\x51\x51\x52\x51\x53\x51\x55\x50\x57\x4a\x57\x49'\
b'\x57\x48\x57\x47\x57\x47\x56\x46\x54\x46\x54\x46\x54\x46\x5e'\
b'\x46\x5e\x46\x5d\x46\x5b\x47\x5b\x48\x5b\x48\x5a\x4b\x58\x51'\
b'\x56\x52\x53\x53\x51\x53\x4d\x53\x48\x50\x46\x4b\x46\x48\x46'\
b'\x45\x49\x40\x4d\x3c\x4f\x3a\x52\x39\x56\x39\x58\x39\x5a\x3a'\
b'\x5b\x3a\x5c\x3a\x5c\x3a\x5d\x3a\x5d\x39\x5e\x39\x43\x40\x64'\
b'\x4d\x44\x58\x44\x5a\x3e\x5a\x3d\x5a\x3c\x5a\x3b\x5a\x3a\x59'\
b'\x3a\x57\x3a\x58\x39\x62\x39\x61\x3a\x60\x3a\x5f\x3a\x5f\x3b'\
b'\x5e\x3b\x5e\x3c\x5d\x3e\x59\x4d\x58\x4f\x58\x50\x58\x50\x59'\
b'\x51\x5b\x51\x5b\x52\x51\x52\x51\x51\x53\x51\x53\x51\x54\x51'\
b'\x54\x50\x55\x50\x55\x4d\x58\x46\x4c\x46\x4a\x4d\x49\x4f\x49'\
b'\x50\x49\x50\x4a\x51\x4c\x51\x4c\x52\x42\x52\x43\x51\x44\x51'\
b'\x45\x51\x45\x51\x46\x50\x46\x4f\x47\x4d\x4b\x3e\x4c\x3c\x4c'\
b'\x3c\x4c\x3b\x4b\x3a\x4a\x3a\x49\x3a\x49\x39\x53\x39\x53\x3a'\
b'\x51\x3a\x51\x3a\x50\x3b\x50\x3b\x4f\x3c\x4e\x3e\x4d\x44\x20'\
b'\x48\x5c\x54\x51\x54\x52\x4a\x52\x4a\x51\x4c\x51\x4c\x51\x4d'\
b'\x51\x4d\x50\x4e\x4f\x4e\x4d\x53\x3e\x53\x3c\x53\x3c\x53\x3b'\
b'\x53\x3a\x52\x3a\x50\x3a\x51\x39\x5a\x39\x5a\x3a\x59\x3a\x58'\
b'\x3a\x57\x3b\x57\x3c\x56\x3e\x52\x4d\x51\x4f\x51\x50\x51\x50'\
b'\x52\x51\x53\x51\x54\x51\x29\x45\x5f\x53\x39\x5d\x39\x5d\x3a'\
b'\x5b\x3a\x59\x3b\x58\x3e\x55\x49\x54\x4c\x53\x4e\x52\x50\x4e'\
b'\x53\x4c\x53\x49\x53\x47\x51\x47\x4f\x47\x4e\x49\x4d\x4a\x4d'\
b'\x4a\x4d\x4b\x4e\x4b\x4e\x4b\x4f\x4b\x50\x4a\x50\x4a\x50\x4a'\
b'\x51\x4b\x51\x4c\x51\x4c\x51\x4e\x51\x50\x4f\x51\x4d\x52\x4b'\
b'\x52\x48\x55\x3e\x56\x3c\x56\x3c\x56\x3b\x55\x3a\x53\x3a\x53'\
b'\x39\x40\x42\x62\x51\x44\x57\x4d\x59\x50\x5b\x51\x5c\x51\x5c'\
b'\x52\x52\x52\x52\x51\x53\x51\x54\x50\x54\x50\x54\x4f\x54\x4f'\
b'\x54\x4e\x53\x4d\x4e\x45\x4c\x4d\x4b\x4f\x4b\x50\x4b\x50\x4c'\
b'\x51\x4e\x51\x4e\x52\x44\x52\x44\x51\x46\x51\x46\x51\x47\x51'\
b'\x47\x50\x48\x4f\x48\x4d\x4d\x3e\x4d\x3d\x4d\x3c\x4d\x3b\x4c'\
b'\x3a\x4b\x3a\x4b\x3a\x4b\x39\x54\x39\x54\x3a\x53\x3a\x52\x3a'\
b'\x51\x3b\x51\x3c\x50\x3e\x4e\x45\x57\x3e\x58\x3d\x59\x3c\x59'\
b'\x3b\x59\x3b\x59\x3b\x59\x3a\x58\x3a\x58\x39\x60\x39\x60\x3a'\
b'\x5f\x3a\x5d\x3b\x5c\x3c\x5c\x3c\x58\x3e\x51\x44\x2a\x46\x5e'\
b'\x5a\x52\x48\x52\x48\x51\x49\x51\x4a\x51\x4b\x51\x4b\x50\x4c'\
b'\x4f\x4c\x4d\x51\x3e\x51\x3c\x51\x3c\x51\x3b\x50\x3a\x4f\x3a'\
b'\x4e\x3a\x4e\x3a\x4e\x39\x58\x39\x58\x3a\x57\x3a\x55\x3b\x55'\
b'\x3b\x54\x3c\x54\x3f\x4f\x4d\x4f\x4f\x4f\x50\x4f\x50\x4f\x50'\
b'\x50\x51\x51\x51\x53\x51\x56\x51\x57\x50\x58\x50\x59\x4f\x5a'\
b'\x4e\x5b\x4c\x5c\x4b\x5c\x4b\x5a\x52\x33\x3e\x66\x4d\x39\x4f'\
b'\x4d\x5e\x39\x64\x39\x64\x3a\x62\x3a\x61\x3a\x61\x3b\x60\x3c'\
b'\x5f\x3e\x5b\x4e\x5a\x4f\x5a\x50\x5a\x50\x5b\x51\x5c\x51\x5d'\
b'\x51\x5d\x51\x5d\x52\x53\x52\x53\x51\x54\x51\x55\x51\x56\x51'\
b'\x56\x51\x57\x4f\x58\x4c\x5c\x3e\x4e\x52\x4d\x52\x4b\x3e\x46'\
b'\x4d\x46\x4f\x46\x50\x46\x50\x47\x51\x49\x51\x48\x52\x40\x52'\
b'\x40\x51\x41\x51\x43\x51\x44\x50\x44\x50\x45\x4e\x4a\x3b\x49'\
b'\x3b\x48\x3a\x47\x3a\x47\x39\x4d\x39\x2b\x41\x63\x4f\x39\x57'\
b'\x4d\x5b\x3e\x5b\x3d\x5b\x3c\x5b\x3b\x5a\x3a\x59\x3a\x59\x3a'\
b'\x59\x3a\x59\x39\x61\x39\x60\x3a\x5f\x3a\x5f\x3a\x5e\x3b\x5d'\
b'\x3b\x5d\x3c\x5c\x3e\x56\x53\x56\x53\x4e\x3e\x49\x4d\x49\x4f'\
b'\x49\x50\x49\x50\x4a\x51\x4b\x51\x4b\x52\x43\x52\x44\x51\x45'\
b'\x51\x46\x51\x46\x51\x47\x50\x47\x4f\x48\x4d\x4d\x3c\x4c\x3b'\
b'\x4a\x3a\x49\x3a\x49\x39\x4f\x39\x26\x44\x60\x56\x39\x58\x39'\
b'\x5c\x3b\x5e\x3f\x5e\x41\x5e\x45\x5a\x4e\x52\x53\x4e\x53\x4b'\
b'\x53\x48\x50\x46\x4c\x46\x4a\x46\x47\x49\x40\x4e\x3b\x53\x39'\
b'\x56\x39\x20\x52\x55\x3a\x53\x3a\x50\x3c\x4d\x40\x4b\x43\x4a'\
b'\x47\x4a\x4b\x4a\x4d\x4c\x51\x4f\x51\x51\x51\x54\x50\x55\x4e'\
b'\x58\x4b\x5b\x44\x5b\x40\x5b\x3e\x58\x3a\x55\x3a\x2c\x44\x60'\
b'\x4d\x39\x56\x39\x5a\x39\x5e\x3d\x5e\x3f\x5e\x41\x5c\x44\x57'\
b'\x47\x54\x47\x52\x47\x50\x46\x4e\x4d\x4d\x4f\x4d\x50\x4d\x50'\
b'\x4e\x51\x50\x51\x50\x52\x46\x52\x46\x51\x48\x51\x4a\x50\x4b'\
b'\x4d\x4f\x3f\x4f\x3c\x4f\x3c\x4f\x3b\x4e\x3a\x4d\x3a\x4d\x39'\
b'\x20\x52\x50\x45\x52\x45\x53\x45\x55\x45\x59\x44\x5a\x40\x5a'\
b'\x3f\x5a\x3d\x58\x3b\x56\x3b\x55\x3b\x53\x3b\x50\x45\x3b\x44'\
b'\x60\x4f\x53\x4a\x56\x4b\x56\x4c\x56\x4d\x56\x4e\x56\x54\x58'\
b'\x55\x58\x57\x58\x5a\x56\x5c\x54\x5c\x55\x5a\x57\x55\x5a\x52'\
b'\x5a\x51\x5a\x4e\x59\x4a\x58\x48\x58\x48\x58\x47\x58\x46\x59'\
b'\x46\x58\x4d\x52\x4a\x52\x46\x4d\x46\x4a\x46\x46\x4b\x3e\x52'\
b'\x39\x56\x39\x59\x39\x5c\x3b\x5e\x3f\x5e\x41\x5e\x46\x5a\x4e'\
b'\x53\x52\x4f\x53\x20\x52\x55\x3a\x54\x3a\x50\x3c\x4d\x40\x4b'\
b'\x43\x4a\x47\x4a\x4b\x4a\x4d\x4c\x51\x4f\x51\x51\x51\x54\x50'\
b'\x56\x4e\x58\x4b\x5b\x44\x5b\x40\x5b\x3e\x58\x3a\x55\x3a\x35'\
b'\x45\x5f\x57\x52\x53\x46\x52\x46\x50\x46\x4e\x4d\x4e\x4f\x4e'\
b'\x50\x4e\x50\x4e\x51\x4f\x51\x51\x51\x50\x52\x47\x52\x47\x51'\
b'\x48\x51\x49\x51\x4a\x51\x4a\x50\x4a\x4f\x4b\x4d\x4f\x3e\x50'\
b'\x3d\x50\x3c\x50\x3b\x4f\x3a\x4d\x3a\x4d\x39\x55\x39\x5a\x39'\
b'\x5d\x3c\x5d\x3f\x5d\x41\x59\x45\x56\x46\x59\x4d\x5a\x50\x5b'\
b'\x51\x5d\x51\x5d\x52\x57\x52\x20\x52\x51\x45\x52\x45\x53\x45'\
b'\x56\x45\x59\x41\x59\x3f\x59\x3d\x57\x3b\x55\x3b\x54\x3b\x54'\
b'\x3b\x51\x45\x3d\x46\x5e\x48\x53\x4a\x49\x4b\x49\x4b\x4b\x4b'\
b'\x4c\x4b\x4e\x4e\x51\x50\x51\x53\x51\x55\x4e\x55\x4c\x55\x4b'\
b'\x55\x4a\x54\x49\x50\x45\x4e\x43\x4e\x42\x4d\x41\x4d\x3f\x4d'\
b'\x3d\x51\x39\x54\x39\x55\x39\x56\x39\x56\x39\x58\x3a\x59\x3a'\
b'\x59\x3a\x59\x3a\x59\x3a\x5a\x3a\x5b\x3a\x5b\x39\x5c\x39\x5a'\
b'\x41\x59\x41\x5a\x40\x5a\x3f\x5a\x3d\x57\x3a\x54\x3a\x52\x3a'\
b'\x50\x3c\x50\x3e\x50\x3f\x51\x41\x57\x47\x59\x4a\x59\x4b\x59'\
b'\x4d\x57\x51\x53\x53\x51\x53\x50\x53\x4e\x52\x4c\x51\x4b\x51'\
b'\x4a\x51\x49\x51\x49\x53\x48\x53\x23\x45\x5f\x4a\x39\x5d\x39'\
b'\x5b\x40\x5a\x40\x5a\x3f\x5a\x3d\x5a\x3c\x5a\x3b\x59\x3b\x56'\
b'\x3b\x54\x3b\x50\x4c\x4f\x4f\x4f\x50\x4f\x50\x50\x51\x51\x51'\
b'\x52\x51\x52\x52\x47\x52\x47\x51\x48\x51\x49\x51\x4a\x51\x4b'\
b'\x51\x4b\x4f\x4c\x4c\x51\x3b\x50\x3b\x4e\x3b\x4b\x3c\x4a\x3e'\
b'\x49\x40\x48\x40\x4a\x39\x34\x43\x61\x46\x39\x50\x39\x50\x3a'\
b'\x4e\x3a\x4d\x3b\x4c\x3c\x4c\x3e\x49\x47\x48\x49\x48\x4a\x48'\
b'\x4b\x48\x4c\x48\x4e\x4b\x51\x4e\x51\x50\x51\x53\x50\x55\x4d'\
b'\x56\x49\x57\x47\x59\x3f\x5a\x3c\x5a\x3c\x5a\x3b\x59\x3a\x57'\
b'\x3a\x57\x39\x5f\x39\x5f\x3a\x5e\x3a\x5c\x3b\x5b\x3c\x5b\x3e'\
b'\x58\x47\x57\x4b\x55\x50\x50\x53\x4d\x53\x49\x53\x45\x4e\x45'\
b'\x4c\x45\x4b\x45\x49\x45\x49\x46\x47\x48\x3e\x49\x3c\x49\x3c'\
b'\x49\x3b\x48\x3a\x46\x3a\x46\x39\x23\x45\x5f\x48\x53\x4a\x3e'\
b'\x4a\x3d\x4a\x3c\x4a\x3b\x49\x3a\x48\x3a\x47\x3a\x47\x39\x51'\
b'\x39\x51\x3a\x4f\x3a\x4e\x3b\x4d\x3b\x4d\x3c\x4d\x3e\x4c\x4c'\
b'\x55\x3f\x57\x3d\x57\x3c\x57\x3c\x57\x3b\x57\x3b\x57\x3a\x55'\
b'\x3a\x56\x39\x5d\x39\x5d\x3a\x5c\x3a\x5c\x3a\x5b\x3b\x59\x3d'\
b'\x56\x40\x49\x53\x48\x53\x33\x41\x63\x43\x53\x45\x3e\x45\x3d'\
b'\x45\x3c\x45\x3b\x44\x3a\x43\x3a\x43\x39\x4c\x39\x4c\x3a\x4a'\
b'\x3a\x49\x3b\x48\x3e\x47\x4b\x50\x3d\x50\x3d\x50\x3c\x50\x3b'\
b'\x4f\x3a\x4d\x3a\x4d\x39\x57\x39\x57\x3a\x55\x3a\x55\x3a\x54'\
b'\x3b\x54\x3b\x54\x3d\x54\x3d\x53\x45\x52\x4b\x5a\x40\x5b\x3e'\
b'\x5c\x3c\x5c\x3b\x5c\x3b\x5b\x3a\x5a\x3a\x5a\x39\x61\x39\x61'\
b'\x3a\x60\x3a\x5f\x3b\x5e\x3c\x5d\x3d\x5b\x40\x4f\x53\x4e\x53'\
b'\x50\x40\x44\x53\x43\x53\x41\x41\x63\x59\x39\x61\x39\x61\x3a'\
b'\x5f\x3a\x5c\x3c\x5a\x3e\x54\x45\x56\x4b\x56\x4c\x56\x4e\x57'\
b'\x50\x58\x51\x59\x51\x5a\x51\x5a\x52\x51\x52\x51\x51\x52\x51'\
b'\x53\x51\x53\x50\x53\x50\x53\x4f\x53\x4e\x51\x47\x4b\x4d\x4a'\
b'\x4f\x49\x4f\x49\x50\x49\x50\x49\x51\x4a\x51\x4a\x51\x4b\x51'\
b'\x4b\x52\x43\x52\x43\x51\x45\x51\x46\x51\x47\x50\x4a\x4d\x51'\
b'\x46\x4f\x3f\x4e\x3c\x4d\x3a\x4b\x3a\x4b\x39\x54\x39\x54\x3a'\
b'\x53\x3a\x52\x3a\x51\x3b\x51\x3b\x51\x3c\x52\x3d\x53\x44\x57'\
b'\x40\x59\x3d\x5a\x3c\x5b\x3b\x5b\x3b\x5b\x3b\x5a\x3a\x5a\x3a'\
b'\x58\x3a\x59\x39\x32\x45\x5f\x51\x45\x56\x3e\x57\x3c\x57\x3b'\
b'\x57\x3b\x57\x3a\x55\x3a\x55\x39\x5d\x39\x5d\x3a\x5b\x3a\x5b'\
b'\x3a\x5a\x3b\x5a\x3b\x59\x3c\x57\x3e\x51\x47\x4f\x4d\x4f\x4f'\
b'\x4f\x50\x4f\x50\x4f\x51\x50\x51\x50\x51\x52\x51\x52\x52\x47'\
b'\x52\x47\x51\x49\x51\x4a\x51\x4a\x51\x4b\x50\x4b\x4f\x4c\x4d'\
b'\x4e\x46\x4c\x3e\x4b\x3b\x4a\x3a\x48\x3a\x48\x39\x51\x39\x51'\
b'\x3a\x50\x3a\x4f\x3a\x4f\x3a\x4e\x3b\x4e\x3c\x4e\x3c\x4f\x3e'\
b'\x51\x45\x15\x45\x5f\x4c\x39\x5d\x39\x5d\x3a\x4b\x51\x4e\x51'\
b'\x53\x51\x56\x50\x59\x4e\x5a\x4c\x5a\x4c\x58\x52\x47\x52\x47'\
b'\x51\x59\x3b\x54\x3b\x50\x3b\x4e\x3b\x4c\x3d\x4b\x3f\x4a\x3f'\
b'\x4c\x39\x09\x47\x5d\x49\x59\x53\x39\x5b\x39\x5a\x3a\x55\x3a'\
b'\x4c\x58\x51\x58\x51\x59\x49\x59\x05\x4e\x56\x51\x38\x54\x53'\
b'\x53\x53\x50\x38\x51\x38\x09\x47\x5d\x5b\x39\x51\x59\x49\x59'\
b'\x4a\x58\x4f\x58\x58\x3a\x53\x3a\x53\x39\x5b\x39\x08\x48\x5c'\
b'\x52\x39\x5a\x46\x58\x46\x52\x3b\x4c\x46\x4a\x46\x52\x39\x52'\
b'\x39\x05\x46\x5e\x5c\x5a\x48\x5a\x48\x58\x5c\x58\x5c\x5a\x05'\
b'\x4d\x57\x53\x39\x55\x3f\x54\x3f\x4f\x39\x53\x39\x39\x48\x5c'\
b'\x5a\x42\x57\x4e\x56\x50\x56\x50\x56\x50\x56\x50\x56\x50\x57'\
b'\x51\x57\x51\x57\x51\x57\x50\x58\x50\x59\x4e\x5a\x4f\x59\x50'\
b'\x56\x52\x55\x52\x54\x52\x53\x52\x53\x51\x53\x50\x54\x4f\x54'\
b'\x4d\x52\x50\x50\x52\x4e\x52\x4d\x52\x4c\x52\x4a\x50\x4a\x4e'\
b'\x4a\x4b\x4d\x45\x50\x43\x52\x42\x54\x42\x55\x42\x56\x43\x57'\
b'\x44\x57\x42\x5a\x42\x20\x52\x54\x43\x53\x43\x51\x44\x50\x45'\
b'\x4d\x4b\x4d\x4e\x4d\x4f\x4e\x50\x4f\x50\x51\x50\x53\x4d\x56'\
b'\x4a\x56\x45\x56\x44\x55\x43\x54\x43\x28\x48\x5c\x54\x38\x50'\
b'\x45\x52\x43\x54\x42\x56\x42\x58\x42\x5a\x44\x5a\x47\x5a\x49'\
b'\x57\x4f\x52\x52\x4f\x52\x4d\x52\x4a\x50\x4f\x3d\x50\x3b\x50'\
b'\x3b\x50\x3a\x50\x3a\x4f\x3a\x4e\x3a\x4e\x3a\x4d\x3a\x4d\x39'\
b'\x54\x38\x20\x52\x4c\x51\x4e\x52\x50\x52\x51\x52\x55\x4f\x57'\
b'\x4a\x57\x47\x57\x45\x56\x43\x54\x43\x53\x43\x50\x46\x4f\x48'\
b'\x4c\x51\x2a\x49\x5b\x58\x4e\x56\x50\x52\x52\x50\x52\x4d\x52'\
b'\x4b\x50\x4b\x4d\x4b\x4a\x4e\x45\x53\x42\x55\x42\x57\x42\x59'\
b'\x43\x59\x44\x59\x46\x59\x46\x58\x47\x57\x47\x57\x47\x56\x46'\
b'\x56\x46\x56\x45\x56\x45\x57\x44\x57\x44\x57\x43\x57\x43\x57'\
b'\x43\x57\x42\x56\x42\x54\x42\x50\x45\x4f\x47\x4e\x4a\x4e\x4d'\
b'\x4e\x4f\x50\x51\x52\x51\x53\x51\x56\x4f\x57\x4e\x58\x4e\x3f'\
b'\x46\x5e\x5c\x38\x55\x4e\x55\x4f\x55\x50\x55\x50\x55\x50\x55'\
b'\x50\x56\x50\x56\x50\x57\x50\x58\x4e\x59\x4e\x57\x50\x55\x52'\
b'\x54\x52\x53\x52\x52\x52\x52\x51\x52\x50\x53\x4e\x53\x4c\x51'\
b'\x50\x4f\x51\x4d\x52\x4c\x52\x4a\x52\x48\x50\x48\x4e\x48\x4b'\
b'\x4c\x45\x4f\x43\x51\x42\x53\x42\x54\x42\x55\x42\x56\x43\x58'\
b'\x3d\x58\x3c\x58\x3c\x58\x3b\x58\x3b\x58\x3a\x58\x3a\x57\x3a'\
b'\x57\x3a\x56\x3a\x55\x3a\x55\x39\x5c\x38\x20\x52\x55\x45\x55'\
b'\x44\x54\x43\x53\x43\x50\x43\x4b\x4a\x4b\x4e\x4b\x4f\x4d\x50'\
b'\x4d\x50\x4f\x50\x55\x48\x55\x45\x29\x49\x5b\x4e\x4b\x4e\x4c'\
b'\x4e\x4d\x4e\x4e\x50\x51\x52\x51\x53\x51\x55\x4f\x58\x4e\x58'\
b'\x4e\x54\x52\x50\x52\x4d\x52\x4b\x4f\x4b\x4d\x4b\x4a\x4e\x45'\
b'\x53\x42\x56\x42\x58\x42\x59\x43\x59\x44\x59\x46\x58\x47\x57'\
b'\x49\x54\x4a\x52\x4b\x4e\x4b\x20\x52\x4e\x4a\x51\x4a\x52\x49'\
b'\x55\x48\x57\x45\x57\x44\x57\x43\x56\x42\x55\x42\x53\x42\x4f'\
b'\x46\x4e\x4a\x45\x44\x60\x57\x42\x57\x43\x55\x43\x53\x4b\x51'\
b'\x50\x50\x53\x4e\x57\x4c\x59\x4a\x5a\x48\x5a\x47\x5a\x47\x59'\
b'\x46\x59\x46\x58\x46\x58\x47\x57\x48\x57\x48\x57\x49\x57\x49'\
b'\x58\x49\x58\x48\x59\x48\x59\x48\x59\x48\x59\x48\x59\x48\x59'\
b'\x49\x59\x4a\x59\x4b\x58\x4d\x56\x4d\x55\x4d\x54\x4f\x4f\x52'\
b'\x43\x4f\x43\x4f\x42\x50\x42\x51\x42\x52\x40\x53\x3f\x54\x3d'\
b'\x55\x3b\x57\x3a\x5a\x38\x5b\x38\x5c\x38\x5e\x3a\x5e\x3a\x5e'\
b'\x3b\x5d\x3c\x5d\x3c\x5c\x3c\x5b\x3b\x5b\x3b\x5b\x3b\x5c\x3a'\
b'\x5c\x3a\x5c\x39\x5c\x39\x5b\x39\x5b\x39\x5a\x39\x59\x3a\x58'\
b'\x3b\x57\x3d\x56\x3e\x55\x42\x57\x42\x52\x46\x5e\x5c\x43\x5c'\
b'\x45\x59\x45\x59\x46\x59\x46\x59\x49\x57\x4b\x55\x4d\x51\x4d'\
b'\x4f\x4d\x4e\x4e\x4e\x4e\x4e\x4f\x4e\x4f\x4f\x50\x50\x50\x54'\
b'\x51\x56\x52\x57\x52\x58\x53\x58\x55\x58\x56\x56\x59\x52\x5a'\
b'\x4f\x5a\x4d\x5a\x49\x59\x48\x57\x48\x56\x48\x55\x49\x54\x4a'\
b'\x53\x4a\x53\x4c\x52\x4c\x51\x4c\x50\x4c\x4f\x4d\x4e\x4f\x4d'\
b'\x4d\x4c\x4b\x4a\x4b\x48\x4b\x46\x50\x42\x53\x42\x55\x42\x56'\
b'\x42\x57\x43\x5c\x43\x20\x52\x56\x46\x56\x44\x54\x42\x53\x42'\
b'\x51\x42\x4e\x47\x4e\x49\x4e\x4a\x50\x4c\x51\x4c\x52\x4c\x54'\
b'\x4b\x55\x49\x56\x46\x56\x46\x20\x52\x4d\x52\x4c\x53\x4a\x55'\
b'\x4a\x56\x4a\x57\x4b\x58\x4d\x59\x50\x59\x52\x59\x56\x57\x56'\
b'\x56\x56\x55\x55\x54\x53\x53\x52\x53\x4d\x52\x38\x48\x5c\x54'\
b'\x38\x4f\x4a\x52\x45\x56\x42\x58\x42\x58\x42\x5a\x43\x5a\x44'\
b'\x5a\x45\x59\x47\x57\x4e\x56\x50\x56\x50\x56\x50\x57\x50\x57'\
b'\x50\x57\x50\x58\x50\x59\x4f\x5a\x4e\x5a\x4e\x5a\x4f\x57\x52'\
b'\x56\x52\x55\x52\x54\x52\x54\x52\x54\x51\x54\x50\x54\x4e\x56'\
b'\x47\x57\x45\x57\x45\x57\x44\x56\x44\x56\x44\x55\x44\x55\x44'\
b'\x53\x45\x52\x47\x51\x48\x4f\x4c\x4e\x4d\x4e\x4e\x4d\x52\x4a'\
b'\x52\x50\x3d\x50\x3b\x50\x3b\x50\x3a\x4f\x3a\x4f\x3a\x4e\x3a'\
b'\x4e\x3a\x4e\x39\x54\x38\x2d\x4c\x58\x54\x3a\x55\x3a\x56\x3b'\
b'\x56\x3c\x56\x3d\x55\x3e\x54\x3e\x54\x3e\x53\x3d\x53\x3c\x53'\
b'\x3b\x54\x3a\x54\x3a\x20\x52\x55\x42\x51\x4e\x51\x50\x51\x50'\
b'\x51\x50\x51\x50\x51\x50\x52\x50\x52\x50\x53\x4f\x54\x4e\x55'\
b'\x4e\x53\x50\x52\x51\x51\x52\x4f\x52\x4f\x52\x4e\x52\x4e\x51'\
b'\x4e\x50\x4e\x4f\x51\x47\x51\x45\x51\x44\x51\x44\x51\x43\x50'\
b'\x43\x50\x43\x4e\x43\x4e\x43\x55\x42\x34\x48\x5c\x59\x3a\x59'\
b'\x3a\x5a\x3b\x5a\x3c\x5a\x3d\x59\x3e\x59\x3e\x58\x3e\x57\x3d'\
b'\x57\x3c\x57\x3b\x58\x3a\x59\x3a\x20\x52\x59\x42\x54\x52\x53'\
b'\x56\x4e\x5a\x4c\x5a\x4b\x5a\x4a\x59\x4a\x58\x4a\x58\x4b\x57'\
b'\x4b\x57\x4c\x57\x4c\x57\x4c\x57\x4c\x58\x4c\x58\x4c\x59\x4c'\
b'\x59\x4c\x59\x4c\x59\x4c\x59\x4c\x59\x4c\x59\x4e\x59\x50\x57'\
b'\x51\x55\x55\x47\x55\x45\x55\x44\x55\x44\x54\x43\x54\x43\x54'\
b'\x43\x53\x43\x53\x43\x53\x43\x53\x43\x59\x42\x35\x47\x5d\x53'\
b'\x38\x4e\x4a\x50\x48\x54\x45\x55\x44\x55\x44\x55\x43\x55\x43'\
b'\x55\x43\x54\x43\x53\x43\x53\x43\x53\x42\x5b\x42\x5b\x43\x59'\
b'\x43\x57\x43\x56\x44\x55\x46\x54\x46\x52\x47\x53\x49\x53\x4b'\
b'\x54\x4f\x55\x50\x55\x50\x55\x50\x56\x50\x56\x50\x57\x4f\x58'\
b'\x4e\x59\x4e\x57\x51\x55\x52\x54\x52\x53\x52\x53\x52\x52\x51'\
b'\x50\x49\x4e\x4c\x4c\x52\x49\x52\x4f\x3d\x50\x3c\x50\x3b\x50'\
b'\x3b\x50\x3a\x4f\x3a\x4e\x3a\x4e\x3a\x4d\x3a\x4d\x39\x53\x38'\
b'\x1f\x4b\x59\x57\x38\x51\x4e\x50\x4f\x50\x50\x50\x50\x50\x50'\
b'\x51\x50\x51\x50\x51\x50\x52\x4f\x53\x4e\x54\x4e\x52\x51\x51'\
b'\x52\x50\x52\x4f\x52\x4e\x52\x4d\x51\x4d\x51\x4d\x50\x4e\x4e'\
b'\x53\x3d\x53\x3b\x53\x3b\x53\x3a\x53\x3a\x52\x3a\x51\x3a\x51'\
b'\x3a\x51\x39\x57\x38\x55\x44\x60\x4d\x42\x4b\x4a\x4c\x47\x4d'\
b'\x45\x4f\x43\x51\x42\x52\x42\x53\x42\x54\x42\x55\x43\x55\x44'\
b'\x55\x45\x55\x46\x53\x4b\x56\x45\x59\x43\x5a\x42\x5c\x42\x5d'\
b'\x42\x5e\x43\x5e\x44\x5e\x45\x5d\x46\x5b\x4d\x5b\x50\x5b\x50'\
b'\x5b\x50\x5b\x50\x5b\x50\x5b\x50\x5b\x50\x5c\x50\x5d\x4f\x5e'\
b'\x4e\x5e\x4e\x5e\x4f\x5c\x52\x5a\x52\x59\x52\x59\x52\x58\x52'\
b'\x58\x51\x58\x50\x58\x4d\x5a\x48\x5b\x46\x5b\x45\x5b\x45\x5b'\
b'\x45\x5b\x44\x5b\x44\x5a\x44\x5a\x44\x59\x44\x58\x45\x56\x47'\
b'\x54\x4b\x52\x4e\x51\x52\x4e\x52\x51\x47\x52\x45\x52\x45\x52'\
b'\x44\x52\x44\x51\x44\x51\x44\x50\x44\x4f\x45\x4b\x49\x4b\x4c'\
b'\x4a\x4d\x48\x52\x46\x52\x49\x46\x4a\x45\x4a\x44\x4a\x44\x4a'\
b'\x44\x49\x43\x48\x43\x48\x43\x47\x43\x47\x43\x4d\x42\x38\x48'\
b'\x5c\x51\x42\x4f\x4a\x52\x45\x56\x42\x58\x42\x58\x42\x5a\x43'\
b'\x5a\x44\x5a\x45\x59\x47\x57\x4e\x57\x50\x57\x50\x57\x50\x57'\
b'\x50\x57\x50\x57\x50\x58\x50\x58\x4f\x5a\x4e\x5a\x4e\x58\x51'\
b'\x57\x52\x56\x52\x55\x52\x54\x52\x54\x52\x54\x51\x54\x50\x54'\
b'\x4e\x56\x47\x57\x45\x57\x45\x57\x44\x56\x44\x56\x44\x55\x44'\
b'\x55\x44\x53\x45\x50\x49\x4f\x4c\x4e\x4d\x4d\x4f\x4d\x52\x4a'\
b'\x52\x4d\x47\x4e\x45\x4e\x44\x4e\x44\x4d\x43\x4d\x43\x4c\x43'\
b'\x4c\x43\x4b\x43\x4b\x43\x51\x42\x1d\x48\x5c\x5a\x47\x5a\x4a'\
b'\x57\x4f\x52\x52\x50\x52\x4d\x52\x4a\x4f\x4a\x4d\x4a\x4a\x4d'\
b'\x45\x52\x42\x55\x42\x57\x42\x5a\x45\x5a\x47\x20\x52\x57\x46'\
b'\x57\x44\x55\x43\x54\x43\x51\x43\x4d\x4a\x4d\x4e\x4d\x50\x4f'\
b'\x52\x50\x52\x53\x52\x57\x4a\x57\x46\x36\x45\x5f\x53\x42\x52'\
b'\x46\x54\x43\x57\x42\x59\x42\x5b\x42\x5d\x44\x5d\x46\x5d\x4a'\
b'\x56\x52\x52\x52\x51\x52\x50\x52\x4f\x52\x4e\x56\x4d\x58\x4d'\
b'\x58\x4d\x58\x4e\x59\x4e\x59\x50\x59\x50\x5a\x47\x5a\x47\x59'\
b'\x49\x59\x4a\x58\x4b\x56\x4f\x46\x50\x44\x50\x44\x50\x44\x4f'\
b'\x43\x4f\x43\x4e\x43\x4d\x43\x4d\x43\x53\x42\x20\x52\x4f\x50'\
b'\x50\x51\x52\x51\x53\x51\x55\x50\x57\x4e\x59\x4c\x5a\x48\x5a'\
b'\x46\x5a\x45\x58\x43\x58\x43\x56\x43\x52\x48\x51\x4b\x4f\x50'\
b'\x33\x48\x5c\x5a\x42\x54\x56\x54\x57\x54\x58\x54\x58\x54\x59'\
b'\x55\x59\x55\x59\x56\x59\x56\x5a\x4d\x5a\x4e\x59\x4f\x59\x50'\
b'\x59\x51\x59\x51\x57\x52\x55\x54\x4d\x52\x50\x50\x51\x4f\x52'\
b'\x4d\x52\x4b\x52\x4a\x4f\x4a\x4e\x4a\x4b\x4d\x45\x50\x43\x52'\
b'\x42\x54\x42\x55\x42\x57\x43\x57\x44\x58\x42\x5a\x42\x20\x52'\
b'\x56\x45\x56\x44\x55\x42\x54\x42\x52\x42\x4d\x4a\x4d\x4d\x4d'\
b'\x4f\x4e\x50\x4f\x50\x50\x50\x51\x4f\x53\x4d\x56\x47\x56\x45'\
b'\x2b\x49\x5b\x4c\x43\x52\x42\x50\x4a\x53\x45\x55\x43\x57\x42'\
b'\x58\x42\x58\x42\x59\x42\x59\x43\x59\x44\x59\x45\x58\x46\x57'\
b'\x46\x57\x46\x56\x46\x56\x45\x56\x45\x56\x45\x56\x44\x56\x44'\
b'\x55\x44\x55\x45\x55\x45\x54\x46\x52\x48\x50\x4b\x50\x4c\x4f'\
b'\x4d\x4e\x4f\x4e\x50\x4e\x52\x4b\x52\x4e\x47\x4f\x45\x4f\x44'\
b'\x4f\x44\x4f\x43\x4e\x43\x4e\x43\x4d\x43\x4c\x43\x4c\x43\x32'\
b'\x49\x5b\x59\x42\x58\x47\x57\x47\x57\x45\x55\x43\x54\x43\x53'\
b'\x43\x51\x44\x51\x45\x51\x45\x52\x46\x53\x47\x55\x4a\x56\x4c'\
b'\x56\x4e\x56\x50\x53\x52\x51\x52\x50\x52\x4e\x52\x4d\x52\x4d'\
b'\x52\x4c\x52\x4c\x52\x4b\x52\x4c\x4d\x4d\x4d\x4d\x4f\x4f\x52'\
b'\x51\x52\x52\x52\x54\x50\x54\x4f\x54\x4e\x54\x4e\x53\x4d\x50'\
b'\x49\x4f\x47\x4f\x46\x4f\x44\x51\x42\x53\x42\x54\x42\x54\x42'\
b'\x55\x42\x57\x42\x57\x42\x58\x42\x58\x42\x59\x42\x20\x4b\x59'\
b'\x55\x3d\x54\x42\x57\x42\x56\x43\x54\x43\x51\x4e\x50\x50\x50'\
b'\x50\x50\x50\x50\x51\x51\x51\x51\x51\x52\x50\x52\x50\x54\x4e'\
b'\x54\x4e\x53\x51\x51\x52\x50\x52\x4f\x52\x4e\x52\x4d\x51\x4d'\
b'\x51\x4d\x50\x4e\x4e\x51\x43\x4e\x43\x4e\x42\x50\x42\x53\x40'\
b'\x55\x3d\x55\x3d\x3e\x48\x5c\x5a\x42\x57\x4d\x56\x4f\x56\x50'\
b'\x56\x50\x57\x51\x57\x51\x57\x51\x58\x50\x59\x4e\x5a\x4e\x58'\
b'\x51\x57\x52\x56\x52\x55\x52\x54\x52\x54\x52\x54\x51\x54\x50'\
b'\x54\x4f\x54\x4e\x55\x4a\x52\x4f\x4e\x52\x4c\x52\x4c\x52\x4a'\
b'\x51\x4a\x50\x4a\x4f\x4b\x4c\x4d\x47\x4d\x45\x4d\x44\x4d\x44'\
b'\x4d\x44\x4d\x44\x4c\x44\x4c\x44\x4a\x46\x4a\x45\x4b\x43\x4d'\
b'\x42\x4e\x42\x4f\x42\x4f\x42\x50\x42\x50\x43\x50\x44\x50\x47'\
b'\x4e\x4c\x4d\x4f\x4d\x4f\x4d\x50\x4e\x50\x4e\x50\x4f\x50\x51'\
b'\x4f\x54\x4b\x56\x47\x57\x43\x57\x42\x5a\x42\x28\x48\x5c\x4a'\
b'\x43\x4f\x42\x50\x43\x50\x44\x51\x46\x51\x49\x51\x4b\x52\x4f'\
b'\x54\x4d\x54\x4c\x57\x49\x57\x48\x58\x47\x58\x47\x58\x46\x58'\
b'\x46\x58\x45\x56\x44\x56\x43\x56\x42\x57\x42\x58\x42\x59\x42'\
b'\x5a\x43\x5a\x44\x5a\x45\x5a\x46\x59\x47\x56\x4b\x54\x4e\x53'\
b'\x4f\x50\x52\x4f\x52\x4e\x47\x4d\x44\x4d\x43\x4c\x43\x4b\x43'\
b'\x4a\x43\x4a\x43\x2d\x44\x60\x55\x42\x56\x4f\x59\x4b\x5b\x48'\
b'\x5c\x46\x5c\x45\x5c\x45\x5c\x45\x5c\x45\x5b\x44\x5b\x43\x5b'\
b'\x43\x5b\x42\x5c\x42\x5c\x42\x5d\x42\x5e\x43\x5e\x44\x5e\x45'\
b'\x5e\x45\x5d\x47\x5c\x49\x5a\x4c\x56\x51\x55\x52\x54\x52\x53'\
b'\x46\x4b\x52\x4a\x52\x4a\x4b\x4a\x46\x49\x44\x49\x44\x48\x43'\
b'\x47\x43\x47\x43\x46\x43\x46\x43\x4b\x42\x4c\x45\x4d\x4b\x4d'\
b'\x4d\x4d\x4e\x54\x42\x55\x42\x48\x47\x5d\x51\x42\x52\x43\x52'\
b'\x43\x53\x44\x53\x47\x55\x45\x56\x44\x57\x42\x58\x42\x59\x42'\
b'\x59\x42\x5a\x42\x5b\x42\x5b\x43\x5b\x44\x5b\x44\x5a\x44\x59'\
b'\x44\x59\x44\x59\x44\x58\x44\x57\x44\x57\x44\x56\x44\x55\x45'\
b'\x54\x48\x55\x4e\x56\x50\x56\x50\x56\x50\x57\x50\x57\x50\x58'\
b'\x4f\x59\x4e\x59\x4e\x58\x50\x57\x52\x56\x52\x55\x52\x54\x52'\
b'\x53\x51\x53\x51\x52\x4b\x4f\x50\x4d\x52\x4c\x52\x4b\x52\x4a'\
b'\x52\x4a\x52\x49\x52\x49\x51\x49\x50\x4a\x4f\x4b\x4f\x4b\x4f'\
b'\x4c\x50\x4c\x50\x4d\x50\x4d\x50\x4d\x50\x4e\x4f\x51\x4b\x51'\
b'\x4a\x50\x45\x50\x45\x50\x44\x4e\x43\x4d\x43\x4d\x43\x4c\x43'\
b'\x4c\x42\x51\x42\x3a\x46\x5e\x51\x42\x52\x43\x52\x44\x53\x47'\
b'\x53\x50\x54\x4f\x57\x4c\x58\x4b\x59\x48\x5a\x47\x5a\x46\x5a'\
b'\x46\x5a\x46\x5a\x45\x5a\x45\x59\x45\x58\x44\x58\x43\x58\x42'\
b'\x59\x42\x5a\x42\x5b\x42\x5c\x43\x5c\x44\x5c\x46\x5a\x49\x54'\
b'\x51\x50\x55\x4d\x58\x4b\x5a\x4a\x5a\x49\x5a\x48\x59\x48\x59'\
b'\x48\x58\x4a\x57\x4a\x57\x4b\x57\x4b\x57\x4b\x57\x4b\x58\x4b'\
b'\x58\x4c\x58\x4c\x58\x4c\x58\x4c\x58\x4d\x57\x4e\x56\x50\x54'\
b'\x51\x53\x50\x48\x50\x45\x4f\x43\x4d\x43\x4d\x43\x4c\x44\x4c'\
b'\x43\x51\x42\x16\x48\x5c\x4e\x42\x5a\x42\x5a\x42\x4d\x50\x53'\
b'\x50\x54\x50\x56\x4f\x56\x4e\x57\x4d\x58\x4d\x56\x52\x4a\x52'\
b'\x4a\x51\x57\x44\x51\x44\x50\x44\x4f\x45\x4f\x45\x4e\x46\x4d'\
b'\x47\x4d\x47\x4e\x42\x26\x48\x5c\x50\x59\x50\x5a\x4d\x5a\x4b'\
b'\x57\x4b\x55\x4b\x53\x4e\x4e\x4e\x4d\x4e\x4b\x4c\x4a\x4a\x49'\
b'\x4b\x49\x4d\x48\x4f\x47\x50\x45\x50\x44\x50\x3f\x52\x3c\x57'\
b'\x39\x5a\x38\x59\x39\x57\x39\x55\x3b\x54\x3d\x54\x3e\x54\x42'\
b'\x52\x45\x4f\x48\x4c\x49\x4e\x4a\x50\x4c\x50\x4e\x50\x50\x4d'\
b'\x55\x4d\x56\x4d\x57\x4e\x59\x50\x59\x05\x4f\x55\x53\x38\x53'\
b'\x5a\x51\x5a\x51\x38\x53\x38\x27\x48\x5c\x54\x39\x54\x38\x57'\
b'\x39\x59\x3b\x59\x3e\x59\x3f\x56\x45\x56\x46\x56\x47\x58\x49'\
b'\x5a\x49\x59\x49\x57\x4a\x55\x4c\x54\x4d\x54\x4e\x54\x53\x52'\
b'\x57\x4d\x5a\x4a\x5a\x4b\x59\x4d\x59\x4f\x57\x50\x56\x50\x55'\
b'\x50\x50\x51\x4f\x52\x4d\x55\x4a\x58\x49\x56\x48\x54\x46\x54'\
b'\x44\x54\x43\x57\x3d\x57\x3c\x57\x3b\x56\x39\x54\x39\x19\x46'\
b'\x5e\x5b\x46\x5c\x46\x5c\x48\x59\x4b\x57\x4b\x56\x4b\x54\x4a'\
b'\x50\x49\x4e\x47\x4c\x47\x4b\x47\x49\x49\x49\x4b\x48\x4b\x48'\
b'\x48\x4b\x46\x4d\x46\x4d\x46\x4e\x46\x50\x47\x56\x49\x57\x49'\
b'\x59\x49\x5b\x47\x5b\x46\x0b\x47\x5d\x49\x52\x49\x3b\x5b\x3b'\
b'\x5b\x52\x49\x52\x20\x52\x49\x51\x5b\x51\x5b\x3b\x49\x3b\x49'\
b'\x51'

_index =\
b'\x00\x00\x03\x00\x4e\x00\x97\x00\xe0\x00\x6d\x01\xfc\x01\x9b'\
b'\x02\xbe\x02\xe5\x02\x0c\x03\xb7\x03\xd4\x03\x03\x04\x10\x04'\
b'\x2d\x04\x3a\x04\x8d\x04\xca\x04\x0b\x05\x6e\x05\x93\x05\xde'\
b'\x05\x2d\x06\x48\x06\xb7\x06\x0c\x07\x45\x07\x92\x07\xa5\x07'\
b'\xbe\x07\xd1\x07\x38\x08\xeb\x08\x40\x09\xbd\x09\x12\x0a\x77'\
b'\x0a\xec\x0a\x51\x0b\xc4\x0b\x4d\x0c\x90\x0c\xe5\x0c\x68\x0d'\
b'\xbf\x0d\x28\x0e\x81\x0e\xd0\x0e\x2b\x0f\xa4\x0f\x11\x10\x8e'\
b'\x10\xd7\x10\x42\x11\x8b\x11\xf4\x11\x79\x12\xe0\x12\x0d\x13'\
b'\x22\x13\x2f\x13\x44\x13\x57\x13\x64\x13\x71\x13\xe6\x13\x39'\
b'\x14\x90\x14\x11\x15\x66\x15\xf3\x15\x9a\x16\x0d\x17\x6a\x17'\
b'\xd5\x17\x42\x18\x83\x18\x30\x19\xa3\x19\xe0\x19\x4f\x1a\xb8'\
b'\x1a\x11\x1b\x78\x1b\xbb\x1b\x3a\x1c\x8d\x1c\xea\x1c\x7d\x1d'\
b'\xf4\x1d\x23\x1e\x72\x1e\x7f\x1e\xd0\x1e\x05\x1f'

FONT = memoryview(_font)
INDEX = memoryview(_index)

