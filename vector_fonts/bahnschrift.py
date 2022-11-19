FIRST = 32
LAST = 127
WIDTH = 26
HEIGHT = 30

_font =\
b'\x01\x4f\x55\x0b\x4e\x56\x50\x3c\x54\x3c\x54\x4c\x50\x4c\x50'\
b'\x3c\x20\x52\x50\x4f\x54\x4f\x54\x52\x50\x52\x50\x4f\x0b\x4c'\
b'\x58\x4e\x3c\x51\x3c\x51\x44\x4e\x44\x4e\x3c\x20\x52\x53\x3c'\
b'\x56\x3c\x56\x44\x53\x44\x53\x3c\x17\x47\x5d\x56\x3c\x58\x3c'\
b'\x54\x52\x52\x52\x56\x3c\x20\x52\x4f\x3c\x52\x3c\x4e\x52\x4b'\
b'\x52\x4f\x3c\x20\x52\x5b\x41\x5b\x44\x4a\x44\x4a\x41\x5b\x41'\
b'\x20\x52\x5a\x4a\x5a\x4d\x49\x4d\x49\x4a\x5a\x4a\x49\x48\x5c'\
b'\x50\x52\x4e\x52\x4b\x50\x4a\x4f\x4a\x4f\x4d\x4c\x4d\x4c\x4e'\
b'\x4e\x50\x4f\x52\x4f\x54\x4f\x56\x4d\x56\x4c\x56\x4c\x56\x4b'\
b'\x55\x49\x54\x49\x52\x48\x52\x48\x52\x48\x52\x48\x52\x48\x52'\
b'\x48\x52\x48\x50\x48\x4d\x47\x4b\x44\x4b\x42\x4b\x42\x4b\x40'\
b'\x4d\x3d\x50\x3b\x53\x3b\x54\x3b\x56\x3c\x58\x3d\x59\x3d\x59'\
b'\x3d\x57\x40\x57\x40\x56\x3f\x54\x3f\x53\x3f\x51\x3f\x4f\x40'\
b'\x4f\x42\x4f\x42\x4f\x43\x50\x44\x52\x45\x53\x45\x53\x45\x53'\
b'\x45\x53\x45\x53\x45\x54\x45\x54\x45\x55\x46\x58\x47\x5a\x4a'\
b'\x5a\x4c\x5a\x4c\x5a\x4e\x58\x51\x54\x52\x52\x52\x50\x52\x20'\
b'\x52\x51\x39\x54\x39\x54\x55\x51\x55\x51\x39\x45\x47\x5d\x57'\
b'\x3c\x59\x3c\x4d\x52\x4a\x52\x57\x3c\x20\x52\x56\x52\x54\x50'\
b'\x54\x4e\x54\x4c\x54\x4b\x56\x48\x58\x48\x59\x48\x5b\x4b\x5b'\
b'\x4c\x5b\x4e\x5b\x50\x59\x52\x58\x52\x56\x52\x20\x52\x58\x50'\
b'\x59\x4f\x59\x4e\x59\x4c\x59\x4c\x58\x4b\x58\x4b\x57\x4b\x56'\
b'\x4c\x56\x4c\x56\x4e\x56\x4f\x57\x50\x58\x50\x58\x50\x20\x52'\
b'\x4b\x45\x49\x43\x49\x41\x49\x3f\x49\x3e\x4b\x3b\x4c\x3b\x4e'\
b'\x3b\x50\x3e\x50\x3f\x50\x41\x50\x43\x4e\x45\x4c\x45\x4b\x45'\
b'\x20\x52\x4d\x43\x4e\x42\x4e\x41\x4e\x3f\x4e\x3f\x4d\x3e\x4c'\
b'\x3e\x4c\x3e\x4b\x3f\x4b\x3f\x4b\x41\x4b\x42\x4c\x43\x4c\x43'\
b'\x4d\x43\x34\x47\x5d\x4f\x49\x4d\x48\x4c\x46\x4b\x43\x4b\x42'\
b'\x4b\x3f\x4e\x3c\x51\x3c\x54\x3c\x57\x3f\x57\x41\x57\x42\x54'\
b'\x42\x54\x41\x54\x40\x52\x3f\x51\x3f\x50\x3f\x4e\x40\x4e\x42'\
b'\x4e\x43\x4f\x44\x50\x46\x51\x47\x5b\x52\x57\x52\x4f\x49\x20'\
b'\x52\x4e\x48\x4c\x4a\x4c\x4c\x4c\x4e\x4e\x4f\x50\x4f\x52\x4f'\
b'\x55\x4d\x56\x49\x56\x47\x59\x47\x59\x4a\x57\x50\x53\x52\x50'\
b'\x52\x4d\x52\x4b\x51\x49\x4e\x49\x4c\x49\x49\x4c\x46\x4f\x46'\
b'\x50\x48\x4e\x48\x05\x4e\x56\x50\x3c\x54\x3c\x54\x44\x50\x44'\
b'\x50\x3c\x0f\x4c\x58\x51\x54\x4e\x4c\x4e\x48\x4e\x44\x51\x3c'\
b'\x54\x39\x56\x3b\x53\x3e\x51\x44\x51\x48\x51\x4c\x53\x52\x56'\
b'\x55\x54\x57\x51\x54\x0f\x4c\x58\x4e\x55\x51\x52\x53\x4c\x53'\
b'\x48\x53\x44\x51\x3e\x4e\x3b\x50\x39\x53\x3c\x56\x44\x56\x48'\
b'\x56\x4c\x53\x54\x50\x57\x4e\x55\x1d\x4a\x5a\x51\x41\x53\x3f'\
b'\x56\x44\x54\x45\x51\x41\x20\x52\x4e\x44\x51\x3f\x53\x41\x50'\
b'\x45\x4e\x44\x20\x52\x4c\x3f\x4d\x3d\x52\x3f\x52\x41\x4c\x3f'\
b'\x20\x52\x51\x3a\x53\x3a\x53\x40\x51\x40\x51\x3a\x20\x52\x52'\
b'\x3f\x57\x3d\x58\x3f\x52\x41\x52\x3f\x0b\x4a\x5a\x58\x46\x58'\
b'\x49\x4c\x49\x4c\x46\x58\x46\x20\x52\x54\x4e\x50\x4e\x50\x41'\
b'\x54\x41\x54\x4e\x05\x4e\x56\x50\x4f\x54\x4f\x54\x54\x50\x57'\
b'\x50\x4f\x05\x4b\x59\x57\x49\x57\x4b\x4d\x4b\x4d\x49\x57\x49'\
b'\x05\x4e\x56\x50\x4f\x54\x4f\x54\x52\x50\x52\x50\x4f\x05\x49'\
b'\x5b\x4e\x56\x4b\x56\x56\x39\x59\x39\x4e\x56\x1f\x4a\x5a\x4f'\
b'\x52\x4c\x4f\x4c\x4c\x4c\x42\x4c\x3f\x4f\x3b\x52\x3b\x55\x3b'\
b'\x58\x3f\x58\x42\x58\x4c\x58\x4f\x55\x52\x52\x52\x4f\x52\x20'\
b'\x52\x54\x4f\x55\x4e\x55\x4c\x55\x42\x55\x40\x54\x3e\x52\x3e'\
b'\x50\x3e\x4f\x40\x4f\x42\x4f\x4c\x4f\x4e\x50\x4f\x52\x4f\x54'\
b'\x4f\x08\x4d\x57\x55\x52\x52\x52\x52\x3f\x4f\x41\x4f\x3e\x52'\
b'\x3c\x55\x3c\x55\x52\x20\x4a\x5a\x4c\x4f\x54\x45\x54\x44\x55'\
b'\x42\x55\x41\x55\x41\x55\x40\x53\x3e\x52\x3e\x51\x3e\x4f\x40'\
b'\x4f\x42\x4f\x42\x4c\x42\x4c\x42\x4c\x40\x4e\x3d\x50\x3b\x52'\
b'\x3b\x54\x3b\x57\x3d\x58\x3f\x58\x41\x58\x41\x58\x42\x57\x45'\
b'\x56\x46\x50\x4f\x58\x4f\x58\x52\x4c\x52\x4c\x4f\x37\x49\x5b'\
b'\x50\x52\x4d\x51\x4c\x4e\x4b\x4c\x4b\x4c\x4f\x4c\x4f\x4c\x4f'\
b'\x4d\x50\x4f\x51\x4f\x52\x4f\x54\x4f\x55\x4e\x55\x4c\x55\x4b'\
b'\x55\x4a\x54\x48\x52\x48\x51\x48\x51\x45\x52\x45\x54\x45\x55'\
b'\x43\x55\x42\x55\x41\x55\x40\x54\x3e\x52\x3e\x51\x3e\x50\x3f'\
b'\x4f\x40\x4f\x41\x4f\x41\x4c\x41\x4c\x41\x4c\x3f\x4e\x3d\x50'\
b'\x3b\x52\x3b\x55\x3b\x58\x3e\x58\x41\x58\x42\x58\x43\x56\x46'\
b'\x55\x46\x57\x47\x59\x4a\x59\x4c\x59\x4c\x59\x4e\x57\x51\x54'\
b'\x52\x52\x52\x50\x52\x0e\x49\x5b\x4b\x4c\x52\x3c\x56\x3c\x4e'\
b'\x4c\x59\x4c\x59\x4f\x4b\x4f\x4b\x4c\x20\x52\x54\x45\x58\x45'\
b'\x58\x52\x54\x52\x54\x45\x27\x4a\x5a\x50\x52\x4e\x51\x4c\x4e'\
b'\x4c\x4d\x4c\x4d\x4f\x4d\x4f\x4d\x4f\x4e\x51\x4f\x52\x4f\x53'\
b'\x4f\x55\x4d\x55\x4b\x55\x4a\x55\x48\x53\x46\x52\x46\x51\x46'\
b'\x50\x47\x4f\x47\x4c\x47\x4c\x3c\x58\x3c\x58\x3f\x4f\x3f\x4f'\
b'\x44\x50\x43\x51\x43\x52\x43\x54\x43\x57\x44\x58\x47\x58\x4a'\
b'\x58\x4b\x58\x4e\x57\x51\x54\x52\x52\x52\x50\x52\x2c\x4a\x5a'\
b'\x50\x52\x4d\x51\x4c\x4e\x4c\x4b\x4c\x4b\x4c\x4a\x4c\x48\x4d'\
b'\x46\x4d\x46\x4d\x46\x4d\x45\x52\x3c\x56\x3c\x50\x47\x50\x46'\
b'\x50\x46\x52\x45\x53\x45\x54\x45\x57\x46\x58\x49\x58\x4b\x58'\
b'\x4b\x58\x4e\x57\x51\x54\x52\x52\x52\x50\x52\x20\x52\x53\x4f'\
b'\x55\x4d\x55\x4c\x55\x4c\x55\x4a\x53\x48\x52\x48\x50\x48\x4f'\
b'\x4a\x4f\x4c\x4f\x4c\x4f\x4d\x51\x4f\x52\x4f\x53\x4f\x0a\x4a'\
b'\x5a\x58\x3e\x52\x52\x4f\x52\x55\x3f\x4f\x3f\x4f\x42\x4c\x42'\
b'\x4c\x3c\x58\x3c\x58\x3e\x49\x49\x5b\x50\x52\x4d\x51\x4b\x4e'\
b'\x4b\x4c\x4b\x4c\x4b\x4a\x4d\x47\x4e\x46\x4d\x46\x4c\x43\x4c'\
b'\x42\x4c\x41\x4c\x40\x4d\x3d\x50\x3b\x52\x3b\x54\x3b\x57\x3d'\
b'\x58\x40\x58\x41\x58\x42\x58\x43\x57\x46\x56\x46\x57\x47\x59'\
b'\x4a\x59\x4c\x59\x4c\x59\x4e\x57\x51\x54\x52\x52\x52\x50\x52'\
b'\x20\x52\x53\x4f\x55\x4e\x56\x4d\x56\x4c\x56\x4c\x56\x4b\x55'\
b'\x49\x53\x48\x52\x48\x51\x48\x4f\x49\x4e\x4b\x4e\x4c\x4e\x4c'\
b'\x4e\x4d\x4f\x4e\x51\x4f\x52\x4f\x53\x4f\x20\x52\x53\x45\x54'\
b'\x44\x55\x43\x55\x42\x55\x42\x55\x41\x54\x3f\x53\x3e\x52\x3e'\
b'\x51\x3e\x50\x3f\x4f\x41\x4f\x42\x4f\x42\x4f\x43\x50\x44\x51'\
b'\x45\x52\x45\x53\x45\x2c\x4a\x5a\x54\x47\x54\x47\x54\x48\x52'\
b'\x49\x51\x49\x50\x49\x4d\x47\x4c\x44\x4c\x42\x4c\x42\x4c\x40'\
b'\x4d\x3d\x50\x3b\x52\x3b\x54\x3b\x57\x3d\x58\x40\x58\x42\x58'\
b'\x42\x58\x44\x58\x46\x57\x48\x57\x48\x57\x48\x57\x48\x52\x52'\
b'\x4f\x52\x54\x47\x20\x52\x53\x46\x55\x44\x55\x42\x55\x42\x55'\
b'\x40\x53\x3e\x52\x3e\x51\x3e\x4f\x40\x4f\x42\x4f\x42\x4f\x44'\
b'\x51\x46\x52\x46\x53\x46\x0e\x46\x5e\x51\x3c\x53\x3c\x5c\x52'\
b'\x58\x52\x52\x40\x4c\x52\x48\x52\x51\x3c\x20\x52\x4c\x4a\x58'\
b'\x4a\x58\x4d\x4c\x4d\x4c\x4a\x0b\x4e\x56\x50\x3c\x54\x3c\x54'\
b'\x4c\x50\x4c\x50\x3c\x20\x52\x50\x4f\x54\x4f\x54\x52\x50\x52'\
b'\x50\x4f\x0b\x4c\x58\x4e\x3c\x51\x3c\x51\x44\x4e\x44\x4e\x3c'\
b'\x20\x52\x53\x3c\x56\x3c\x56\x44\x53\x44\x53\x3c\x17\x47\x5d'\
b'\x56\x3c\x58\x3c\x54\x52\x52\x52\x56\x3c\x20\x52\x4f\x3c\x52'\
b'\x3c\x4e\x52\x4b\x52\x4f\x3c\x20\x52\x5b\x41\x5b\x44\x4a\x44'\
b'\x4a\x41\x5b\x41\x20\x52\x5a\x4a\x5a\x4d\x49\x4d\x49\x4a\x5a'\
b'\x4a\x49\x48\x5c\x50\x52\x4e\x52\x4b\x50\x4a\x4f\x4a\x4f\x4d'\
b'\x4c\x4d\x4c\x4e\x4e\x50\x4f\x52\x4f\x54\x4f\x56\x4d\x56\x4c'\
b'\x56\x4c\x56\x4b\x55\x49\x54\x49\x52\x48\x52\x48\x52\x48\x52'\
b'\x48\x52\x48\x52\x48\x52\x48\x50\x48\x4d\x47\x4b\x44\x4b\x42'\
b'\x4b\x42\x4b\x40\x4d\x3d\x50\x3b\x53\x3b\x54\x3b\x56\x3c\x58'\
b'\x3d\x59\x3d\x59\x3d\x57\x40\x57\x40\x56\x3f\x54\x3f\x53\x3f'\
b'\x51\x3f\x4f\x40\x4f\x42\x4f\x42\x4f\x43\x50\x44\x52\x45\x53'\
b'\x45\x53\x45\x53\x45\x53\x45\x53\x45\x54\x45\x54\x45\x55\x46'\
b'\x58\x47\x5a\x4a\x5a\x4c\x5a\x4c\x5a\x4e\x58\x51\x54\x52\x52'\
b'\x52\x50\x52\x20\x52\x51\x39\x54\x39\x54\x55\x51\x55\x51\x39'\
b'\x45\x47\x5d\x57\x3c\x59\x3c\x4d\x52\x4a\x52\x57\x3c\x20\x52'\
b'\x56\x52\x54\x50\x54\x4e\x54\x4c\x54\x4b\x56\x48\x58\x48\x59'\
b'\x48\x5b\x4b\x5b\x4c\x5b\x4e\x5b\x50\x59\x52\x58\x52\x56\x52'\
b'\x20\x52\x58\x50\x59\x4f\x59\x4e\x59\x4c\x59\x4c\x58\x4b\x58'\
b'\x4b\x57\x4b\x56\x4c\x56\x4c\x56\x4e\x56\x4f\x57\x50\x58\x50'\
b'\x58\x50\x20\x52\x4b\x45\x49\x43\x49\x41\x49\x3f\x49\x3e\x4b'\
b'\x3b\x4c\x3b\x4e\x3b\x50\x3e\x50\x3f\x50\x41\x50\x43\x4e\x45'\
b'\x4c\x45\x4b\x45\x20\x52\x4d\x43\x4e\x42\x4e\x41\x4e\x3f\x4e'\
b'\x3f\x4d\x3e\x4c\x3e\x4c\x3e\x4b\x3f\x4b\x3f\x4b\x41\x4b\x42'\
b'\x4c\x43\x4c\x43\x4d\x43\x34\x47\x5d\x4f\x49\x4d\x48\x4c\x46'\
b'\x4b\x43\x4b\x42\x4b\x3f\x4e\x3c\x51\x3c\x54\x3c\x57\x3f\x57'\
b'\x41\x57\x42\x54\x42\x54\x41\x54\x40\x52\x3f\x51\x3f\x50\x3f'\
b'\x4e\x40\x4e\x42\x4e\x43\x4f\x44\x50\x46\x51\x47\x5b\x52\x57'\
b'\x52\x4f\x49\x20\x52\x4e\x48\x4c\x4a\x4c\x4c\x4c\x4e\x4e\x4f'\
b'\x50\x4f\x52\x4f\x55\x4d\x56\x49\x56\x47\x59\x47\x59\x4a\x57'\
b'\x50\x53\x52\x50\x52\x4d\x52\x4b\x51\x49\x4e\x49\x4c\x49\x49'\
b'\x4c\x46\x4f\x46\x50\x48\x4e\x48\x05\x4e\x56\x50\x3c\x54\x3c'\
b'\x54\x44\x50\x44\x50\x3c\x0f\x4c\x58\x51\x54\x4e\x4c\x4e\x48'\
b'\x4e\x44\x51\x3c\x54\x39\x56\x3b\x53\x3e\x51\x44\x51\x48\x51'\
b'\x4c\x53\x52\x56\x55\x54\x57\x51\x54\x0f\x4c\x58\x4e\x55\x51'\
b'\x52\x53\x4c\x53\x48\x53\x44\x51\x3e\x4e\x3b\x50\x39\x53\x3c'\
b'\x56\x44\x56\x48\x56\x4c\x53\x54\x50\x57\x4e\x55\x1d\x4a\x5a'\
b'\x51\x41\x53\x3f\x56\x44\x54\x45\x51\x41\x20\x52\x4e\x44\x51'\
b'\x3f\x53\x41\x50\x45\x4e\x44\x20\x52\x4c\x3f\x4d\x3d\x52\x3f'\
b'\x52\x41\x4c\x3f\x20\x52\x51\x3a\x53\x3a\x53\x40\x51\x40\x51'\
b'\x3a\x20\x52\x52\x3f\x57\x3d\x58\x3f\x52\x41\x52\x3f\x0b\x4a'\
b'\x5a\x58\x46\x58\x49\x4c\x49\x4c\x46\x58\x46\x20\x52\x54\x4e'\
b'\x50\x4e\x50\x41\x54\x41\x54\x4e\x05\x4e\x56\x50\x4f\x54\x4f'\
b'\x54\x54\x50\x57\x50\x4f\x05\x4b\x59\x57\x49\x57\x4b\x4d\x4b'\
b'\x4d\x49\x57\x49\x05\x4e\x56\x50\x4f\x54\x4f\x54\x52\x50\x52'\
b'\x50\x4f\x05\x49\x5b\x4e\x56\x4b\x56\x56\x39\x59\x39\x4e\x56'\
b'\x0b\x4e\x56\x50\x4f\x54\x4f\x54\x52\x50\x52\x50\x4f\x20\x52'\
b'\x50\x42\x54\x42\x54\x45\x50\x45\x50\x42\x0b\x4e\x56\x50\x4f'\
b'\x54\x4f\x54\x54\x50\x57\x50\x4f\x20\x52\x50\x42\x54\x42\x54'\
b'\x45\x50\x45\x50\x42\x0b\x4b\x59\x52\x48\x4d\x48\x57\x42\x57'\
b'\x45\x52\x48\x20\x52\x57\x4e\x4d\x48\x52\x48\x57\x4a\x57\x4e'\
b'\x0b\x4b\x59\x4d\x44\x57\x44\x57\x47\x4d\x47\x4d\x44\x20\x52'\
b'\x4d\x49\x57\x49\x57\x4c\x4d\x4c\x4d\x49\x0b\x4b\x59\x4d\x42'\
b'\x57\x48\x52\x48\x4d\x45\x4d\x42\x20\x52\x52\x48\x57\x48\x4d'\
b'\x4e\x4d\x4a\x52\x48\x2b\x4a\x5a\x50\x4b\x51\x48\x52\x46\x53'\
b'\x45\x53\x44\x54\x43\x55\x42\x55\x41\x55\x41\x55\x40\x53\x3e'\
b'\x52\x3e\x51\x3e\x4f\x40\x4f\x42\x4f\x42\x4c\x42\x4c\x42\x4c'\
b'\x40\x4e\x3d\x50\x3b\x52\x3b\x54\x3b\x56\x3d\x58\x3f\x58\x41'\
b'\x58\x41\x58\x42\x57\x44\x56\x45\x56\x46\x55\x47\x54\x49\x53'\
b'\x4b\x53\x4c\x50\x4c\x50\x4b\x20\x52\x50\x4f\x53\x4f\x53\x52'\
b'\x50\x52\x50\x4f\x51\x44\x60\x4f\x52\x4c\x4f\x4c\x4b\x4c\x49'\
b'\x4c\x45\x4f\x42\x52\x42\x55\x42\x58\x45\x58\x49\x58\x4e\x56'\
b'\x4f\x56\x50\x53\x52\x51\x52\x4f\x52\x20\x52\x54\x4f\x55\x4d'\
b'\x55\x4b\x55\x49\x55\x47\x54\x45\x52\x45\x4f\x45\x4f\x49\x4f'\
b'\x4b\x4f\x4d\x50\x4f\x52\x4f\x54\x4f\x20\x52\x4e\x58\x49\x55'\
b'\x46\x50\x46\x4c\x46\x4b\x46\x49\x46\x48\x46\x44\x49\x3f\x4e'\
b'\x3c\x52\x3c\x56\x3c\x5b\x3f\x5e\x44\x5e\x48\x5e\x4d\x5e\x50'\
b'\x5b\x52\x59\x52\x57\x52\x55\x50\x55\x4d\x58\x4d\x58\x4e\x59'\
b'\x50\x59\x50\x5a\x50\x5b\x4f\x5b\x4d\x5b\x48\x5b\x45\x59\x41'\
b'\x55\x3f\x52\x3f\x4f\x3f\x4b\x41\x49\x45\x49\x48\x49\x49\x49'\
b'\x4b\x49\x4c\x49\x4f\x4b\x53\x4f\x55\x52\x55\x57\x55\x57\x58'\
b'\x52\x58\x4e\x58\x0e\x46\x5e\x51\x3c\x53\x3c\x5c\x52\x58\x52'\
b'\x52\x40\x4c\x52\x48\x52\x51\x3c\x20\x52\x4c\x4a\x58\x4a\x58'\
b'\x4d\x4c\x4d\x4c\x4a\x31\x48\x5c\x4c\x4f\x52\x4f\x54\x4f\x57'\
b'\x4d\x57\x4c\x57\x4c\x57\x4a\x56\x49\x54\x48\x53\x48\x4c\x48'\
b'\x4c\x45\x53\x45\x55\x45\x56\x44\x56\x42\x56\x42\x56\x40\x54'\
b'\x3f\x52\x3f\x4c\x3f\x4c\x3c\x53\x3c\x55\x3c\x58\x3d\x5a\x40'\
b'\x5a\x42\x5a\x42\x5a\x43\x59\x45\x57\x46\x55\x47\x57\x47\x59'\
b'\x48\x5a\x4b\x5a\x4c\x5a\x4c\x5a\x4e\x58\x50\x55\x52\x53\x52'\
b'\x4c\x52\x4c\x4f\x20\x52\x4a\x3c\x4d\x3c\x4d\x52\x4a\x52\x4a'\
b'\x3c\x29\x48\x5c\x50\x52\x4c\x50\x4a\x4c\x4a\x4a\x4a\x44\x4a'\
b'\x41\x4c\x3e\x50\x3b\x52\x3b\x54\x3b\x57\x3d\x59\x40\x5a\x42'\
b'\x5a\x42\x57\x42\x57\x42\x56\x41\x55\x3f\x53\x3f\x52\x3f\x51'\
b'\x3f\x4f\x40\x4d\x42\x4d\x44\x4d\x4a\x4d\x4b\x4f\x4e\x51\x4f'\
b'\x52\x4f\x53\x4f\x55\x4e\x56\x4d\x57\x4c\x57\x4c\x5a\x4c\x5a'\
b'\x4c\x59\x4e\x57\x51\x54\x52\x52\x52\x50\x52\x1d\x48\x5c\x4c'\
b'\x4f\x51\x4f\x54\x4f\x57\x4c\x57\x4a\x57\x44\x57\x41\x54\x3f'\
b'\x51\x3f\x4c\x3f\x4c\x3c\x51\x3c\x54\x3c\x58\x3e\x5a\x41\x5a'\
b'\x44\x5a\x4a\x5a\x4d\x58\x50\x54\x52\x51\x52\x4c\x52\x4c\x4f'\
b'\x20\x52\x4a\x3c\x4d\x3c\x4d\x52\x4a\x52\x4a\x3c\x17\x49\x5b'\
b'\x4b\x3c\x4e\x3c\x4e\x52\x4b\x52\x4b\x3c\x20\x52\x4c\x4f\x59'\
b'\x4f\x59\x52\x4c\x52\x4c\x4f\x20\x52\x4c\x45\x57\x45\x57\x48'\
b'\x4c\x48\x4c\x45\x20\x52\x4c\x3c\x59\x3c\x59\x3f\x4c\x3f\x4c'\
b'\x3c\x11\x49\x5b\x4b\x3c\x4e\x3c\x4e\x52\x4b\x52\x4b\x3c\x20'\
b'\x52\x4d\x46\x57\x46\x57\x49\x4d\x49\x4d\x46\x20\x52\x4d\x3c'\
b'\x59\x3c\x59\x3f\x4d\x3f\x4d\x3c\x2b\x48\x5c\x5a\x46\x5a\x4a'\
b'\x5a\x4c\x58\x50\x54\x52\x52\x52\x50\x52\x4c\x50\x4a\x4d\x4a'\
b'\x4a\x4a\x44\x4a\x41\x4c\x3e\x50\x3b\x52\x3b\x54\x3b\x57\x3d'\
b'\x59\x40\x5a\x42\x5a\x42\x56\x42\x56\x42\x56\x41\x55\x3f\x53'\
b'\x3f\x52\x3f\x51\x3f\x4e\x40\x4d\x42\x4d\x44\x4d\x4a\x4d\x4c'\
b'\x4f\x4e\x51\x4f\x52\x4f\x53\x4f\x56\x4e\x57\x4c\x57\x4a\x57'\
b'\x49\x52\x49\x52\x46\x5a\x46\x11\x48\x5c\x57\x3c\x5a\x3c\x5a'\
b'\x52\x57\x52\x57\x3c\x20\x52\x4a\x3c\x4d\x3c\x4d\x52\x4a\x52'\
b'\x4a\x3c\x20\x52\x4c\x46\x58\x46\x58\x49\x4c\x49\x4c\x46\x05'\
b'\x4e\x56\x54\x52\x50\x52\x50\x3c\x54\x3c\x54\x52\x12\x4a\x5a'\
b'\x50\x52\x4d\x51\x4c\x4f\x4e\x4e\x4f\x4e\x50\x4f\x51\x4f\x53'\
b'\x4f\x55\x4d\x55\x4b\x55\x3c\x58\x3c\x58\x4b\x58\x4d\x57\x51'\
b'\x54\x52\x51\x52\x50\x52\x11\x47\x5d\x4c\x48\x56\x3c\x5a\x3c'\
b'\x4b\x4d\x4c\x48\x20\x52\x49\x3c\x4d\x3c\x4d\x52\x49\x52\x49'\
b'\x3c\x20\x52\x50\x46\x52\x44\x5b\x52\x57\x52\x50\x46\x0b\x49'\
b'\x5b\x4b\x3c\x4e\x3c\x4e\x52\x4b\x52\x4b\x3c\x20\x52\x4c\x4f'\
b'\x59\x4f\x59\x52\x4c\x52\x4c\x4f\x10\x47\x5d\x59\x3c\x5b\x3c'\
b'\x5b\x52\x58\x52\x58\x41\x59\x42\x53\x4f\x51\x4f\x4b\x43\x4c'\
b'\x41\x4c\x52\x49\x52\x49\x3c\x4b\x3c\x52\x4a\x59\x3c\x0d\x48'\
b'\x5c\x4a\x3c\x4d\x3c\x58\x4d\x57\x4d\x57\x3c\x5a\x3c\x5a\x52'\
b'\x57\x52\x4c\x41\x4d\x41\x4d\x52\x4a\x52\x4a\x3c\x27\x48\x5c'\
b'\x50\x52\x4c\x50\x4a\x4c\x4a\x4a\x4a\x44\x4a\x41\x4c\x3e\x50'\
b'\x3b\x52\x3b\x54\x3b\x58\x3e\x5a\x41\x5a\x44\x5a\x4a\x5a\x4c'\
b'\x58\x50\x54\x52\x52\x52\x50\x52\x20\x52\x53\x4f\x55\x4e\x57'\
b'\x4c\x57\x4a\x57\x44\x57\x42\x55\x40\x53\x3f\x52\x3f\x51\x3f'\
b'\x4f\x40\x4d\x42\x4d\x44\x4d\x4a\x4d\x4c\x4f\x4e\x51\x4f\x52'\
b'\x4f\x53\x4f\x1f\x48\x5c\x4c\x46\x53\x46\x54\x46\x56\x45\x56'\
b'\x44\x56\x43\x56\x43\x56\x41\x56\x40\x54\x3f\x53\x3f\x4c\x3f'\
b'\x4c\x3c\x53\x3c\x55\x3c\x58\x3d\x5a\x40\x5a\x43\x5a\x43\x5a'\
b'\x45\x58\x48\x55\x49\x53\x49\x4c\x49\x4c\x46\x20\x52\x4a\x3c'\
b'\x4d\x3c\x4d\x52\x4a\x52\x4a\x3c\x2d\x47\x5d\x51\x4c\x53\x4a'\
b'\x5b\x50\x59\x52\x51\x4c\x20\x52\x4f\x52\x4b\x50\x49\x4c\x49'\
b'\x4a\x49\x44\x49\x41\x4b\x3e\x4f\x3b\x51\x3b\x53\x3b\x57\x3e'\
b'\x59\x41\x59\x44\x59\x4a\x59\x4c\x57\x50\x53\x52\x51\x52\x4f'\
b'\x52\x20\x52\x52\x4f\x54\x4e\x56\x4c\x56\x4a\x56\x44\x56\x42'\
b'\x54\x40\x52\x3f\x51\x3f\x50\x3f\x4d\x40\x4c\x42\x4c\x44\x4c'\
b'\x4a\x4c\x4c\x4d\x4e\x50\x4f\x51\x4f\x52\x4f\x25\x48\x5c\x4b'\
b'\x46\x53\x46\x54\x46\x55\x45\x56\x43\x56\x42\x56\x42\x56\x41'\
b'\x55\x40\x54\x3f\x53\x3f\x4b\x3f\x4b\x3c\x53\x3c\x55\x3c\x58'\
b'\x3d\x59\x40\x59\x42\x59\x42\x59\x44\x58\x47\x55\x49\x53\x49'\
b'\x4b\x49\x4b\x46\x20\x52\x4a\x3c\x4d\x3c\x4d\x52\x4a\x52\x4a'\
b'\x3c\x20\x52\x51\x48\x54\x47\x5a\x52\x56\x52\x51\x48\x41\x48'\
b'\x5c\x50\x52\x4d\x52\x4b\x50\x4a\x4f\x4a\x4f\x4c\x4d\x4c\x4d'\
b'\x4d\x4e\x50\x4f\x52\x4f\x54\x4f\x57\x4d\x57\x4c\x57\x4c\x57'\
b'\x4b\x56\x49\x54\x49\x52\x48\x52\x48\x52\x48\x52\x48\x52\x48'\
b'\x50\x48\x4d\x47\x4b\x44\x4b\x42\x4b\x42\x4b\x40\x4d\x3d\x50'\
b'\x3b\x53\x3b\x54\x3b\x56\x3c\x59\x3d\x5a\x3e\x5a\x3e\x58\x40'\
b'\x58\x40\x57\x3f\x54\x3e\x53\x3e\x51\x3e\x4e\x40\x4e\x42\x4e'\
b'\x42\x4e\x43\x4f\x44\x51\x45\x53\x45\x53\x45\x53\x45\x53\x45'\
b'\x53\x45\x53\x45\x54\x45\x56\x46\x58\x47\x5a\x4a\x5a\x4c\x5a'\
b'\x4c\x5a\x4e\x58\x51\x55\x52\x52\x52\x50\x52\x0b\x48\x5c\x50'\
b'\x3e\x54\x3e\x54\x52\x50\x52\x50\x3e\x20\x52\x4a\x3c\x5a\x3c'\
b'\x5a\x3f\x4a\x3f\x4a\x3c\x15\x48\x5c\x50\x52\x4c\x50\x4a\x4d'\
b'\x4a\x4a\x4a\x3c\x4d\x3c\x4d\x4a\x4d\x4c\x50\x4f\x52\x4f\x54'\
b'\x4f\x57\x4c\x57\x4a\x57\x3c\x5a\x3c\x5a\x4a\x5a\x4d\x58\x50'\
b'\x54\x52\x52\x52\x50\x52\x08\x47\x5d\x49\x3c\x4d\x3c\x52\x4d'\
b'\x57\x3c\x5b\x3c\x53\x52\x51\x52\x49\x3c\x0e\x43\x61\x51\x3c'\
b'\x53\x3c\x58\x4d\x5c\x3c\x5f\x3c\x59\x52\x56\x52\x52\x42\x4e'\
b'\x52\x4b\x52\x45\x3c\x48\x3c\x4c\x4d\x51\x3c\x11\x47\x5d\x51'\
b'\x48\x51\x47\x4a\x3c\x4d\x3c\x52\x45\x53\x46\x5b\x52\x57\x52'\
b'\x51\x48\x20\x52\x51\x45\x57\x3c\x5a\x3c\x53\x48\x4d\x52\x49'\
b'\x52\x51\x45\x0a\x48\x5c\x54\x49\x54\x52\x50\x52\x50\x49\x4a'\
b'\x3c\x4d\x3c\x52\x46\x57\x3c\x5a\x3c\x54\x49\x0b\x49\x5b\x59'\
b'\x3e\x4f\x4f\x59\x4f\x59\x52\x4b\x52\x4b\x4f\x55\x3f\x4b\x3f'\
b'\x4b\x3c\x59\x3c\x59\x3e\x11\x4d\x57\x4f\x39\x52\x39\x52\x57'\
b'\x4f\x57\x4f\x39\x20\x52\x51\x54\x55\x54\x55\x57\x51\x57\x51'\
b'\x54\x20\x52\x51\x39\x55\x39\x55\x3c\x51\x3c\x51\x39\x05\x49'\
b'\x5b\x4e\x39\x59\x56\x56\x56\x4b\x39\x4e\x39\x11\x4d\x57\x52'\
b'\x39\x55\x39\x55\x57\x52\x57\x52\x39\x20\x52\x4f\x54\x53\x54'\
b'\x53\x57\x4f\x57\x4f\x54\x20\x52\x4f\x39\x53\x39\x53\x3c\x4f'\
b'\x3c\x4f\x39\x0b\x4a\x5a\x52\x3f\x52\x3a\x58\x43\x55\x43\x52'\
b'\x3f\x20\x52\x4c\x43\x52\x3a\x52\x3f\x4f\x43\x4c\x43\x05\x4a'\
b'\x5a\x58\x52\x58\x55\x4c\x55\x4c\x52\x58\x52\x05\x4d\x57\x4f'\
b'\x3a\x51\x38\x55\x3d\x53\x3f\x4f\x3a\x2b\x4a\x5a\x55\x48\x55'\
b'\x46\x54\x45\x52\x45\x51\x45\x4f\x45\x4f\x46\x4c\x44\x4d\x43'\
b'\x50\x42\x52\x42\x54\x42\x57\x43\x58\x46\x58\x48\x58\x52\x55'\
b'\x52\x55\x48\x20\x52\x4f\x52\x4c\x50\x4c\x4d\x4c\x4b\x4e\x49'\
b'\x51\x49\x56\x49\x56\x4b\x51\x4b\x50\x4b\x4f\x4c\x4f\x4d\x4f'\
b'\x4f\x50\x50\x52\x50\x54\x50\x55\x4f\x55\x4e\x56\x50\x55\x51'\
b'\x54\x52\x52\x52\x51\x52\x4f\x52\x27\x4a\x5a\x51\x52\x4f\x51'\
b'\x4f\x4f\x4f\x4c\x4f\x4d\x50\x4f\x51\x4f\x52\x4f\x53\x4f\x55'\
b'\x4e\x55\x4c\x55\x48\x55\x47\x53\x45\x52\x45\x51\x45\x50\x45'\
b'\x4f\x47\x4f\x48\x4e\x45\x4f\x43\x52\x42\x53\x42\x55\x42\x57'\
b'\x43\x58\x46\x58\x48\x58\x4c\x58\x4e\x57\x51\x55\x52\x53\x52'\
b'\x51\x52\x20\x52\x4c\x3c\x4f\x3c\x4f\x52\x4c\x52\x4c\x3c\x25'\
b'\x4a\x5a\x50\x52\x4d\x51\x4c\x4e\x4c\x4b\x4c\x49\x4c\x47\x4d'\
b'\x43\x50\x42\x53\x42\x54\x42\x56\x42\x58\x44\x58\x44\x58\x44'\
b'\x56\x46\x56\x46\x55\x46\x54\x45\x53\x45\x51\x45\x4f\x47\x4f'\
b'\x49\x4f\x4b\x4f\x4d\x51\x4f\x53\x4f\x54\x4f\x55\x4e\x56\x4e'\
b'\x56\x4e\x58\x50\x58\x50\x58\x51\x56\x52\x54\x52\x53\x52\x50'\
b'\x52\x27\x4a\x5a\x55\x3c\x58\x3c\x58\x52\x55\x52\x55\x3c\x20'\
b'\x52\x4f\x52\x4d\x51\x4c\x4e\x4c\x4c\x4c\x48\x4c\x46\x4d\x43'\
b'\x4f\x42\x51\x42\x52\x42\x55\x43\x56\x45\x55\x48\x55\x47\x54'\
b'\x45\x53\x45\x52\x45\x51\x45\x4f\x47\x4f\x48\x4f\x4c\x4f\x4e'\
b'\x51\x4f\x52\x4f\x53\x4f\x54\x4f\x55\x4d\x55\x4c\x55\x4f\x55'\
b'\x51\x53\x52\x51\x52\x4f\x52\x26\x49\x5b\x50\x52\x4d\x51\x4b'\
b'\x4d\x4b\x4b\x4b\x49\x4b\x47\x4d\x44\x50\x42\x52\x42\x54\x42'\
b'\x57\x44\x59\x48\x59\x4a\x59\x4b\x4e\x4b\x4e\x49\x56\x49\x56'\
b'\x49\x55\x47\x54\x45\x52\x45\x50\x45\x4e\x47\x4e\x49\x4e\x4b'\
b'\x4e\x4d\x51\x4f\x52\x4f\x53\x4f\x55\x4e\x56\x4e\x56\x4e\x58'\
b'\x50\x58\x50\x57\x51\x54\x52\x52\x52\x50\x52\x13\x4c\x58\x50'\
b'\x40\x50\x3e\x52\x3c\x54\x3c\x56\x3c\x56\x3f\x54\x3f\x53\x3f'\
b'\x53\x3f\x53\x40\x53\x52\x50\x52\x50\x40\x20\x52\x4e\x42\x56'\
b'\x42\x56\x45\x4e\x45\x4e\x42\x36\x4a\x5a\x50\x58\x4d\x57\x4c'\
b'\x56\x4c\x56\x4e\x54\x4e\x54\x4f\x55\x50\x56\x51\x56\x53\x56'\
b'\x55\x54\x55\x52\x55\x42\x58\x42\x58\x52\x58\x54\x57\x57\x54'\
b'\x58\x51\x58\x50\x58\x20\x52\x4f\x52\x4d\x51\x4c\x4e\x4c\x4c'\
b'\x4c\x48\x4c\x46\x4d\x43\x4f\x42\x51\x42\x52\x42\x55\x43\x56'\
b'\x45\x55\x48\x55\x47\x54\x45\x53\x45\x52\x45\x51\x45\x4f\x47'\
b'\x4f\x48\x4f\x4c\x4f\x4e\x51\x4f\x52\x4f\x53\x4f\x54\x4f\x55'\
b'\x4d\x55\x4c\x55\x4f\x55\x51\x53\x52\x51\x52\x4f\x52\x17\x4a'\
b'\x5a\x4c\x3c\x4f\x3c\x4f\x52\x4c\x52\x4c\x3c\x20\x52\x55\x48'\
b'\x55\x47\x54\x45\x52\x45\x50\x45\x4f\x46\x4f\x48\x4e\x45\x4f'\
b'\x43\x52\x42\x53\x42\x56\x42\x58\x45\x58\x48\x58\x52\x55\x52'\
b'\x55\x48\x0b\x4e\x56\x50\x3c\x54\x3c\x54\x3f\x50\x3f\x50\x3c'\
b'\x20\x52\x50\x42\x54\x42\x54\x52\x50\x52\x50\x42\x13\x4d\x57'\
b'\x4f\x55\x51\x55\x51\x55\x52\x55\x52\x54\x52\x42\x55\x42\x55'\
b'\x54\x55\x56\x53\x58\x51\x58\x4f\x58\x4f\x55\x20\x52\x52\x3c'\
b'\x55\x3c\x55\x3f\x52\x3f\x52\x3c\x11\x49\x5b\x4c\x4c\x55\x42'\
b'\x58\x42\x4c\x50\x4c\x4c\x20\x52\x4b\x3c\x4e\x3c\x4e\x52\x4b'\
b'\x52\x4b\x3c\x20\x52\x50\x49\x52\x47\x59\x52\x56\x52\x50\x49'\
b'\x0d\x4d\x57\x52\x4e\x52\x4e\x53\x4f\x53\x4f\x55\x4f\x55\x52'\
b'\x53\x52\x51\x52\x4f\x50\x4f\x4e\x4f\x3c\x52\x3c\x52\x4e\x2b'\
b'\x45\x5f\x5a\x48\x5a\x47\x58\x45\x57\x45\x55\x45\x54\x47\x54'\
b'\x48\x53\x45\x54\x44\x56\x42\x58\x42\x59\x42\x5c\x43\x5d\x46'\
b'\x5d\x48\x5d\x52\x5a\x52\x5a\x48\x20\x52\x47\x42\x4a\x42\x4a'\
b'\x52\x47\x52\x47\x42\x20\x52\x50\x48\x50\x47\x4f\x45\x4d\x45'\
b'\x4c\x45\x4a\x46\x4a\x48\x4a\x45\x4a\x43\x4d\x42\x4e\x42\x50'\
b'\x42\x52\x43\x54\x46\x54\x48\x54\x52\x50\x52\x50\x48\x17\x4a'\
b'\x5a\x4c\x42\x4f\x42\x4f\x52\x4c\x52\x4c\x42\x20\x52\x55\x48'\
b'\x55\x47\x54\x45\x52\x45\x50\x45\x4f\x46\x4f\x48\x4e\x45\x4f'\
b'\x43\x52\x42\x53\x42\x56\x42\x58\x45\x58\x48\x58\x52\x55\x52'\
b'\x55\x48\x0b\x48\x5c\x4a\x52\x4a\x3c\x5a\x3c\x5a\x52\x4a\x52'\
b'\x20\x52\x4c\x4f\x58\x4f\x58\x3e\x4c\x3e\x4c\x4f'

_index =\
b'\x00\x00\x03\x00\x1c\x00\x35\x00\x66\x00\xfb\x00\x88\x01\xf3'\
b'\x01\x00\x02\x21\x02\x42\x02\x7f\x02\x98\x02\xa5\x02\xb2\x02'\
b'\xbf\x02\xcc\x02\x0d\x03\x20\x03\x63\x03\xd4\x03\xf3\x03\x44'\
b'\x04\x9f\x04\xb6\x04\x4b\x05\xa6\x05\xc5\x05\xde\x05\xf7\x05'\
b'\x28\x06\xbd\x06\x4a\x07\xb5\x07\xc2\x07\xe3\x07\x04\x08\x41'\
b'\x08\x5a\x08\x67\x08\x74\x08\x81\x08\x8e\x08\xa7\x08\xc0\x08'\
b'\xd9\x08\xf2\x08\x0b\x09\x64\x09\x09\x0a\x28\x0a\x8d\x0a\xe2'\
b'\x0a\x1f\x0b\x50\x0b\x75\x0b\xce\x0b\xf3\x0b\x00\x0c\x27\x0c'\
b'\x4c\x0c\x65\x0c\x88\x0c\xa5\x0c\xf6\x0c\x37\x0d\x94\x0d\xe1'\
b'\x0d\x66\x0e\x7f\x0e\xac\x0e\xbf\x0e\xde\x0e\x03\x0f\x1a\x0f'\
b'\x33\x0f\x58\x0f\x65\x0f\x8a\x0f\xa3\x0f\xb0\x0f\xbd\x0f\x16'\
b'\x10\x67\x10\xb4\x10\x05\x11\x54\x11\x7d\x11\xec\x11\x1d\x12'\
b'\x36\x12\x5f\x12\x84\x12\xa1\x12\xfa\x12\x2b\x13'

FONT = memoryview(_font)
INDEX = memoryview(_index)

