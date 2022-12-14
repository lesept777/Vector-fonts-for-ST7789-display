FIRST = 32
LAST = 127
WIDTH = 33
HEIGHT = 36

_font =\
b'\x01\x4e\x56\x1b\x4c\x58\x52\x4b\x50\x4b\x53\x39\x56\x39\x52'\
b'\x4b\x20\x52\x52\x50\x52\x51\x51\x51\x51\x52\x50\x52\x50\x52'\
b'\x4f\x52\x4f\x52\x4e\x51\x4e\x51\x4e\x50\x4e\x50\x4e\x4f\x4f'\
b'\x4f\x4f\x4e\x50\x4e\x50\x4e\x51\x4f\x51\x4f\x52\x50\x52\x50'\
b'\x0b\x4c\x58\x56\x41\x53\x41\x53\x39\x56\x39\x56\x41\x20\x52'\
b'\x51\x41\x4e\x41\x4e\x39\x51\x39\x51\x41\x23\x46\x5e\x5c\x42'\
b'\x57\x42\x56\x47\x5b\x47\x5a\x49\x56\x49\x54\x50\x52\x50\x53'\
b'\x49\x4f\x49\x4d\x50\x4b\x50\x4d\x49\x48\x49\x48\x47\x4d\x47'\
b'\x4e\x42\x49\x42\x4a\x40\x4e\x40\x50\x39\x52\x39\x51\x40\x55'\
b'\x40\x57\x39\x59\x39\x57\x40\x5c\x40\x5c\x42\x20\x52\x50\x42'\
b'\x4f\x47\x54\x47\x55\x42\x50\x42\x4b\x47\x5d\x5a\x3c\x5a\x3c'\
b'\x59\x3c\x58\x3b\x56\x3b\x56\x3b\x54\x45\x55\x45\x56\x47\x58'\
b'\x48\x59\x4a\x59\x4b\x59\x4c\x58\x4f\x56\x51\x53\x52\x51\x52'\
b'\x50\x56\x4e\x56\x4f\x52\x4e\x52\x4d\x52\x4b\x52\x4a\x51\x49'\
b'\x51\x4a\x4e\x4a\x4e\x4c\x4f\x4d\x4f\x4f\x50\x4f\x50\x51\x47'\
b'\x50\x46\x4f\x44\x4d\x43\x4c\x41\x4c\x3f\x4c\x3e\x4e\x3b\x50'\
b'\x39\x53\x38\x54\x38\x55\x35\x57\x35\x56\x38\x57\x39\x5a\x39'\
b'\x5b\x3a\x5a\x3c\x20\x52\x54\x3b\x53\x3b\x51\x3c\x50\x3d\x4f'\
b'\x3e\x4f\x3f\x4f\x40\x50\x41\x51\x42\x51\x43\x52\x43\x54\x3b'\
b'\x20\x52\x56\x4c\x56\x4b\x55\x4a\x55\x49\x54\x48\x53\x48\x51'\
b'\x50\x52\x50\x54\x4f\x55\x4e\x56\x4c\x56\x4c\x61\x43\x61\x5f'\
b'\x4a\x5f\x4c\x5e\x4f\x5c\x51\x59\x52\x58\x52\x56\x52\x54\x51'\
b'\x53\x50\x53\x4e\x53\x4d\x53\x4c\x54\x49\x55\x47\x58\x45\x5a'\
b'\x45\x5b\x45\x5d\x46\x5e\x47\x5f\x49\x5f\x4a\x20\x52\x48\x52'\
b'\x46\x52\x5c\x39\x5e\x39\x48\x52\x20\x52\x51\x3d\x51\x3f\x50'\
b'\x42\x4f\x44\x4c\x45\x4b\x45\x4a\x45\x48\x45\x47\x44\x46\x43'\
b'\x46\x42\x45\x41\x45\x40\x45\x3f\x46\x3d\x47\x3c\x48\x3a\x49'\
b'\x39\x4b\x38\x4c\x38\x4e\x38\x4f\x39\x51\x3a\x51\x3c\x51\x3d'\
b'\x20\x52\x5c\x4b\x5c\x4a\x5c\x49\x5b\x48\x5a\x47\x59\x47\x58'\
b'\x47\x57\x48\x56\x4a\x55\x4c\x55\x4d\x55\x4e\x55\x4f\x56\x50'\
b'\x57\x50\x58\x50\x59\x50\x5a\x4f\x5c\x4e\x5c\x4c\x5c\x4b\x20'\
b'\x52\x4f\x3e\x4f\x3d\x4f\x3c\x4e\x3b\x4d\x3a\x4c\x3a\x4b\x3a'\
b'\x4a\x3b\x48\x3d\x48\x3f\x48\x40\x48\x41\x48\x42\x49\x43\x4a'\
b'\x43\x4b\x43\x4c\x43\x4d\x42\x4e\x41\x4f\x3f\x4f\x3e\x6d\x43'\
b'\x61\x5c\x52\x5b\x52\x59\x52\x58\x51\x57\x4f\x56\x4e\x55\x4f'\
b'\x53\x51\x51\x52\x4e\x52\x4c\x52\x4b\x52\x48\x51\x46\x50\x45'\
b'\x4d\x45\x4c\x45\x4a\x46\x48\x48\x45\x4b\x44\x4d\x43\x4c\x43'\
b'\x4b\x42\x4b\x41\x4a\x3f\x4a\x3f\x4a\x3d\x4c\x3b\x4e\x39\x50'\
b'\x38\x52\x38\x53\x38\x55\x39\x57\x3a\x58\x3c\x58\x3d\x58\x3e'\
b'\x57\x40\x55\x42\x53\x43\x52\x44\x53\x44\x54\x46\x56\x47\x57'\
b'\x49\x57\x4a\x5a\x48\x5c\x42\x5c\x3e\x5f\x3e\x5f\x40\x5e\x44'\
b'\x5c\x48\x5a\x4b\x58\x4c\x59\x4d\x59\x4f\x5a\x4f\x5b\x50\x5c'\
b'\x50\x5d\x50\x5e\x4f\x5e\x4f\x5e\x52\x5d\x52\x5c\x52\x5c\x52'\
b'\x20\x52\x4d\x50\x4e\x50\x50\x4f\x52\x4e\x54\x4d\x55\x4c\x55'\
b'\x4a\x53\x48\x52\x47\x50\x45\x4f\x45\x4e\x45\x4b\x46\x49\x48'\
b'\x48\x4a\x48\x4c\x48\x4d\x49\x4e\x4a\x4f\x4b\x50\x4d\x50\x20'\
b'\x52\x55\x3d\x55\x3d\x54\x3c\x54\x3b\x52\x3b\x52\x3b\x51\x3b'\
b'\x4f\x3b\x4e\x3c\x4d\x3e\x4d\x3f\x4d\x40\x4f\x42\x4f\x42\x50'\
b'\x42\x52\x41\x54\x40\x55\x3e\x55\x3d\x05\x4f\x55\x53\x41\x51'\
b'\x41\x51\x39\x53\x39\x53\x41\x17\x4a\x5a\x58\x39\x56\x3b\x52'\
b'\x3f\x50\x44\x4f\x4a\x4f\x4c\x4f\x4e\x4f\x51\x50\x54\x51\x56'\
b'\x51\x57\x4f\x57\x4e\x56\x4d\x53\x4c\x51\x4c\x4e\x4c\x4d\x4c'\
b'\x4a\x4d\x44\x50\x3f\x53\x3b\x55\x39\x58\x39\x17\x4a\x5a\x58'\
b'\x43\x58\x46\x57\x4c\x54\x51\x51\x55\x4f\x57\x4c\x57\x4e\x55'\
b'\x52\x51\x54\x4c\x55\x46\x55\x43\x55\x42\x55\x3f\x54\x3c\x53'\
b'\x3a\x53\x39\x55\x39\x56\x3a\x57\x3d\x58\x3f\x58\x42\x58\x43'\
b'\x10\x4a\x5a\x53\x3f\x57\x44\x55\x45\x52\x40\x4f\x45\x4d\x44'\
b'\x51\x3f\x4c\x3f\x4d\x3c\x51\x3e\x51\x39\x53\x39\x53\x3e\x57'\
b'\x3c\x58\x3f\x53\x3f\x0d\x48\x5c\x53\x49\x53\x50\x51\x50\x51'\
b'\x49\x4a\x49\x4a\x46\x51\x46\x51\x3f\x53\x3f\x53\x46\x5a\x46'\
b'\x5a\x49\x53\x49\x05\x4d\x57\x51\x57\x4f\x57\x52\x4e\x55\x4e'\
b'\x51\x57\x05\x4b\x59\x57\x49\x4d\x49\x4d\x47\x57\x47\x57\x49'\
b'\x15\x4e\x56\x54\x50\x54\x51\x54\x52\x53\x52\x52\x52\x52\x52'\
b'\x52\x52\x51\x52\x50\x52\x50\x51\x50\x50\x50\x50\x50\x4f\x51'\
b'\x4f\x52\x4e\x52\x4e\x52\x4e\x53\x4f\x54\x4f\x54\x50\x54\x50'\
b'\x05\x45\x5f\x4a\x56\x47\x56\x5a\x39\x5d\x39\x4a\x56\x38\x47'\
b'\x5d\x5b\x40\x5b\x41\x5b\x44\x5a\x47\x59\x4a\x58\x4c\x57\x4f'\
b'\x56\x50\x53\x52\x50\x52\x4e\x52\x4c\x51\x4a\x4f\x49\x4c\x49'\
b'\x4a\x49\x48\x4a\x44\x4b\x40\x4d\x3c\x4e\x3b\x50\x3a\x53\x38'\
b'\x55\x38\x56\x38\x58\x39\x5a\x3b\x5b\x3e\x5b\x40\x20\x52\x58'\
b'\x40\x58\x3e\x56\x3b\x54\x3b\x53\x3b\x51\x3c\x51\x3d\x50\x3d'\
b'\x4f\x3f\x4e\x42\x4d\x44\x4c\x47\x4c\x49\x4c\x4a\x4c\x4c\x4d'\
b'\x4e\x4e\x4f\x4f\x50\x50\x50\x51\x50\x53\x4f\x53\x4e\x54\x4d'\
b'\x56\x4a\x57\x46\x58\x42\x58\x40\x07\x4b\x59\x4f\x52\x53\x3c'\
b'\x4d\x3e\x4e\x3b\x57\x38\x52\x52\x4f\x52\x22\x47\x5d\x58\x3e'\
b'\x58\x3d\x56\x3b\x55\x3b\x53\x3b\x4f\x3c\x4e\x3e\x4f\x3a\x50'\
b'\x39\x53\x38\x55\x38\x58\x38\x5b\x3b\x5b\x3e\x5b\x40\x5a\x43'\
b'\x57\x46\x54\x48\x51\x4a\x4e\x4c\x4d\x4e\x4c\x4f\x59\x4f\x58'\
b'\x52\x49\x52\x49\x51\x49\x4f\x4b\x4c\x4e\x49\x52\x46\x54\x45'\
b'\x57\x42\x58\x40\x58\x3e\x41\x47\x5d\x5b\x3e\x5b\x3f\x5a\x41'\
b'\x59\x43\x56\x45\x54\x45\x54\x45\x55\x45\x57\x46\x58\x48\x59'\
b'\x49\x59\x4b\x59\x4c\x58\x4f\x55\x51\x52\x52\x4f\x52\x4e\x52'\
b'\x4d\x52\x4b\x52\x4a\x51\x49\x51\x4a\x4e\x4a\x4f\x4b\x4f\x4d'\
b'\x50\x4f\x50\x4f\x50\x51\x50\x54\x4f\x55\x4e\x56\x4c\x56\x4b'\
b'\x56\x49\x53\x46\x50\x46\x4e\x46\x4e\x44\x50\x44\x52\x44\x55'\
b'\x43\x57\x42\x58\x40\x58\x3e\x58\x3e\x58\x3c\x56\x3b\x55\x3b'\
b'\x54\x3b\x53\x3b\x51\x3b\x50\x3b\x4f\x3c\x4e\x3c\x4f\x39\x4f'\
b'\x39\x50\x39\x52\x38\x53\x38\x54\x38\x56\x38\x59\x39\x5a\x3b'\
b'\x5b\x3d\x5b\x3e\x14\x47\x5d\x5b\x39\x58\x49\x5b\x49\x5b\x4c'\
b'\x57\x4c\x56\x52\x53\x52\x54\x4c\x49\x4c\x49\x4a\x4d\x46\x55'\
b'\x3d\x58\x39\x5b\x39\x20\x52\x55\x49\x58\x3d\x53\x43\x4d\x49'\
b'\x55\x49\x1e\x47\x5d\x5a\x3b\x51\x3b\x4f\x43\x51\x43\x55\x43'\
b'\x59\x46\x59\x49\x59\x4c\x56\x50\x52\x52\x4f\x52\x4d\x52\x4a'\
b'\x52\x49\x51\x4a\x4f\x4b\x4f\x4d\x50\x4f\x50\x51\x50\x54\x4e'\
b'\x56\x4c\x56\x4a\x56\x48\x53\x45\x50\x45\x4e\x45\x4c\x45\x4f'\
b'\x39\x5b\x39\x5a\x3b\x43\x47\x5d\x5a\x3c\x59\x3b\x57\x3b\x56'\
b'\x3b\x55\x3b\x52\x3c\x51\x3d\x50\x3d\x4f\x3f\x4d\x42\x4d\x44'\
b'\x4c\x46\x4c\x46\x4d\x45\x4e\x44\x50\x43\x52\x42\x53\x42\x54'\
b'\x42\x57\x43\x58\x45\x59\x47\x59\x49\x59\x4b\x58\x4e\x56\x51'\
b'\x53\x52\x50\x52\x4f\x52\x4c\x51\x4a\x4f\x49\x4c\x49\x4a\x49'\
b'\x47\x4a\x43\x4c\x3f\x4e\x3c\x4f\x3b\x51\x39\x55\x38\x57\x38'\
b'\x58\x38\x5a\x39\x5b\x39\x5a\x3c\x20\x52\x56\x49\x56\x48\x56'\
b'\x47\x54\x45\x53\x45\x52\x45\x50\x45\x4e\x46\x4d\x47\x4c\x49'\
b'\x4c\x4a\x4c\x4c\x4d\x4e\x4e\x4f\x50\x50\x51\x50\x52\x50\x54'\
b'\x4f\x55\x4d\x56\x4b\x56\x49\x0c\x47\x5d\x4c\x52\x49\x52\x4b'\
b'\x4d\x52\x41\x57\x3b\x4a\x3b\x4b\x39\x5b\x39\x5b\x3a\x55\x41'\
b'\x4e\x4d\x4c\x52\x3a\x47\x5d\x49\x4c\x49\x49\x4c\x45\x4f\x44'\
b'\x4e\x43\x4d\x41\x4d\x3f\x4d\x3d\x4f\x3a\x52\x38\x55\x38\x58'\
b'\x38\x5b\x3b\x5b\x3e\x5b\x40\x59\x43\x56\x44\x58\x45\x5a\x48'\
b'\x5a\x4a\x5a\x4c\x57\x50\x53\x52\x50\x52\x4d\x52\x49\x4f\x49'\
b'\x4c\x20\x52\x4c\x4c\x4c\x4e\x4e\x50\x51\x50\x52\x50\x55\x4e'\
b'\x57\x4b\x57\x4a\x57\x48\x54\x46\x52\x46\x51\x46\x4e\x47\x4c'\
b'\x4a\x4c\x4c\x20\x52\x50\x40\x50\x41\x52\x43\x53\x43\x54\x43'\
b'\x57\x42\x58\x40\x58\x3e\x58\x3d\x56\x3b\x55\x3b\x52\x3b\x50'\
b'\x3e\x50\x40\x45\x47\x5d\x5b\x41\x5b\x43\x5a\x47\x58\x4b\x56'\
b'\x4f\x54\x50\x53\x51\x4f\x52\x4d\x52\x4c\x52\x4a\x52\x49\x52'\
b'\x4a\x4f\x4a\x4f\x4c\x50\x4d\x50\x4f\x50\x52\x4f\x53\x4e\x54'\
b'\x4d\x55\x4c\x56\x49\x57\x47\x58\x45\x58\x45\x57\x46\x56\x47'\
b'\x54\x48\x52\x49\x51\x49\x50\x49\x4d\x47\x4c\x45\x4b\x43\x4b'\
b'\x42\x4b\x41\x4b\x3e\x4c\x3c\x4e\x3a\x50\x39\x52\x38\x54\x38'\
b'\x55\x38\x58\x3a\x5a\x3c\x5b\x3f\x5b\x41\x20\x52\x58\x40\x58'\
b'\x3f\x57\x3d\x56\x3c\x54\x3b\x53\x3b\x52\x3b\x50\x3c\x4f\x3e'\
b'\x4e\x40\x4e\x41\x4e\x42\x4e\x44\x4f\x45\x51\x46\x52\x46\x54'\
b'\x46\x56\x45\x57\x43\x58\x41\x58\x40\x2b\x4c\x58\x56\x41\x56'\
b'\x42\x55\x43\x55\x43\x54\x43\x54\x43\x53\x43\x52\x43\x52\x43'\
b'\x52\x42\x52\x41\x52\x41\x52\x40\x52\x40\x53\x40\x54\x40\x54'\
b'\x40\x55\x40\x55\x40\x56\x41\x56\x41\x20\x52\x52\x50\x52\x51'\
b'\x52\x52\x52\x52\x51\x52\x50\x52\x50\x52\x4f\x52\x4f\x52\x4e'\
b'\x51\x4e\x50\x4e\x50\x4f\x4f\x4f\x4f\x50\x4e\x50\x4e\x51\x4e'\
b'\x52\x4f\x52\x4f\x52\x50\x52\x50\x1b\x4b\x59\x57\x41\x57\x42'\
b'\x56\x43\x56\x43\x55\x43\x55\x43\x54\x43\x54\x43\x53\x43\x53'\
b'\x42\x53\x41\x53\x41\x53\x40\x54\x40\x54\x40\x55\x40\x55\x40'\
b'\x56\x40\x56\x40\x57\x41\x57\x41\x20\x52\x50\x57\x4d\x57\x51'\
b'\x4e\x54\x4e\x50\x57\x09\x48\x5c\x4a\x48\x4a\x47\x5a\x3f\x5a'\
b'\x41\x4e\x48\x4e\x48\x5a\x4d\x5a\x50\x4a\x48\x0b\x48\x5c\x4a'\
b'\x45\x4a\x43\x5a\x43\x5a\x45\x4a\x45\x20\x52\x4a\x4c\x4a\x4a'\
b'\x5a\x4a\x5a\x4c\x4a\x4c\x09\x48\x5c\x4a\x50\x4a\x4d\x56\x48'\
b'\x56\x48\x4a\x41\x4a\x3f\x5a\x47\x5a\x48\x4a\x50\x3d\x4a\x5a'\
b'\x58\x3e\x58\x3f\x58\x41\x57\x43\x55\x44\x54\x45\x53\x46\x51'\
b'\x47\x51\x48\x50\x4a\x50\x4b\x4d\x4b\x4d\x4a\x4e\x48\x4f\x46'\
b'\x50\x44\x52\x44\x53\x43\x54\x42\x55\x40\x56\x3f\x56\x3e\x56'\
b'\x3d\x55\x3c\x54\x3b\x53\x3b\x52\x3b\x51\x3b\x4e\x3b\x4d\x3c'\
b'\x4d\x39\x4e\x39\x51\x38\x52\x38\x54\x38\x56\x39\x58\x3b\x58'\
b'\x3d\x58\x3e\x20\x52\x4f\x50\x4f\x51\x4f\x51\x4f\x52\x4e\x52'\
b'\x4e\x52\x4d\x52\x4c\x52\x4c\x51\x4c\x51\x4c\x50\x4c\x50\x4c'\
b'\x4f\x4c\x4f\x4d\x4e\x4e\x4e\x4e\x4e\x4f\x4f\x4f\x4f\x4f\x50'\
b'\x4f\x50\x7c\x42\x62\x60\x44\x60\x46\x5f\x4a\x5d\x4d\x5a\x4f'\
b'\x58\x4f\x57\x4f\x56\x4e\x55\x4d\x54\x4c\x54\x4c\x54\x4b\x54'\
b'\x4b\x54\x4b\x54\x4b\x53\x4d\x51\x4f\x4f\x4f\x4e\x4f\x4c\x4e'\
b'\x4b\x4d\x4a\x4b\x4a\x49\x4a\x47\x4c\x43\x4e\x41\x51\x3f\x53'\
b'\x3f\x54\x3f\x55\x3f\x56\x40\x57\x41\x57\x41\x57\x41\x57\x41'\
b'\x57\x41\x57\x40\x57\x3f\x57\x3f\x5a\x3f\x59\x40\x59\x42\x58'\
b'\x44\x58\x46\x57\x49\x57\x4a\x57\x4b\x57\x4c\x57\x4d\x58\x4d'\
b'\x5a\x4d\x5c\x4b\x5d\x49\x5e\x46\x5e\x44\x5e\x43\x5e\x41\x5d'\
b'\x3e\x5b\x3d\x58\x3b\x55\x3a\x53\x3a\x52\x3a\x4e\x3b\x4b\x3d'\
b'\x49\x3f\x47\x42\x46\x46\x46\x48\x46\x4b\x47\x4f\x4a\x52\x4f'\
b'\x53\x52\x53\x53\x53\x56\x53\x58\x52\x5a\x52\x5a\x52\x5a\x54'\
b'\x59\x54\x58\x55\x56\x55\x53\x55\x52\x55\x4e\x55\x49\x53\x46'\
b'\x50\x44\x4b\x44\x48\x44\x46\x45\x42\x47\x3e\x4a\x3b\x4d\x39'\
b'\x52\x38\x54\x38\x57\x38\x5c\x3a\x5f\x3d\x60\x42\x60\x44\x20'\
b'\x52\x56\x44\x56\x42\x54\x41\x53\x41\x52\x41\x50\x42\x4e\x45'\
b'\x4d\x48\x4d\x49\x4d\x4a\x4d\x4b\x4e\x4c\x4f\x4d\x50\x4d\x51'\
b'\x4d\x52\x4c\x54\x4a\x55\x47\x55\x45\x56\x44\x56\x44\x1b\x45'\
b'\x5f\x5a\x52\x59\x4b\x4e\x4b\x4a\x52\x47\x52\x56\x39\x59\x39'\
b'\x5d\x52\x5a\x52\x20\x52\x57\x3d\x57\x3d\x57\x3d\x57\x3d\x57'\
b'\x3c\x57\x3c\x57\x3c\x57\x3c\x57\x3c\x57\x3c\x57\x3c\x56\x3d'\
b'\x56\x3d\x56\x3d\x50\x48\x59\x48\x57\x3d\x36\x47\x5d\x5b\x3e'\
b'\x5b\x3f\x5b\x42\x59\x43\x57\x45\x56\x45\x56\x45\x57\x45\x58'\
b'\x46\x59\x47\x5a\x49\x5a\x4a\x5a\x4c\x58\x4f\x56\x51\x52\x52'\
b'\x50\x52\x49\x52\x4e\x39\x55\x39\x57\x39\x59\x3a\x5a\x3b\x5b'\
b'\x3d\x5b\x3e\x20\x52\x58\x3f\x58\x3e\x58\x3d\x57\x3c\x55\x3b'\
b'\x54\x3b\x51\x3b\x4f\x44\x52\x44\x54\x44\x56\x43\x57\x42\x58'\
b'\x40\x58\x3f\x58\x3f\x20\x52\x57\x4a\x57\x48\x54\x46\x52\x46'\
b'\x4e\x46\x4c\x4f\x50\x4f\x52\x4f\x54\x4f\x56\x4d\x57\x4b\x57'\
b'\x4a\x27\x45\x5f\x5c\x3d\x5c\x3d\x5a\x3c\x59\x3b\x57\x3b\x56'\
b'\x3b\x53\x3b\x4f\x3d\x4c\x40\x4a\x45\x4a\x47\x4a\x49\x4b\x4c'\
b'\x4e\x4f\x51\x50\x52\x50\x54\x50\x56\x4f\x57\x4f\x59\x4e\x59'\
b'\x4e\x59\x51\x57\x52\x54\x52\x52\x52\x4f\x52\x4b\x51\x49\x4e'\
b'\x47\x4a\x47\x47\x47\x44\x49\x3e\x4d\x3a\x53\x38\x56\x38\x58'\
b'\x38\x5c\x39\x5d\x3a\x5c\x3d\x1d\x44\x60\x5e\x43\x5e\x45\x5d'\
b'\x48\x5b\x4c\x59\x4f\x55\x51\x51\x52\x4e\x52\x46\x52\x4c\x39'\
b'\x53\x39\x55\x39\x59\x3a\x5c\x3d\x5e\x41\x5e\x43\x20\x52\x5b'\
b'\x43\x5b\x3f\x56\x3b\x52\x3b\x4e\x3b\x4a\x4f\x4f\x4f\x52\x4f'\
b'\x56\x4d\x59\x4a\x5b\x46\x5b\x43\x0d\x47\x5d\x5b\x3b\x51\x3b'\
b'\x4f\x44\x58\x44\x57\x47\x4e\x47\x4c\x4f\x57\x4f\x56\x52\x49'\
b'\x52\x4e\x39\x5b\x39\x5b\x3b\x0b\x47\x5d\x5b\x3b\x51\x3b\x4f'\
b'\x44\x58\x44\x57\x47\x4e\x47\x4c\x52\x49\x52\x4e\x39\x5b\x39'\
b'\x5b\x3b\x2d\x45\x5f\x5c\x3d\x5c\x3d\x5a\x3c\x59\x3b\x56\x3b'\
b'\x55\x3b\x53\x3b\x4e\x3d\x4c\x40\x4a\x44\x4a\x47\x4a\x49\x4b'\
b'\x4c\x4d\x4f\x50\x50\x52\x50\x54\x50\x56\x4f\x57\x4f\x58\x48'\
b'\x52\x48\x53\x45\x5c\x45\x59\x51\x58\x51\x54\x52\x52\x52\x4f'\
b'\x52\x4b\x51\x49\x4e\x47\x4a\x47\x47\x47\x45\x48\x41\x4a\x3e'\
b'\x4c\x3b\x4f\x39\x53\x38\x56\x38\x57\x38\x59\x39\x5b\x39\x5c'\
b'\x3a\x5d\x3a\x5c\x3d\x0d\x44\x60\x59\x52\x56\x52\x58\x47\x4b'\
b'\x47\x49\x52\x46\x52\x4b\x39\x4e\x39\x4c\x44\x59\x44\x5b\x39'\
b'\x5e\x39\x59\x52\x05\x4c\x58\x51\x52\x4e\x52\x53\x39\x56\x39'\
b'\x51\x52\x19\x49\x5b\x56\x49\x55\x4b\x54\x4f\x52\x51\x4f\x52'\
b'\x4e\x52\x4d\x52\x4c\x52\x4b\x52\x4b\x52\x4b\x52\x4b\x4f\x4b'\
b'\x4f\x4c\x4f\x4c\x50\x4d\x50\x4e\x50\x4e\x50\x50\x4f\x51\x4e'\
b'\x52\x4b\x53\x49\x56\x39\x59\x39\x56\x49\x14\x45\x5f\x50\x45'\
b'\x58\x52\x55\x52\x4d\x46\x4d\x46\x4d\x46\x4d\x46\x4c\x46\x4a'\
b'\x52\x47\x52\x4c\x39\x4f\x39\x4d\x45\x4d\x45\x4d\x44\x4d\x44'\
b'\x4e\x44\x59\x39\x5d\x39\x50\x45\x07\x49\x5b\x58\x52\x4b\x52'\
b'\x50\x39\x54\x39\x4f\x4f\x59\x4f\x58\x52\x27\x42\x62\x5b\x52'\
b'\x58\x52\x5b\x41\x5c\x40\x5c\x3d\x5d\x3c\x5d\x3c\x5d\x3c\x5c'\
b'\x3d\x5b\x3e\x5b\x3f\x5a\x3f\x51\x4b\x50\x4b\x4c\x3f\x4c\x3f'\
b'\x4c\x3e\x4b\x3d\x4b\x3c\x4b\x3c\x4b\x3c\x4b\x3d\x4b\x3f\x4a'\
b'\x41\x47\x52\x44\x52\x49\x39\x4d\x39\x51\x45\x51\x46\x51\x47'\
b'\x51\x47\x51\x47\x52\x47\x53\x45\x53\x45\x5c\x39\x60\x39\x5b'\
b'\x52\x21\x43\x61\x5a\x52\x56\x52\x4d\x3e\x4d\x3e\x4d\x3d\x4d'\
b'\x3d\x4d\x3c\x4d\x3c\x4c\x3c\x4c\x3c\x4c\x3d\x4c\x3d\x4c\x3e'\
b'\x4c\x3e\x48\x52\x45\x52\x4a\x39\x4e\x39\x57\x4d\x57\x4d\x57'\
b'\x4d\x57\x4e\x57\x4e\x58\x4e\x58\x4e\x58\x4e\x58\x4d\x58\x4d'\
b'\x58\x4c\x58\x4c\x5c\x39\x5f\x39\x5a\x52\x37\x44\x60\x5e\x43'\
b'\x5e\x45\x5d\x48\x5c\x4b\x5b\x4e\x5a\x4f\x59\x4f\x57\x51\x54'\
b'\x52\x52\x52\x50\x52\x4e\x52\x4a\x51\x47\x4e\x46\x4a\x46\x48'\
b'\x46\x44\x48\x3e\x4b\x3c\x4c\x3a\x51\x38\x54\x38\x56\x38\x5a'\
b'\x3a\x5c\x3d\x5e\x41\x5e\x43\x20\x52\x5b\x43\x5b\x41\x5a\x3e'\
b'\x58\x3c\x55\x3b\x54\x3b\x52\x3b\x4e\x3d\x4d\x3e\x4c\x3f\x4b'\
b'\x41\x4a\x44\x49\x46\x49\x48\x49\x49\x4a\x4c\x4c\x4f\x4f\x50'\
b'\x50\x50\x52\x50\x56\x4e\x57\x4d\x58\x4c\x5a\x49\x5a\x47\x5b'\
b'\x44\x5b\x43\x1f\x46\x5e\x5c\x3f\x5c\x41\x5a\x45\x58\x47\x54'\
b'\x48\x51\x48\x4d\x48\x4b\x52\x48\x52\x4e\x39\x54\x39\x56\x39'\
b'\x59\x3a\x5b\x3c\x5c\x3e\x5c\x3f\x20\x52\x59\x40\x59\x3f\x58'\
b'\x3d\x57\x3c\x55\x3b\x54\x3b\x50\x3b\x4e\x46\x51\x46\x53\x46'\
b'\x56\x45\x58\x43\x59\x41\x59\x40\x23\x44\x60\x5e\x43\x5e\x47'\
b'\x5b\x4d\x56\x51\x53\x52\x58\x58\x54\x58\x50\x52\x4d\x52\x49'\
b'\x50\x46\x4b\x46\x48\x46\x41\x4e\x38\x54\x38\x57\x38\x5b\x3b'\
b'\x5e\x40\x5e\x43\x20\x52\x5b\x43\x5b\x3f\x57\x3b\x54\x3b\x51'\
b'\x3b\x4c\x3e\x49\x44\x49\x48\x49\x4b\x4d\x50\x50\x50\x53\x50'\
b'\x58\x4d\x5b\x46\x5b\x43\x29\x46\x5e\x5c\x3f\x5c\x41\x5b\x43'\
b'\x59\x45\x56\x46\x54\x46\x54\x47\x55\x47\x56\x48\x57\x4a\x59'\
b'\x52\x55\x52\x54\x4a\x53\x49\x51\x47\x50\x47\x4e\x47\x4b\x52'\
b'\x48\x52\x4e\x39\x55\x39\x57\x39\x59\x3a\x5b\x3b\x5c\x3e\x5c'\
b'\x3f\x20\x52\x59\x3f\x59\x3e\x58\x3d\x57\x3c\x55\x3b\x54\x3b'\
b'\x50\x3b\x4e\x45\x52\x45\x54\x45\x56\x44\x58\x42\x59\x40\x59'\
b'\x3f\x41\x47\x5d\x5a\x3c\x5a\x3c\x58\x3c\x57\x3b\x56\x3b\x55'\
b'\x3b\x53\x3b\x51\x3c\x50\x3d\x50\x3e\x50\x3f\x50\x40\x50\x41'\
b'\x51\x42\x53\x44\x54\x44\x55\x45\x56\x47\x58\x48\x58\x4a\x58'\
b'\x4b\x58\x4c\x58\x4d\x57\x4f\x56\x51\x54\x52\x52\x52\x50\x52'\
b'\x4f\x52\x4d\x52\x4b\x52\x4a\x51\x49\x51\x4a\x4e\x4a\x4e\x4c'\
b'\x4f\x4d\x4f\x4f\x50\x50\x50\x51\x50\x53\x4f\x55\x4e\x55\x4c'\
b'\x55\x4c\x55\x4b\x55\x4a\x54\x48\x52\x47\x51\x46\x50\x46\x4f'\
b'\x44\x4d\x43\x4d\x41\x4d\x3f\x4d\x3e\x4e\x3b\x50\x39\x53\x38'\
b'\x55\x38\x56\x38\x57\x38\x59\x39\x5a\x39\x5b\x39\x5a\x3c\x09'\
b'\x47\x5d\x5a\x3b\x53\x3b\x4f\x52\x4b\x52\x50\x3b\x49\x3b\x49'\
b'\x39\x5b\x39\x5a\x3b\x23\x45\x5f\x5a\x48\x59\x4b\x58\x4e\x55'\
b'\x51\x52\x52\x4f\x52\x4d\x52\x4a\x51\x48\x4f\x47\x4c\x47\x4a'\
b'\x47\x4a\x47\x48\x47\x47\x4a\x39\x4d\x39\x4a\x47\x4a\x47\x4a'\
b'\x48\x4a\x49\x4a\x4a\x4a\x4a\x4a\x4c\x4b\x4e\x4c\x4f\x4e\x50'\
b'\x4f\x50\x51\x50\x53\x4f\x55\x4d\x56\x4a\x57\x48\x5a\x39\x5d'\
b'\x39\x5a\x48\x11\x45\x5f\x4e\x52\x4b\x52\x47\x39\x4a\x39\x4d'\
b'\x4d\x4d\x4d\x4d\x4e\x4d\x4f\x4d\x4f\x4d\x4e\x4d\x4e\x4e\x4d'\
b'\x4e\x4d\x4e\x4d\x59\x39\x5d\x39\x4e\x52\x27\x3f\x65\x56\x52'\
b'\x53\x52\x51\x3f\x51\x3f\x51\x3d\x51\x3d\x51\x3d\x51\x3d\x51'\
b'\x3f\x50\x3f\x47\x52\x43\x52\x41\x39\x45\x39\x46\x4c\x46\x4d'\
b'\x46\x4e\x46\x4e\x46\x4e\x46\x4e\x46\x4e\x46\x4d\x47\x4c\x47'\
b'\x4c\x51\x39\x53\x39\x55\x4c\x55\x4d\x55\x4e\x55\x4e\x55\x4e'\
b'\x55\x4e\x55\x4e\x56\x4d\x56\x4c\x56\x4c\x5f\x39\x63\x39\x56'\
b'\x52\x43\x43\x61\x5f\x39\x5f\x39\x5e\x3a\x5c\x3c\x5a\x3e\x59'\
b'\x40\x57\x42\x55\x44\x54\x45\x54\x45\x54\x45\x55\x47\x55\x48'\
b'\x56\x4b\x57\x4d\x58\x4f\x59\x51\x59\x52\x59\x52\x56\x52\x52'\
b'\x48\x52\x48\x52\x48\x52\x47\x52\x47\x52\x47\x52\x47\x52\x47'\
b'\x52\x47\x51\x48\x51\x48\x51\x48\x49\x52\x45\x52\x45\x52\x46'\
b'\x51\x48\x4f\x4a\x4d\x4c\x4b\x4e\x48\x4f\x47\x50\x45\x50\x45'\
b'\x50\x45\x50\x43\x4f\x42\x4e\x40\x4d\x3e\x4c\x3c\x4c\x3a\x4b'\
b'\x39\x4b\x39\x4f\x39\x52\x42\x52\x42\x52\x43\x52\x43\x53\x43'\
b'\x53\x43\x53\x43\x53\x43\x53\x43\x53\x43\x53\x42\x54\x42\x5b'\
b'\x39\x5f\x39\x11\x46\x5e\x50\x48\x4e\x52\x4b\x52\x4d\x48\x48'\
b'\x39\x4b\x39\x4f\x44\x4f\x45\x4f\x46\x4f\x46\x4f\x46\x4f\x46'\
b'\x50\x45\x50\x44\x58\x39\x5c\x39\x50\x48\x0b\x44\x60\x5e\x39'\
b'\x4b\x4f\x59\x4f\x59\x52\x46\x52\x46\x51\x59\x3b\x4c\x3b\x4c'\
b'\x39\x5e\x39\x5e\x39\x09\x49\x5b\x58\x3b\x54\x3b\x4e\x56\x52'\
b'\x56\x52\x58\x4b\x58\x52\x39\x59\x39\x58\x3b\x05\x4c\x58\x54'\
b'\x56\x4e\x39\x50\x39\x56\x56\x54\x56\x09\x49\x5b\x52\x58\x4b'\
b'\x58\x4c\x56\x50\x56\x56\x3b\x52\x3b\x52\x39\x59\x39\x52\x58'\
b'\x09\x48\x5c\x58\x47\x52\x3c\x52\x3c\x4c\x47\x4a\x47\x51\x38'\
b'\x52\x38\x5a\x47\x58\x47\x05\x48\x5c\x4a\x57\x4b\x55\x5a\x55'\
b'\x59\x57\x4a\x57\x05\x4d\x57\x53\x3c\x4f\x37\x52\x37\x55\x3c'\
b'\x53\x3c\x3b\x47\x5d\x58\x4c\x58\x4d\x58\x4f\x57\x50\x57\x52'\
b'\x57\x52\x54\x52\x54\x52\x54\x51\x55\x50\x55\x4f\x55\x4e\x55'\
b'\x4e\x54\x4f\x53\x51\x52\x52\x50\x52\x4f\x52\x4e\x52\x4c\x52'\
b'\x4a\x50\x49\x4d\x49\x4c\x49\x4b\x4a\x48\x4b\x45\x4d\x43\x4f'\
b'\x41\x52\x3f\x55\x3f\x56\x3f\x59\x40\x5b\x40\x58\x4c\x20\x52'\
b'\x57\x42\x57\x42\x55\x42\x54\x42\x53\x42\x50\x43\x4f\x44\x4d'\
b'\x47\x4d\x49\x4c\x4b\x4c\x4c\x4c\x4d\x4d\x4e\x4e\x4f\x4f\x50'\
b'\x50\x50\x50\x50\x52\x4f\x53\x4e\x54\x4c\x55\x4b\x56\x49\x56'\
b'\x48\x57\x42\x33\x47\x5d\x5b\x46\x5b\x47\x5a\x4a\x59\x4d\x57'\
b'\x4f\x55\x51\x52\x52\x50\x52\x4f\x52\x4d\x52\x4c\x52\x4a\x51'\
b'\x49\x51\x4f\x37\x52\x37\x50\x40\x50\x41\x4f\x43\x4f\x43\x4f'\
b'\x43\x50\x42\x51\x41\x53\x40\x54\x3f\x55\x3f\x58\x3f\x5b\x43'\
b'\x5b\x46\x20\x52\x58\x46\x58\x45\x57\x44\x56\x43\x55\x42\x54'\
b'\x42\x53\x42\x51\x43\x4f\x45\x4e\x48\x4e\x4a\x4d\x4f\x4d\x50'\
b'\x4f\x50\x50\x50\x51\x50\x53\x4f\x55\x4e\x56\x4c\x57\x4a\x58'\
b'\x47\x58\x46\x27\x49\x5b\x59\x43\x58\x43\x56\x42\x54\x42\x53'\
b'\x42\x51\x43\x50\x44\x4f\x46\x4e\x48\x4e\x4a\x4e\x4b\x4e\x4d'\
b'\x50\x50\x52\x50\x53\x50\x55\x4f\x57\x4e\x56\x51\x55\x52\x53'\
b'\x52\x51\x52\x50\x52\x4d\x51\x4c\x4f\x4b\x4d\x4b\x4b\x4b\x4a'\
b'\x4b\x47\x4d\x44\x4e\x42\x50\x40\x53\x3f\x55\x3f\x56\x3f\x57'\
b'\x40\x58\x40\x59\x40\x59\x41\x59\x43\x3d\x47\x5d\x57\x4c\x57'\
b'\x4d\x57\x4f\x57\x50\x56\x52\x56\x52\x53\x52\x53\x52\x53\x51'\
b'\x54\x50\x54\x4f\x54\x4e\x54\x4e\x53\x4f\x52\x51\x50\x52\x4f'\
b'\x52\x4e\x52\x4d\x52\x4b\x52\x49\x50\x49\x4d\x49\x4c\x49\x4a'\
b'\x49\x48\x4a\x45\x4c\x42\x4e\x41\x52\x3f\x53\x3f\x54\x3f\x56'\
b'\x40\x57\x40\x59\x37\x5b\x37\x57\x4c\x20\x52\x56\x42\x56\x42'\
b'\x54\x42\x53\x42\x52\x42\x4f\x43\x4e\x44\x4c\x47\x4c\x49\x4b'\
b'\x4b\x4b\x4c\x4b\x4d\x4c\x4e\x4d\x4f\x4e\x50\x4f\x50\x50\x50'\
b'\x51\x4f\x52\x4e\x53\x4c\x54\x4a\x55\x48\x55\x48\x56\x42\x36'\
b'\x48\x5c\x5a\x44\x5a\x46\x58\x48\x56\x4a\x51\x4b\x4d\x4b\x4d'\
b'\x4b\x4d\x4b\x4d\x4b\x4d\x4b\x4d\x4c\x4e\x4e\x4f\x4f\x51\x50'\
b'\x52\x50\x53\x50\x56\x4f\x57\x4e\x57\x51\x56\x52\x53\x52\x51'\
b'\x52\x4f\x52\x4d\x51\x4b\x4f\x4a\x4c\x4a\x4b\x4a\x49\x4b\x46'\
b'\x4c\x44\x4e\x42\x50\x40\x53\x3f\x54\x3f\x55\x3f\x58\x40\x59'\
b'\x42\x5a\x43\x5a\x44\x20\x52\x57\x44\x57\x43\x55\x42\x54\x42'\
b'\x53\x42\x51\x43\x4f\x45\x4e\x47\x4e\x48\x50\x48\x54\x48\x56'\
b'\x47\x57\x45\x57\x44\x1d\x49\x5b\x59\x3a\x59\x3a\x58\x39\x58'\
b'\x39\x57\x39\x57\x39\x55\x39\x54\x3b\x53\x3d\x53\x40\x57\x40'\
b'\x56\x42\x52\x42\x4e\x58\x4b\x58\x4f\x42\x4c\x42\x4d\x40\x50'\
b'\x40\x51\x3d\x51\x3b\x52\x39\x54\x37\x56\x37\x57\x37\x58\x37'\
b'\x59\x37\x59\x37\x59\x3a\x40\x46\x5e\x58\x51\x58\x53\x56\x56'\
b'\x54\x59\x50\x5a\x4e\x5a\x4c\x5a\x4a\x5a\x48\x59\x49\x56\x4a'\
b'\x57\x4d\x58\x4e\x58\x50\x58\x52\x57\x54\x55\x55\x53\x55\x51'\
b'\x56\x4e\x56\x4e\x55\x4f\x54\x51\x52\x52\x51\x52\x50\x52\x4f'\
b'\x52\x4d\x52\x4b\x50\x4a\x4d\x4a\x4c\x4a\x4a\x4b\x47\x4c\x44'\
b'\x4e\x42\x51\x40\x54\x3f\x55\x3f\x57\x3f\x5a\x40\x5c\x40\x58'\
b'\x51\x20\x52\x58\x42\x58\x42\x56\x42\x55\x42\x53\x42\x51\x43'\
b'\x4f\x46\x4d\x4a\x4d\x4c\x4d\x4d\x4e\x4e\x4e\x4f\x50\x50\x50'\
b'\x50\x51\x50\x53\x4f\x54\x4e\x56\x4c\x56\x4a\x57\x49\x57\x48'\
b'\x58\x42\x24\x47\x5d\x5b\x44\x5b\x45\x5b\x46\x5a\x47\x5a\x48'\
b'\x5a\x48\x58\x52\x55\x52\x57\x47\x57\x47\x58\x46\x58\x46\x58'\
b'\x45\x58\x45\x58\x43\x56\x42\x55\x42\x54\x42\x52\x43\x50\x45'\
b'\x4e\x48\x4e\x49\x4c\x52\x49\x52\x4f\x37\x52\x37\x4f\x44\x4f'\
b'\x44\x50\x43\x51\x41\x53\x40\x55\x3f\x56\x3f\x58\x3f\x5b\x42'\
b'\x5b\x44\x25\x4c\x58\x54\x52\x53\x52\x52\x52\x52\x52\x50\x52'\
b'\x4e\x50\x4e\x4f\x4e\x4f\x4e\x4d\x4f\x4c\x51\x40\x54\x40\x51'\
b'\x4d\x51\x4d\x51\x4e\x51\x4e\x51\x4f\x52\x50\x53\x50\x53\x50'\
b'\x54\x50\x54\x50\x54\x52\x20\x52\x56\x39\x56\x3a\x55\x3b\x54'\
b'\x3b\x53\x3b\x52\x3a\x52\x39\x52\x39\x53\x38\x54\x38\x55\x38'\
b'\x56\x39\x56\x39\x23\x48\x5c\x55\x51\x54\x56\x50\x5a\x4c\x5a'\
b'\x4c\x5a\x4b\x5a\x4b\x5a\x4a\x5a\x4a\x5a\x4a\x57\x4b\x57\x4b'\
b'\x58\x4c\x58\x4c\x58\x4d\x58\x4f\x58\x51\x55\x52\x52\x55\x40'\
b'\x58\x40\x55\x51\x20\x52\x5a\x39\x5a\x3a\x59\x3b\x58\x3b\x58'\
b'\x3b\x56\x3a\x56\x39\x56\x39\x58\x38\x58\x38\x59\x38\x5a\x39'\
b'\x5a\x39\x0e\x47\x5d\x51\x48\x57\x52\x54\x52\x4e\x48\x4e\x48'\
b'\x4c\x52\x49\x52\x4f\x37\x52\x37\x4e\x48\x4e\x48\x57\x40\x5b'\
b'\x40\x51\x48\x17\x4c\x58\x54\x52\x53\x52\x52\x52\x52\x52\x50'\
b'\x52\x4e\x50\x4e\x4f\x4e\x4f\x4e\x4d\x4e\x4c\x53\x37\x56\x37'\
b'\x51\x4d\x51\x4d\x51\x4e\x51\x4e\x51\x4f\x52\x50\x53\x50\x53'\
b'\x50\x54\x50\x54\x50\x54\x52\x4b\x42\x62\x60\x44\x60\x45\x60'\
b'\x46\x60\x47\x60\x48\x60\x48\x5d\x52\x5b\x52\x5d\x47\x5d\x47'\
b'\x5d\x46\x5d\x46\x5d\x45\x5d\x45\x5d\x43\x5c\x42\x5b\x42\x5a'\
b'\x42\x59\x43\x57\x44\x56\x45\x55\x47\x54\x48\x54\x49\x52\x52'\
b'\x4f\x52\x51\x47\x52\x47\x52\x46\x52\x46\x52\x45\x52\x45\x52'\
b'\x43\x51\x42\x4f\x42\x4f\x42\x4d\x43\x4c\x44\x4b\x45\x4a\x47'\
b'\x49\x48\x49\x49\x47\x52\x44\x52\x47\x45\x47\x44\x47\x43\x47'\
b'\x42\x47\x40\x48\x40\x4a\x40\x4a\x41\x4a\x42\x4a\x43\x4a\x43'\
b'\x4a\x44\x4a\x44\x4a\x43\x4c\x41\x4e\x40\x4f\x3f\x50\x3f\x51'\
b'\x3f\x53\x40\x54\x41\x55\x43\x55\x44\x55\x43\x57\x41\x59\x40'\
b'\x5b\x3f\x5c\x3f\x5e\x3f\x60\x42\x60\x44\x2f\x47\x5d\x5b\x44'\
b'\x5b\x45\x5b\x46\x5a\x47\x5a\x48\x5a\x48\x58\x52\x55\x52\x57'\
b'\x47\x57\x47\x58\x46\x58\x46\x58\x45\x58\x45\x58\x43\x56\x42'\
b'\x55\x42\x54\x42\x52\x43\x50\x45\x4e\x48\x4e\x49\x4c\x52\x49'\
b'\x52\x4c\x45\x4c\x44\x4c\x43\x4d\x42\x4d\x40\x4d\x40\x50\x40'\
b'\x50\x41\x4f\x42\x4f\x43\x4f\x43\x4f\x44\x4f\x44\x50\x43\x51'\
b'\x42\x53\x40\x55\x3f\x56\x3f\x57\x3f\x59\x40\x5a\x42\x5b\x43'\
b'\x5b\x44\x2b\x48\x5c\x5a\x47\x5a\x49\x59\x4d\x56\x51\x53\x52'\
b'\x50\x52\x4f\x52\x4c\x51\x4b\x50\x4a\x4d\x4a\x4b\x4a\x49\x4b'\
b'\x44\x4e\x41\x51\x3f\x54\x3f\x55\x3f\x58\x40\x59\x42\x5a\x45'\
b'\x5a\x47\x20\x52\x57\x47\x57\x46\x57\x44\x56\x43\x54\x42\x53'\
b'\x42\x52\x42\x4f\x44\x4e\x46\x4d\x49\x4d\x4b\x4d\x4c\x4d\x4e'\
b'\x4e\x4f\x50\x50\x51\x50\x52\x50\x55\x4e\x56\x4c\x57\x48\x57'\
b'\x47\x3d\x46\x5e\x5c\x46\x5c\x48\x5b\x4a\x5a\x4d\x58\x50\x56'\
b'\x51\x53\x52\x51\x52\x50\x52\x4e\x52\x4d\x52\x4b\x5a\x48\x5a'\
b'\x4d\x45\x4d\x45\x4d\x43\x4d\x42\x4d\x40\x4d\x40\x50\x40\x50'\
b'\x40\x50\x41\x50\x42\x50\x43\x50\x44\x50\x44\x51\x42\x54\x3f'\
b'\x56\x3f\x58\x3f\x59\x40\x5b\x42\x5c\x45\x5c\x46\x20\x52\x59'\
b'\x46\x59\x45\x58\x44\x58\x43\x56\x42\x55\x42\x55\x42\x53\x43'\
b'\x52\x44\x50\x46\x50\x47\x4f\x49\x4f\x4a\x4e\x4f\x4e\x4f\x4f'\
b'\x50\x50\x50\x51\x50\x51\x50\x52\x50\x54\x4f\x56\x4e\x57\x4c'\
b'\x58\x4a\x59\x47\x59\x46\x37\x47\x5d\x55\x5a\x52\x5a\x54\x52'\
b'\x54\x51\x54\x4f\x55\x4f\x55\x4f\x54\x4f\x53\x51\x51\x52\x50'\
b'\x52\x4f\x52\x4e\x52\x4c\x52\x4a\x50\x49\x4d\x49\x4c\x49\x4b'\
b'\x4a\x48\x4b\x45\x4d\x43\x4f\x41\x52\x3f\x55\x3f\x56\x3f\x57'\
b'\x40\x59\x40\x5a\x40\x5b\x40\x55\x5a\x20\x52\x57\x42\x57\x42'\
b'\x55\x42\x54\x42\x53\x42\x50\x43\x4f\x44\x4d\x46\x4d\x49\x4c'\
b'\x4b\x4c\x4c\x4c\x4d\x4d\x4e\x4d\x4f\x4f\x50\x50\x50\x50\x50'\
b'\x52\x4f\x53\x4e\x54\x4c\x55\x4a\x56\x49\x56\x48\x57\x42\x22'\
b'\x49\x5b\x58\x43\x58\x43\x58\x43\x56\x42\x56\x42\x55\x42\x53'\
b'\x44\x51\x46\x50\x49\x50\x4a\x4e\x52\x4b\x52\x4e\x46\x4e\x45'\
b'\x4e\x44\x4f\x42\x4f\x41\x4f\x40\x52\x40\x52\x40\x52\x42\x52'\
b'\x43\x51\x44\x51\x44\x51\x44\x52\x43\x53\x41\x54\x40\x56\x3f'\
b'\x57\x3f\x57\x3f\x58\x40\x59\x40\x58\x43\x33\x49\x5b\x58\x43'\
b'\x57\x43\x55\x42\x54\x42\x53\x42\x51\x43\x51\x45\x51\x45\x51'\
b'\x46\x52\x47\x53\x48\x53\x48\x55\x49\x57\x4c\x57\x4d\x57\x4e'\
b'\x56\x50\x55\x52\x52\x52\x50\x52\x50\x52\x4e\x52\x4d\x52\x4c'\
b'\x52\x4b\x51\x4c\x4f\x4c\x4f\x4d\x4f\x4f\x50\x50\x50\x51\x50'\
b'\x52\x50\x54\x4f\x54\x4d\x54\x4d\x54\x4c\x53\x4b\x52\x4a\x51'\
b'\x4a\x4f\x49\x4e\x47\x4e\x45\x4e\x44\x4f\x42\x50\x40\x53\x3f'\
b'\x54\x3f\x55\x3f\x58\x40\x59\x40\x58\x43\x27\x4a\x5a\x57\x42'\
b'\x52\x42\x50\x4c\x50\x4d\x50\x4e\x50\x4e\x50\x4f\x51\x50\x52'\
b'\x50\x52\x50\x53\x50\x53\x50\x54\x4f\x54\x4f\x54\x52\x53\x52'\
b'\x52\x52\x51\x52\x50\x52\x4e\x52\x4d\x51\x4d\x4f\x4d\x4f\x4d'\
b'\x4e\x4d\x4d\x4d\x4c\x50\x42\x4c\x42\x4d\x40\x50\x40\x51\x3b'\
b'\x51\x3b\x52\x3b\x53\x3b\x54\x3b\x54\x3b\x53\x40\x58\x40\x57'\
b'\x42\x31\x47\x5d\x58\x4d\x58\x4e\x58\x4f\x57\x50\x57\x52\x57'\
b'\x52\x54\x52\x54\x51\x55\x50\x55\x4f\x55\x4e\x55\x4e\x55\x4e'\
b'\x54\x4f\x53\x50\x51\x52\x4f\x52\x4e\x52\x4d\x52\x4b\x52\x4a'\
b'\x50\x49\x4f\x49\x4d\x49\x4d\x49\x4c\x4a\x4b\x4a\x4a\x4a\x4a'\
b'\x4c\x40\x4f\x40\x4d\x4b\x4d\x4b\x4c\x4c\x4c\x4c\x4c\x4d\x4c'\
b'\x4d\x4c\x4e\x4e\x50\x4f\x50\x50\x50\x51\x4f\x53\x4e\x54\x4d'\
b'\x55\x4b\x56\x4a\x56\x49\x58\x40\x5b\x40\x58\x4d\x13\x48\x5c'\
b'\x4f\x52\x4d\x52\x4a\x40\x4d\x40\x4e\x4b\x4e\x4c\x4f\x4c\x4f'\
b'\x4d\x4f\x4e\x4f\x4f\x4f\x4f\x4f\x4e\x4f\x4d\x50\x4d\x50\x4c'\
b'\x50\x4b\x57\x40\x5a\x40\x4f\x52\x2a\x43\x61\x55\x52\x52\x52'\
b'\x51\x45\x51\x45\x51\x45\x51\x45\x51\x44\x51\x44\x51\x43\x51'\
b'\x43\x51\x44\x51\x44\x51\x45\x51\x45\x51\x45\x4a\x52\x47\x52'\
b'\x45\x40\x48\x40\x49\x4d\x49\x4e\x49\x4f\x49\x4f\x49\x4f\x49'\
b'\x4f\x4a\x4e\x4a\x4d\x51\x40\x53\x40\x54\x4d\x54\x4e\x54\x4f'\
b'\x54\x4f\x54\x4f\x55\x4f\x55\x4f\x55\x4e\x55\x4e\x55\x4d\x5c'\
b'\x40\x5f\x40\x55\x52\x1f\x46\x5e\x54\x49\x58\x52\x55\x52\x52'\
b'\x4c\x52\x4c\x52\x4b\x52\x4b\x52\x4b\x51\x4b\x51\x4b\x51\x4c'\
b'\x51\x4c\x50\x4c\x4c\x52\x48\x52\x50\x49\x4c\x40\x50\x40\x52'\
b'\x46\x52\x46\x52\x47\x52\x47\x52\x47\x52\x47\x53\x47\x53\x46'\
b'\x53\x46\x54\x46\x58\x40\x5c\x40\x54\x49\x1e\x45\x5f\x50\x55'\
b'\x4f\x56\x4e\x58\x4c\x5a\x4a\x5a\x49\x5a\x48\x5a\x47\x5a\x47'\
b'\x5a\x47\x58\x48\x58\x49\x58\x49\x58\x4a\x58\x4c\x57\x4d\x55'\
b'\x4f\x52\x4c\x40\x4f\x40\x51\x4e\x51\x4e\x51\x4f\x51\x4f\x51'\
b'\x4f\x51\x4f\x52\x4e\x52\x4e\x5a\x40\x5d\x40\x50\x55\x0b\x47'\
b'\x5d\x5b\x41\x4e\x50\x58\x50\x57\x52\x49\x52\x49\x51\x56\x42'\
b'\x4d\x42\x4d\x40\x5b\x40\x5b\x41\x31\x4a\x5a\x57\x3b\x56\x3b'\
b'\x54\x3c\x54\x3e\x53\x43\x52\x45\x51\x48\x4f\x48\x4f\x48\x50'\
b'\x49\x51\x4a\x51\x4b\x51\x4c\x51\x4d\x51\x4d\x50\x52\x50\x52'\
b'\x50\x53\x50\x53\x50\x54\x51\x55\x52\x55\x51\x57\x50\x57\x4e'\
b'\x57\x4d\x56\x4d\x54\x4d\x54\x4d\x53\x4d\x52\x4d\x52\x4e\x4d'\
b'\x4e\x4d\x4e\x4c\x4e\x4c\x4e\x4a\x4d\x49\x4c\x49\x4d\x47\x4e'\
b'\x47\x50\x45\x50\x43\x51\x3e\x52\x3d\x53\x3a\x55\x39\x57\x39'\
b'\x58\x39\x57\x3b\x05\x4f\x55\x51\x5a\x51\x36\x53\x36\x53\x5a'\
b'\x51\x5a\x32\x4a\x5a\x57\x49\x57\x49\x55\x4a\x55\x4a\x54\x4c'\
b'\x54\x4d\x53\x52\x52\x54\x51\x56\x4f\x57\x4d\x57\x4c\x57\x4d'\
b'\x55\x4e\x55\x50\x54\x50\x52\x51\x4d\x52\x4b\x53\x48\x55\x48'\
b'\x55\x48\x54\x48\x53\x46\x53\x45\x53\x44\x53\x44\x53\x43\x54'\
b'\x3f\x54\x3e\x54\x3d\x54\x3c\x53\x3b\x52\x3b\x53\x39\x54\x39'\
b'\x56\x39\x57\x3a\x57\x3c\x57\x3d\x57\x3d\x57\x3e\x57\x3e\x56'\
b'\x43\x56\x44\x56\x44\x56\x45\x56\x46\x57\x47\x58\x47\x57\x49'\
b'\x29\x47\x5d\x5b\x45\x5b\x46\x5a\x48\x59\x49\x57\x4a\x56\x4a'\
b'\x55\x4a\x54\x4a\x53\x49\x52\x49\x51\x48\x51\x48\x50\x48\x4f'\
b'\x47\x4f\x47\x4e\x47\x4d\x47\x4c\x49\x4c\x4a\x49\x4a\x49\x49'\
b'\x4a\x47\x4b\x46\x4d\x45\x4e\x45\x4f\x45\x50\x45\x51\x45\x52'\
b'\x46\x52\x46\x53\x47\x54\x47\x55\x48\x55\x48\x56\x48\x56\x48'\
b'\x57\x47\x58\x47\x58\x45\x58\x45\x5b\x45\x0b\x47\x5d\x49\x52'\
b'\x49\x39\x5b\x39\x5b\x52\x49\x52\x20\x52\x4c\x4f\x58\x4f\x58'\
b'\x3c\x4c\x3c\x4c\x4f'

_index =\
b'\x00\x00\x03\x00\x3c\x00\x55\x00\x9e\x00\x37\x01\xfc\x01\xd9'\
b'\x02\xe6\x02\x17\x03\x48\x03\x6b\x03\x88\x03\x95\x03\xa2\x03'\
b'\xcf\x03\xdc\x03\x4f\x04\x60\x04\xa7\x04\x2c\x05\x57\x05\x96'\
b'\x05\x1f\x06\x3a\x06\xb1\x06\x3e\x07\x97\x07\xd0\x07\xe5\x07'\
b'\xfe\x07\x13\x08\x90\x08\x8b\x09\xc4\x09\x33\x0a\x84\x0a\xc1'\
b'\x0a\xde\x0a\xf7\x0a\x54\x0b\x71\x0b\x7e\x0b\xb3\x0b\xde\x0b'\
b'\xef\x0b\x40\x0c\x85\x0c\xf6\x0c\x37\x0d\x80\x0d\xd5\x0d\x5a'\
b'\x0e\x6f\x0e\xb8\x0e\xdd\x0e\x2e\x0f\xb7\x0f\xdc\x0f\xf5\x0f'\
b'\x0a\x10\x17\x10\x2c\x10\x41\x10\x4e\x10\x5b\x10\xd4\x10\x3d'\
b'\x11\x8e\x11\x0b\x12\x7a\x12\xb7\x12\x3a\x13\x85\x13\xd2\x13'\
b'\x1b\x14\x3a\x14\x6b\x14\x04\x15\x65\x15\xbe\x15\x3b\x16\xac'\
b'\x16\xf3\x16\x5c\x17\xad\x17\x12\x18\x3b\x18\x92\x18\xd3\x18'\
b'\x12\x19\x2b\x19\x90\x19\x9d\x19\x04\x1a\x59\x1a'

FONT = memoryview(_font)
INDEX = memoryview(_index)

