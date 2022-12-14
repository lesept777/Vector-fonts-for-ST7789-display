FIRST = 32
LAST = 127
WIDTH = 38
HEIGHT = 43

_font =\
b'\x01\x4e\x56\x18\x4d\x57\x55\x3a\x55\x3e\x53\x47\x51\x47\x50'\
b'\x3e\x50\x3a\x50\x36\x53\x36\x55\x36\x55\x3a\x20\x52\x55\x4f'\
b'\x55\x50\x53\x52\x52\x52\x51\x52\x4f\x50\x4f\x4f\x4f\x4e\x51'\
b'\x4c\x52\x4c\x54\x4c\x55\x4e\x55\x4f\x17\x49\x5b\x59\x38\x59'\
b'\x3c\x56\x43\x55\x43\x54\x3b\x54\x38\x54\x34\x56\x34\x58\x34'\
b'\x59\x36\x59\x38\x20\x52\x50\x38\x50\x3c\x4d\x43\x4d\x43\x4b'\
b'\x3b\x4b\x38\x4b\x34\x4e\x34\x4f\x34\x50\x36\x50\x38\x37\x46'\
b'\x5e\x5c\x3f\x5c\x41\x58\x41\x58\x43\x57\x44\x57\x45\x56\x47'\
b'\x5a\x47\x5a\x49\x55\x49\x52\x51\x52\x52\x4f\x52\x50\x51\x53'\
b'\x49\x4e\x49\x4b\x51\x4b\x52\x48\x52\x48\x51\x4b\x49\x48\x49'\
b'\x48\x47\x4c\x47\x4d\x46\x4d\x45\x4e\x43\x4e\x41\x4a\x41\x4a'\
b'\x3f\x4f\x3f\x52\x38\x52\x37\x55\x37\x54\x37\x52\x3f\x57\x3f'\
b'\x59\x38\x59\x37\x5c\x37\x5c\x37\x59\x3f\x5c\x3f\x20\x52\x56'\
b'\x41\x51\x41\x50\x43\x50\x44\x4f\x45\x4f\x47\x54\x47\x54\x46'\
b'\x54\x45\x55\x43\x56\x41\x33\x49\x5b\x59\x4b\x59\x51\x53\x51'\
b'\x53\x55\x54\x58\x51\x58\x51\x55\x51\x52\x4e\x52\x4b\x51\x4b'\
b'\x4e\x4e\x4f\x51\x4f\x56\x4f\x56\x4c\x56\x4b\x55\x4a\x54\x4a'\
b'\x52\x49\x4f\x48\x4d\x47\x4b\x45\x4b\x42\x4b\x40\x4e\x3d\x51'\
b'\x3d\x51\x39\x51\x36\x54\x36\x53\x39\x53\x3d\x57\x3d\x58\x3d'\
b'\x58\x40\x55\x3f\x53\x3f\x4f\x3f\x4f\x42\x4f\x43\x50\x44\x53'\
b'\x45\x56\x46\x57\x47\x59\x49\x59\x4b\x20\x52\x52\x53\x52\x53'\
b'\x20\x52\x52\x3c\x52\x3c\x41\x46\x5e\x53\x3c\x53\x3e\x50\x41'\
b'\x4e\x41\x4b\x41\x48\x3e\x48\x3c\x48\x3a\x4b\x37\x4e\x37\x50'\
b'\x37\x53\x3a\x53\x3c\x20\x52\x5c\x4d\x5c\x4f\x59\x52\x56\x52'\
b'\x54\x52\x51\x4f\x51\x4d\x51\x4b\x54\x48\x56\x48\x59\x48\x5c'\
b'\x4b\x5c\x4d\x20\x52\x5b\x37\x5b\x39\x4b\x50\x4b\x52\x48\x52'\
b'\x48\x50\x59\x39\x59\x37\x5b\x37\x20\x52\x59\x4d\x59\x4c\x58'\
b'\x4a\x56\x4a\x55\x4a\x53\x4c\x53\x4d\x53\x4f\x55\x50\x56\x50'\
b'\x58\x50\x59\x4f\x59\x4d\x20\x52\x51\x3c\x51\x3a\x4f\x38\x4e'\
b'\x38\x4c\x38\x4b\x3a\x4b\x3c\x4b\x3d\x4c\x3f\x4e\x3f\x4f\x3f'\
b'\x51\x3d\x51\x3c\x46\x43\x61\x5f\x52\x5b\x52\x5b\x51\x5a\x4f'\
b'\x58\x4d\x57\x4d\x57\x4d\x53\x53\x4c\x53\x49\x53\x45\x4f\x45'\
b'\x4b\x45\x48\x48\x43\x4b\x42\x4b\x42\x47\x3f\x47\x3c\x47\x39'\
b'\x4b\x36\x4e\x36\x51\x36\x55\x39\x55\x3c\x55\x3e\x54\x3f\x53'\
b'\x41\x51\x42\x51\x42\x53\x43\x58\x48\x58\x48\x59\x46\x59\x42'\
b'\x5d\x42\x5d\x43\x5c\x45\x5b\x48\x59\x49\x59\x49\x5b\x4b\x5d'\
b'\x4e\x5f\x51\x5f\x52\x20\x52\x56\x4b\x56\x4b\x54\x49\x53\x48'\
b'\x4f\x44\x4d\x43\x48\x45\x48\x4a\x48\x4d\x4b\x50\x4e\x50\x52'\
b'\x50\x56\x4b\x20\x52\x51\x3d\x51\x3b\x4f\x39\x4e\x39\x4d\x39'\
b'\x4b\x3a\x4b\x3c\x4b\x3f\x4f\x41\x51\x40\x51\x3d\x0b\x4e\x56'\
b'\x54\x38\x54\x3c\x52\x43\x51\x43\x50\x3b\x50\x38\x50\x34\x52'\
b'\x34\x54\x34\x54\x36\x54\x38\x14\x4a\x5a\x58\x5a\x56\x5c\x53'\
b'\x5b\x51\x58\x4c\x52\x4c\x48\x4c\x3d\x51\x36\x54\x34\x57\x32'\
b'\x58\x34\x55\x36\x54\x38\x4f\x3f\x4f\x48\x4f\x50\x54\x56\x55'\
b'\x57\x57\x59\x58\x5a\x13\x4a\x5a\x58\x46\x58\x51\x53\x58\x50'\
b'\x5b\x4d\x5c\x4c\x5a\x4f\x59\x50\x56\x55\x4f\x55\x46\x55\x3e'\
b'\x50\x38\x4e\x36\x4c\x34\x4e\x32\x51\x34\x53\x36\x58\x3c\x58'\
b'\x46\x2f\x47\x5d\x5b\x3c\x5b\x3e\x57\x3e\x55\x3e\x53\x3d\x53'\
b'\x3e\x58\x42\x58\x43\x58\x44\x56\x45\x55\x45\x53\x45\x52\x3f'\
b'\x52\x3f\x4f\x45\x4e\x45\x4d\x45\x4b\x43\x4b\x42\x4b\x41\x50'\
b'\x3e\x50\x3d\x4e\x3d\x4a\x3c\x49\x3c\x49\x3b\x49\x3a\x4a\x38'\
b'\x4b\x38\x4c\x38\x51\x3c\x51\x3c\x50\x37\x50\x35\x50\x35\x51'\
b'\x34\x52\x34\x54\x34\x54\x35\x54\x37\x53\x3c\x53\x3c\x58\x39'\
b'\x59\x39\x5a\x39\x5b\x3b\x5b\x3c\x0d\x47\x5d\x5b\x49\x53\x49'\
b'\x53\x50\x51\x50\x51\x49\x49\x49\x49\x46\x51\x46\x51\x3e\x53'\
b'\x3e\x53\x46\x5b\x46\x5b\x49\x12\x4c\x58\x56\x50\x56\x52\x53'\
b'\x57\x50\x5a\x4e\x59\x52\x55\x52\x52\x50\x51\x50\x4f\x50\x4e'\
b'\x51\x4c\x53\x4c\x54\x4c\x56\x4e\x56\x50\x20\x52\x53\x52\x53'\
b'\x52\x05\x4b\x59\x57\x46\x56\x49\x4d\x49\x4e\x46\x57\x46\x0d'\
b'\x4d\x57\x55\x4f\x55\x50\x53\x52\x52\x52\x51\x52\x4f\x50\x4f'\
b'\x4f\x4f\x4e\x51\x4c\x52\x4c\x54\x4c\x55\x4e\x55\x4f\x09\x4b'\
b'\x59\x57\x33\x57\x35\x50\x55\x50\x58\x4d\x58\x4d\x57\x54\x37'\
b'\x54\x33\x57\x33\x1b\x47\x5d\x5b\x47\x5b\x4c\x56\x53\x52\x53'\
b'\x4d\x53\x49\x4c\x49\x48\x49\x42\x4e\x3c\x52\x3c\x57\x3c\x5b'\
b'\x42\x5b\x47\x20\x52\x58\x48\x58\x43\x55\x3e\x52\x3e\x4f\x3e'\
b'\x4c\x43\x4c\x47\x4c\x4b\x4f\x50\x52\x50\x55\x50\x58\x4b\x58'\
b'\x48\x0e\x4b\x59\x57\x52\x53\x52\x53\x4e\x53\x49\x53\x43\x53'\
b'\x41\x4e\x43\x4d\x41\x55\x3c\x57\x3c\x56\x42\x56\x49\x56\x4d'\
b'\x57\x52\x17\x48\x5c\x5a\x4f\x59\x52\x4a\x52\x4b\x4f\x50\x4b'\
b'\x54\x46\x54\x43\x54\x3f\x4f\x3f\x4c\x3f\x4a\x3f\x4b\x3c\x4c'\
b'\x3c\x4f\x3c\x54\x3c\x58\x3f\x58\x42\x58\x46\x52\x4c\x4e\x4f'\
b'\x4e\x4f\x54\x4f\x5a\x4f\x20\x47\x5d\x5b\x4f\x5b\x53\x52\x5a'\
b'\x4a\x5a\x49\x58\x50\x57\x57\x53\x57\x50\x57\x4c\x52\x4a\x4d'\
b'\x4a\x4d\x47\x51\x47\x56\x45\x56\x43\x56\x40\x53\x3f\x4f\x3f'\
b'\x4d\x3f\x4b\x3f\x4b\x3c\x4d\x3c\x51\x3c\x55\x3c\x59\x3f\x59'\
b'\x41\x59\x46\x54\x47\x54\x48\x57\x48\x5b\x4c\x5b\x4f\x1d\x46'\
b'\x5e\x5c\x4b\x5b\x4f\x58\x4f\x58\x53\x58\x59\x54\x59\x55\x54'\
b'\x55\x4f\x49\x4f\x48\x4c\x48\x4c\x54\x3c\x54\x3c\x58\x3c\x58'\
b'\x41\x58\x4c\x5a\x4c\x5c\x4b\x20\x52\x55\x3f\x55\x3f\x55\x3f'\
b'\x4c\x4b\x4c\x4c\x4c\x4c\x4f\x4c\x55\x4c\x55\x45\x55\x3f\x16'\
b'\x48\x5c\x5a\x4e\x5a\x53\x52\x59\x4b\x5a\x4a\x57\x50\x57\x56'\
b'\x53\x56\x4f\x56\x4c\x51\x49\x4a\x49\x4b\x3f\x4b\x3c\x58\x3c'\
b'\x58\x3f\x54\x3f\x4e\x3f\x4d\x43\x4d\x46\x54\x46\x5a\x4a\x5a'\
b'\x4e\x20\x47\x5d\x5b\x4a\x5b\x4d\x56\x53\x52\x53\x4e\x53\x49'\
b'\x4d\x49\x47\x49\x37\x57\x36\x58\x38\x52\x39\x4d\x3e\x4c\x44'\
b'\x4d\x44\x4f\x41\x53\x41\x57\x41\x5b\x46\x5b\x4a\x20\x52\x58'\
b'\x4a\x58\x47\x54\x44\x51\x44\x4e\x44\x4c\x46\x4c\x4b\x50\x50'\
b'\x52\x50\x55\x50\x58\x4d\x58\x4a\x12\x48\x5c\x5a\x3c\x5a\x40'\
b'\x57\x47\x56\x49\x52\x52\x4f\x58\x4f\x59\x4b\x58\x4b\x57\x4e'\
b'\x52\x54\x48\x54\x47\x57\x41\x57\x3f\x53\x3f\x4a\x3f\x4a\x3c'\
b'\x5a\x3c\x32\x47\x5d\x5b\x4a\x5b\x4e\x56\x52\x52\x52\x4e\x52'\
b'\x49\x4e\x49\x4b\x49\x48\x4c\x44\x4f\x43\x4f\x43\x4a\x40\x4a'\
b'\x3c\x4a\x39\x4f\x35\x52\x35\x55\x35\x5a\x39\x5a\x3b\x5a\x3d'\
b'\x57\x41\x55\x42\x55\x42\x5b\x46\x5b\x4a\x20\x52\x58\x4b\x58'\
b'\x47\x51\x44\x4f\x44\x4c\x48\x4c\x4a\x4c\x4d\x50\x50\x52\x50'\
b'\x54\x50\x58\x4d\x58\x4b\x20\x52\x56\x3c\x56\x3a\x54\x38\x52'\
b'\x38\x50\x38\x4e\x3a\x4e\x3b\x4e\x3f\x53\x41\x56\x3f\x56\x3c'\
b'\x1f\x47\x5d\x5b\x48\x5b\x5a\x4c\x5a\x4b\x58\x57\x57\x58\x4b'\
b'\x57\x4b\x55\x4e\x51\x4e\x4d\x4e\x49\x49\x49\x45\x49\x41\x4e'\
b'\x3c\x52\x3c\x56\x3c\x5b\x42\x5b\x48\x20\x52\x58\x48\x58\x43'\
b'\x54\x3f\x52\x3f\x4f\x3f\x4c\x42\x4c\x44\x4c\x47\x50\x4b\x53'\
b'\x4b\x56\x4b\x58\x48\x1b\x4d\x57\x55\x41\x55\x42\x53\x44\x52'\
b'\x44\x51\x44\x4f\x42\x4f\x41\x4f\x40\x51\x3e\x52\x3e\x54\x3e'\
b'\x55\x3f\x55\x41\x20\x52\x55\x4f\x55\x50\x53\x52\x52\x52\x51'\
b'\x52\x4f\x50\x4f\x4f\x4f\x4e\x51\x4c\x52\x4c\x54\x4c\x55\x4e'\
b'\x55\x4f\x20\x4c\x58\x56\x50\x56\x52\x53\x57\x50\x5a\x4e\x59'\
b'\x52\x55\x52\x52\x50\x51\x50\x4f\x50\x4e\x51\x4c\x53\x4c\x54'\
b'\x4c\x56\x4e\x56\x50\x20\x52\x53\x52\x53\x52\x20\x52\x56\x41'\
b'\x56\x42\x54\x44\x52\x44\x51\x44\x50\x42\x50\x41\x50\x40\x52'\
b'\x3e\x53\x3e\x54\x3e\x56\x3f\x56\x41\x09\x47\x5d\x5b\x4f\x59'\
b'\x51\x49\x48\x49\x46\x59\x3d\x5b\x40\x4d\x47\x4d\x48\x5b\x4f'\
b'\x0b\x47\x5d\x5b\x44\x49\x44\x49\x42\x5b\x42\x5b\x44\x20\x52'\
b'\x5b\x4d\x49\x4d\x49\x4a\x5b\x4a\x5b\x4d\x09\x47\x5d\x5b\x48'\
b'\x4b\x51\x49\x4f\x57\x47\x57\x47\x49\x40\x4b\x3d\x5b\x46\x5b'\
b'\x48\x1b\x4a\x5a\x58\x3d\x58\x41\x52\x44\x52\x47\x50\x47\x50'\
b'\x42\x55\x41\x55\x3d\x55\x39\x4c\x39\x4c\x36\x58\x36\x58\x3d'\
b'\x20\x52\x54\x4f\x54\x50\x52\x52\x51\x52\x4f\x52\x4e\x50\x4e'\
b'\x4f\x4e\x4e\x50\x4c\x51\x4c\x52\x4c\x54\x4e\x54\x4f\x42\x3d'\
b'\x67\x65\x45\x65\x4b\x60\x53\x5b\x53\x59\x53\x56\x50\x56\x4d'\
b'\x56\x4d\x53\x53\x4f\x53\x4c\x53\x49\x4e\x49\x4a\x49\x45\x4f'\
b'\x3d\x53\x3d\x56\x3d\x57\x3f\x58\x3f\x58\x3e\x5b\x3e\x59\x48'\
b'\x59\x4a\x59\x4d\x5a\x50\x5d\x50\x5f\x50\x61\x4a\x61\x46\x61'\
b'\x40\x5a\x36\x52\x36\x4b\x36\x42\x41\x42\x48\x42\x4f\x4b\x59'\
b'\x52\x59\x55\x59\x58\x58\x58\x5b\x56\x5c\x52\x5c\x49\x5c\x3f'\
b'\x50\x3f\x48\x3f\x40\x49\x33\x52\x33\x5b\x33\x65\x3e\x65\x45'\
b'\x20\x52\x57\x42\x56\x40\x54\x40\x50\x40\x4d\x47\x4d\x4a\x4d'\
b'\x4d\x4e\x50\x50\x50\x52\x50\x54\x4c\x57\x48\x57\x42\x17\x43'\
b'\x61\x5f\x52\x5b\x52\x5b\x51\x58\x49\x4c\x49\x49\x50\x49\x52'\
b'\x45\x52\x45\x51\x50\x38\x50\x37\x55\x37\x55\x38\x5f\x51\x5f'\
b'\x52\x20\x52\x57\x46\x52\x3a\x52\x39\x52\x39\x52\x3a\x4d\x46'\
b'\x57\x46\x32\x46\x5e\x5c\x4a\x5c\x4e\x58\x50\x55\x52\x4f\x52'\
b'\x4d\x52\x48\x52\x49\x4b\x49\x44\x49\x3c\x48\x37\x4b\x37\x4c'\
b'\x37\x50\x37\x51\x37\x5a\x37\x5a\x3d\x5a\x41\x56\x43\x56\x43'\
b'\x5c\x44\x5c\x4a\x20\x52\x58\x4a\x58\x45\x4f\x45\x4d\x45\x4c'\
b'\x45\x4c\x4b\x4c\x4f\x4d\x4f\x4f\x4f\x54\x4f\x56\x4e\x58\x4d'\
b'\x58\x4a\x20\x52\x56\x3e\x56\x39\x50\x39\x4e\x39\x4c\x3a\x4c'\
b'\x3b\x4c\x42\x4d\x42\x4e\x42\x52\x42\x54\x41\x56\x40\x56\x3e'\
b'\x17\x46\x5e\x5c\x4f\x5c\x52\x59\x53\x56\x53\x4f\x53\x48\x4b'\
b'\x48\x45\x48\x3f\x50\x36\x57\x36\x59\x36\x5b\x37\x5a\x3a\x58'\
b'\x39\x56\x39\x51\x39\x4c\x40\x4c\x44\x4c\x49\x52\x50\x57\x50'\
b'\x59\x50\x5c\x4f\x21\x45\x5f\x5d\x43\x5d\x49\x55\x52\x4e\x52'\
b'\x4c\x52\x47\x52\x48\x4b\x48\x44\x48\x3c\x47\x37\x4a\x37\x4a'\
b'\x37\x4e\x37\x4e\x37\x56\x37\x5d\x3e\x5d\x43\x20\x52\x59\x44'\
b'\x59\x40\x53\x39\x4d\x39\x4c\x39\x4b\x3a\x4b\x3e\x4b\x44\x4b'\
b'\x49\x4b\x4f\x4d\x4f\x4e\x4f\x54\x4f\x59\x49\x59\x44\x16\x47'\
b'\x5d\x5b\x4f\x5a\x52\x49\x52\x4a\x4b\x4a\x44\x4a\x3c\x49\x37'\
b'\x59\x37\x59\x3a\x53\x3a\x4d\x3a\x4d\x3d\x4d\x42\x53\x42\x57'\
b'\x42\x57\x45\x52\x45\x4d\x45\x4d\x4a\x4d\x4f\x54\x4f\x5b\x4f'\
b'\x13\x48\x5c\x5a\x37\x5a\x3a\x54\x3a\x4d\x3a\x4e\x3d\x4e\x43'\
b'\x52\x43\x57\x43\x57\x46\x53\x46\x4e\x46\x4e\x4e\x4e\x52\x4a'\
b'\x52\x4a\x4b\x4a\x44\x4a\x3c\x4a\x37\x5a\x37\x1f\x45\x5f\x5d'\
b'\x51\x59\x53\x56\x53\x4f\x53\x47\x4b\x47\x45\x47\x3f\x4f\x36'\
b'\x56\x36\x59\x36\x5b\x37\x5b\x3a\x57\x3a\x55\x3a\x50\x3a\x4b'\
b'\x40\x4b\x44\x4b\x49\x51\x50\x57\x50\x58\x50\x5a\x4f\x59\x4d'\
b'\x59\x4a\x59\x48\x59\x46\x5d\x46\x5d\x48\x5d\x4b\x5d\x4d\x5d'\
b'\x51\x17\x46\x5e\x5c\x52\x58\x52\x58\x4b\x58\x45\x4c\x45\x4c'\
b'\x4a\x4c\x52\x48\x52\x48\x4a\x48\x44\x48\x3d\x48\x37\x4c\x37'\
b'\x4c\x3d\x4c\x42\x58\x42\x58\x3e\x58\x37\x5c\x37\x5c\x3d\x5c'\
b'\x44\x5c\x4b\x5c\x52\x0b\x4e\x56\x54\x52\x50\x52\x50\x4b\x50'\
b'\x44\x50\x3c\x50\x37\x54\x37\x54\x3c\x54\x44\x54\x4b\x54\x52'\
b'\x16\x49\x5b\x59\x37\x59\x3a\x59\x42\x59\x46\x59\x4a\x58\x4e'\
b'\x55\x51\x51\x53\x4f\x53\x4d\x53\x4b\x52\x4b\x4f\x4d\x50\x4e'\
b'\x50\x50\x50\x53\x4f\x55\x4d\x55\x49\x55\x47\x55\x3d\x55\x37'\
b'\x59\x37\x20\x45\x5f\x5d\x52\x58\x52\x58\x52\x56\x4e\x53\x4a'\
b'\x50\x48\x4d\x44\x4c\x44\x4b\x44\x4b\x49\x4b\x52\x47\x52\x48'\
b'\x4b\x48\x44\x48\x3c\x47\x37\x4b\x37\x4b\x3c\x4b\x42\x4c\x42'\
b'\x4d\x42\x56\x37\x56\x37\x5a\x37\x5a\x37\x51\x40\x4f\x42\x4f'\
b'\x42\x52\x43\x57\x4b\x5d\x51\x5d\x52\x0e\x48\x5c\x5a\x4f\x5a'\
b'\x52\x4a\x52\x4a\x4d\x4a\x44\x4a\x3c\x4a\x37\x4e\x37\x4d\x3b'\
b'\x4d\x44\x4d\x4b\x4d\x4f\x53\x4f\x5a\x4f\x22\x41\x63\x61\x52'\
b'\x5d\x52\x5d\x4d\x5c\x3c\x5c\x3a\x5c\x3a\x59\x41\x53\x51\x53'\
b'\x52\x50\x52\x50\x51\x4a\x40\x49\x3b\x48\x3a\x48\x3a\x48\x3d'\
b'\x47\x4e\x47\x52\x43\x52\x43\x52\x46\x3b\x46\x37\x4b\x37\x4b'\
b'\x39\x52\x4b\x52\x4d\x52\x4d\x52\x4b\x5a\x39\x5a\x37\x5f\x37'\
b'\x5f\x3b\x61\x52\x61\x52\x1f\x45\x5f\x5d\x52\x5a\x52\x5a\x52'\
b'\x53\x48\x4c\x3e\x4b\x3b\x4a\x3b\x4b\x40\x4b\x44\x4b\x4b\x4b'\
b'\x52\x47\x52\x48\x4b\x48\x44\x48\x3c\x47\x37\x4b\x37\x4b\x37'\
b'\x52\x40\x58\x4a\x59\x4d\x5a\x4d\x59\x47\x59\x44\x59\x3c\x59'\
b'\x37\x5d\x37\x5c\x3c\x5c\x44\x5c\x4b\x5d\x52\x1b\x43\x61\x5f'\
b'\x44\x5f\x4b\x57\x53\x52\x53\x4d\x53\x45\x4b\x45\x45\x45\x3e'\
b'\x4d\x36\x52\x36\x57\x36\x5f\x3e\x5f\x44\x20\x52\x5b\x44\x5b'\
b'\x3f\x55\x39\x52\x39\x4e\x39\x49\x3f\x49\x45\x49\x4a\x4f\x50'\
b'\x52\x50\x56\x50\x5b\x4a\x5b\x44\x20\x47\x5d\x5b\x3d\x5b\x42'\
b'\x54\x47\x4e\x47\x4d\x47\x4c\x47\x4c\x4c\x4d\x52\x49\x52\x49'\
b'\x4c\x49\x44\x49\x3c\x49\x37\x4c\x37\x4c\x37\x51\x37\x52\x37'\
b'\x56\x37\x5b\x3a\x5b\x3d\x20\x52\x58\x3f\x58\x39\x50\x39\x4f'\
b'\x39\x4c\x3a\x4c\x3d\x4c\x44\x4d\x44\x4e\x44\x58\x44\x58\x3f'\
b'\x2d\x43\x61\x5f\x5b\x5b\x5b\x5a\x56\x58\x54\x57\x53\x51\x53'\
b'\x4c\x53\x49\x4f\x45\x4b\x45\x45\x45\x3e\x49\x3a\x4d\x36\x52'\
b'\x36\x57\x36\x5a\x3a\x5e\x3d\x5e\x44\x5e\x49\x5c\x4c\x5a\x50'\
b'\x57\x51\x57\x51\x5b\x52\x5c\x54\x5e\x56\x5f\x5b\x20\x52\x5b'\
b'\x44\x5b\x3f\x58\x3c\x55\x39\x51\x39\x4e\x39\x4b\x3c\x49\x3f'\
b'\x49\x45\x49\x4a\x4c\x4d\x4e\x50\x52\x50\x55\x50\x58\x4d\x5b'\
b'\x4a\x5b\x44\x2a\x46\x5e\x5c\x52\x58\x52\x56\x4c\x55\x4a\x54'\
b'\x48\x53\x47\x52\x46\x4e\x46\x4d\x46\x4b\x46\x4b\x4d\x4c\x52'\
b'\x48\x52\x48\x4b\x48\x44\x48\x3c\x48\x37\x4b\x37\x4c\x37\x4e'\
b'\x37\x50\x37\x5a\x37\x5a\x3d\x5a\x42\x54\x44\x54\x45\x57\x45'\
b'\x58\x48\x59\x4a\x5c\x52\x20\x52\x56\x3e\x56\x39\x4f\x39\x4d'\
b'\x39\x4b\x3a\x4b\x3d\x4b\x44\x4d\x44\x4e\x44\x56\x44\x56\x3e'\
b'\x25\x47\x5d\x5b\x4b\x5b\x53\x50\x53\x4c\x53\x49\x52\x4a\x4e'\
b'\x4d\x50\x51\x50\x58\x50\x58\x4c\x58\x4a\x56\x48\x55\x47\x51'\
b'\x46\x4d\x44\x4c\x43\x49\x41\x49\x3e\x49\x3a\x4c\x39\x4e\x36'\
b'\x52\x36\x57\x36\x59\x37\x59\x3a\x56\x39\x52\x39\x4d\x39\x4d'\
b'\x3d\x4d\x3f\x4e\x40\x4f\x41\x53\x42\x57\x44\x58\x45\x5b\x48'\
b'\x5b\x4b\x11\x46\x5e\x5c\x37\x5c\x3a\x58\x39\x54\x39\x54\x3d'\
b'\x54\x44\x54\x4a\x54\x52\x50\x52\x50\x4b\x50\x44\x50\x3e\x50'\
b'\x39\x4d\x39\x48\x3a\x48\x37\x5c\x37\x1f\x45\x5f\x5d\x37\x5d'\
b'\x3b\x5d\x42\x5d\x45\x5d\x53\x52\x53\x4f\x53\x4b\x51\x48\x4d'\
b'\x47\x48\x47\x45\x47\x42\x47\x3b\x47\x37\x4b\x37\x4b\x3f\x4b'\
b'\x43\x4b\x47\x4b\x4b\x4d\x4f\x50\x50\x52\x50\x54\x50\x57\x4f'\
b'\x59\x4c\x5a\x47\x5a\x43\x5a\x41\x59\x3b\x59\x37\x5d\x37\x11'\
b'\x44\x60\x5e\x37\x5e\x38\x53\x50\x53\x52\x50\x52\x50\x50\x46'\
b'\x38\x46\x37\x4a\x37\x4a\x38\x52\x4c\x52\x4e\x52\x4e\x52\x4c'\
b'\x5a\x39\x5a\x37\x5e\x37\x23\x3d\x67\x65\x37\x65\x38\x5c\x51'\
b'\x5c\x52\x59\x52\x59\x50\x56\x47\x52\x3e\x52\x3b\x51\x3b\x51'\
b'\x3e\x4e\x48\x4b\x51\x4b\x52\x48\x52\x48\x50\x3f\x37\x3f\x37'\
b'\x43\x37\x43\x38\x4a\x4c\x4a\x4e\x4a\x4e\x4a\x4b\x50\x38\x50'\
b'\x37\x54\x37\x54\x38\x5b\x4d\x5b\x4e\x5b\x4e\x5b\x4c\x61\x39'\
b'\x61\x37\x65\x37\x28\x44\x60\x5e\x52\x59\x52\x59\x51\x56\x4c'\
b'\x53\x47\x52\x45\x51\x45\x50\x47\x4d\x4c\x4b\x51\x4b\x52\x46'\
b'\x52\x46\x51\x4b\x4b\x4f\x44\x50\x43\x50\x43\x4f\x42\x4b\x3d'\
b'\x48\x37\x48\x37\x4c\x37\x4c\x37\x4f\x3c\x51\x40\x52\x41\x53'\
b'\x41\x54\x40\x58\x37\x58\x37\x5d\x37\x5d\x37\x59\x3c\x55\x41'\
b'\x54\x43\x54\x43\x55\x45\x5a\x4b\x5e\x51\x5e\x52\x1b\x45\x5f'\
b'\x5d\x37\x5d\x37\x5b\x3b\x57\x41\x56\x42\x53\x47\x53\x49\x53'\
b'\x4d\x54\x52\x50\x52\x50\x4e\x50\x49\x50\x47\x4e\x42\x4c\x40'\
b'\x49\x3b\x47\x37\x47\x37\x4b\x37\x4b\x37\x52\x44\x52\x45\x52'\
b'\x45\x52\x43\x59\x38\x59\x37\x5d\x37\x15\x47\x5d\x5b\x4e\x5b'\
b'\x52\x49\x52\x49\x4f\x4c\x4c\x51\x44\x56\x3b\x56\x3a\x56\x39'\
b'\x52\x39\x49\x3a\x49\x37\x5a\x37\x5a\x39\x58\x3d\x53\x45\x4e'\
b'\x4e\x4e\x4f\x4e\x4f\x52\x4f\x5b\x4e\x11\x4b\x59\x57\x59\x57'\
b'\x5c\x4d\x5c\x4d\x4e\x4d\x48\x4d\x44\x4d\x32\x57\x32\x57\x36'\
b'\x52\x36\x51\x36\x50\x44\x50\x48\x50\x4b\x51\x59\x52\x59\x57'\
b'\x59\x09\x4b\x59\x57\x58\x54\x58\x54\x55\x4d\x35\x4d\x33\x50'\
b'\x33\x50\x37\x57\x57\x57\x58\x11\x4b\x59\x57\x5c\x4d\x5c\x4d'\
b'\x59\x52\x59\x53\x59\x54\x4a\x54\x46\x54\x43\x53\x35\x52\x35'\
b'\x4d\x36\x4d\x32\x57\x32\x57\x41\x57\x46\x57\x4a\x57\x5c\x09'\
b'\x46\x5e\x5c\x44\x5a\x45\x52\x38\x52\x38\x4a\x45\x48\x44\x51'\
b'\x34\x53\x34\x5c\x44\x05\x45\x5f\x5d\x5d\x47\x5d\x47\x5a\x5d'\
b'\x5a\x5d\x5d\x09\x4c\x58\x56\x3b\x54\x3b\x54\x3b\x4e\x35\x4e'\
b'\x34\x52\x34\x52\x35\x56\x3b\x56\x3b\x2b\x48\x5c\x5a\x52\x57'\
b'\x52\x57\x51\x57\x50\x57\x50\x54\x53\x50\x53\x4d\x53\x4a\x50'\
b'\x4a\x4d\x4a\x4a\x4f\x46\x57\x46\x57\x45\x57\x45\x57\x42\x54'\
b'\x40\x51\x40\x4e\x40\x4b\x41\x4b\x3e\x4e\x3d\x52\x3d\x56\x3d'\
b'\x5a\x40\x5a\x44\x5a\x45\x5a\x4a\x5a\x4b\x5a\x4f\x5a\x52\x20'\
b'\x52\x57\x4e\x57\x4b\x57\x48\x53\x48\x51\x49\x4d\x4a\x4d\x4d'\
b'\x4d\x50\x51\x50\x55\x50\x57\x4e\x24\x46\x5e\x5c\x47\x5c\x4c'\
b'\x56\x53\x52\x53\x4e\x53\x4d\x51\x4c\x51\x4c\x52\x49\x52\x49'\
b'\x4b\x49\x42\x49\x3b\x48\x34\x4d\x34\x4c\x38\x4c\x40\x4c\x40'\
b'\x4f\x3d\x53\x3d\x57\x3d\x5c\x43\x5c\x47\x20\x52\x58\x48\x58'\
b'\x45\x55\x40\x52\x40\x4e\x40\x4c\x42\x4c\x4a\x4d\x4f\x4e\x50'\
b'\x51\x50\x54\x50\x58\x4b\x58\x48\x17\x48\x5c\x5a\x4f\x5a\x52'\
b'\x58\x53\x55\x53\x50\x53\x4a\x4d\x4a\x48\x4a\x44\x50\x3d\x55'\
b'\x3d\x58\x3d\x59\x3e\x59\x41\x56\x40\x54\x40\x51\x40\x4e\x45'\
b'\x4e\x48\x4e\x4b\x52\x50\x56\x50\x57\x50\x5a\x4f\x25\x47\x5d'\
b'\x5b\x52\x58\x52\x58\x51\x58\x50\x58\x50\x56\x53\x51\x53\x4d'\
b'\x53\x49\x4d\x49\x49\x49\x44\x4e\x3d\x53\x3d\x56\x3d\x57\x3f'\
b'\x58\x3f\x58\x3a\x57\x35\x5b\x34\x5b\x3a\x5b\x42\x5b\x4b\x5b'\
b'\x52\x20\x52\x58\x4e\x58\x47\x58\x41\x56\x40\x53\x40\x50\x40'\
b'\x4c\x45\x4c\x48\x4c\x4b\x50\x50\x53\x50\x56\x50\x58\x4e\x1c'\
b'\x47\x5d\x5b\x46\x5b\x47\x5b\x48\x4c\x48\x4d\x4b\x51\x50\x55'\
b'\x50\x58\x50\x5b\x4f\x5a\x52\x58\x53\x54\x53\x4f\x53\x49\x4d'\
b'\x49\x48\x49\x44\x4e\x3d\x53\x3d\x57\x3d\x5b\x42\x5b\x46\x20'\
b'\x52\x57\x46\x57\x40\x53\x40\x4d\x40\x4d\x46\x57\x46\x1b\x49'\
b'\x5b\x59\x34\x58\x37\x57\x37\x56\x37\x54\x37\x53\x3a\x53\x3e'\
b'\x55\x3e\x58\x3e\x58\x41\x54\x41\x53\x41\x53\x4b\x53\x52\x4f'\
b'\x52\x4f\x4b\x4f\x41\x4e\x41\x4b\x41\x4b\x3e\x4e\x3e\x4f\x3e'\
b'\x4f\x39\x53\x34\x56\x34\x57\x34\x59\x34\x4c\x45\x5f\x5d\x3b'\
b'\x5c\x3e\x58\x3e\x58\x40\x58\x40\x59\x41\x59\x44\x59\x47\x55'\
b'\x4b\x50\x4b\x4e\x4b\x4d\x4b\x4c\x4b\x4c\x4c\x4c\x4e\x4d\x4e'\
b'\x4f\x4f\x54\x4f\x5c\x4f\x5c\x54\x5c\x58\x56\x5d\x51\x5d\x4c'\
b'\x5d\x47\x59\x47\x57\x47\x54\x4a\x51\x4b\x51\x4b\x51\x49\x50'\
b'\x49\x4e\x49\x4c\x4c\x4a\x4c\x4a\x4a\x49\x48\x47\x48\x45\x48'\
b'\x42\x4d\x3d\x51\x3d\x54\x3d\x56\x3f\x57\x3f\x57\x3b\x5a\x3b'\
b'\x5c\x3b\x5d\x3b\x20\x52\x59\x56\x59\x54\x56\x52\x52\x52\x4f'\
b'\x52\x4d\x52\x4a\x53\x4a\x55\x4a\x5a\x51\x5a\x55\x5a\x59\x58'\
b'\x59\x56\x20\x52\x56\x44\x56\x42\x53\x40\x51\x40\x4f\x40\x4c'\
b'\x42\x4c\x44\x4c\x46\x4f\x49\x51\x49\x53\x49\x56\x47\x56\x44'\
b'\x1e\x47\x5d\x5b\x52\x57\x52\x58\x4c\x58\x46\x58\x43\x55\x40'\
b'\x53\x40\x50\x40\x4d\x43\x4d\x4e\x4d\x52\x49\x52\x4a\x4c\x4a'\
b'\x42\x4a\x3a\x49\x34\x4d\x34\x4d\x3b\x4d\x40\x4d\x40\x50\x3d'\
b'\x54\x3d\x57\x3d\x5b\x41\x5b\x44\x5b\x45\x5b\x47\x5b\x48\x5b'\
b'\x4b\x5b\x52\x19\x4d\x57\x54\x52\x50\x52\x50\x4e\x50\x48\x50'\
b'\x42\x4f\x3e\x54\x3e\x53\x42\x53\x48\x53\x4d\x54\x52\x20\x52'\
b'\x55\x38\x55\x39\x53\x3a\x52\x3a\x51\x3a\x50\x39\x50\x38\x50'\
b'\x37\x51\x36\x52\x36\x53\x36\x55\x37\x55\x38\x1e\x4c\x58\x55'\
b'\x3e\x54\x44\x54\x4b\x54\x4c\x55\x52\x55\x53\x55\x5a\x4f\x5b'\
b'\x4e\x5a\x50\x58\x51\x56\x51\x54\x51\x4c\x51\x43\x51\x3e\x55'\
b'\x3e\x20\x52\x56\x38\x56\x39\x54\x3a\x53\x3a\x52\x3a\x51\x39'\
b'\x51\x38\x51\x37\x52\x36\x53\x36\x54\x36\x56\x37\x56\x38\x1f'\
b'\x47\x5d\x5b\x52\x56\x52\x56\x51\x52\x4c\x4e\x47\x4d\x47\x4d'\
b'\x47\x4d\x4c\x4d\x52\x49\x52\x4a\x4a\x4a\x42\x4a\x3a\x49\x34'\
b'\x4d\x34\x4d\x39\x4d\x46\x4d\x46\x4e\x46\x55\x3f\x55\x3e\x59'\
b'\x3e\x59\x3f\x56\x42\x53\x44\x51\x46\x51\x46\x53\x48\x57\x4d'\
b'\x5b\x51\x5b\x52\x0b\x4e\x56\x54\x52\x50\x52\x50\x4b\x50\x42'\
b'\x50\x3a\x50\x34\x54\x34\x54\x3a\x54\x42\x54\x4b\x54\x52\x2e'\
b'\x41\x63\x5e\x46\x5e\x43\x5c\x40\x59\x40\x57\x40\x54\x43\x54'\
b'\x45\x54\x48\x54\x4b\x54\x52\x50\x52\x51\x4c\x51\x46\x51\x43'\
b'\x4f\x40\x4c\x40\x49\x40\x47\x43\x47\x49\x47\x52\x43\x52\x44'\
b'\x4b\x44\x48\x44\x43\x43\x3e\x47\x3e\x47\x40\x47\x40\x4a\x3d'\
b'\x4d\x3d\x52\x3d\x54\x40\x54\x40\x57\x3d\x5a\x3d\x5e\x3d\x61'\
b'\x40\x61\x44\x61\x45\x61\x47\x61\x48\x61\x4b\x61\x52\x5d\x52'\
b'\x5e\x4d\x5e\x46\x1d\x47\x5d\x5b\x52\x57\x52\x58\x4c\x58\x46'\
b'\x58\x43\x55\x40\x53\x40\x50\x40\x4d\x43\x4d\x4a\x4d\x52\x49'\
b'\x52\x4a\x4b\x4a\x48\x4a\x43\x49\x3e\x4d\x3e\x4d\x40\x4d\x40'\
b'\x50\x3d\x54\x3d\x57\x3d\x5b\x40\x5b\x44\x5b\x45\x5b\x47\x5b'\
b'\x48\x5b\x4b\x5b\x52\x1b\x46\x5e\x5c\x47\x5c\x4d\x56\x53\x52'\
b'\x53\x4e\x53\x48\x4d\x48\x49\x48\x43\x4e\x3d\x52\x3d\x56\x3d'\
b'\x5c\x43\x5c\x47\x20\x52\x58\x48\x58\x45\x55\x40\x52\x40\x4f'\
b'\x40\x4c\x45\x4c\x48\x4c\x4b\x4f\x50\x52\x50\x55\x50\x58\x4b'\
b'\x58\x48\x24\x46\x5e\x5c\x47\x5c\x4c\x57\x53\x52\x53\x4e\x53'\
b'\x4d\x51\x4d\x51\x4d\x57\x4d\x5c\x49\x5c\x49\x56\x49\x4e\x49'\
b'\x44\x48\x3e\x4c\x3e\x4c\x40\x4c\x40\x4f\x3d\x53\x3d\x57\x3d'\
b'\x5c\x43\x5c\x47\x20\x52\x58\x48\x58\x45\x55\x40\x52\x40\x4e'\
b'\x40\x4c\x42\x4d\x4a\x4d\x4f\x4e\x50\x51\x50\x55\x50\x58\x4b'\
b'\x58\x48\x24\x46\x5e\x5c\x5c\x58\x5c\x58\x56\x58\x50\x58\x50'\
b'\x56\x53\x51\x53\x4d\x53\x48\x4d\x48\x49\x48\x44\x4e\x3d\x52'\
b'\x3d\x56\x3d\x58\x3f\x58\x3f\x59\x3e\x5c\x3e\x5b\x45\x5b\x4c'\
b'\x5b\x54\x5c\x5c\x20\x52\x58\x4d\x58\x46\x58\x41\x56\x40\x53'\
b'\x40\x50\x40\x4c\x45\x4c\x48\x4c\x4b\x4f\x50\x52\x50\x56\x50'\
b'\x58\x4d\x15\x49\x5b\x59\x3e\x58\x41\x56\x41\x55\x41\x51\x41'\
b'\x50\x45\x50\x4e\x50\x52\x4c\x52\x4c\x4b\x4c\x48\x4c\x43\x4b'\
b'\x3e\x4f\x3e\x4f\x40\x4f\x41\x50\x41\x52\x3d\x55\x3d\x56\x3d'\
b'\x59\x3e\x22\x49\x5b\x59\x4c\x59\x52\x51\x52\x4e\x52\x4b\x52'\
b'\x4c\x4f\x4e\x50\x51\x50\x56\x50\x56\x4d\x56\x4c\x54\x4a\x52'\
b'\x49\x4f\x48\x4d\x47\x4b\x46\x4b\x43\x4b\x41\x4f\x3d\x53\x3d'\
b'\x56\x3d\x58\x3e\x58\x41\x55\x40\x53\x40\x4e\x40\x4e\x43\x4e'\
b'\x44\x50\x45\x53\x46\x56\x47\x57\x48\x59\x4a\x59\x4c\x1f\x49'\
b'\x5b\x59\x4f\x58\x52\x57\x52\x55\x52\x52\x52\x4f\x4f\x4f\x4a'\
b'\x4f\x46\x4f\x41\x4e\x41\x4b\x41\x4b\x3e\x4d\x3e\x4f\x3e\x4f'\
b'\x3d\x4f\x39\x53\x38\x52\x3d\x52\x3e\x54\x3e\x58\x3e\x58\x41'\
b'\x54\x41\x52\x41\x52\x44\x52\x48\x52\x4d\x54\x50\x56\x50\x57'\
b'\x50\x59\x4f\x1e\x47\x5d\x5b\x52\x58\x52\x57\x51\x57\x50\x57'\
b'\x50\x54\x53\x50\x53\x4d\x53\x49\x4f\x49\x4a\x49\x49\x49\x46'\
b'\x49\x45\x49\x42\x49\x3e\x4d\x3e\x4d\x42\x4d\x45\x4d\x4c\x4e'\
b'\x50\x51\x50\x55\x50\x57\x4e\x57\x42\x57\x3e\x5b\x3e\x5a\x42'\
b'\x5a\x49\x5a\x4d\x5b\x52\x11\x47\x5d\x5b\x3e\x5b\x3f\x53\x51'\
b'\x53\x52\x50\x52\x50\x51\x49\x3f\x49\x3e\x4d\x3e\x4d\x3f\x52'\
b'\x4d\x52\x4e\x52\x4e\x52\x4d\x57\x40\x57\x3e\x5b\x3e\x23\x40'\
b'\x64\x62\x3e\x62\x3f\x5a\x51\x5a\x52\x57\x52\x57\x51\x55\x4c'\
b'\x53\x45\x52\x42\x52\x42\x51\x45\x4e\x4c\x4c\x51\x4c\x52\x49'\
b'\x52\x49\x51\x42\x3f\x42\x3e\x46\x3e\x46\x3f\x4b\x4d\x4b\x4e'\
b'\x4b\x4e\x4b\x4c\x50\x3f\x50\x3e\x54\x3e\x54\x3f\x59\x4d\x59'\
b'\x4e\x59\x4e\x59\x4d\x5e\x40\x5e\x3e\x62\x3e\x21\x46\x5e\x5c'\
b'\x52\x57\x52\x57\x51\x53\x4b\x52\x49\x51\x49\x50\x4b\x4d\x51'\
b'\x4d\x52\x48\x52\x48\x51\x4e\x49\x50\x47\x50\x47\x4f\x46\x49'\
b'\x3e\x49\x3e\x4e\x3e\x4e\x3f\x51\x44\x52\x45\x52\x45\x53\x44'\
b'\x57\x3f\x57\x3e\x5b\x3e\x5b\x3e\x55\x46\x54\x47\x54\x47\x56'\
b'\x49\x5c\x52\x5c\x52\x19\x47\x5d\x5b\x3e\x5b\x3f\x58\x47\x54'\
b'\x4f\x53\x52\x52\x58\x51\x59\x4f\x5b\x4b\x5b\x4b\x58\x4d\x58'\
b'\x51\x55\x51\x52\x51\x50\x49\x3e\x49\x3e\x4d\x3e\x4d\x3f\x53'\
b'\x4d\x53\x4e\x53\x4e\x53\x4d\x57\x40\x57\x3e\x5b\x3e\x15\x48'\
b'\x5c\x5a\x4f\x5a\x52\x4a\x52\x4a\x4f\x4c\x4e\x50\x48\x55\x42'\
b'\x55\x41\x55\x41\x4e\x41\x4a\x41\x4b\x3e\x59\x3e\x59\x41\x57'\
b'\x43\x53\x48\x4f\x4e\x4f\x4f\x4f\x4f\x55\x4f\x5a\x4f\x23\x49'\
b'\x5b\x59\x5a\x57\x5c\x4e\x5a\x4e\x56\x4e\x54\x50\x4d\x50\x4c'\
b'\x50\x49\x4b\x49\x4b\x46\x50\x45\x50\x42\x50\x41\x4e\x3b\x4e'\
b'\x39\x4e\x33\x58\x32\x59\x35\x52\x36\x52\x3a\x52\x3c\x54\x42'\
b'\x54\x42\x54\x45\x50\x47\x4f\x47\x4f\x47\x50\x47\x54\x4a\x54'\
b'\x4c\x54\x4d\x52\x53\x52\x54\x52\x58\x59\x5a\x0b\x4e\x56\x54'\
b'\x5d\x50\x5d\x50\x55\x50\x48\x50\x3b\x50\x31\x54\x31\x54\x3a'\
b'\x54\x48\x54\x56\x54\x5d\x23\x49\x5b\x59\x49\x54\x49\x54\x4c'\
b'\x54\x4d\x56\x54\x56\x55\x56\x5b\x4c\x5c\x4b\x5a\x52\x59\x52'\
b'\x54\x52\x53\x50\x4d\x50\x4c\x50\x4a\x54\x47\x55\x47\x55\x47'\
b'\x54\x47\x50\x45\x50\x42\x50\x42\x52\x3b\x52\x3a\x52\x36\x4b'\
b'\x35\x4d\x32\x56\x34\x56\x39\x56\x3a\x54\x41\x54\x42\x54\x45'\
b'\x59\x46\x59\x49\x11\x45\x5f\x5d\x45\x5a\x4a\x56\x4a\x54\x4a'\
b'\x4f\x48\x4e\x48\x4c\x48\x49\x4b\x47\x4a\x4a\x45\x4e\x45\x50'\
b'\x45\x55\x46\x56\x46\x59\x46\x5b\x44\x5d\x45\x36\x46\x5e\x5c'\
b'\x37\x5c\x52\x48\x52\x48\x37\x5c\x37\x20\x52\x5a\x50\x5a\x38'\
b'\x4a\x38\x4a\x50\x5a\x50\x20\x52\x51\x49\x51\x48\x51\x46\x52'\
b'\x44\x53\x43\x54\x42\x55\x41\x55\x40\x55\x3f\x53\x3d\x52\x3d'\
b'\x51\x3d\x4f\x3e\x4f\x40\x4d\x40\x4d\x3d\x50\x3b\x52\x3b\x54'\
b'\x3b\x57\x3d\x57\x40\x57\x41\x56\x43\x54\x44\x53\x46\x53\x47'\
b'\x53\x49\x51\x49\x20\x52\x50\x4c\x50\x4c\x51\x4b\x52\x4b\x52'\
b'\x4b\x53\x4c\x53\x4c\x53\x4d\x52\x4e\x52\x4e\x51\x4e\x50\x4d'\
b'\x50\x4c'

_index =\
b'\x00\x00\x03\x00\x36\x00\x67\x00\xd8\x00\x41\x01\xc6\x01\x55'\
b'\x02\x6e\x02\x99\x02\xc2\x02\x23\x03\x40\x03\x67\x03\x74\x03'\
b'\x91\x03\xa6\x03\xdf\x03\xfe\x03\x2f\x04\x72\x04\xaf\x04\xde'\
b'\x04\x21\x05\x48\x05\xaf\x05\xf0\x05\x29\x06\x6c\x06\x81\x06'\
b'\x9a\x06\xaf\x06\xe8\x06\x6f\x07\xa0\x07\x07\x08\x38\x08\x7d'\
b'\x08\xac\x08\xd5\x08\x16\x09\x47\x09\x60\x09\x8f\x09\xd2\x09'\
b'\xf1\x09\x38\x0a\x79\x0a\xb2\x0a\xf5\x0a\x52\x0b\xa9\x0b\xf6'\
b'\x0b\x1b\x0c\x5c\x0c\x81\x0c\xca\x0c\x1d\x0d\x56\x0d\x83\x0d'\
b'\xa8\x0d\xbd\x0d\xe2\x0d\xf7\x0d\x04\x0e\x19\x0e\x72\x0e\xbd'\
b'\x0e\xee\x0e\x3b\x0f\x76\x0f\xaf\x0f\x4a\x10\x89\x10\xbe\x10'\
b'\xfd\x10\x3e\x11\x57\x11\xb6\x11\xf3\x11\x2c\x12\x77\x12\xc2'\
b'\x12\xef\x12\x36\x13\x77\x13\xb6\x13\xdb\x13\x24\x14\x69\x14'\
b'\x9e\x14\xcb\x14\x14\x15\x2d\x15\x76\x15\x9b\x15'

FONT = memoryview(_font)
INDEX = memoryview(_index)

