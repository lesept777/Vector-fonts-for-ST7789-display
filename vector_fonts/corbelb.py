FIRST = 32
LAST = 127
WIDTH = 35
HEIGHT = 38

_font =\
b'\x01\x4d\x57\x0b\x4d\x57\x55\x38\x54\x49\x50\x49\x4f\x38\x55'\
b'\x38\x20\x52\x4f\x4d\x55\x4d\x55\x52\x4f\x52\x4f\x4d\x0b\x4a'\
b'\x5a\x50\x43\x4c\x43\x4c\x38\x50\x38\x50\x43\x20\x52\x58\x43'\
b'\x54\x43\x54\x38\x58\x38\x58\x43\x23\x45\x5f\x4d\x3f\x4f\x38'\
b'\x52\x38\x51\x3f\x56\x3f\x57\x38\x5b\x38\x59\x3f\x5d\x3f\x5d'\
b'\x42\x59\x42\x58\x48\x5b\x48\x5b\x4b\x57\x4b\x55\x52\x52\x52'\
b'\x53\x4b\x4e\x4b\x4d\x52\x49\x52\x4b\x4b\x47\x4b\x47\x48\x4b'\
b'\x48\x4c\x42\x49\x42\x49\x3f\x4d\x3f\x20\x52\x4f\x48\x54\x48'\
b'\x55\x42\x50\x42\x4f\x48\x3b\x48\x5c\x50\x51\x4f\x51\x4b\x51'\
b'\x4a\x50\x4a\x4d\x4b\x4d\x4c\x4d\x4e\x4d\x50\x4e\x50\x4e\x50'\
b'\x49\x4f\x49\x4d\x49\x4b\x47\x4a\x45\x4a\x44\x4a\x43\x4b\x41'\
b'\x4c\x3f\x4f\x3e\x50\x3e\x50\x3c\x54\x3c\x54\x3e\x55\x3e\x58'\
b'\x3f\x59\x3f\x59\x43\x56\x42\x54\x42\x54\x46\x55\x46\x57\x47'\
b'\x59\x48\x5a\x4a\x5a\x4c\x5a\x4e\x57\x51\x54\x51\x54\x53\x50'\
b'\x53\x50\x51\x20\x52\x4e\x44\x4e\x45\x4f\x45\x50\x46\x50\x42'\
b'\x4f\x42\x4e\x43\x4e\x44\x20\x52\x56\x4c\x56\x4b\x55\x4a\x54'\
b'\x4a\x54\x4e\x56\x4d\x56\x4c\x5d\x40\x64\x5d\x4a\x5d\x49\x5d'\
b'\x47\x5d\x46\x5c\x45\x5b\x45\x5b\x45\x5a\x46\x5a\x47\x59\x49'\
b'\x59\x4a\x59\x4b\x5a\x4d\x5a\x4e\x5b\x4f\x5b\x4f\x5c\x4f\x5d'\
b'\x4e\x5d\x4d\x5d\x4b\x5d\x4a\x20\x52\x55\x4a\x55\x48\x56\x45'\
b'\x58\x42\x5a\x41\x5b\x41\x5d\x41\x5f\x42\x61\x45\x62\x48\x62'\
b'\x4a\x62\x4c\x61\x4f\x5f\x51\x5d\x52\x5b\x52\x5a\x52\x58\x51'\
b'\x56\x4f\x55\x4c\x55\x4a\x20\x52\x5d\x39\x4a\x53\x47\x51\x5a'\
b'\x37\x5d\x39\x20\x52\x4b\x40\x4b\x3f\x4a\x3d\x4a\x3c\x49\x3b'\
b'\x49\x3b\x48\x3b\x47\x3c\x47\x3d\x47\x3f\x47\x40\x47\x41\x47'\
b'\x43\x47\x44\x48\x45\x49\x45\x49\x45\x4a\x44\x4a\x43\x4b\x41'\
b'\x4b\x40\x20\x52\x42\x40\x42\x3e\x43\x3b\x45\x39\x47\x38\x49'\
b'\x38\x4a\x38\x4c\x39\x4e\x3b\x4f\x3e\x4f\x40\x4f\x42\x4e\x45'\
b'\x4c\x47\x4a\x48\x49\x48\x47\x48\x45\x47\x43\x45\x42\x42\x42'\
b'\x40\x5d\x44\x60\x5c\x44\x5c\x47\x5b\x4b\x59\x4d\x5a\x4e\x5c'\
b'\x50\x5d\x51\x5e\x52\x5e\x52\x58\x52\x58\x52\x57\x51\x56\x50'\
b'\x54\x51\x50\x52\x4e\x52\x4c\x52\x49\x51\x47\x50\x46\x4d\x46'\
b'\x4c\x46\x4a\x46\x48\x48\x46\x4a\x45\x4b\x44\x4a\x44\x49\x42'\
b'\x48\x41\x47\x3f\x47\x3e\x47\x3c\x48\x3a\x4a\x38\x4d\x38\x4f'\
b'\x38\x51\x38\x54\x38\x56\x3a\x57\x3c\x57\x3e\x57\x3f\x56\x41'\
b'\x54\x43\x53\x44\x52\x45\x53\x46\x55\x48\x56\x4a\x57\x49\x58'\
b'\x46\x58\x44\x5c\x44\x20\x52\x4e\x4f\x4f\x4f\x52\x4e\x53\x4d'\
b'\x53\x4c\x51\x4b\x50\x49\x4e\x48\x4e\x47\x4d\x48\x4c\x49\x4b'\
b'\x4a\x4a\x4b\x4a\x4b\x4a\x4c\x4b\x4d\x4c\x4e\x4d\x4f\x4e\x4f'\
b'\x20\x52\x4c\x3e\x4c\x3e\x4c\x3f\x4d\x40\x4e\x41\x4f\x42\x4f'\
b'\x41\x51\x41\x51\x40\x52\x3e\x52\x3e\x52\x3d\x50\x3b\x4f\x3b'\
b'\x4e\x3b\x4d\x3c\x4c\x3c\x4c\x3d\x4c\x3e\x05\x4e\x56\x54\x43'\
b'\x50\x43\x50\x38\x54\x38\x54\x43\x1b\x4b\x59\x4d\x48\x4d\x46'\
b'\x4e\x42\x4f\x3f\x51\x3c\x52\x39\x54\x38\x54\x37\x57\x3a\x56'\
b'\x3b\x54\x3e\x52\x41\x51\x45\x51\x48\x51\x4a\x52\x4f\x54\x52'\
b'\x56\x55\x57\x56\x54\x59\x54\x58\x52\x56\x51\x54\x4f\x51\x4e'\
b'\x4e\x4d\x4a\x4d\x48\x1b\x4b\x59\x57\x48\x57\x4a\x56\x4e\x55'\
b'\x51\x53\x54\x52\x56\x50\x58\x50\x59\x4d\x56\x4e\x55\x50\x52'\
b'\x52\x4f\x53\x4a\x53\x48\x53\x45\x52\x41\x50\x3e\x4e\x3b\x4d'\
b'\x3a\x50\x37\x50\x38\x52\x39\x53\x3c\x55\x3f\x56\x42\x57\x46'\
b'\x57\x48\x1f\x47\x5d\x53\x3f\x56\x3d\x59\x3c\x5b\x40\x57\x41'\
b'\x54\x41\x54\x41\x56\x44\x59\x47\x56\x49\x53\x46\x52\x42\x52'\
b'\x42\x51\x46\x4e\x49\x4b\x47\x4e\x44\x50\x41\x50\x41\x4d\x41'\
b'\x49\x40\x4b\x3c\x4e\x3d\x51\x3f\x51\x3f\x50\x3c\x50\x38\x54'\
b'\x38\x54\x3c\x53\x3f\x53\x3f\x0d\x48\x5c\x4a\x46\x50\x46\x50'\
b'\x3f\x54\x3f\x54\x46\x5a\x46\x5a\x4a\x54\x4a\x54\x50\x50\x50'\
b'\x50\x4a\x4a\x4a\x4a\x46\x05\x4b\x59\x51\x4d\x57\x4d\x52\x5a'\
b'\x4d\x5a\x51\x4d\x05\x4c\x58\x4e\x46\x56\x46\x56\x4a\x4e\x4a'\
b'\x4e\x46\x05\x4d\x57\x4f\x4d\x55\x4d\x55\x52\x4f\x52\x4f\x4d'\
b'\x05\x4a\x5a\x4c\x57\x54\x38\x58\x38\x50\x57\x4c\x57\x23\x47'\
b'\x5d\x56\x49\x56\x46\x54\x42\x52\x42\x50\x42\x4e\x46\x4e\x49'\
b'\x4e\x4c\x50\x4f\x52\x4f\x54\x4f\x56\x4c\x56\x49\x20\x52\x5b'\
b'\x49\x5b\x4b\x5a\x4e\x58\x51\x54\x52\x52\x52\x50\x52\x4c\x51'\
b'\x4a\x4e\x49\x4b\x49\x49\x49\x46\x4a\x43\x4c\x40\x50\x3f\x52'\
b'\x3f\x54\x3f\x58\x40\x5a\x43\x5b\x46\x5b\x49\x0c\x48\x5c\x50'\
b'\x4e\x50\x44\x4a\x46\x4a\x42\x51\x3f\x55\x3f\x55\x4e\x5a\x4e'\
b'\x5a\x52\x4a\x52\x4a\x4e\x50\x4e\x25\x48\x5c\x59\x45\x59\x46'\
b'\x58\x49\x56\x4b\x53\x4d\x51\x4e\x51\x4e\x54\x4e\x55\x4e\x5a'\
b'\x4e\x5a\x52\x4a\x52\x4a\x4f\x4c\x4e\x50\x4b\x52\x49\x54\x46'\
b'\x54\x45\x54\x44\x53\x44\x52\x43\x51\x43\x51\x43\x4f\x43\x4c'\
b'\x44\x4a\x44\x4a\x41\x4b\x40\x4c\x40\x4e\x3f\x50\x3f\x51\x3f'\
b'\x53\x3f\x56\x40\x58\x41\x59\x43\x59\x45\x3d\x48\x5c\x59\x46'\
b'\x59\x48\x58\x4b\x56\x4c\x56\x4c\x57\x4c\x58\x4d\x59\x4f\x5a'\
b'\x51\x5a\x52\x5a\x54\x59\x57\x56\x59\x52\x5a\x50\x5a\x4f\x5a'\
b'\x4e\x5a\x4c\x5a\x4b\x59\x4a\x59\x4a\x55\x4b\x55\x4e\x56\x50'\
b'\x56\x51\x56\x53\x55\x55\x54\x55\x53\x55\x52\x55\x50\x54\x4f'\
b'\x53\x4e\x53\x4e\x51\x4e\x50\x4e\x4d\x4e\x4d\x4a\x4f\x4a\x50'\
b'\x4a\x52\x4a\x52\x4a\x53\x49\x55\x47\x55\x46\x55\x45\x54\x44'\
b'\x53\x43\x51\x43\x50\x43\x4f\x43\x4c\x43\x4b\x44\x4b\x40\x4c'\
b'\x3f\x4f\x3f\x51\x3f\x53\x3f\x56\x40\x58\x42\x59\x44\x59\x46'\
b'\x13\x47\x5d\x4e\x4e\x4e\x4e\x4f\x4e\x51\x4e\x53\x4e\x53\x49'\
b'\x58\x49\x58\x4e\x5b\x4e\x5b\x52\x58\x52\x58\x5a\x53\x5a\x53'\
b'\x52\x49\x52\x49\x4f\x50\x3f\x54\x3f\x4e\x4e\x26\x48\x5c\x50'\
b'\x49\x50\x49\x51\x49\x53\x49\x56\x4a\x59\x4d\x5a\x50\x5a\x51'\
b'\x5a\x53\x59\x56\x56\x59\x52\x5a\x50\x5a\x4e\x5a\x4b\x59\x4a'\
b'\x59\x4a\x55\x4c\x56\x4e\x56\x4f\x56\x51\x56\x53\x55\x55\x54'\
b'\x55\x52\x55\x51\x55\x50\x54\x4f\x53\x4e\x51\x4d\x4f\x4d\x4e'\
b'\x4d\x4c\x4d\x4b\x4d\x4d\x3f\x5a\x3f\x5a\x43\x51\x43\x50\x49'\
b'\x38\x47\x5d\x52\x4f\x53\x4f\x55\x4e\x56\x4d\x56\x4b\x56\x4a'\
b'\x56\x49\x56\x47\x55\x46\x53\x46\x52\x46\x51\x46\x4f\x46\x4e'\
b'\x47\x4e\x49\x4e\x4c\x50\x4e\x51\x4f\x52\x4f\x20\x52\x53\x42'\
b'\x54\x42\x58\x43\x5a\x45\x5b\x48\x5b\x4a\x5b\x4c\x5a\x4f\x58'\
b'\x51\x54\x52\x52\x52\x50\x52\x4d\x51\x4a\x4e\x49\x49\x49\x47'\
b'\x49\x44\x4a\x3e\x4d\x3a\x52\x38\x55\x38\x56\x38\x59\x38\x5a'\
b'\x39\x5a\x3d\x59\x3c\x56\x3b\x55\x3b\x54\x3b\x52\x3c\x50\x3e'\
b'\x4e\x41\x4e\x43\x4e\x43\x50\x42\x53\x42\x08\x48\x5c\x4a\x43'\
b'\x4a\x3f\x5a\x3f\x5a\x42\x4f\x5a\x4b\x5a\x55\x43\x4a\x43\x4f'\
b'\x47\x5d\x52\x43\x54\x42\x56\x40\x56\x3f\x56\x3e\x55\x3d\x54'\
b'\x3c\x53\x3b\x52\x3b\x51\x3b\x50\x3c\x4f\x3d\x4e\x3e\x4e\x3f'\
b'\x4e\x40\x50\x42\x52\x43\x20\x52\x52\x4f\x53\x4f\x55\x4e\x56'\
b'\x4d\x56\x4c\x56\x4b\x56\x4a\x56\x48\x55\x47\x53\x47\x52\x46'\
b'\x51\x47\x4f\x47\x4e\x48\x4e\x4a\x4e\x4b\x4e\x4c\x4e\x4d\x4f'\
b'\x4e\x51\x4f\x52\x4f\x20\x52\x52\x52\x50\x52\x4d\x51\x4a\x4f'\
b'\x49\x4d\x49\x4b\x49\x4a\x4a\x48\x4b\x46\x4c\x45\x4d\x45\x4d'\
b'\x44\x4c\x44\x49\x41\x49\x3f\x49\x3d\x4b\x3a\x4d\x39\x50\x38'\
b'\x52\x38\x54\x38\x57\x39\x59\x3a\x5b\x3d\x5b\x3f\x5b\x41\x58'\
b'\x44\x57\x44\x57\x45\x58\x45\x59\x46\x5a\x48\x5b\x4a\x5b\x4b'\
b'\x5b\x4d\x5a\x4f\x57\x51\x54\x52\x52\x52\x39\x47\x5d\x4f\x56'\
b'\x52\x56\x56\x52\x56\x4e\x56\x4e\x55\x4f\x53\x4f\x51\x4f\x4f'\
b'\x4f\x4c\x4e\x4a\x4c\x49\x49\x49\x47\x49\x46\x4a\x42\x4c\x40'\
b'\x50\x3f\x52\x3f\x54\x3f\x57\x40\x5a\x43\x5b\x48\x5b\x4b\x5b'\
b'\x4d\x5b\x51\x59\x54\x57\x57\x55\x59\x51\x5a\x4f\x5a\x4e\x5a'\
b'\x4b\x59\x49\x59\x49\x55\x4b\x55\x4e\x56\x4f\x56\x20\x52\x52'\
b'\x4b\x53\x4b\x55\x4b\x56\x4a\x56\x48\x56\x45\x54\x43\x53\x43'\
b'\x52\x43\x51\x43\x4f\x43\x4e\x44\x4e\x46\x4e\x47\x4e\x48\x4e'\
b'\x4a\x4f\x4b\x51\x4b\x52\x4b\x0b\x4d\x57\x4f\x4d\x55\x4d\x55'\
b'\x52\x4f\x52\x4f\x4d\x20\x52\x4f\x41\x55\x41\x55\x46\x4f\x46'\
b'\x4f\x41\x0b\x4b\x59\x51\x4d\x57\x4d\x52\x5a\x4d\x5a\x51\x4d'\
b'\x20\x52\x51\x41\x56\x41\x56\x46\x51\x46\x51\x41\x09\x48\x5c'\
b'\x4a\x46\x5a\x3e\x5a\x42\x4e\x48\x4e\x48\x5a\x4d\x5a\x51\x4a'\
b'\x4a\x4a\x46\x0b\x48\x5c\x5a\x46\x4a\x46\x4a\x42\x5a\x42\x5a'\
b'\x46\x20\x52\x5a\x4d\x4a\x4d\x4a\x4a\x5a\x4a\x5a\x4d\x09\x48'\
b'\x5c\x5a\x4a\x4a\x51\x4a\x4d\x56\x48\x56\x48\x4a\x42\x4a\x3e'\
b'\x5a\x46\x5a\x4a\x31\x49\x5b\x59\x3e\x59\x3f\x59\x41\x58\x42'\
b'\x57\x43\x56\x44\x55\x44\x54\x45\x53\x46\x52\x47\x52\x48\x52'\
b'\x49\x4e\x49\x4e\x49\x4e\x48\x4e\x48\x4e\x46\x4f\x44\x50\x43'\
b'\x51\x42\x52\x41\x52\x41\x53\x40\x54\x40\x54\x3f\x54\x3e\x54'\
b'\x3d\x52\x3b\x50\x3b\x4f\x3b\x4c\x3c\x4b\x3d\x4b\x39\x4b\x39'\
b'\x4d\x38\x4f\x38\x50\x38\x51\x38\x53\x38\x56\x38\x58\x3a\x59'\
b'\x3d\x59\x3e\x20\x52\x4e\x4d\x53\x4d\x53\x52\x4e\x52\x4e\x4d'\
b'\x7b\x3f\x65\x56\x50\x56\x50\x55\x51\x53\x52\x51\x52\x50\x52'\
b'\x4f\x52\x4d\x51\x4b\x50\x4a\x4e\x4a\x4c\x4a\x4b\x4c\x49\x4d'\
b'\x47\x50\x46\x52\x46\x53\x46\x55\x46\x55\x47\x55\x46\x55\x45'\
b'\x55\x44\x54\x43\x53\x43\x51\x43\x50\x43\x4e\x43\x4c\x44\x4c'\
b'\x40\x4d\x40\x4e\x40\x4f\x3f\x51\x3f\x52\x3f\x54\x3f\x57\x40'\
b'\x59\x42\x5a\x44\x5a\x45\x5a\x4d\x5a\x4d\x5a\x4e\x5a\x4f\x5b'\
b'\x4f\x5b\x4f\x5c\x4f\x5e\x4e\x5f\x4c\x5f\x49\x5f\x47\x5f\x44'\
b'\x5d\x3f\x5a\x3c\x55\x3b\x52\x3b\x4f\x3b\x49\x3d\x46\x41\x45'\
b'\x46\x45\x49\x45\x4c\x46\x51\x4a\x55\x4f\x57\x53\x57\x55\x57'\
b'\x58\x57\x5a\x56\x5d\x55\x5d\x55\x5d\x58\x5d\x59\x5a\x59\x57'\
b'\x5a\x54\x5a\x53\x5a\x50\x5a\x4c\x59\x48\x57\x45\x54\x42\x50'\
b'\x41\x4c\x41\x49\x41\x45\x44\x3f\x48\x3a\x4e\x38\x52\x38\x56'\
b'\x38\x5c\x3a\x60\x3e\x63\x43\x63\x47\x63\x4a\x62\x4e\x5f\x51'\
b'\x5c\x52\x5a\x52\x59\x52\x58\x52\x57\x51\x56\x50\x56\x50\x56'\
b'\x50\x20\x52\x55\x4a\x55\x4a\x53\x49\x52\x49\x51\x49\x4f\x4b'\
b'\x4f\x4c\x4f\x4d\x4f\x4e\x50\x4e\x51\x4e\x52\x4e\x52\x4e\x53'\
b'\x4e\x54\x4e\x55\x4d\x55\x4d\x55\x4a\x13\x44\x60\x57\x4b\x4d'\
b'\x4b\x4b\x52\x46\x52\x50\x38\x54\x38\x5e\x52\x59\x52\x57\x4b'\
b'\x20\x52\x52\x3e\x51\x42\x50\x45\x4f\x47\x55\x47\x54\x45\x53'\
b'\x42\x52\x3e\x52\x3e\x41\x46\x5e\x5b\x3f\x5b\x41\x59\x43\x58'\
b'\x44\x58\x44\x59\x45\x5a\x46\x5b\x47\x5c\x49\x5c\x4a\x5c\x4b'\
b'\x5b\x4d\x5a\x4f\x57\x51\x55\x51\x55\x52\x54\x52\x52\x52\x51'\
b'\x52\x50\x52\x48\x52\x48\x38\x51\x38\x54\x38\x56\x39\x57\x39'\
b'\x59\x3a\x5a\x3c\x5b\x3e\x5b\x3f\x20\x52\x4d\x47\x4d\x4e\x50'\
b'\x4e\x51\x4e\x53\x4e\x54\x4e\x55\x4e\x56\x4d\x57\x4c\x57\x4b'\
b'\x57\x4a\x57\x49\x56\x47\x55\x47\x54\x47\x52\x47\x51\x47\x4d'\
b'\x47\x20\x52\x51\x43\x53\x43\x54\x42\x55\x42\x56\x40\x56\x3f'\
b'\x56\x3e\x55\x3d\x54\x3c\x53\x3c\x52\x3c\x51\x3c\x4d\x3c\x4d'\
b'\x43\x51\x43\x23\x46\x5e\x56\x3c\x54\x3c\x51\x3d\x4e\x3f\x4d'\
b'\x43\x4d\x45\x4d\x47\x4e\x4b\x51\x4d\x54\x4e\x56\x4e\x57\x4e'\
b'\x5a\x4e\x5c\x4e\x5c\x52\x5a\x52\x57\x52\x56\x52\x52\x52\x4d'\
b'\x51\x4a\x4d\x48\x48\x48\x45\x48\x43\x4a\x3d\x4d\x3a\x53\x38'\
b'\x56\x38\x57\x38\x5a\x38\x5c\x38\x5c\x3c\x5a\x3c\x57\x3c\x56'\
b'\x3c\x28\x45\x5f\x47\x52\x47\x38\x4e\x38\x4f\x38\x50\x38\x52'\
b'\x38\x54\x39\x55\x39\x57\x3a\x5a\x3c\x5c\x3f\x5d\x43\x5d\x45'\
b'\x5d\x47\x5c\x4b\x5a\x4e\x57\x50\x55\x51\x54\x51\x50\x52\x4d'\
b'\x52\x47\x52\x20\x52\x4e\x4e\x52\x4e\x54\x4d\x56\x4c\x58\x48'\
b'\x58\x45\x58\x43\x58\x41\x56\x3f\x54\x3d\x53\x3d\x52\x3c\x4f'\
b'\x3c\x4e\x3c\x4c\x3c\x4c\x4e\x4e\x4e\x0d\x47\x5d\x4e\x4e\x5b'\
b'\x4e\x5b\x52\x49\x52\x49\x38\x5a\x38\x5a\x3c\x4e\x3c\x4e\x43'\
b'\x58\x43\x58\x47\x4e\x47\x4e\x4e\x0b\x48\x5c\x4e\x52\x4a\x52'\
b'\x4a\x38\x5a\x38\x5a\x3c\x4e\x3c\x4e\x43\x59\x43\x59\x47\x4e'\
b'\x47\x4e\x52\x29\x45\x5f\x58\x48\x52\x48\x52\x44\x5d\x44\x5d'\
b'\x51\x5c\x51\x5b\x52\x58\x52\x56\x52\x55\x52\x51\x52\x4c\x51'\
b'\x49\x4d\x47\x48\x47\x46\x47\x44\x48\x40\x4a\x3d\x4c\x3a\x4f'\
b'\x38\x53\x38\x55\x38\x57\x38\x5b\x38\x5c\x39\x5c\x3d\x5b\x3c'\
b'\x58\x3c\x56\x3c\x54\x3c\x50\x3d\x4d\x3f\x4c\x43\x4c\x45\x4c'\
b'\x4a\x51\x4e\x55\x4e\x56\x4e\x58\x4e\x58\x4e\x58\x48\x0d\x45'\
b'\x5f\x4c\x43\x58\x43\x58\x38\x5d\x38\x5d\x52\x58\x52\x58\x47'\
b'\x4c\x47\x4c\x52\x47\x52\x47\x38\x4c\x38\x4c\x43\x05\x4e\x56'\
b'\x50\x52\x50\x38\x54\x38\x54\x52\x50\x52\x16\x4a\x5a\x53\x38'\
b'\x58\x38\x58\x4b\x58\x4d\x58\x4e\x57\x4f\x57\x50\x55\x51\x53'\
b'\x52\x51\x52\x50\x52\x4f\x52\x4d\x52\x4c\x52\x4c\x4e\x4d\x4e'\
b'\x4f\x4e\x50\x4e\x52\x4e\x53\x4d\x53\x4b\x53\x38\x0e\x45\x5f'\
b'\x47\x52\x47\x38\x4c\x38\x4c\x44\x4c\x44\x56\x38\x5c\x38\x51'\
b'\x45\x5d\x52\x57\x52\x4c\x46\x4c\x46\x4c\x52\x47\x52\x07\x48'\
b'\x5c\x4e\x38\x4e\x4e\x5a\x4e\x5a\x52\x4a\x52\x4a\x38\x4e\x38'\
b'\x1f\x43\x61\x52\x4b\x53\x48\x54\x44\x59\x38\x5f\x38\x5f\x52'\
b'\x5b\x52\x5b\x45\x5b\x42\x5b\x3e\x5b\x3e\x5a\x3f\x59\x42\x59'\
b'\x43\x54\x52\x50\x52\x4b\x43\x4b\x42\x4a\x3f\x49\x3e\x49\x3e'\
b'\x49\x42\x49\x45\x49\x52\x45\x52\x45\x38\x4b\x38\x50\x44\x51'\
b'\x47\x52\x4b\x52\x4b\x15\x45\x5f\x54\x44\x57\x48\x59\x4b\x59'\
b'\x4b\x59\x46\x59\x44\x59\x38\x5d\x38\x5d\x52\x58\x52\x50\x46'\
b'\x4e\x43\x4b\x3f\x4b\x3f\x4b\x44\x4b\x46\x4b\x52\x47\x52\x47'\
b'\x38\x4c\x38\x54\x44\x2b\x43\x61\x5a\x45\x5a\x43\x59\x3f\x57'\
b'\x3d\x54\x3c\x52\x3c\x50\x3c\x4d\x3d\x4b\x3f\x4a\x43\x4a\x45'\
b'\x4a\x47\x4b\x4b\x4d\x4d\x50\x4e\x52\x4e\x54\x4e\x57\x4d\x59'\
b'\x4b\x5a\x47\x5a\x45\x20\x52\x5f\x45\x5f\x48\x5d\x4d\x5a\x51'\
b'\x55\x52\x52\x52\x4f\x52\x4a\x51\x47\x4d\x45\x48\x45\x45\x45'\
b'\x42\x47\x3d\x4a\x3a\x4f\x38\x52\x38\x55\x38\x5a\x3a\x5d\x3d'\
b'\x5f\x42\x5f\x45\x25\x47\x5d\x50\x48\x4f\x48\x4e\x48\x4d\x48'\
b'\x4d\x52\x49\x52\x49\x38\x50\x38\x52\x38\x55\x38\x56\x39\x59'\
b'\x3a\x5b\x3d\x5b\x40\x5b\x42\x5a\x45\x57\x47\x53\x48\x50\x48'\
b'\x20\x52\x4d\x44\x4e\x44\x4f\x44\x50\x44\x52\x44\x54\x43\x56'\
b'\x42\x57\x41\x57\x40\x57\x3f\x55\x3d\x54\x3c\x53\x3c\x51\x3c'\
b'\x50\x3c\x4d\x3c\x4d\x44\x3b\x43\x61\x59\x45\x59\x43\x58\x3f'\
b'\x56\x3d\x53\x3c\x51\x3c\x50\x3c\x4d\x3d\x4b\x3f\x4a\x43\x4a'\
b'\x45\x4a\x47\x4b\x4b\x4d\x4d\x50\x4e\x51\x4e\x53\x4e\x56\x4d'\
b'\x58\x4b\x59\x47\x59\x45\x20\x52\x5a\x4f\x5a\x4f\x5b\x4e\x5d'\
b'\x4e\x5e\x4e\x5f\x4e\x5f\x4e\x5f\x52\x5e\x52\x5b\x52\x5a\x52'\
b'\x58\x52\x56\x52\x54\x52\x52\x52\x51\x52\x4e\x52\x4a\x50\x46'\
b'\x4d\x45\x48\x45\x45\x45\x42\x47\x3d\x4a\x3a\x4e\x38\x51\x38'\
b'\x54\x38\x59\x3a\x5c\x3d\x5e\x42\x5e\x45\x5e\x46\x5e\x49\x5c'\
b'\x4c\x5b\x4e\x5a\x4f\x5a\x4f\x24\x46\x5e\x5b\x40\x5b\x43\x58'\
b'\x46\x55\x47\x55\x47\x5c\x52\x57\x52\x50\x48\x4c\x48\x4c\x52'\
b'\x48\x52\x48\x38\x50\x38\x51\x38\x55\x38\x56\x39\x58\x3a\x5b'\
b'\x3d\x5b\x40\x20\x52\x4f\x44\x50\x44\x53\x44\x53\x43\x55\x43'\
b'\x56\x41\x56\x40\x56\x3f\x55\x3d\x54\x3d\x53\x3c\x51\x3c\x50'\
b'\x3c\x4c\x3c\x4c\x44\x4f\x44\x35\x47\x5d\x56\x4b\x56\x4a\x55'\
b'\x48\x54\x48\x52\x47\x50\x47\x4f\x47\x4c\x46\x4a\x44\x49\x41'\
b'\x49\x40\x49\x3e\x4a\x3b\x4d\x39\x50\x38\x52\x38\x54\x38\x58'\
b'\x38\x5a\x39\x5a\x3d\x58\x3c\x54\x3c\x53\x3c\x50\x3c\x4e\x3d'\
b'\x4e\x3f\x4e\x40\x4f\x41\x50\x42\x52\x43\x53\x43\x55\x43\x58'\
b'\x44\x5a\x46\x5b\x48\x5b\x4a\x5b\x4c\x5a\x50\x57\x52\x53\x52'\
b'\x50\x52\x4e\x52\x4a\x52\x49\x51\x49\x4d\x4b\x4e\x4e\x4e\x50'\
b'\x4e\x51\x4e\x54\x4e\x55\x4d\x56\x4c\x56\x4b\x09\x45\x5f\x54'\
b'\x52\x50\x52\x50\x3c\x47\x3c\x47\x38\x5d\x38\x5d\x3c\x54\x3c'\
b'\x54\x52\x21\x45\x5f\x52\x52\x50\x52\x4d\x52\x4a\x50\x48\x4e'\
b'\x48\x4d\x47\x4c\x47\x49\x47\x47\x47\x38\x4c\x38\x4c\x47\x4c'\
b'\x4a\x4d\x4b\x4d\x4d\x50\x4e\x52\x4e\x54\x4e\x57\x4d\x57\x4b'\
b'\x58\x4a\x58\x47\x58\x38\x5d\x38\x5d\x47\x5d\x49\x5d\x4c\x5c'\
b'\x4d\x5c\x4e\x5a\x50\x57\x52\x54\x52\x52\x52\x0f\x44\x60\x52'\
b'\x4c\x53\x4a\x53\x48\x54\x45\x59\x38\x5e\x38\x54\x52\x50\x52'\
b'\x46\x38\x4b\x38\x50\x45\x51\x48\x51\x4a\x52\x4c\x52\x4c\x1d'\
b'\x3e\x66\x52\x3f\x51\x42\x50\x46\x4d\x52\x49\x52\x40\x38\x45'\
b'\x38\x48\x42\x4a\x47\x4b\x4b\x4b\x4b\x4c\x47\x4d\x43\x50\x38'\
b'\x54\x38\x57\x43\x58\x47\x59\x4b\x59\x4b\x5a\x47\x5c\x42\x5f'\
b'\x38\x64\x38\x5b\x52\x57\x52\x54\x46\x53\x42\x52\x3f\x52\x3f'\
b'\x17\x44\x60\x4f\x3d\x51\x40\x52\x41\x52\x41\x53\x40\x55\x3d'\
b'\x58\x38\x5e\x38\x55\x45\x5e\x52\x59\x52\x55\x4c\x53\x4a\x52'\
b'\x48\x52\x48\x51\x4a\x4f\x4c\x4b\x52\x46\x52\x4f\x45\x46\x38'\
b'\x4c\x38\x4f\x3d\x0b\x44\x60\x52\x43\x59\x38\x5e\x38\x54\x48'\
b'\x54\x52\x50\x52\x50\x48\x46\x38\x4b\x38\x52\x43\x52\x43\x0b'\
b'\x46\x5e\x5c\x38\x5c\x3b\x4e\x4e\x5c\x4e\x5c\x52\x48\x52\x48'\
b'\x4f\x56\x3c\x48\x3c\x48\x38\x5c\x38\x09\x4c\x58\x4e\x38\x56'\
b'\x38\x56\x3b\x52\x3b\x52\x54\x56\x54\x56\x58\x4e\x58\x4e\x38'\
b'\x05\x4a\x5a\x54\x57\x4c\x38\x50\x38\x58\x57\x54\x57\x09\x4c'\
b'\x58\x56\x58\x4e\x58\x4e\x54\x52\x54\x52\x3b\x4e\x3b\x4e\x38'\
b'\x56\x38\x56\x58\x09\x47\x5d\x54\x38\x5b\x48\x57\x48\x52\x3c'\
b'\x52\x3c\x4d\x48\x49\x48\x50\x38\x54\x38\x05\x46\x5e\x48\x55'\
b'\x5c\x55\x5c\x57\x48\x57\x48\x55\x08\x4a\x5a\x55\x35\x58\x3c'\
b'\x54\x3c\x51\x35\x55\x35\x20\x52\x4c\x3f\x4c\x3f\x3f\x48\x5c'\
b'\x56\x50\x56\x50\x55\x50\x54\x51\x53\x52\x51\x52\x50\x52\x4f'\
b'\x52\x4c\x52\x4b\x50\x4a\x4e\x4a\x4c\x4a\x4b\x4b\x49\x4d\x47'\
b'\x50\x46\x51\x46\x53\x46\x55\x46\x55\x47\x55\x46\x55\x45\x55'\
b'\x44\x54\x43\x52\x42\x51\x42\x50\x42\x4d\x43\x4b\x44\x4b\x40'\
b'\x4d\x3f\x50\x3f\x52\x3f\x54\x3f\x57\x40\x59\x41\x5a\x44\x5a'\
b'\x45\x5a\x4c\x5a\x4e\x5a\x51\x5a\x52\x56\x52\x56\x50\x20\x52'\
b'\x55\x4a\x55\x4a\x53\x4a\x52\x4a\x50\x4a\x4f\x4b\x4f\x4c\x4f'\
b'\x4d\x4f\x4e\x50\x4f\x51\x4f\x51\x4f\x52\x4f\x53\x4e\x54\x4e'\
b'\x55\x4d\x55\x4d\x55\x4a\x37\x47\x5d\x5b\x48\x5b\x4b\x59\x4f'\
b'\x57\x51\x54\x52\x53\x52\x52\x52\x50\x52\x4f\x51\x4e\x50\x4d'\
b'\x50\x4d\x50\x4d\x52\x49\x52\x49\x51\x49\x4f\x49\x4e\x49\x36'\
b'\x4e\x36\x4e\x3e\x4e\x3f\x4e\x40\x4e\x40\x4e\x40\x4e\x40\x4f'\
b'\x3f\x50\x3f\x52\x3f\x53\x3f\x54\x3f\x57\x40\x5a\x42\x5b\x46'\
b'\x5b\x48\x20\x52\x56\x49\x56\x47\x55\x44\x54\x43\x52\x42\x52'\
b'\x42\x51\x42\x4f\x43\x4e\x44\x4e\x4d\x4e\x4d\x4f\x4e\x50\x4e'\
b'\x51\x4f\x52\x4f\x53\x4f\x54\x4e\x56\x4c\x56\x4a\x56\x49\x23'\
b'\x49\x5b\x59\x52\x58\x52\x56\x52\x54\x52\x52\x52\x4f\x51\x4c'\
b'\x4f\x4b\x4b\x4b\x49\x4b\x46\x4c\x42\x4f\x40\x53\x3f\x54\x3f'\
b'\x56\x3f\x58\x3f\x59\x40\x59\x43\x58\x43\x56\x42\x55\x42\x54'\
b'\x42\x52\x43\x50\x45\x4f\x47\x4f\x49\x4f\x4a\x50\x4c\x52\x4e'\
b'\x54\x4f\x55\x4f\x56\x4f\x58\x4e\x59\x4e\x59\x52\x35\x47\x5d'\
b'\x52\x4f\x53\x4f\x54\x4e\x55\x4e\x56\x4d\x56\x4d\x56\x44\x55'\
b'\x43\x53\x42\x52\x42\x52\x42\x50\x43\x4f\x44\x4e\x47\x4e\x49'\
b'\x4e\x4c\x50\x4f\x52\x4f\x20\x52\x49\x49\x49\x47\x4a\x43\x4d'\
b'\x40\x50\x3f\x51\x3f\x52\x3f\x54\x3f\x55\x3f\x56\x40\x56\x40'\
b'\x56\x40\x56\x40\x56\x3f\x56\x3e\x56\x36\x5b\x36\x5b\x4c\x5b'\
b'\x4e\x5b\x51\x5b\x52\x57\x52\x57\x50\x57\x50\x56\x50\x55\x51'\
b'\x54\x52\x52\x52\x51\x52\x4f\x52\x4d\x51\x4a\x4f\x49\x4b\x49'\
b'\x49\x2c\x47\x5d\x54\x4f\x55\x4f\x58\x4e\x5a\x4e\x5a\x51\x59'\
b'\x52\x55\x52\x53\x52\x51\x52\x4e\x51\x4b\x4f\x49\x4c\x49\x49'\
b'\x49\x46\x4b\x43\x4d\x40\x51\x3f\x52\x3f\x54\x3f\x57\x40\x59'\
b'\x42\x5b\x46\x5b\x48\x5b\x49\x5a\x4a\x4e\x4a\x4e\x4b\x4f\x4d'\
b'\x51\x4e\x53\x4f\x54\x4f\x20\x52\x52\x42\x51\x42\x50\x43\x4f'\
b'\x44\x4e\x46\x4e\x46\x56\x46\x56\x46\x55\x44\x54\x43\x53\x42'\
b'\x52\x42\x1d\x49\x5b\x59\x3a\x58\x39\x57\x39\x56\x39\x55\x39'\
b'\x54\x3a\x53\x3a\x53\x3c\x53\x3d\x53\x3f\x58\x3f\x58\x43\x53'\
b'\x43\x53\x52\x4e\x52\x4e\x43\x4b\x43\x4b\x3f\x4e\x3f\x4e\x3d'\
b'\x4e\x3b\x4f\x38\x51\x36\x54\x35\x55\x35\x56\x35\x58\x36\x59'\
b'\x36\x59\x3a\x47\x47\x5d\x56\x52\x56\x52\x56\x51\x56\x51\x56'\
b'\x51\x56\x51\x55\x52\x53\x52\x52\x52\x51\x52\x50\x52\x4d\x51'\
b'\x4a\x4f\x49\x4b\x49\x49\x49\x46\x4a\x43\x4d\x40\x50\x3f\x51'\
b'\x3f\x53\x3f\x56\x40\x57\x41\x57\x41\x57\x3f\x5b\x3f\x5b\x52'\
b'\x5b\x54\x5a\x56\x5a\x57\x59\x58\x57\x5a\x55\x5b\x52\x5c\x50'\
b'\x5c\x4f\x5c\x4d\x5b\x4c\x5b\x4b\x5b\x4a\x5b\x4a\x57\x4b\x57'\
b'\x4e\x58\x50\x58\x53\x58\x56\x55\x56\x53\x56\x52\x20\x52\x52'\
b'\x4f\x53\x4f\x54\x4e\x55\x4e\x56\x4d\x56\x4d\x56\x45\x56\x44'\
b'\x53\x42\x52\x42\x52\x42\x51\x43\x50\x43\x4f\x44\x4e\x46\x4e'\
b'\x47\x4e\x49\x4e\x4a\x4e\x4c\x4f\x4e\x51\x4f\x52\x4f\x23\x47'\
b'\x5d\x4e\x3e\x4e\x3f\x4e\x41\x4e\x42\x4e\x42\x4e\x41\x50\x40'\
b'\x51\x3f\x53\x3f\x54\x3f\x55\x3f\x57\x3f\x58\x40\x59\x41\x5a'\
b'\x42\x5a\x43\x5b\x45\x5b\x46\x5b\x52\x56\x52\x56\x47\x56\x46'\
b'\x56\x45\x56\x44\x55\x43\x54\x43\x53\x43\x51\x43\x4f\x44\x4e'\
b'\x45\x4e\x52\x49\x52\x49\x36\x4e\x36\x4e\x3e\x0b\x4e\x56\x50'\
b'\x3f\x54\x3f\x54\x52\x50\x52\x50\x3f\x20\x52\x50\x36\x54\x36'\
b'\x54\x3b\x50\x3b\x50\x36\x1c\x4b\x59\x57\x54\x57\x57\x57\x59'\
b'\x56\x5a\x52\x5c\x50\x5c\x4f\x5c\x4d\x5b\x4d\x5b\x4d\x57\x4d'\
b'\x57\x4f\x58\x4f\x58\x50\x58\x52\x57\x52\x57\x52\x56\x53\x55'\
b'\x53\x54\x53\x3f\x57\x3f\x57\x54\x20\x52\x53\x36\x57\x36\x57'\
b'\x3b\x53\x3b\x53\x36\x0e\x47\x5d\x49\x36\x4e\x36\x4e\x47\x4e'\
b'\x47\x55\x3f\x5b\x3f\x52\x48\x5b\x52\x55\x52\x4e\x49\x4e\x49'\
b'\x4e\x52\x49\x52\x49\x36\x05\x4e\x56\x50\x52\x50\x36\x54\x36'\
b'\x54\x52\x50\x52\x39\x42\x62\x5c\x47\x5c\x46\x5c\x45\x5c\x45'\
b'\x5b\x44\x5a\x43\x59\x43\x58\x43\x57\x43\x56\x44\x55\x44\x54'\
b'\x45\x54\x52\x50\x52\x50\x47\x50\x46\x50\x45\x50\x45\x4f\x44'\
b'\x4e\x43\x4d\x43\x4c\x43\x4b\x43\x4a\x44\x49\x44\x48\x45\x48'\
b'\x52\x44\x52\x44\x3f\x47\x3f\x48\x42\x48\x42\x48\x41\x4a\x40'\
b'\x4b\x3f\x4d\x3f\x4e\x3f\x50\x3f\x53\x40\x54\x42\x54\x42\x54'\
b'\x41\x56\x40\x57\x3f\x59\x3f\x5a\x3f\x5c\x3f\x5f\x40\x60\x42'\
b'\x60\x42\x60\x43\x60\x44\x60\x45\x60\x46\x60\x52\x5c\x52\x5c'\
b'\x47\x20\x47\x5d\x4e\x42\x4e\x42\x4e\x41\x4f\x40\x51\x3f\x53'\
b'\x3f\x54\x3f\x55\x3f\x57\x3f\x59\x40\x5a\x42\x5a\x43\x5a\x43'\
b'\x5b\x45\x5b\x46\x5b\x52\x56\x52\x56\x47\x56\x46\x56\x45\x56'\
b'\x44\x55\x43\x54\x43\x53\x43\x52\x43\x4f\x44\x4e\x45\x4e\x52'\
b'\x49\x52\x49\x3f\x4d\x3f\x4e\x42\x2b\x47\x5d\x57\x49\x57\x47'\
b'\x56\x45\x55\x43\x53\x42\x52\x42\x51\x42\x4f\x43\x4e\x45\x4d'\
b'\x47\x4d\x49\x4d\x4a\x4e\x4c\x4f\x4e\x51\x4f\x52\x4f\x53\x4f'\
b'\x55\x4e\x56\x4c\x57\x4a\x57\x49\x20\x52\x5b\x49\x5b\x4b\x5a'\
b'\x4e\x58\x51\x54\x52\x52\x52\x50\x52\x4c\x51\x4a\x4e\x49\x4b'\
b'\x49\x49\x49\x46\x4a\x43\x4c\x40\x50\x3f\x52\x3f\x54\x3f\x58'\
b'\x40\x5a\x43\x5b\x46\x5b\x49\x30\x47\x5d\x52\x42\x51\x42\x4f'\
b'\x44\x4e\x45\x4e\x4d\x4e\x4d\x4f\x4e\x50\x4e\x51\x4f\x52\x4f'\
b'\x53\x4f\x54\x4e\x56\x4c\x56\x4a\x56\x49\x56\x47\x56\x45\x54'\
b'\x43\x53\x42\x52\x42\x20\x52\x53\x52\x51\x52\x4f\x51\x4e\x51'\
b'\x4e\x51\x4e\x51\x4e\x52\x4e\x53\x4e\x5b\x49\x5b\x49\x3f\x4d'\
b'\x3f\x4d\x41\x4d\x41\x4e\x40\x51\x3f\x53\x3f\x54\x3f\x57\x40'\
b'\x5a\x42\x5b\x46\x5b\x48\x5b\x4b\x59\x4f\x57\x51\x54\x52\x53'\
b'\x52\x32\x47\x5d\x52\x4f\x53\x4f\x54\x4e\x55\x4e\x56\x4d\x56'\
b'\x4d\x56\x45\x56\x44\x54\x42\x52\x42\x52\x42\x50\x43\x4f\x44'\
b'\x4e\x47\x4e\x49\x4e\x4a\x4e\x4c\x4f\x4e\x51\x4f\x52\x4f\x20'\
b'\x52\x57\x41\x57\x3f\x5b\x3f\x5b\x5b\x56\x5b\x56\x53\x56\x52'\
b'\x56\x51\x56\x51\x56\x51\x56\x51\x55\x52\x53\x52\x52\x52\x51'\
b'\x52\x50\x52\x4d\x51\x4a\x4f\x49\x4b\x49\x49\x49\x46\x4a\x43'\
b'\x4d\x40\x50\x3f\x51\x3f\x53\x3f\x56\x40\x57\x41\x57\x41\x11'\
b'\x4a\x5a\x58\x43\x57\x43\x55\x43\x52\x44\x51\x45\x51\x52\x4c'\
b'\x52\x4c\x3f\x50\x3f\x51\x42\x51\x42\x52\x40\x54\x3f\x56\x3f'\
b'\x57\x3f\x58\x3f\x58\x43\x39\x49\x5b\x54\x4d\x54\x4c\x54\x4b'\
b'\x53\x4b\x51\x4a\x50\x4a\x4f\x4a\x4d\x49\x4c\x48\x4b\x46\x4b'\
b'\x45\x4b\x43\x4c\x41\x4e\x3f\x51\x3f\x52\x3f\x54\x3f\x57\x3f'\
b'\x58\x40\x58\x43\x57\x43\x56\x43\x55\x43\x53\x42\x53\x42\x52'\
b'\x42\x51\x43\x50\x43\x50\x44\x50\x44\x50\x45\x50\x46\x51\x46'\
b'\x53\x47\x53\x47\x54\x47\x56\x48\x58\x49\x59\x4b\x59\x4c\x59'\
b'\x4e\x58\x50\x56\x52\x53\x52\x51\x52\x4f\x52\x4c\x52\x4b\x51'\
b'\x4b\x4e\x4d\x4e\x4f\x4f\x50\x4f\x51\x4f\x53\x4f\x54\x4e\x54'\
b'\x4d\x54\x4d\x1c\x49\x5b\x59\x52\x58\x52\x56\x52\x55\x52\x53'\
b'\x52\x50\x51\x4f\x50\x4f\x4e\x4f\x4d\x4f\x43\x4b\x43\x4b\x3f'\
b'\x4f\x3f\x4f\x3a\x53\x3a\x53\x3f\x59\x3f\x59\x43\x53\x43\x53'\
b'\x4c\x53\x4d\x54\x4e\x54\x4f\x56\x4f\x57\x4f\x58\x4e\x59\x4e'\
b'\x59\x52\x1f\x47\x5d\x52\x52\x4f\x52\x4b\x51\x4a\x4f\x4a\x4e'\
b'\x49\x4c\x49\x4b\x49\x3f\x4e\x3f\x4e\x4a\x4e\x4b\x4e\x4d\x4f'\
b'\x4d\x4f\x4e\x51\x4f\x52\x4f\x53\x4f\x55\x4e\x55\x4d\x56\x4c'\
b'\x56\x4a\x56\x3f\x5b\x3f\x5b\x4b\x5b\x4d\x5a\x4f\x59\x4f\x58'\
b'\x51\x56\x52\x53\x52\x52\x52\x0d\x46\x5e\x5c\x3f\x54\x52\x50'\
b'\x52\x48\x3f\x4d\x3f\x50\x46\x51\x49\x52\x4c\x52\x4c\x53\x4a'\
b'\x54\x46\x57\x3f\x5c\x3f\x1d\x41\x63\x52\x44\x51\x47\x51\x4a'\
b'\x4e\x52\x4a\x52\x43\x3f\x48\x3f\x4b\x47\x4b\x4a\x4c\x4c\x4c'\
b'\x4c\x4d\x4a\x4d\x47\x50\x3f\x54\x3f\x57\x47\x57\x4a\x58\x4c'\
b'\x58\x4c\x59\x4a\x59\x47\x5c\x3f\x61\x3f\x5a\x52\x56\x52\x53'\
b'\x4a\x53\x47\x52\x44\x52\x44\x0d\x46\x5e\x52\x4b\x4d\x52\x48'\
b'\x52\x4f\x48\x48\x3f\x4e\x3f\x52\x45\x57\x3f\x5c\x3f\x55\x48'\
b'\x5c\x52\x57\x52\x52\x4b\x0e\x46\x5e\x48\x3f\x4d\x3f\x50\x46'\
b'\x51\x4a\x52\x4c\x52\x4c\x53\x4a\x54\x46\x57\x3f\x5c\x3f\x50'\
b'\x5b\x4b\x5b\x50\x51\x48\x3f\x0b\x48\x5c\x53\x43\x4a\x43\x4a'\
b'\x3f\x59\x3f\x59\x42\x50\x4e\x5a\x4e\x5a\x52\x4a\x52\x4a\x4f'\
b'\x53\x43\x49\x4b\x59\x51\x48\x52\x48\x53\x49\x54\x4a\x54\x4b'\
b'\x54\x4c\x54\x4d\x54\x4f\x54\x4f\x53\x50\x52\x52\x52\x52\x52'\
b'\x54\x54\x55\x56\x55\x57\x55\x57\x58\x56\x58\x54\x58\x51\x58'\
b'\x4f\x56\x4e\x54\x4e\x53\x4e\x52\x4e\x51\x4f\x50\x4f\x4f\x50'\
b'\x4f\x50\x4e\x51\x4d\x51\x4c\x51\x4b\x50\x4a\x4f\x4a\x4e\x49'\
b'\x4d\x49\x4d\x46\x4e\x46\x4f\x46\x50\x46\x51\x45\x51\x44\x51'\
b'\x43\x50\x42\x4f\x41\x4f\x40\x4e\x3e\x4e\x3d\x4e\x3c\x4f\x3a'\
b'\x51\x38\x54\x38\x56\x38\x57\x38\x57\x3b\x56\x3b\x54\x3b\x52'\
b'\x3c\x52\x3d\x52\x3e\x53\x3f\x53\x40\x53\x40\x54\x41\x54\x42'\
b'\x54\x43\x54\x44\x54\x45\x54\x46\x53\x47\x52\x48\x51\x48\x51'\
b'\x48\x05\x4e\x56\x54\x5b\x50\x5b\x50\x36\x54\x36\x54\x5b\x49'\
b'\x4b\x59\x53\x48\x52\x48\x51\x47\x50\x46\x50\x45\x50\x44\x50'\
b'\x43\x50\x42\x50\x41\x51\x40\x51\x40\x51\x3f\x52\x3e\x52\x3d'\
b'\x52\x3c\x50\x3b\x4e\x3b\x4d\x3b\x4d\x38\x4e\x38\x50\x38\x53'\
b'\x38\x55\x3a\x56\x3c\x56\x3d\x56\x3e\x55\x40\x55\x41\x54\x42'\
b'\x53\x43\x53\x44\x53\x45\x54\x46\x55\x46\x56\x46\x57\x46\x57'\
b'\x49\x56\x49\x55\x4a\x54\x4a\x53\x4b\x53\x4c\x53\x4d\x54\x4e'\
b'\x54\x4f\x55\x4f\x55\x50\x56\x51\x56\x52\x56\x53\x56\x54\x55'\
b'\x56\x53\x58\x50\x58\x4e\x58\x4d\x58\x4d\x55\x4e\x55\x50\x55'\
b'\x52\x54\x52\x52\x52\x52\x51\x50\x50\x4f\x50\x4f\x50\x4d\x50'\
b'\x4c\x50\x4b\x50\x4a\x51\x49\x52\x48\x53\x48\x53\x48\x1b\x47'\
b'\x5d\x49\x49\x4a\x48\x4d\x46\x4f\x46\x50\x46\x51\x47\x52\x47'\
b'\x53\x47\x55\x48\x55\x48\x56\x48\x58\x47\x58\x46\x5b\x48\x5a'\
b'\x4a\x57\x4c\x55\x4c\x55\x4c\x53\x4b\x52\x4b\x51\x4a\x4f\x4a'\
b'\x4f\x4a\x4e\x4a\x4c\x4b\x4c\x4b\x49\x49\x39\x47\x5d\x5b\x38'\
b'\x5b\x52\x49\x52\x49\x38\x5b\x38\x20\x52\x59\x50\x59\x3a\x4b'\
b'\x3a\x4b\x50\x59\x50\x20\x52\x50\x4e\x50\x4b\x52\x4b\x52\x4e'\
b'\x50\x4e\x20\x52\x57\x41\x57\x41\x56\x42\x56\x43\x55\x44\x55'\
b'\x44\x54\x45\x53\x45\x52\x46\x52\x47\x52\x48\x52\x48\x50\x48'\
b'\x50\x48\x50\x48\x50\x48\x50\x47\x51\x45\x52\x44\x53\x44\x53'\
b'\x43\x54\x43\x55\x42\x55\x41\x55\x40\x53\x3e\x52\x3e\x51\x3e'\
b'\x4f\x3f\x4e\x3f\x4e\x3e\x4f\x3d\x51\x3d\x52\x3d\x53\x3d\x55'\
b'\x3d\x56\x3e\x57\x40\x57\x41'

_index =\
b'\x00\x00\x03\x00\x1c\x00\x35\x00\x7e\x00\xf7\x00\xb4\x01\x71'\
b'\x02\x7e\x02\xb7\x02\xf0\x02\x31\x03\x4e\x03\x5b\x03\x68\x03'\
b'\x75\x03\x82\x03\xcb\x03\xe6\x03\x33\x04\xb0\x04\xd9\x04\x28'\
b'\x05\x9b\x05\xae\x05\x4f\x06\xc4\x06\xdd\x06\xf6\x06\x0b\x07'\
b'\x24\x07\x39\x07\x9e\x07\x97\x08\xc0\x08\x45\x09\x8e\x09\xe1'\
b'\x09\xfe\x09\x17\x0a\x6c\x0a\x89\x0a\x96\x0a\xc5\x0a\xe4\x0a'\
b'\xf5\x0a\x36\x0b\x63\x0b\xbc\x0b\x09\x0c\x82\x0c\xcd\x0c\x3a'\
b'\x0d\x4f\x0d\x94\x0d\xb5\x0d\xf2\x0d\x23\x0e\x3c\x0e\x55\x0e'\
b'\x6a\x0e\x77\x0e\x8c\x0e\xa1\x0e\xae\x0e\xc1\x0e\x42\x0f\xb3'\
b'\x0f\xfc\x0f\x69\x10\xc4\x10\x01\x11\x92\x11\xdb\x11\xf4\x11'\
b'\x2f\x12\x4e\x12\x5b\x12\xd0\x12\x13\x13\x6c\x13\xcf\x13\x36'\
b'\x14\x5b\x14\xd0\x14\x0b\x15\x4c\x15\x69\x15\xa6\x15\xc3\x15'\
b'\xe2\x15\xfb\x15\x90\x16\x9d\x16\x32\x17\x6b\x17'

FONT = memoryview(_font)
INDEX = memoryview(_index)

