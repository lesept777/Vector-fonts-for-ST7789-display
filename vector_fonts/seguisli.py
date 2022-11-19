FIRST = 32
LAST = 127
WIDTH = 32
HEIGHT = 37

_font =\
b'\x01\x4e\x56\x13\x4c\x58\x53\x38\x56\x38\x52\x4b\x50\x4b\x53'\
b'\x38\x20\x52\x4e\x51\x4e\x50\x4f\x4f\x50\x4f\x50\x4f\x51\x50'\
b'\x51\x51\x51\x51\x50\x52\x50\x52\x4f\x52\x4e\x51\x4e\x51\x0b'\
b'\x4d\x57\x53\x38\x55\x38\x55\x40\x53\x40\x53\x38\x20\x52\x4f'\
b'\x38\x51\x38\x50\x40\x4f\x40\x4f\x38\x23\x46\x5e\x4d\x49\x48'\
b'\x49\x48\x47\x4d\x47\x4f\x41\x49\x41\x4a\x40\x4f\x40\x50\x38'\
b'\x52\x38\x51\x40\x55\x40\x57\x38\x59\x38\x57\x40\x5c\x40\x5c'\
b'\x41\x57\x41\x56\x47\x5b\x47\x5a\x49\x55\x49\x54\x50\x52\x50'\
b'\x53\x49\x4f\x49\x4d\x50\x4b\x50\x4d\x49\x20\x52\x54\x47\x55'\
b'\x41\x50\x41\x4f\x47\x54\x47\x33\x48\x5c\x4a\x4e\x4b\x4f\x4e'\
b'\x50\x4f\x50\x52\x46\x4f\x44\x4d\x41\x4d\x3f\x4d\x3c\x51\x38'\
b'\x54\x38\x55\x35\x57\x35\x56\x38\x58\x39\x5a\x39\x5a\x3c\x58'\
b'\x3a\x56\x3a\x53\x45\x56\x47\x58\x4a\x58\x4b\x58\x4e\x54\x52'\
b'\x51\x52\x50\x56\x4e\x56\x4f\x52\x4e\x52\x4a\x51\x4a\x51\x4a'\
b'\x4e\x20\x52\x54\x3a\x52\x3a\x4f\x3d\x4f\x3f\x4f\x40\x50\x42'\
b'\x52\x44\x54\x3a\x20\x52\x51\x50\x53\x50\x56\x4e\x56\x4c\x56'\
b'\x4a\x54\x48\x53\x47\x51\x50\x40\x43\x61\x58\x52\x55\x52\x53'\
b'\x50\x53\x4d\x53\x4b\x55\x47\x58\x45\x5a\x45\x5c\x45\x5f\x48'\
b'\x5f\x4a\x5f\x4e\x5b\x52\x58\x52\x20\x52\x5c\x38\x5e\x38\x49'\
b'\x52\x46\x52\x5c\x38\x20\x52\x4a\x45\x48\x45\x45\x42\x45\x40'\
b'\x45\x3e\x47\x3a\x4a\x38\x4c\x38\x4f\x38\x51\x3b\x51\x3d\x51'\
b'\x3f\x4f\x43\x4c\x45\x4a\x45\x20\x52\x58\x51\x5a\x51\x5d\x4d'\
b'\x5d\x4a\x5d\x49\x5b\x47\x5a\x47\x58\x47\x55\x4b\x55\x4d\x55'\
b'\x4f\x56\x51\x58\x51\x20\x52\x4a\x44\x4c\x44\x4f\x40\x4f\x3d'\
b'\x4f\x3c\x4e\x3a\x4c\x3a\x4a\x3a\x47\x3d\x47\x40\x47\x42\x49'\
b'\x44\x4a\x44\x37\x45\x5f\x57\x4f\x53\x52\x4e\x52\x4b\x52\x47'\
b'\x4f\x47\x4c\x47\x49\x4a\x46\x4e\x44\x4d\x42\x4c\x40\x4c\x3e'\
b'\x4c\x3c\x50\x38\x53\x38\x56\x38\x59\x3b\x59\x3d\x59\x40\x56'\
b'\x43\x52\x45\x57\x4c\x5a\x49\x5b\x44\x5d\x44\x5c\x4a\x58\x4e'\
b'\x5b\x52\x59\x52\x57\x4f\x20\x52\x57\x3d\x57\x3c\x55\x3a\x53'\
b'\x3a\x51\x3a\x4e\x3c\x4e\x3e\x4e\x3f\x4f\x42\x50\x43\x54\x42'\
b'\x57\x3f\x57\x3d\x20\x52\x55\x4e\x50\x45\x4c\x47\x49\x4a\x49'\
b'\x4c\x49\x4e\x4c\x51\x4e\x51\x52\x51\x55\x4e\x05\x4f\x55\x51'\
b'\x38\x53\x38\x53\x40\x51\x40\x51\x38\x0e\x4a\x5a\x4f\x57\x4c'\
b'\x52\x4c\x4c\x4c\x47\x51\x3d\x56\x38\x58\x38\x53\x3d\x4e\x47'\
b'\x4e\x4c\x4e\x4f\x50\x55\x51\x57\x4f\x57\x0d\x4a\x5a\x4c\x57'\
b'\x51\x52\x56\x49\x56\x43\x56\x3d\x53\x38\x55\x38\x58\x3e\x58'\
b'\x43\x58\x49\x53\x52\x4e\x57\x4c\x57\x10\x4a\x5a\x51\x3f\x4c'\
b'\x3e\x4c\x3c\x51\x3e\x51\x38\x53\x38\x53\x3e\x58\x3c\x58\x3e'\
b'\x53\x3f\x57\x44\x55\x45\x52\x40\x4f\x45\x4d\x44\x51\x3f\x0d'\
b'\x48\x5c\x4a\x46\x51\x46\x51\x3f\x53\x3f\x53\x46\x5a\x46\x5a'\
b'\x48\x53\x48\x53\x50\x51\x50\x51\x48\x4a\x48\x4a\x46\x05\x4d'\
b'\x57\x53\x4e\x55\x4e\x51\x57\x4f\x57\x53\x4e\x05\x4b\x59\x4d'\
b'\x47\x57\x47\x57\x49\x4d\x49\x4d\x47\x0d\x4e\x56\x52\x52\x51'\
b'\x52\x50\x51\x50\x51\x50\x50\x51\x4f\x52\x4f\x53\x4f\x54\x50'\
b'\x54\x51\x54\x51\x53\x52\x52\x52\x05\x46\x5e\x5a\x38\x5c\x38'\
b'\x4a\x56\x48\x56\x5a\x38\x20\x47\x5d\x5b\x40\x5b\x45\x58\x4d'\
b'\x53\x52\x50\x52\x4d\x52\x49\x4e\x49\x4a\x49\x45\x4c\x3d\x52'\
b'\x38\x55\x38\x58\x38\x5b\x3c\x5b\x40\x20\x52\x58\x40\x58\x3d'\
b'\x56\x3a\x54\x3a\x53\x3a\x4f\x3d\x4d\x41\x4c\x47\x4c\x4a\x4c'\
b'\x4d\x4e\x50\x50\x50\x52\x50\x56\x4c\x58\x44\x58\x40\x07\x4b'\
b'\x59\x54\x3b\x4d\x3d\x4e\x3b\x57\x38\x51\x52\x4f\x52\x54\x3b'\
b'\x21\x47\x5d\x59\x3e\x59\x3c\x57\x3a\x55\x3a\x52\x3a\x4e\x3c'\
b'\x4f\x3a\x52\x38\x55\x38\x58\x38\x5b\x3b\x5b\x3e\x5b\x40\x5a'\
b'\x43\x57\x46\x54\x48\x51\x4a\x4d\x4c\x4c\x4e\x4b\x50\x58\x50'\
b'\x58\x52\x49\x52\x49\x51\x49\x4f\x4a\x4d\x4c\x4b\x4f\x48\x52'\
b'\x47\x55\x45\x58\x42\x59\x40\x59\x3e\x29\x47\x5d\x4a\x4f\x4b'\
b'\x50\x4e\x50\x4f\x50\x53\x50\x56\x4d\x56\x4b\x56\x48\x53\x46'\
b'\x50\x46\x4e\x46\x4f\x44\x50\x44\x54\x44\x58\x41\x58\x3e\x58'\
b'\x3c\x56\x3a\x54\x3a\x51\x3a\x4f\x3b\x4f\x39\x52\x38\x54\x38'\
b'\x57\x38\x5b\x3b\x5b\x3e\x5b\x40\x57\x44\x54\x45\x54\x45\x56'\
b'\x45\x59\x48\x59\x4b\x59\x4e\x54\x52\x4f\x52\x4e\x52\x4a\x52'\
b'\x49\x51\x4a\x4f\x14\x47\x5d\x59\x38\x5b\x38\x57\x4a\x5b\x4a'\
b'\x5b\x4c\x57\x4c\x56\x52\x53\x52\x55\x4c\x49\x4c\x49\x4a\x4d'\
b'\x46\x56\x3c\x59\x38\x20\x52\x55\x4a\x58\x3c\x53\x43\x4c\x4a'\
b'\x55\x4a\x1c\x47\x5d\x4a\x4f\x4b\x50\x4d\x50\x4f\x50\x51\x50'\
b'\x54\x4f\x56\x4c\x56\x4a\x56\x45\x50\x45\x4e\x45\x4c\x45\x50'\
b'\x38\x5b\x38\x5a\x3b\x51\x3b\x4f\x43\x51\x43\x55\x43\x58\x46'\
b'\x58\x49\x58\x4c\x56\x50\x52\x52\x4f\x52\x4b\x52\x49\x52\x4a'\
b'\x4f\x2c\x47\x5d\x4c\x46\x4d\x44\x50\x42\x52\x42\x55\x42\x59'\
b'\x46\x59\x49\x59\x4c\x57\x50\x53\x52\x50\x52\x4d\x52\x49\x4e'\
b'\x49\x49\x49\x45\x4d\x3d\x53\x38\x57\x38\x59\x38\x5b\x39\x5a'\
b'\x3b\x58\x3a\x56\x3a\x54\x3a\x4f\x3d\x4c\x43\x4c\x46\x4c\x46'\
b'\x20\x52\x50\x50\x52\x50\x55\x4f\x56\x4b\x56\x49\x56\x47\x54'\
b'\x44\x52\x44\x50\x44\x4d\x46\x4c\x49\x4c\x4a\x4c\x4d\x4e\x50'\
b'\x50\x50\x0d\x47\x5d\x49\x52\x4b\x4d\x52\x42\x57\x3b\x4a\x3b'\
b'\x4b\x38\x5b\x38\x5b\x3a\x56\x40\x51\x48\x4d\x4f\x4c\x52\x49'\
b'\x52\x3a\x47\x5d\x50\x44\x4e\x43\x4d\x41\x4d\x3f\x4d\x3d\x4f'\
b'\x3a\x52\x38\x55\x38\x57\x38\x5b\x3b\x5b\x3e\x5b\x40\x58\x43'\
b'\x56\x44\x57\x45\x59\x48\x59\x4a\x59\x4c\x57\x50\x53\x52\x50'\
b'\x52\x4d\x52\x49\x4f\x49\x4c\x49\x49\x4d\x45\x50\x44\x20\x52'\
b'\x4c\x4c\x4c\x4e\x4e\x50\x50\x50\x52\x50\x55\x4f\x57\x4c\x57'\
b'\x4a\x57\x48\x54\x45\x52\x45\x50\x45\x4d\x47\x4c\x4a\x4c\x4c'\
b'\x20\x52\x4f\x3f\x4f\x41\x51\x43\x53\x43\x54\x43\x57\x42\x59'\
b'\x3f\x59\x3e\x59\x3c\x56\x3a\x54\x3a\x52\x3a\x4f\x3d\x4f\x3f'\
b'\x2c\x47\x5d\x4a\x50\x4c\x50\x4e\x50\x52\x50\x57\x4a\x58\x45'\
b'\x58\x45\x57\x47\x54\x49\x52\x49\x50\x49\x4d\x47\x4b\x44\x4b'\
b'\x42\x4b\x3f\x4d\x3b\x51\x38\x54\x38\x57\x38\x5b\x3d\x5b\x41'\
b'\x5b\x46\x57\x4e\x51\x52\x4d\x52\x4b\x52\x49\x52\x4a\x50\x20'\
b'\x52\x52\x47\x54\x47\x57\x45\x58\x42\x58\x40\x58\x3d\x56\x3a'\
b'\x54\x3a\x52\x3a\x4f\x3c\x4e\x3f\x4e\x41\x4e\x44\x50\x47\x52'\
b'\x47\x1b\x4d\x57\x54\x43\x53\x43\x52\x42\x52\x41\x52\x40\x53'\
b'\x3f\x54\x3f\x54\x3f\x55\x40\x55\x41\x55\x42\x54\x43\x54\x43'\
b'\x20\x52\x50\x52\x50\x52\x4f\x51\x4f\x51\x4f\x50\x50\x4f\x50'\
b'\x4f\x51\x4f\x52\x50\x52\x51\x52\x51\x51\x52\x50\x52\x13\x4c'\
b'\x58\x55\x43\x54\x43\x53\x42\x53\x41\x53\x40\x54\x3f\x55\x3f'\
b'\x55\x3f\x56\x40\x56\x41\x56\x42\x55\x43\x55\x43\x20\x52\x51'\
b'\x4e\x53\x4e\x50\x57\x4e\x57\x51\x4e\x09\x48\x5c\x4a\x47\x5a'\
b'\x3f\x5a\x41\x4e\x47\x4e\x47\x5a\x4d\x5a\x4f\x4a\x48\x4a\x47'\
b'\x0e\x48\x5c\x4a\x43\x5a\x43\x5a\x45\x4a\x45\x4a\x43\x20\x52'\
b'\x4a\x4a\x5a\x4a\x5a\x4c\x4a\x4c\x4a\x4a\x20\x52\x4c\x46\x4c'\
b'\x46\x09\x48\x5c\x4a\x4d\x56\x48\x56\x47\x4a\x41\x4a\x3f\x5a'\
b'\x47\x5a\x48\x4a\x4f\x4a\x4d\x27\x4a\x5a\x4d\x4b\x4e\x48\x50'\
b'\x45\x52\x44\x54\x42\x56\x3f\x56\x3e\x56\x3c\x54\x3a\x52\x3a'\
b'\x50\x3a\x4d\x3b\x4d\x39\x50\x38\x52\x38\x55\x38\x58\x3b\x58'\
b'\x3d\x58\x40\x56\x43\x53\x45\x52\x46\x50\x48\x50\x4b\x4d\x4b'\
b'\x20\x52\x4c\x51\x4c\x50\x4d\x4f\x4e\x4f\x4e\x4f\x4f\x50\x4f'\
b'\x51\x4f\x51\x4e\x52\x4e\x52\x4d\x52\x4c\x51\x4c\x51\x4d\x42'\
b'\x62\x52\x55\x4b\x55\x44\x4e\x44\x48\x44\x43\x48\x3c\x4f\x38'\
b'\x54\x38\x57\x38\x5d\x3b\x60\x40\x60\x44\x60\x47\x5e\x4c\x5b'\
b'\x4f\x58\x4f\x57\x4f\x55\x4d\x55\x4b\x55\x4a\x55\x4a\x53\x4d'\
b'\x51\x4f\x4f\x4f\x4d\x4f\x4b\x4c\x4b\x49\x4b\x47\x4d\x42\x51'\
b'\x3f\x53\x3f\x56\x3f\x57\x41\x57\x41\x57\x3f\x59\x3f\x57\x48'\
b'\x57\x4a\x57\x4b\x57\x4c\x57\x4d\x59\x4d\x5b\x4d\x5e\x48\x5e'\
b'\x44\x5e\x3f\x59\x3a\x53\x3a\x50\x3a\x49\x3d\x46\x44\x46\x48'\
b'\x46\x4d\x4c\x54\x52\x54\x54\x54\x59\x53\x5a\x52\x5a\x54\x56'\
b'\x55\x52\x55\x20\x52\x56\x44\x56\x42\x54\x40\x53\x40\x51\x40'\
b'\x4e\x43\x4d\x47\x4d\x49\x4d\x4b\x4e\x4d\x4f\x4d\x51\x4d\x54'\
b'\x4a\x56\x45\x56\x44\x14\x45\x5f\x56\x38\x59\x38\x5d\x52\x5a'\
b'\x52\x59\x4a\x4e\x4a\x4a\x52\x47\x52\x56\x38\x20\x52\x59\x48'\
b'\x57\x3d\x57\x3c\x57\x3b\x57\x3b\x57\x3b\x57\x3c\x56\x3d\x4f'\
b'\x48\x59\x48\x26\x47\x5d\x4e\x38\x55\x38\x58\x38\x5b\x3b\x5b'\
b'\x3e\x5b\x41\x58\x44\x55\x45\x55\x45\x57\x45\x5a\x48\x5a\x4a'\
b'\x5a\x4e\x55\x52\x50\x52\x49\x52\x4e\x38\x20\x52\x52\x44\x55'\
b'\x44\x59\x41\x59\x3e\x59\x3d\x56\x3b\x54\x3b\x50\x3b\x4e\x44'\
b'\x52\x44\x20\x52\x50\x50\x57\x50\x57\x4a\x57\x48\x54\x46\x51'\
b'\x46\x4e\x46\x4c\x50\x50\x50\x1b\x45\x5f\x52\x52\x4d\x52\x47'\
b'\x4c\x47\x47\x47\x43\x4b\x3c\x52\x38\x56\x38\x5a\x38\x5d\x3a'\
b'\x5c\x3c\x59\x3a\x56\x3a\x52\x3a\x4d\x3d\x4a\x43\x4a\x47\x4a'\
b'\x4b\x4e\x50\x52\x50\x56\x50\x59\x4f\x58\x51\x57\x52\x54\x52'\
b'\x52\x52\x52\x52\x15\x44\x60\x4c\x38\x52\x38\x58\x38\x5e\x3e'\
b'\x5e\x43\x5e\x47\x5a\x4e\x53\x52\x4e\x52\x46\x52\x4c\x38\x20'\
b'\x52\x4e\x50\x54\x50\x5b\x49\x5b\x43\x5b\x3b\x52\x3b\x4e\x3b'\
b'\x49\x50\x4e\x50\x0d\x47\x5d\x4e\x38\x5b\x38\x5a\x3b\x50\x3b'\
b'\x4e\x44\x58\x44\x57\x46\x4e\x46\x4c\x50\x57\x50\x56\x52\x49'\
b'\x52\x4e\x38\x0b\x47\x5d\x4e\x38\x5b\x38\x5a\x3b\x50\x3b\x4e'\
b'\x44\x58\x44\x57\x46\x4e\x46\x4b\x52\x49\x52\x4e\x38\x1d\x45'\
b'\x5f\x59\x47\x53\x47\x53\x45\x5c\x45\x59\x51\x56\x52\x52\x52'\
b'\x4f\x52\x4a\x50\x47\x4a\x47\x47\x47\x43\x4b\x3c\x51\x38\x56'\
b'\x38\x59\x38\x5d\x3a\x5d\x3c\x59\x3a\x55\x3a\x50\x3a\x49\x41'\
b'\x49\x47\x49\x4b\x4e\x50\x52\x50\x55\x50\x57\x4f\x59\x47\x0d'\
b'\x44\x60\x4b\x38\x4e\x38\x4b\x44\x59\x44\x5c\x38\x5e\x38\x59'\
b'\x52\x56\x52\x59\x46\x4b\x46\x48\x52\x46\x52\x4b\x38\x05\x4c'\
b'\x58\x54\x38\x56\x38\x50\x52\x4e\x52\x54\x38\x11\x49\x5b\x4b'\
b'\x50\x4c\x50\x4d\x50\x4e\x50\x50\x50\x52\x4d\x53\x4a\x57\x38'\
b'\x59\x38\x56\x49\x55\x4e\x51\x52\x4d\x52\x4d\x52\x4b\x52\x4b'\
b'\x52\x4b\x50\x10\x45\x5f\x4d\x38\x4f\x38\x4c\x44\x4d\x44\x4d'\
b'\x44\x5a\x38\x5d\x38\x4f\x45\x58\x52\x55\x52\x4d\x46\x4c\x45'\
b'\x4c\x45\x4a\x52\x47\x52\x4d\x38\x07\x49\x5b\x51\x38\x53\x38'\
b'\x4e\x50\x59\x50\x58\x52\x4b\x52\x51\x38\x21\x42\x62\x49\x38'\
b'\x4b\x38\x50\x46\x51\x47\x51\x48\x51\x48\x52\x47\x53\x46\x5e'\
b'\x38\x60\x38\x5b\x52\x59\x52\x5d\x40\x5d\x3e\x5e\x3c\x5e\x3c'\
b'\x5e\x3c\x5d\x3c\x5c\x3e\x51\x4b\x50\x4b\x4b\x3e\x4b\x3e\x4b'\
b'\x3d\x4b\x3d\x4a\x3c\x4a\x3c\x4a\x3c\x4a\x3c\x4a\x3f\x46\x52'\
b'\x44\x52\x49\x38\x13\x43\x61\x4b\x38\x4d\x38\x57\x4d\x57\x4e'\
b'\x58\x4e\x58\x4e\x58\x4c\x5c\x38\x5f\x38\x59\x52\x57\x52\x4d'\
b'\x3d\x4d\x3d\x4c\x3c\x4c\x3c\x4c\x3d\x48\x52\x45\x52\x4b\x38'\
b'\x1f\x44\x60\x50\x52\x4c\x52\x46\x4c\x46\x47\x46\x43\x4a\x3c'\
b'\x50\x38\x54\x38\x58\x38\x5e\x3e\x5e\x43\x5e\x47\x5a\x4e\x54'\
b'\x52\x50\x52\x20\x52\x50\x50\x54\x50\x59\x4d\x5c\x47\x5c\x43'\
b'\x5c\x3f\x57\x3a\x54\x3a\x50\x3a\x4b\x3e\x48\x44\x48\x47\x48'\
b'\x4c\x4d\x50\x50\x50\x17\x47\x5d\x4e\x38\x54\x38\x58\x38\x5b'\
b'\x3c\x5b\x3f\x5b\x43\x56\x48\x51\x48\x4d\x48\x4b\x52\x49\x52'\
b'\x4e\x38\x20\x52\x52\x46\x55\x46\x59\x42\x59\x3f\x59\x3d\x56'\
b'\x3b\x54\x3b\x50\x3b\x4d\x46\x52\x46\x22\x44\x60\x55\x58\x50'\
b'\x52\x4c\x52\x46\x4c\x46\x48\x46\x43\x4a\x3c\x50\x38\x54\x38'\
b'\x58\x38\x5e\x3e\x5e\x43\x5e\x47\x5b\x4d\x56\x52\x53\x52\x58'\
b'\x58\x55\x58\x20\x52\x50\x50\x54\x50\x59\x4d\x5c\x47\x5c\x43'\
b'\x5c\x3f\x57\x3a\x54\x3a\x51\x3a\x4b\x3e\x48\x44\x48\x47\x48'\
b'\x4c\x4d\x50\x50\x50\x20\x47\x5d\x4e\x38\x55\x38\x58\x38\x5b'\
b'\x3c\x5b\x3f\x5b\x42\x57\x46\x54\x46\x54\x46\x55\x47\x56\x4a'\
b'\x58\x52\x56\x52\x54\x4a\x53\x49\x52\x47\x50\x47\x4d\x47\x4b'\
b'\x52\x49\x52\x4e\x38\x20\x52\x52\x45\x55\x45\x59\x42\x59\x3f'\
b'\x59\x3d\x57\x3b\x54\x3b\x50\x3b\x4e\x45\x52\x45\x26\x47\x5d'\
b'\x4a\x4e\x4b\x4f\x4e\x50\x50\x50\x53\x50\x56\x4e\x56\x4c\x56'\
b'\x4a\x54\x48\x51\x46\x4f\x44\x4d\x41\x4d\x3f\x4d\x3c\x52\x38'\
b'\x55\x38\x58\x38\x5b\x39\x5a\x3b\x58\x3a\x55\x3a\x53\x3a\x4f'\
b'\x3d\x4f\x3f\x4f\x40\x51\x43\x53\x45\x56\x46\x58\x49\x58\x4b'\
b'\x58\x4d\x56\x51\x52\x52\x50\x52\x4e\x52\x4b\x52\x49\x51\x4a'\
b'\x4e\x09\x47\x5d\x51\x3b\x49\x3b\x4a\x38\x5b\x38\x5a\x3b\x53'\
b'\x3b\x4e\x52\x4c\x52\x51\x3b\x17\x45\x5f\x4b\x38\x4d\x38\x4a'\
b'\x47\x49\x49\x49\x4a\x49\x4d\x4d\x50\x4f\x50\x53\x50\x56\x4d'\
b'\x57\x49\x5b\x38\x5d\x38\x5a\x48\x58\x4e\x53\x52\x4f\x52\x4b'\
b'\x52\x47\x4e\x47\x4b\x47\x49\x47\x47\x4b\x38\x0d\x45\x5f\x47'\
b'\x38\x4a\x38\x4d\x4d\x4d\x4d\x4d\x4f\x4d\x4f\x4d\x4e\x4e\x4d'\
b'\x5a\x38\x5d\x38\x4d\x52\x4b\x52\x47\x38\x1a\x40\x64\x42\x38'\
b'\x44\x38\x46\x4c\x46\x4f\x46\x4f\x46\x4e\x47\x4c\x51\x38\x53'\
b'\x38\x55\x4d\x55\x4f\x55\x4f\x55\x4d\x56\x4c\x5f\x38\x62\x38'\
b'\x55\x52\x53\x52\x51\x3f\x51\x3c\x51\x3c\x51\x3e\x50\x3f\x46'\
b'\x52\x44\x52\x42\x38\x1a\x44\x60\x46\x52\x51\x45\x50\x44\x4e'\
b'\x3e\x4c\x38\x4e\x38\x52\x42\x52\x43\x52\x44\x53\x44\x53\x43'\
b'\x54\x42\x5c\x38\x5e\x38\x54\x45\x54\x46\x59\x52\x56\x52\x52'\
b'\x48\x52\x47\x52\x47\x52\x47\x51\x48\x51\x48\x49\x52\x46\x52'\
b'\x0d\x47\x5d\x4d\x48\x49\x38\x4b\x38\x4e\x44\x4f\x46\x4f\x46'\
b'\x50\x45\x59\x38\x5b\x38\x50\x48\x4e\x52\x4b\x52\x4d\x48\x0b'\
b'\x44\x60\x5a\x3b\x4c\x3b\x4d\x38\x5e\x38\x5e\x39\x4a\x50\x59'\
b'\x50\x58\x52\x46\x52\x46\x51\x5a\x3b\x09\x4a\x5a\x52\x38\x58'\
b'\x38\x58\x3a\x54\x3a\x4e\x56\x52\x56\x52\x58\x4c\x58\x52\x38'\
b'\x05\x4c\x58\x4e\x38\x50\x38\x56\x56\x54\x56\x4e\x38\x09\x4a'\
b'\x5a\x4c\x56\x50\x56\x56\x3a\x52\x3a\x52\x38\x58\x38\x52\x58'\
b'\x4c\x58\x4c\x56\x09\x48\x5c\x51\x38\x52\x38\x5a\x46\x58\x46'\
b'\x52\x3b\x52\x3b\x4c\x46\x4a\x46\x51\x38\x05\x48\x5c\x4b\x55'\
b'\x5a\x55\x59\x57\x4a\x57\x4b\x55\x05\x4d\x57\x4f\x37\x51\x37'\
b'\x55\x3d\x53\x3d\x4f\x37\x24\x48\x5c\x55\x52\x55\x50\x56\x4d'\
b'\x55\x4d\x54\x50\x51\x52\x4f\x52\x4c\x52\x4a\x4f\x4a\x4c\x4a'\
b'\x48\x4c\x42\x52\x3f\x55\x3f\x57\x3f\x5a\x40\x58\x4c\x58\x4d'\
b'\x57\x51\x57\x52\x55\x52\x20\x52\x58\x42\x56\x41\x54\x41\x52'\
b'\x41\x4e\x44\x4c\x49\x4c\x4c\x4c\x50\x4f\x50\x51\x50\x54\x4e'\
b'\x56\x49\x57\x47\x58\x42\x22\x48\x5c\x4f\x37\x51\x37\x4f\x40'\
b'\x4e\x44\x4f\x44\x51\x3f\x55\x3f\x58\x3f\x5a\x43\x5a\x46\x5a'\
b'\x49\x58\x4f\x53\x52\x50\x52\x4e\x52\x4b\x52\x4a\x51\x4f\x37'\
b'\x20\x52\x4c\x50\x4e\x50\x50\x50\x52\x50\x56\x4e\x58\x49\x58'\
b'\x46\x58\x44\x56\x41\x55\x41\x53\x41\x50\x44\x4e\x48\x4d\x4a'\
b'\x4c\x50\x1a\x49\x5b\x51\x52\x4e\x52\x4b\x4f\x4b\x4b\x4b\x48'\
b'\x4d\x42\x52\x3f\x55\x3f\x57\x3f\x59\x41\x59\x43\x57\x41\x55'\
b'\x41\x52\x41\x4f\x44\x4d\x48\x4d\x4b\x4d\x4e\x50\x50\x52\x50'\
b'\x54\x50\x56\x4f\x56\x51\x54\x52\x52\x52\x51\x52\x26\x47\x5d'\
b'\x54\x52\x54\x50\x55\x4d\x54\x4d\x53\x50\x50\x52\x4e\x52\x4b'\
b'\x52\x49\x4f\x49\x4c\x49\x48\x4b\x43\x51\x3f\x54\x3f\x55\x3f'\
b'\x57\x40\x59\x37\x5b\x37\x57\x4c\x57\x4d\x56\x51\x56\x52\x54'\
b'\x52\x20\x52\x57\x42\x55\x41\x53\x41\x51\x41\x4d\x44\x4b\x49'\
b'\x4b\x4c\x4b\x50\x4e\x50\x50\x50\x53\x4e\x55\x49\x56\x47\x57'\
b'\x42\x22\x48\x5c\x4d\x4b\x4d\x4e\x4f\x50\x52\x50\x54\x50\x57'\
b'\x4f\x57\x51\x54\x52\x51\x52\x4e\x52\x4a\x4e\x4a\x4b\x4a\x48'\
b'\x4d\x42\x52\x3f\x54\x3f\x57\x3f\x5a\x42\x5a\x44\x5a\x47\x53'\
b'\x4a\x4d\x4a\x4d\x4b\x20\x52\x4d\x48\x52\x48\x57\x46\x57\x44'\
b'\x57\x43\x56\x41\x54\x41\x51\x41\x4e\x45\x4d\x48\x16\x49\x5b'\
b'\x50\x42\x4c\x42\x4d\x40\x50\x40\x51\x3c\x52\x37\x57\x37\x58'\
b'\x37\x59\x37\x59\x39\x58\x38\x57\x38\x55\x38\x53\x3b\x53\x3d'\
b'\x52\x40\x57\x40\x56\x42\x52\x42\x4d\x58\x4b\x58\x50\x42\x2b'\
b'\x47\x5d\x49\x57\x4c\x59\x4e\x59\x51\x59\x55\x55\x56\x51\x56'\
b'\x4d\x56\x4d\x55\x50\x52\x52\x50\x52\x4d\x52\x4b\x4f\x4b\x4c'\
b'\x4b\x48\x4d\x43\x52\x3f\x56\x3f\x57\x3f\x5a\x40\x5b\x40\x58'\
b'\x51\x57\x56\x52\x5b\x4e\x5b\x4b\x5b\x49\x59\x49\x57\x20\x52'\
b'\x59\x42\x57\x41\x55\x41\x53\x41\x4f\x44\x4d\x49\x4d\x4c\x4d'\
b'\x50\x50\x50\x52\x50\x55\x4e\x57\x49\x58\x47\x59\x42\x1a\x47'\
b'\x5d\x4f\x37\x51\x37\x4f\x44\x4f\x44\x52\x3f\x56\x3f\x58\x3f'\
b'\x5b\x42\x5b\x44\x5b\x45\x5a\x46\x5a\x47\x58\x52\x56\x52\x58'\
b'\x47\x58\x45\x58\x45\x58\x41\x55\x41\x54\x41\x51\x44\x4e\x47'\
b'\x4e\x49\x4c\x52\x49\x52\x4f\x37\x20\x4c\x58\x52\x40\x54\x40'\
b'\x51\x4d\x51\x4e\x51\x4f\x51\x50\x52\x50\x53\x50\x54\x50\x53'\
b'\x52\x52\x52\x51\x52\x50\x52\x4e\x51\x4e\x4f\x4e\x4e\x4f\x4d'\
b'\x52\x40\x20\x52\x54\x3b\x53\x3b\x52\x3a\x52\x3a\x52\x39\x53'\
b'\x38\x54\x38\x55\x38\x56\x39\x56\x3a\x56\x3a\x55\x3b\x54\x3b'\
b'\x20\x48\x5c\x4a\x58\x4c\x59\x4d\x59\x4f\x59\x51\x55\x52\x52'\
b'\x56\x40\x58\x40\x55\x51\x53\x56\x50\x5b\x4d\x5b\x4c\x5b\x4a'\
b'\x5a\x4a\x5a\x4a\x58\x20\x52\x57\x3a\x57\x39\x58\x38\x58\x38'\
b'\x59\x38\x5a\x39\x5a\x3a\x5a\x3a\x59\x3b\x58\x3b\x58\x3b\x58'\
b'\x3b\x57\x3b\x57\x3a\x57\x3a\x0e\x47\x5d\x4f\x37\x51\x37\x4e'\
b'\x48\x4e\x48\x58\x40\x5b\x40\x50\x48\x57\x52\x54\x52\x4e\x49'\
b'\x4e\x49\x4c\x52\x49\x52\x4f\x37\x12\x4c\x58\x53\x37\x56\x37'\
b'\x51\x4d\x51\x4e\x51\x4f\x51\x50\x52\x50\x53\x50\x54\x50\x53'\
b'\x52\x52\x52\x51\x52\x50\x52\x4e\x51\x4e\x4f\x4e\x4e\x4f\x4d'\
b'\x53\x37\x2c\x42\x62\x48\x40\x4a\x40\x4a\x42\x49\x45\x49\x45'\
b'\x4c\x3f\x50\x3f\x52\x3f\x54\x42\x54\x45\x56\x42\x5a\x3f\x5c'\
b'\x3f\x60\x3f\x60\x44\x60\x45\x5f\x48\x5d\x52\x5b\x52\x5d\x47'\
b'\x5e\x45\x5e\x44\x5e\x41\x5b\x41\x5a\x41\x57\x44\x54\x47\x54'\
b'\x49\x52\x52\x50\x52\x52\x47\x52\x45\x52\x45\x52\x41\x50\x41'\
b'\x4e\x41\x4b\x44\x49\x48\x48\x49\x46\x52\x44\x52\x47\x45\x48'\
b'\x41\x48\x40\x1c\x47\x5d\x4d\x40\x4f\x40\x4f\x42\x4f\x45\x4f'\
b'\x45\x50\x42\x54\x3f\x56\x3f\x5b\x3f\x5b\x44\x5b\x45\x5a\x48'\
b'\x58\x52\x56\x52\x58\x47\x58\x45\x58\x45\x58\x41\x55\x41\x54'\
b'\x41\x51\x44\x4e\x47\x4e\x49\x4c\x52\x49\x52\x4c\x45\x4d\x42'\
b'\x4d\x40\x1e\x48\x5c\x50\x52\x4d\x52\x4a\x4f\x4a\x4b\x4a\x48'\
b'\x4c\x42\x51\x3f\x54\x3f\x57\x3f\x5a\x43\x5a\x46\x5a\x4a\x58'\
b'\x4f\x53\x52\x50\x52\x20\x52\x51\x50\x53\x50\x56\x4e\x58\x49'\
b'\x58\x47\x58\x44\x56\x41\x53\x41\x50\x41\x4c\x47\x4c\x4b\x4c'\
b'\x4e\x4f\x50\x51\x50\x26\x47\x5d\x4e\x40\x50\x40\x50\x40\x4f'\
b'\x44\x4f\x45\x4f\x45\x52\x3f\x56\x3f\x59\x3f\x5b\x43\x5b\x46'\
b'\x5b\x49\x58\x4f\x54\x52\x51\x52\x4f\x52\x4d\x52\x4b\x5b\x49'\
b'\x5b\x4d\x45\x4d\x44\x4e\x40\x4e\x40\x20\x52\x4d\x50\x4f\x50'\
b'\x51\x50\x53\x50\x57\x4e\x59\x49\x59\x46\x59\x41\x56\x41\x54'\
b'\x41\x51\x44\x4f\x48\x4e\x4b\x4d\x50\x21\x48\x5c\x55\x4d\x55'\
b'\x4d\x54\x50\x51\x52\x4f\x52\x4c\x52\x4a\x4f\x4a\x4c\x4a\x48'\
b'\x4c\x43\x51\x3f\x55\x3f\x57\x3f\x5a\x40\x55\x5b\x53\x5b\x55'\
b'\x4f\x55\x4d\x20\x52\x58\x42\x56\x41\x54\x41\x52\x41\x4e\x44'\
b'\x4c\x49\x4c\x4c\x4c\x50\x4f\x50\x51\x50\x54\x4e\x56\x4a\x57'\
b'\x47\x58\x42\x15\x4a\x5a\x4f\x40\x51\x40\x51\x44\x51\x44\x52'\
b'\x42\x55\x3f\x56\x3f\x58\x3f\x58\x40\x58\x42\x58\x42\x57\x41'\
b'\x56\x41\x54\x41\x50\x46\x50\x4a\x4e\x52\x4c\x52\x4e\x46\x4f'\
b'\x42\x4f\x40\x26\x4a\x5a\x4c\x4f\x4d\x50\x4f\x50\x51\x50\x52'\
b'\x50\x55\x4f\x55\x4d\x55\x4c\x53\x4b\x52\x4a\x50\x49\x4e\x46'\
b'\x4e\x45\x4e\x42\x51\x3f\x54\x3f\x55\x3f\x58\x40\x58\x40\x58'\
b'\x42\x56\x41\x54\x41\x52\x41\x50\x43\x50\x45\x50\x46\x51\x47'\
b'\x53\x48\x55\x49\x57\x4c\x57\x4d\x57\x50\x53\x52\x50\x52\x4f'\
b'\x52\x4c\x52\x4c\x51\x4c\x4f\x1b\x4b\x59\x50\x42\x4d\x42\x4d'\
b'\x40\x50\x40\x51\x3b\x54\x3a\x53\x40\x57\x40\x57\x42\x52\x42'\
b'\x50\x4c\x50\x4e\x50\x4f\x50\x50\x50\x50\x51\x50\x52\x50\x54'\
b'\x50\x53\x52\x53\x52\x51\x52\x51\x52\x4d\x52\x4d\x4f\x4d\x4e'\
b'\x4e\x4c\x50\x42\x1d\x47\x5d\x4c\x40\x4e\x40\x4c\x4a\x4c\x4d'\
b'\x4c\x4d\x4c\x50\x4f\x50\x50\x50\x53\x4e\x56\x4a\x56\x48\x58'\
b'\x40\x5b\x40\x58\x4d\x57\x50\x57\x52\x55\x52\x55\x4d\x55\x4d'\
b'\x54\x50\x50\x52\x4e\x52\x4c\x52\x49\x50\x49\x4d\x49\x4d\x4a'\
b'\x4b\x4a\x4a\x4c\x40\x0d\x48\x5c\x4a\x40\x4c\x40\x4e\x4d\x4f'\
b'\x4e\x4f\x4f\x4f\x4f\x4f\x4e\x50\x4d\x57\x40\x5a\x40\x4f\x52'\
b'\x4d\x52\x4a\x40\x1d\x44\x60\x46\x40\x48\x40\x49\x4e\x49\x4e'\
b'\x49\x4f\x49\x50\x49\x50\x49\x4f\x4a\x4e\x51\x40\x53\x40\x54'\
b'\x4e\x54\x50\x54\x50\x54\x4f\x55\x4e\x5c\x40\x5e\x40\x55\x52'\
b'\x53\x52\x51\x45\x51\x44\x52\x43\x51\x43\x51\x43\x51\x44\x4a'\
b'\x52\x47\x52\x46\x40\x13\x47\x5d\x51\x49\x4d\x40\x4f\x40\x52'\
b'\x47\x52\x48\x52\x48\x53\x46\x59\x40\x5b\x40\x53\x49\x57\x52'\
b'\x55\x52\x52\x4c\x52\x4a\x52\x4a\x51\x4c\x4b\x52\x49\x52\x51'\
b'\x49\x16\x45\x5f\x47\x58\x48\x59\x49\x59\x4a\x59\x4c\x57\x4d'\
b'\x55\x4f\x52\x4c\x40\x4f\x40\x51\x4e\x51\x50\x51\x50\x52\x4f'\
b'\x5a\x40\x5d\x40\x50\x55\x4e\x58\x4b\x5b\x49\x5b\x48\x5b\x47'\
b'\x5a\x47\x58\x0b\x47\x5d\x57\x42\x4d\x42\x4d\x40\x5b\x40\x5b'\
b'\x40\x4d\x50\x58\x50\x57\x52\x49\x52\x49\x51\x57\x42\x27\x4a'\
b'\x5a\x4f\x4b\x4f\x49\x4c\x49\x4d\x47\x4e\x47\x50\x45\x50\x43'\
b'\x52\x3e\x52\x3b\x55\x38\x58\x38\x57\x3a\x56\x3a\x54\x3c\x54'\
b'\x3e\x53\x43\x52\x45\x50\x48\x4f\x48\x4f\x48\x51\x49\x51\x4b'\
b'\x51\x4c\x50\x4d\x4f\x52\x4f\x53\x4f\x54\x4f\x55\x50\x56\x51'\
b'\x56\x51\x58\x4f\x57\x4d\x55\x4d\x54\x4d\x53\x4d\x52\x4e\x4d'\
b'\x4f\x4c\x4f\x4b\x05\x4f\x55\x51\x36\x53\x36\x53\x5b\x51\x5b'\
b'\x51\x36\x26\x4a\x5a\x55\x48\x55\x48\x53\x47\x53\x45\x53\x44'\
b'\x54\x43\x55\x3e\x55\x3d\x55\x3c\x55\x3b\x54\x3a\x53\x3a\x53'\
b'\x38\x57\x39\x57\x3c\x57\x3d\x57\x3e\x56\x43\x55\x44\x55\x45'\
b'\x55\x47\x58\x47\x57\x49\x56\x49\x54\x4b\x54\x4d\x52\x52\x52'\
b'\x55\x4f\x58\x4c\x58\x4d\x56\x4e\x56\x50\x54\x50\x52\x51\x4d'\
b'\x52\x4b\x54\x48\x55\x48\x1a\x48\x5c\x4a\x4a\x4a\x47\x4c\x45'\
b'\x4e\x45\x50\x45\x51\x46\x52\x46\x54\x48\x55\x48\x56\x48\x57'\
b'\x48\x58\x46\x58\x45\x5a\x45\x5a\x47\x58\x4a\x56\x4a\x54\x4a'\
b'\x52\x49\x51\x48\x51\x47\x4f\x47\x4e\x47\x4c\x47\x4c\x4a\x4a'\
b'\x4a\x0b\x47\x5d\x49\x39\x5b\x39\x5b\x52\x49\x52\x49\x39\x20'\
b'\x52\x58\x4f\x58\x3c\x4c\x3c\x4c\x4f\x58\x4f'

_index =\
b'\x00\x00\x03\x00\x2c\x00\x45\x00\x8e\x00\xf7\x00\x7a\x01\xeb'\
b'\x01\xf8\x01\x17\x02\x34\x02\x57\x02\x74\x02\x81\x02\x8e\x02'\
b'\xab\x02\xb8\x02\xfb\x02\x0c\x03\x51\x03\xa6\x03\xd1\x03\x0c'\
b'\x04\x67\x04\x84\x04\xfb\x04\x56\x05\x8f\x05\xb8\x05\xcd\x05'\
b'\xec\x05\x01\x06\x52\x06\xef\x06\x1a\x07\x69\x07\xa2\x07\xcf'\
b'\x07\xec\x07\x05\x08\x42\x08\x5f\x08\x6c\x08\x91\x08\xb4\x08'\
b'\xc5\x08\x0a\x09\x33\x09\x74\x09\xa5\x09\xec\x09\x2f\x0a\x7e'\
b'\x0a\x93\x0a\xc4\x0a\xe1\x0a\x18\x0b\x4f\x0b\x6c\x0b\x85\x0b'\
b'\x9a\x0b\xa7\x0b\xbc\x0b\xd1\x0b\xde\x0b\xeb\x0b\x36\x0c\x7d'\
b'\x0c\xb4\x0c\x03\x0d\x4a\x0d\x79\x0d\xd2\x0d\x09\x0e\x4c\x0e'\
b'\x8f\x0e\xae\x0e\xd5\x0e\x30\x0f\x6b\x0f\xaa\x0f\xf9\x0f\x3e'\
b'\x10\x6b\x10\xba\x10\xf3\x10\x30\x11\x4d\x11\x8a\x11\xb3\x11'\
b'\xe2\x11\xfb\x11\x4c\x12\x59\x12\xa8\x12\xdf\x12'

FONT = memoryview(_font)
INDEX = memoryview(_index)
