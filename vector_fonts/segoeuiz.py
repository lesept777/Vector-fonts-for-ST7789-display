FIRST = 32
LAST = 127
WIDTH = 34
HEIGHT = 34

_font =\
b'\x01\x4d\x57\x1b\x4b\x59\x53\x4b\x4f\x4b\x52\x3a\x57\x3a\x53'\
b'\x4b\x20\x52\x53\x4f\x53\x50\x53\x51\x52\x52\x51\x52\x50\x52'\
b'\x4f\x52\x4e\x52\x4d\x51\x4d\x50\x4d\x50\x4d\x4f\x4d\x4e\x4e'\
b'\x4d\x4f\x4d\x50\x4d\x51\x4d\x52\x4d\x53\x4e\x53\x4f\x53\x4f'\
b'\x0b\x4b\x59\x57\x41\x54\x41\x53\x3a\x57\x3a\x57\x41\x20\x52'\
b'\x50\x41\x4d\x41\x4d\x3a\x51\x3a\x50\x41\x23\x47\x5d\x5b\x43'\
b'\x58\x43\x57\x47\x5a\x47\x5a\x4a\x56\x4a\x55\x50\x52\x50\x53'\
b'\x4a\x4f\x4a\x4e\x50\x4a\x50\x4c\x4a\x49\x4a\x49\x47\x4c\x47'\
b'\x4d\x43\x4a\x43\x4a\x40\x4e\x40\x4f\x3a\x52\x3a\x51\x40\x55'\
b'\x40\x56\x3a\x5a\x3a\x58\x40\x5b\x40\x5b\x43\x20\x52\x51\x43'\
b'\x50\x47\x53\x47\x54\x43\x51\x43\x47\x47\x5d\x5a\x3f\x59\x3f'\
b'\x57\x3e\x55\x3e\x54\x44\x57\x46\x59\x49\x59\x4b\x59\x4c\x59'\
b'\x4f\x57\x51\x53\x52\x51\x52\x50\x55\x4e\x55\x4f\x52\x4e\x52'\
b'\x4c\x52\x4b\x51\x49\x51\x49\x51\x4a\x4c\x4a\x4d\x4c\x4d\x4d'\
b'\x4e\x4f\x4e\x50\x4e\x51\x48\x50\x47\x4e\x46\x4c\x44\x4b\x42'\
b'\x4b\x41\x4b\x40\x4c\x3d\x4f\x3b\x52\x3a\x54\x3a\x54\x37\x57'\
b'\x37\x56\x3a\x57\x3a\x58\x3a\x59\x3b\x5b\x3b\x5b\x3b\x5a\x3f'\
b'\x20\x52\x52\x3e\x51\x3e\x50\x3f\x50\x40\x50\x41\x50\x42\x51'\
b'\x43\x52\x43\x53\x3e\x52\x3e\x20\x52\x55\x4b\x55\x4b\x55\x4a'\
b'\x54\x4a\x54\x49\x53\x49\x52\x4e\x53\x4e\x54\x4e\x55\x4d\x55'\
b'\x4c\x55\x4b\x63\x43\x61\x5f\x4b\x5f\x4c\x5e\x4d\x5e\x4f\x5d'\
b'\x51\x5b\x52\x59\x52\x58\x52\x56\x52\x54\x51\x53\x50\x53\x4e'\
b'\x53\x4d\x53\x4c\x53\x4b\x54\x49\x55\x48\x56\x47\x58\x46\x59'\
b'\x46\x5b\x46\x5d\x47\x5e\x48\x5f\x4a\x5f\x4b\x20\x52\x4a\x52'\
b'\x46\x52\x5a\x3a\x5e\x3a\x4a\x52\x20\x52\x51\x3f\x51\x40\x51'\
b'\x43\x4f\x45\x4d\x46\x4b\x46\x49\x46\x47\x45\x46\x44\x45\x42'\
b'\x45\x41\x45\x40\x46\x3f\x46\x3d\x47\x3c\x49\x3a\x4b\x3a\x4c'\
b'\x3a\x4d\x3a\x4f\x3a\x51\x3c\x51\x3e\x51\x3f\x20\x52\x5b\x4b'\
b'\x5b\x4b\x5b\x4a\x5a\x49\x5a\x49\x59\x49\x58\x49\x57\x4a\x57'\
b'\x4b\x56\x4d\x56\x4d\x56\x4e\x56\x4e\x57\x4f\x58\x4f\x58\x4f'\
b'\x59\x4f\x5a\x4f\x5b\x4d\x5b\x4c\x5b\x4b\x20\x52\x4e\x3f\x4e'\
b'\x3f\x4e\x3e\x4d\x3d\x4d\x3d\x4c\x3d\x4b\x3d\x4a\x3e\x49\x3f'\
b'\x49\x40\x49\x41\x49\x41\x49\x42\x4a\x43\x4a\x43\x4b\x43\x4c'\
b'\x43\x4d\x42\x4d\x41\x4e\x40\x4e\x3f\x6e\x42\x62\x5b\x52\x5a'\
b'\x52\x58\x52\x57\x51\x56\x50\x55\x4f\x55\x50\x53\x51\x51\x52'\
b'\x4e\x52\x4c\x52\x4a\x52\x47\x51\x45\x50\x44\x4d\x44\x4c\x44'\
b'\x4a\x45\x47\x47\x46\x4a\x44\x4c\x44\x4b\x43\x4b\x43\x4a\x42'\
b'\x4a\x40\x4a\x40\x4a\x3e\x4b\x3c\x4d\x3a\x50\x3a\x51\x3a\x53'\
b'\x3a\x55\x3a\x57\x3c\x58\x3e\x58\x3f\x58\x40\x57\x42\x56\x43'\
b'\x54\x44\x53\x44\x53\x44\x54\x46\x56\x47\x57\x49\x57\x49\x58'\
b'\x48\x5a\x46\x5b\x44\x5b\x41\x5b\x40\x5b\x40\x5b\x3f\x5b\x3f'\
b'\x60\x3f\x60\x40\x60\x40\x60\x41\x5f\x44\x5e\x46\x5d\x48\x5b'\
b'\x4a\x5a\x4c\x59\x4d\x59\x4e\x5b\x4e\x5c\x4e\x5d\x4e\x5e\x4e'\
b'\x5f\x4e\x5e\x52\x5d\x52\x5c\x52\x5b\x52\x20\x52\x4d\x4e\x4f'\
b'\x4e\x52\x4d\x54\x4c\x53\x4a\x50\x47\x4e\x46\x4e\x46\x4c\x47'\
b'\x4a\x48\x4a\x4a\x4a\x4b\x4a\x4c\x4a\x4d\x4b\x4e\x4c\x4e\x4d'\
b'\x4e\x20\x52\x50\x42\x50\x42\x51\x41\x53\x41\x53\x40\x53\x3f'\
b'\x53\x3e\x52\x3d\x51\x3d\x51\x3d\x50\x3e\x4f\x3e\x4e\x3f\x4e'\
b'\x40\x4e\x41\x4f\x42\x50\x42\x05\x4e\x56\x54\x41\x50\x41\x50'\
b'\x3a\x54\x3a\x54\x41\x17\x49\x5b\x57\x3c\x53\x40\x51\x45\x50'\
b'\x4a\x50\x4d\x50\x4f\x50\x51\x51\x54\x52\x56\x52\x57\x4e\x57'\
b'\x4d\x56\x4c\x54\x4c\x51\x4b\x4e\x4b\x4d\x4b\x4a\x4d\x45\x4f'\
b'\x40\x52\x3c\x54\x3a\x59\x3a\x57\x3c\x17\x49\x5b\x59\x45\x59'\
b'\x47\x57\x4d\x55\x51\x52\x55\x50\x57\x4b\x57\x4d\x55\x51\x51'\
b'\x53\x4c\x54\x47\x54\x44\x54\x43\x54\x40\x53\x3e\x52\x3b\x52'\
b'\x3a\x56\x3a\x57\x3b\x58\x3e\x58\x41\x59\x43\x59\x45\x10\x49'\
b'\x5b\x54\x41\x57\x45\x54\x47\x52\x42\x50\x47\x4d\x45\x50\x41'\
b'\x4b\x40\x4d\x3d\x51\x3f\x50\x3a\x54\x3a\x53\x3f\x57\x3d\x59'\
b'\x40\x54\x41\x0d\x48\x5c\x54\x4a\x54\x50\x50\x50\x50\x4a\x4a'\
b'\x4a\x4a\x47\x50\x47\x50\x40\x54\x40\x54\x47\x5a\x47\x5a\x4a'\
b'\x54\x4a\x05\x4c\x58\x52\x56\x4e\x56\x51\x4e\x56\x4e\x52\x56'\
b'\x05\x4b\x59\x56\x4b\x4d\x4b\x4e\x47\x57\x47\x56\x4b\x15\x4d'\
b'\x57\x55\x50\x55\x50\x55\x51\x54\x52\x53\x52\x52\x52\x51\x52'\
b'\x50\x52\x4f\x51\x4f\x50\x4f\x50\x4f\x4f\x4f\x4e\x50\x4d\x51'\
b'\x4d\x52\x4d\x53\x4d\x54\x4d\x55\x4e\x55\x4f\x55\x50\x05\x45'\
b'\x5f\x4c\x56\x47\x56\x58\x3a\x5d\x3a\x4c\x56\x20\x47\x5d\x5b'\
b'\x41\x5b\x45\x5a\x4b\x57\x50\x53\x52\x50\x52\x4d\x52\x49\x4e'\
b'\x49\x4a\x49\x46\x4c\x3e\x51\x3a\x54\x3a\x57\x3a\x5b\x3e\x5b'\
b'\x41\x20\x52\x56\x41\x56\x3f\x55\x3e\x54\x3e\x52\x3e\x50\x41'\
b'\x4e\x48\x4e\x4b\x4e\x4d\x4f\x4e\x50\x4e\x52\x4e\x54\x4b\x56'\
b'\x44\x56\x41\x07\x4a\x5a\x4d\x52\x51\x3f\x4c\x40\x4d\x3c\x58'\
b'\x3a\x53\x52\x4d\x52\x20\x46\x5e\x4f\x4e\x59\x4e\x58\x52\x48'\
b'\x52\x49\x50\x49\x4e\x4d\x49\x51\x47\x53\x45\x55\x44\x56\x42'\
b'\x56\x41\x56\x3f\x54\x3e\x53\x3e\x50\x3e\x4d\x40\x4e\x3b\x4f'\
b'\x3b\x53\x3a\x54\x3a\x58\x3a\x5c\x3d\x5c\x40\x5c\x42\x5a\x44'\
b'\x58\x47\x56\x48\x54\x49\x52\x4b\x4f\x4d\x4f\x4e\x28\x47\x5d'\
b'\x5b\x3f\x5b\x42\x58\x45\x55\x46\x55\x46\x57\x46\x59\x49\x59'\
b'\x4b\x59\x4d\x57\x51\x53\x52\x4f\x52\x4c\x52\x49\x51\x4a\x4d'\
b'\x4b\x4e\x4e\x4e\x4f\x4e\x51\x4e\x54\x4d\x54\x4b\x54\x48\x4f'\
b'\x48\x4d\x48\x4e\x44\x51\x44\x53\x44\x56\x42\x56\x40\x56\x3f'\
b'\x54\x3e\x52\x3e\x50\x3e\x4d\x3f\x4e\x3b\x51\x3a\x54\x3a\x57'\
b'\x3a\x5b\x3d\x5b\x3f\x14\x46\x5e\x5c\x3a\x58\x49\x5c\x49\x5b'\
b'\x4d\x58\x4d\x56\x52\x52\x52\x53\x4d\x48\x4d\x49\x49\x4d\x45'\
b'\x54\x3d\x57\x3a\x5c\x3a\x20\x52\x4e\x49\x54\x49\x55\x41\x52'\
b'\x45\x4e\x49\x1f\x47\x5d\x5a\x3e\x52\x3e\x51\x43\x51\x43\x52'\
b'\x43\x55\x43\x59\x47\x59\x4a\x59\x4c\x56\x50\x52\x52\x4f\x52'\
b'\x4d\x52\x49\x52\x49\x51\x4a\x4d\x4a\x4e\x4d\x4e\x4f\x4e\x50'\
b'\x4e\x53\x4d\x54\x4b\x54\x4a\x54\x49\x52\x47\x4f\x47\x4d\x47'\
b'\x4b\x47\x4e\x3a\x5b\x3a\x5a\x3e\x2a\x47\x5d\x5a\x3f\x58\x3e'\
b'\x56\x3e\x54\x3e\x51\x3f\x4f\x43\x4e\x45\x4f\x45\x4f\x44\x52'\
b'\x43\x54\x43\x56\x43\x5a\x46\x5a\x49\x5a\x4c\x57\x50\x53\x52'\
b'\x51\x52\x4d\x52\x49\x4e\x49\x49\x49\x45\x4c\x3e\x53\x3a\x56'\
b'\x3a\x59\x3a\x5b\x3a\x5a\x3f\x20\x52\x55\x4a\x55\x48\x53\x47'\
b'\x52\x47\x50\x47\x4e\x49\x4e\x4b\x4e\x4c\x50\x4e\x51\x4e\x53'\
b'\x4e\x55\x4c\x55\x4a\x0d\x47\x5d\x4e\x52\x49\x52\x4b\x4d\x50'\
b'\x44\x55\x3e\x4a\x3e\x4b\x3a\x5b\x3a\x5b\x3d\x57\x42\x53\x48'\
b'\x4f\x4f\x4e\x52\x36\x46\x5e\x48\x4c\x48\x49\x4b\x46\x4e\x45'\
b'\x4c\x43\x4c\x41\x4c\x3f\x4e\x3b\x52\x3a\x54\x3a\x58\x3a\x5c'\
b'\x3d\x5c\x40\x5c\x42\x59\x45\x56\x46\x5a\x47\x5a\x4b\x5a\x4d'\
b'\x57\x50\x53\x52\x50\x52\x4e\x52\x4a\x51\x48\x4e\x48\x4c\x20'\
b'\x52\x4d\x4b\x4d\x4d\x4f\x4f\x51\x4f\x52\x4f\x54\x4c\x54\x4b'\
b'\x54\x49\x53\x48\x51\x48\x50\x48\x4d\x4a\x4d\x4b\x20\x52\x51'\
b'\x41\x51\x42\x52\x44\x53\x44\x55\x44\x57\x42\x57\x40\x57\x3f'\
b'\x55\x3e\x54\x3e\x52\x3e\x51\x3f\x51\x41\x2b\x47\x5d\x5b\x43'\
b'\x5b\x46\x59\x4c\x56\x50\x51\x52\x4e\x52\x4c\x52\x4a\x52\x49'\
b'\x52\x4a\x4d\x4a\x4e\x4d\x4e\x4e\x4e\x51\x4e\x55\x4b\x56\x47'\
b'\x55\x47\x53\x49\x50\x49\x4e\x49\x4a\x46\x4a\x43\x4a\x40\x4d'\
b'\x3c\x51\x3a\x53\x3a\x57\x3a\x5b\x3f\x5b\x43\x20\x52\x56\x41'\
b'\x56\x40\x54\x3e\x53\x3e\x52\x3e\x50\x40\x50\x42\x50\x44\x51'\
b'\x46\x52\x46\x54\x46\x56\x43\x56\x41\x2b\x4c\x58\x56\x43\x56'\
b'\x44\x56\x45\x55\x46\x54\x46\x53\x46\x53\x46\x51\x46\x51\x45'\
b'\x50\x44\x50\x44\x50\x43\x51\x42\x52\x41\x53\x41\x53\x41\x54'\
b'\x41\x55\x41\x56\x42\x56\x43\x56\x43\x20\x52\x54\x50\x54\x50'\
b'\x53\x51\x52\x52\x51\x52\x51\x52\x50\x52\x4f\x52\x4e\x51\x4e'\
b'\x50\x4e\x50\x4e\x4f\x4e\x4e\x4f\x4d\x50\x4d\x51\x4d\x51\x4d'\
b'\x53\x4d\x53\x4e\x54\x4f\x54\x50\x1b\x4a\x5a\x58\x43\x58\x44'\
b'\x57\x45\x56\x46\x55\x46\x54\x46\x54\x46\x53\x46\x52\x45\x51'\
b'\x44\x51\x44\x51\x43\x52\x42\x53\x41\x54\x41\x55\x41\x55\x41'\
b'\x56\x41\x57\x42\x58\x43\x58\x43\x20\x52\x51\x56\x4c\x56\x50'\
b'\x4e\x55\x4e\x51\x56\x09\x48\x5c\x4a\x4a\x4a\x47\x5a\x3f\x5a'\
b'\x43\x4f\x48\x4f\x48\x5a\x4d\x5a\x51\x4a\x4a\x0b\x48\x5c\x4a'\
b'\x46\x4a\x43\x5a\x43\x5a\x46\x4a\x46\x20\x52\x4a\x4e\x4a\x4a'\
b'\x5a\x4a\x5a\x4e\x4a\x4e\x09\x48\x5c\x4a\x51\x4a\x4d\x55\x48'\
b'\x55\x48\x4a\x43\x4a\x3f\x5a\x47\x5a\x4a\x4a\x51\x3f\x49\x5b'\
b'\x59\x3f\x59\x40\x59\x42\x57\x44\x56\x45\x54\x46\x53\x47\x52'\
b'\x48\x52\x49\x51\x4a\x51\x4b\x4d\x4b\x4d\x4a\x4d\x48\x4e\x46'\
b'\x4f\x45\x50\x44\x51\x44\x53\x42\x53\x42\x54\x41\x54\x40\x54'\
b'\x40\x53\x3f\x53\x3e\x52\x3e\x51\x3e\x50\x3e\x4d\x3f\x4c\x3f'\
b'\x4d\x3b\x4d\x3a\x4f\x3a\x50\x3a\x52\x39\x52\x39\x54\x39\x57'\
b'\x3a\x58\x3c\x59\x3e\x59\x3f\x20\x52\x51\x4f\x51\x50\x51\x51'\
b'\x50\x52\x4f\x52\x4e\x52\x4d\x52\x4c\x52\x4b\x51\x4b\x50\x4b'\
b'\x50\x4b\x4f\x4b\x4e\x4c\x4d\x4d\x4d\x4e\x4d\x4f\x4d\x50\x4d'\
b'\x51\x4e\x51\x4f\x51\x4f\x77\x42\x62\x60\x44\x60\x46\x60\x48'\
b'\x5f\x4b\x5d\x4d\x5b\x4e\x59\x4f\x57\x4f\x56\x4f\x55\x4e\x54'\
b'\x4e\x54\x4d\x54\x4c\x54\x4c\x54\x4c\x54\x4c\x54\x4c\x53\x4d'\
b'\x50\x4f\x4f\x4f\x4e\x4f\x4c\x4e\x4b\x4d\x4b\x4b\x4b\x49\x4b'\
b'\x48\x4b\x46\x4c\x44\x4d\x42\x4f\x41\x51\x40\x53\x40\x53\x40'\
b'\x54\x40\x55\x41\x56\x42\x56\x42\x56\x42\x56\x40\x5a\x40\x5a'\
b'\x41\x59\x43\x59\x45\x58\x47\x58\x49\x57\x4a\x57\x4b\x57\x4b'\
b'\x58\x4c\x58\x4c\x59\x4c\x5b\x4b\x5c\x49\x5d\x46\x5d\x45\x5d'\
b'\x43\x5c\x40\x5a\x3e\x56\x3d\x54\x3d\x51\x3d\x4d\x3f\x49\x42'\
b'\x48\x46\x48\x49\x48\x4b\x49\x4e\x4b\x51\x4f\x52\x51\x52\x53'\
b'\x52\x55\x52\x57\x51\x59\x51\x59\x51\x59\x54\x58\x54\x57\x55'\
b'\x55\x55\x52\x55\x51\x55\x4e\x55\x49\x53\x45\x50\x44\x4c\x44'\
b'\x49\x44\x47\x45\x43\x47\x40\x4a\x3d\x4d\x3b\x51\x3a\x54\x3a'\
b'\x57\x3a\x5c\x3b\x5f\x3e\x60\x42\x60\x44\x20\x52\x55\x45\x55'\
b'\x44\x54\x43\x53\x43\x52\x43\x50\x44\x4f\x46\x4f\x48\x4f\x49'\
b'\x4f\x4b\x50\x4c\x50\x4c\x51\x4c\x52\x4b\x53\x4a\x54\x47\x55'\
b'\x46\x55\x46\x55\x45\x55\x45\x19\x44\x60\x58\x52\x58\x4d\x4f'\
b'\x4d\x4c\x52\x46\x52\x54\x3a\x5a\x3a\x5e\x52\x58\x52\x20\x52'\
b'\x56\x40\x56\x40\x56\x40\x56\x3f\x56\x3e\x56\x3e\x56\x3e\x56'\
b'\x3f\x56\x3f\x56\x40\x56\x40\x55\x40\x51\x49\x57\x49\x56\x40'\
b'\x35\x46\x5e\x5c\x3f\x5c\x41\x5c\x43\x5a\x44\x58\x45\x57\x45'\
b'\x57\x46\x58\x46\x59\x47\x5b\x48\x5b\x4a\x5b\x4a\x5b\x4c\x5a'\
b'\x4f\x57\x51\x54\x52\x51\x52\x48\x52\x4d\x3a\x55\x3a\x57\x3a'\
b'\x5a\x3b\x5c\x3c\x5c\x3e\x5c\x3f\x20\x52\x57\x41\x57\x40\x56'\
b'\x3f\x56\x3e\x54\x3e\x53\x3e\x51\x3e\x50\x44\x53\x44\x54\x44'\
b'\x55\x43\x56\x42\x57\x41\x57\x41\x20\x52\x56\x4a\x56\x49\x54'\
b'\x48\x52\x48\x4f\x48\x4e\x4e\x51\x4e\x52\x4e\x54\x4d\x55\x4d'\
b'\x56\x4b\x56\x4a\x2b\x45\x5f\x5c\x40\x5b\x40\x5a\x3f\x59\x3f'\
b'\x57\x3e\x56\x3e\x54\x3e\x50\x40\x4e\x42\x4d\x46\x4d\x48\x4d'\
b'\x49\x4e\x4b\x50\x4d\x52\x4e\x53\x4e\x54\x4e\x56\x4e\x57\x4d'\
b'\x59\x4d\x59\x4c\x58\x51\x57\x52\x54\x52\x52\x52\x50\x52\x4c'\
b'\x51\x49\x4e\x47\x4a\x47\x48\x47\x46\x48\x43\x4a\x3f\x4c\x3d'\
b'\x50\x3b\x54\x3a\x56\x3a\x57\x3a\x59\x3a\x5b\x3a\x5c\x3b\x5d'\
b'\x3b\x5c\x40\x1f\x44\x60\x5e\x44\x5e\x46\x5d\x49\x5c\x4c\x59'\
b'\x4f\x56\x51\x52\x52\x50\x52\x46\x52\x4b\x3a\x53\x3a\x56\x3a'\
b'\x5a\x3c\x5d\x3e\x5e\x42\x5e\x44\x20\x52\x58\x44\x58\x43\x58'\
b'\x41\x56\x3f\x54\x3e\x52\x3e\x4f\x3e\x4c\x4e\x50\x4e\x52\x4e'\
b'\x55\x4c\x57\x4a\x58\x46\x58\x44\x0d\x47\x5d\x5a\x3e\x52\x3e'\
b'\x51\x44\x59\x44\x58\x48\x50\x48\x4f\x4e\x58\x4e\x57\x52\x49'\
b'\x52\x4e\x3a\x5b\x3a\x5a\x3e\x0b\x47\x5d\x5b\x3f\x52\x3f\x51'\
b'\x44\x59\x44\x58\x49\x50\x49\x4e\x52\x49\x52\x4e\x3a\x5b\x3a'\
b'\x5b\x3f\x2f\x45\x5f\x5c\x40\x5b\x40\x5a\x3f\x58\x3e\x57\x3e'\
b'\x56\x3e\x54\x3e\x50\x40\x4e\x42\x4d\x45\x4d\x48\x4d\x49\x4d'\
b'\x4b\x4f\x4d\x51\x4e\x53\x4e\x53\x4e\x55\x4e\x55\x4e\x56\x49'\
b'\x51\x49\x52\x44\x5c\x44\x5a\x51\x59\x51\x57\x52\x55\x52\x53'\
b'\x52\x52\x52\x4f\x52\x4b\x51\x48\x4e\x47\x4a\x47\x48\x47\x46'\
b'\x48\x42\x49\x3f\x4c\x3d\x4f\x3b\x53\x3a\x56\x3a\x57\x3a\x59'\
b'\x3a\x5b\x3a\x5c\x3b\x5d\x3b\x5c\x40\x0d\x43\x61\x5a\x52\x54'\
b'\x52\x56\x48\x4d\x48\x4b\x52\x45\x52\x4a\x3a\x50\x3a\x4e\x44'\
b'\x57\x44\x59\x3a\x5f\x3a\x5a\x52\x05\x4b\x59\x52\x52\x4d\x52'\
b'\x52\x3a\x57\x3a\x52\x52\x17\x47\x5d\x58\x48\x57\x4b\x55\x4e'\
b'\x53\x51\x4f\x52\x4d\x52\x4d\x52\x4c\x52\x4b\x52\x4a\x52\x49'\
b'\x52\x4a\x4d\x4b\x4d\x4b\x4d\x4c\x4e\x4d\x4e\x4d\x4e\x4f\x4e'\
b'\x52\x4b\x52\x48\x55\x3a\x5b\x3a\x58\x48\x2c\x44\x60\x5e\x3b'\
b'\x5c\x3c\x5a\x3f\x58\x41\x55\x43\x54\x45\x53\x46\x54\x46\x55'\
b'\x48\x56\x4b\x57\x4d\x59\x4f\x5a\x51\x5a\x52\x53\x52\x53\x52'\
b'\x52\x50\x51\x4e\x50\x4c\x4f\x4a\x4e\x48\x4e\x48\x4e\x47\x4e'\
b'\x47\x4e\x46\x4e\x46\x4b\x52\x46\x52\x4b\x3a\x50\x3a\x4e\x45'\
b'\x4e\x45\x4e\x45\x4f\x44\x4f\x44\x4f\x44\x51\x42\x52\x40\x54'\
b'\x3e\x56\x3c\x57\x3b\x58\x3a\x5e\x3a\x5e\x3b\x07\x48\x5c\x59'\
b'\x52\x4a\x52\x4f\x3a\x55\x3a\x51\x4e\x5a\x4e\x59\x52\x29\x41'\
b'\x63\x5c\x52\x57\x52\x5a\x44\x5a\x41\x5b\x3f\x5b\x3f\x5b\x3f'\
b'\x5a\x40\x5a\x41\x59\x42\x59\x42\x53\x4b\x4f\x4b\x4c\x42\x4c'\
b'\x42\x4c\x41\x4c\x40\x4c\x3f\x4c\x3f\x4c\x40\x4b\x43\x4b\x44'\
b'\x48\x52\x43\x52\x48\x3a\x4f\x3a\x51\x42\x51\x43\x52\x44\x52'\
b'\x45\x52\x45\x52\x46\x52\x46\x52\x45\x52\x45\x53\x44\x53\x43'\
b'\x54\x42\x5a\x3a\x61\x3a\x5c\x52\x1f\x43\x61\x5a\x52\x56\x52'\
b'\x4e\x43\x4e\x43\x4e\x42\x4d\x42\x4d\x41\x4d\x41\x4d\x41\x4d'\
b'\x41\x4d\x43\x4d\x44\x4a\x52\x45\x52\x4a\x3a\x4f\x3a\x56\x49'\
b'\x56\x49\x56\x49\x57\x4a\x57\x4a\x57\x4b\x57\x4b\x57\x4a\x57'\
b'\x4a\x57\x49\x57\x49\x57\x48\x5a\x3a\x5f\x3a\x5a\x52\x3b\x44'\
b'\x60\x5e\x44\x5e\x45\x5d\x48\x5c\x4b\x5b\x4e\x5a\x4f\x59\x4f'\
b'\x57\x51\x55\x52\x52\x52\x50\x52\x4e\x52\x4a\x51\x48\x4e\x46'\
b'\x4a\x46\x48\x46\x47\x47\x44\x48\x41\x4a\x3e\x4b\x3d\x4b\x3c'\
b'\x4d\x3b\x50\x3a\x52\x3a\x54\x3a\x56\x3a\x5a\x3b\x5c\x3e\x5e'\
b'\x42\x5e\x44\x20\x52\x58\x44\x58\x43\x57\x41\x56\x3f\x54\x3e'\
b'\x53\x3e\x52\x3e\x4f\x40\x4e\x41\x4e\x41\x4d\x43\x4c\x45\x4c'\
b'\x47\x4c\x48\x4c\x49\x4d\x4c\x4e\x4d\x50\x4e\x51\x4e\x52\x4e'\
b'\x55\x4d\x56\x4b\x56\x4b\x57\x49\x58\x47\x58\x45\x58\x44\x1d'\
b'\x45\x5f\x5d\x41\x5d\x43\x5b\x46\x59\x48\x55\x4a\x52\x4a\x4f'\
b'\x4a\x4d\x52\x47\x52\x4d\x3a\x55\x3a\x57\x3a\x5a\x3b\x5c\x3d'\
b'\x5d\x3f\x5d\x41\x20\x52\x57\x41\x57\x40\x55\x3e\x53\x3e\x51'\
b'\x3e\x4f\x46\x52\x46\x53\x46\x55\x45\x56\x44\x57\x42\x57\x41'\
b'\x23\x44\x60\x5e\x44\x5e\x47\x5b\x4d\x57\x51\x55\x52\x5a\x58'\
b'\x53\x58\x4f\x52\x4d\x52\x49\x50\x46\x4b\x46\x48\x46\x44\x4a'\
b'\x3e\x50\x3a\x54\x3a\x58\x3a\x5e\x3f\x5e\x44\x20\x52\x58\x44'\
b'\x58\x41\x55\x3e\x53\x3e\x51\x3e\x4e\x41\x4c\x45\x4c\x48\x4c'\
b'\x4b\x4f\x4e\x51\x4e\x53\x4e\x56\x4b\x58\x47\x58\x44\x27\x46'\
b'\x5e\x5c\x40\x5c\x42\x5b\x44\x59\x46\x57\x47\x55\x47\x55\x47'\
b'\x57\x48\x58\x4a\x58\x4b\x5a\x52\x54\x52\x53\x4c\x53\x4a\x51'\
b'\x49\x50\x49\x4f\x49\x4d\x52\x48\x52\x4d\x3a\x55\x3a\x57\x3a'\
b'\x5a\x3b\x5c\x3d\x5c\x3f\x5c\x40\x20\x52\x57\x41\x57\x40\x55'\
b'\x3e\x53\x3e\x51\x3e\x50\x45\x52\x45\x53\x45\x55\x44\x56\x43'\
b'\x57\x42\x57\x41\x41\x47\x5d\x5a\x40\x5a\x3f\x58\x3f\x57\x3e'\
b'\x55\x3e\x55\x3e\x54\x3e\x52\x3e\x52\x3f\x51\x40\x51\x40\x51'\
b'\x41\x52\x42\x52\x43\x54\x44\x54\x44\x56\x45\x57\x46\x59\x48'\
b'\x59\x4a\x59\x4b\x59\x4c\x59\x4d\x58\x4f\x57\x51\x55\x52\x52'\
b'\x52\x50\x52\x4f\x52\x4d\x52\x4b\x52\x49\x51\x49\x51\x4a\x4c'\
b'\x4a\x4c\x4c\x4d\x4d\x4e\x4f\x4e\x50\x4e\x51\x4e\x52\x4e\x53'\
b'\x4d\x54\x4c\x54\x4c\x54\x4b\x53\x4a\x52\x49\x51\x48\x50\x48'\
b'\x4f\x47\x4d\x46\x4c\x44\x4c\x42\x4c\x41\x4c\x40\x4d\x3d\x4f'\
b'\x3b\x52\x3a\x55\x3a\x56\x3a\x57\x3a\x59\x3a\x5b\x3b\x5b\x3b'\
b'\x5a\x40\x09\x46\x5e\x5b\x3e\x54\x3e\x50\x52\x4b\x52\x4f\x3e'\
b'\x48\x3e\x49\x3a\x5c\x3a\x5b\x3e\x21\x45\x5f\x5a\x48\x5a\x4b'\
b'\x58\x4e\x56\x51\x52\x52\x4f\x52\x4d\x52\x4a\x51\x48\x4f\x47'\
b'\x4c\x47\x4a\x47\x49\x47\x47\x47\x46\x4a\x3a\x4f\x3a\x4c\x47'\
b'\x4c\x47\x4c\x49\x4c\x4a\x4c\x4b\x4c\x4c\x4e\x4d\x4f\x4e\x50'\
b'\x4e\x51\x4e\x52\x4d\x54\x4c\x55\x4a\x55\x48\x58\x3a\x5d\x3a'\
b'\x5a\x48\x0f\x45\x5f\x50\x52\x4a\x52\x47\x3a\x4c\x3a\x4e\x4b'\
b'\x4e\x4b\x4e\x4c\x4e\x4d\x4e\x4d\x4e\x4c\x4f\x4b\x4f\x4b\x57'\
b'\x3a\x5d\x3a\x50\x52\x2f\x3f\x65\x58\x52\x52\x52\x51\x42\x51'\
b'\x42\x51\x42\x51\x41\x51\x40\x51\x40\x51\x40\x51\x40\x51\x41'\
b'\x50\x42\x50\x42\x50\x42\x48\x52\x42\x52\x41\x3a\x47\x3a\x47'\
b'\x4a\x47\x4a\x47\x4b\x47\x4c\x47\x4c\x47\x4d\x47\x4d\x47\x4c'\
b'\x47\x4c\x47\x4b\x48\x4a\x48\x4a\x4f\x3a\x55\x3a\x56\x4a\x56'\
b'\x4a\x56\x4b\x56\x4c\x56\x4c\x56\x4d\x56\x4d\x56\x4c\x56\x4c'\
b'\x56\x4b\x57\x4a\x57\x4a\x5d\x3a\x63\x3a\x58\x52\x21\x42\x62'\
b'\x56\x46\x5a\x52\x54\x52\x52\x4a\x52\x4a\x52\x4a\x52\x49\x52'\
b'\x49\x52\x49\x52\x49\x52\x49\x51\x4a\x51\x4a\x4b\x52\x44\x52'\
b'\x4f\x46\x4a\x3a\x50\x3a\x52\x41\x53\x42\x53\x42\x53\x43\x53'\
b'\x43\x53\x43\x53\x43\x53\x43\x53\x43\x53\x42\x53\x42\x54\x42'\
b'\x59\x3a\x60\x3a\x56\x46\x11\x46\x5e\x51\x49\x50\x52\x4a\x52'\
b'\x4c\x49\x48\x3a\x4d\x3a\x4f\x43\x4f\x44\x50\x45\x50\x45\x50'\
b'\x45\x50\x45\x50\x44\x50\x43\x56\x3a\x5c\x3a\x51\x49\x0b\x44'\
b'\x60\x5e\x3d\x4e\x4e\x5a\x4e\x59\x52\x46\x52\x46\x4f\x56\x3e'\
b'\x4b\x3e\x4c\x3a\x5e\x3a\x5e\x3d\x09\x49\x5b\x58\x3d\x55\x3d'\
b'\x50\x54\x54\x54\x53\x57\x4b\x57\x51\x3a\x59\x3a\x58\x3d\x05'\
b'\x4b\x59\x53\x56\x4d\x3a\x51\x3a\x57\x56\x53\x56\x09\x49\x5b'\
b'\x53\x57\x4b\x57\x4c\x54\x4f\x54\x54\x3d\x50\x3d\x51\x3a\x59'\
b'\x3a\x53\x57\x09\x47\x5d\x57\x48\x52\x3e\x52\x3e\x4d\x48\x49'\
b'\x48\x50\x3a\x53\x3a\x5b\x48\x57\x48\x05\x49\x5b\x4b\x57\x4b'\
b'\x55\x59\x55\x59\x57\x4b\x57\x05\x4c\x58\x52\x3e\x4e\x39\x52'\
b'\x39\x56\x3e\x52\x3e\x3b\x47\x5d\x59\x4c\x59\x4d\x59\x4e\x59'\
b'\x50\x58\x51\x58\x52\x53\x52\x53\x52\x53\x51\x53\x50\x53\x4f'\
b'\x53\x4f\x53\x4f\x53\x50\x52\x51\x50\x52\x4f\x52\x4e\x52\x4d'\
b'\x52\x4b\x52\x49\x50\x49\x4d\x49\x4c\x49\x4b\x49\x49\x4a\x46'\
b'\x4c\x44\x4e\x42\x52\x41\x54\x41\x55\x41\x57\x41\x59\x41\x5b'\
b'\x41\x5b\x41\x59\x4c\x20\x52\x55\x44\x54\x44\x54\x44\x53\x44'\
b'\x51\x45\x50\x46\x4f\x48\x4e\x49\x4e\x4b\x4e\x4c\x4e\x4c\x4e'\
b'\x4d\x4f\x4e\x50\x4e\x50\x4e\x51\x4e\x52\x4d\x54\x4c\x54\x49'\
b'\x55\x48\x55\x44\x55\x44\x35\x47\x5d\x5b\x47\x5b\x48\x5b\x4a'\
b'\x5a\x4d\x58\x4f\x56\x51\x52\x52\x50\x52\x4f\x52\x4d\x52\x4b'\
b'\x52\x49\x51\x49\x51\x4e\x39\x53\x39\x51\x40\x51\x41\x51\x41'\
b'\x51\x42\x51\x43\x51\x43\x51\x43\x51\x43\x52\x42\x54\x41\x55'\
b'\x41\x56\x41\x57\x41\x59\x41\x5b\x43\x5b\x45\x5b\x47\x20\x52'\
b'\x56\x47\x56\x46\x55\x45\x54\x45\x53\x45\x52\x45\x50\x47\x50'\
b'\x49\x4f\x4a\x4e\x4e\x4f\x4e\x50\x4f\x51\x4f\x52\x4f\x53\x4e'\
b'\x54\x4d\x55\x4c\x56\x4a\x56\x48\x56\x47\x27\x49\x5b\x59\x46'\
b'\x58\x45\x56\x45\x55\x45\x54\x45\x52\x46\x51\x47\x50\x4a\x50'\
b'\x4b\x50\x4d\x51\x4e\x53\x4e\x54\x4e\x55\x4e\x56\x4e\x57\x4d'\
b'\x57\x4d\x56\x51\x55\x52\x53\x52\x51\x52\x50\x52\x4d\x51\x4b'\
b'\x50\x4b\x4d\x4b\x4b\x4b\x4a\x4b\x47\x4c\x45\x4e\x43\x51\x41'\
b'\x53\x41\x55\x41\x56\x41\x57\x41\x58\x41\x59\x41\x59\x41\x59'\
b'\x46\x39\x46\x5e\x58\x4c\x58\x4d\x58\x4e\x58\x50\x57\x51\x57'\
b'\x52\x52\x52\x52\x52\x52\x51\x52\x50\x52\x4f\x52\x4f\x52\x4f'\
b'\x52\x50\x51\x51\x4f\x52\x4e\x52\x4d\x52\x4c\x52\x4a\x52\x48'\
b'\x50\x48\x4d\x48\x4c\x48\x4a\x49\x46\x4c\x42\x50\x41\x53\x41'\
b'\x53\x41\x55\x41\x55\x41\x57\x39\x5c\x39\x58\x4c\x20\x52\x54'\
b'\x44\x53\x44\x53\x44\x52\x44\x50\x45\x4f\x46\x4e\x48\x4d\x49'\
b'\x4d\x4b\x4d\x4c\x4d\x4c\x4d\x4d\x4e\x4e\x4f\x4e\x4f\x4e\x50'\
b'\x4e\x52\x4d\x53\x4c\x53\x49\x54\x48\x55\x44\x54\x44\x35\x48'\
b'\x5c\x5a\x45\x5a\x47\x59\x49\x57\x4a\x52\x4b\x4f\x4b\x4f\x4c'\
b'\x4f\x4c\x4f\x4c\x4f\x4c\x4f\x4d\x50\x4e\x51\x4f\x52\x4f\x53'\
b'\x4f\x54\x4e\x56\x4e\x57\x4d\x58\x4d\x57\x51\x57\x51\x55\x52'\
b'\x54\x52\x52\x52\x51\x52\x4f\x52\x4c\x51\x4b\x4f\x4a\x4d\x4a'\
b'\x4b\x4a\x49\x4b\x45\x4e\x42\x52\x41\x54\x41\x56\x41\x58\x41'\
b'\x5a\x43\x5a\x44\x5a\x45\x20\x52\x55\x45\x55\x45\x54\x44\x53'\
b'\x44\x53\x44\x51\x45\x50\x46\x4f\x47\x4f\x48\x52\x48\x55\x47'\
b'\x55\x45\x19\x48\x5c\x59\x3d\x59\x3d\x58\x3c\x57\x3c\x56\x3c'\
b'\x55\x3e\x54\x3f\x54\x41\x58\x41\x57\x45\x53\x45\x4f\x58\x4a'\
b'\x58\x4e\x45\x4b\x45\x4c\x41\x4f\x41\x4f\x3e\x50\x3b\x54\x38'\
b'\x57\x38\x58\x38\x5a\x39\x5a\x39\x59\x3d\x42\x46\x5e\x59\x50'\
b'\x59\x52\x57\x56\x54\x59\x50\x5a\x4d\x5a\x4c\x5a\x49\x59\x48'\
b'\x59\x49\x55\x4a\x55\x4c\x56\x4e\x56\x4f\x56\x51\x55\x52\x54'\
b'\x53\x52\x54\x51\x54\x4f\x54\x4f\x53\x50\x52\x51\x51\x52\x50'\
b'\x52\x4f\x52\x4d\x52\x4b\x51\x4a\x50\x49\x4d\x49\x4c\x49\x4b'\
b'\x4a\x48\x4b\x45\x4d\x43\x50\x41\x53\x41\x55\x41\x56\x41\x58'\
b'\x41\x5a\x41\x5b\x41\x5c\x41\x59\x50\x20\x52\x56\x44\x55\x44'\
b'\x54\x44\x53\x44\x51\x45\x50\x47\x4f\x4a\x4f\x4c\x4f\x4c\x4f'\
b'\x4d\x50\x4e\x50\x4e\x51\x4e\x51\x4e\x53\x4e\x54\x4d\x54\x4c'\
b'\x55\x4a\x55\x49\x55\x48\x56\x44\x56\x44\x22\x47\x5d\x5b\x45'\
b'\x5b\x45\x5b\x46\x5b\x47\x5b\x48\x5b\x48\x59\x52\x54\x52\x56'\
b'\x48\x56\x48\x56\x47\x56\x46\x56\x45\x55\x45\x54\x45\x54\x45'\
b'\x52\x45\x51\x47\x50\x49\x50\x4a\x4e\x52\x49\x52\x4e\x39\x53'\
b'\x39\x51\x44\x51\x44\x51\x43\x53\x42\x55\x41\x56\x41\x57\x41'\
b'\x59\x41\x5b\x43\x5b\x45\x3b\x4b\x59\x57\x3b\x57\x3c\x56\x3d'\
b'\x55\x3e\x54\x3e\x54\x3e\x53\x3e\x52\x3e\x51\x3d\x51\x3c\x51'\
b'\x3c\x51\x3b\x51\x3a\x52\x39\x53\x39\x54\x39\x54\x39\x55\x39'\
b'\x56\x3a\x57\x3b\x57\x3b\x20\x52\x55\x52\x55\x52\x54\x52\x53'\
b'\x52\x52\x52\x52\x52\x50\x52\x4f\x52\x4e\x51\x4d\x4f\x4d\x4e'\
b'\x4d\x4e\x4d\x4d\x4e\x4c\x4e\x4b\x4e\x4b\x4e\x4a\x4e\x49\x4f'\
b'\x47\x4f\x45\x50\x43\x50\x41\x50\x41\x55\x41\x53\x4b\x53\x4b'\
b'\x53\x4d\x53\x4d\x53\x4e\x54\x4e\x54\x4e\x55\x4e\x55\x4e\x56'\
b'\x4e\x56\x4f\x55\x51\x55\x52\x2b\x48\x5c\x5a\x3b\x5a\x3c\x5a'\
b'\x3d\x59\x3e\x58\x3e\x57\x3e\x56\x3e\x55\x3e\x55\x3d\x54\x3c'\
b'\x54\x3c\x54\x3b\x55\x3a\x55\x39\x57\x39\x57\x39\x58\x39\x59'\
b'\x39\x5a\x3a\x5a\x3b\x5a\x3b\x20\x52\x55\x51\x55\x53\x54\x56'\
b'\x52\x59\x4f\x5a\x4c\x5a\x4c\x5a\x4a\x5a\x4a\x59\x4b\x55\x4b'\
b'\x56\x4b\x56\x4c\x56\x4c\x56\x4c\x56\x4e\x56\x4f\x54\x50\x52'\
b'\x53\x41\x59\x41\x55\x51\x0e\x46\x5e\x54\x49\x59\x52\x53\x52'\
b'\x4f\x49\x4f\x49\x4d\x52\x48\x52\x4d\x39\x52\x39\x4f\x48\x4f'\
b'\x48\x56\x41\x5c\x41\x54\x49\x27\x4b\x59\x55\x52\x54\x52\x54'\
b'\x52\x53\x52\x52\x52\x51\x52\x50\x52\x4f\x52\x4e\x51\x4d\x4f'\
b'\x4d\x4e\x4d\x4e\x4d\x4d\x4d\x4c\x4e\x4b\x4e\x4b\x4e\x4a\x4e'\
b'\x49\x4f\x46\x4f\x43\x50\x40\x51\x3d\x51\x3b\x51\x39\x51\x39'\
b'\x57\x39\x53\x4b\x53\x4b\x53\x4d\x53\x4d\x53\x4e\x53\x4e\x54'\
b'\x4e\x54\x4e\x55\x4e\x56\x4e\x55\x4f\x55\x51\x55\x52\x41\x41'\
b'\x63\x61\x45\x61\x45\x61\x46\x61\x47\x60\x48\x60\x48\x5e\x52'\
b'\x59\x52\x5b\x48\x5b\x48\x5b\x47\x5b\x46\x5b\x45\x5b\x45\x5a'\
b'\x45\x59\x45\x58\x45\x56\x47\x55\x49\x55\x4a\x53\x52\x4e\x52'\
b'\x50\x48\x50\x48\x50\x47\x50\x46\x50\x45\x50\x45\x4f\x45\x4e'\
b'\x45\x4d\x45\x4b\x47\x4b\x49\x4a\x4a\x49\x52\x43\x52\x46\x46'\
b'\x46\x46\x46\x44\x46\x43\x47\x41\x47\x41\x4c\x41\x4c\x41\x4c'\
b'\x42\x4c\x43\x4b\x44\x4b\x44\x4b\x44\x4c\x43\x4e\x42\x4f\x41'\
b'\x51\x41\x52\x41\x54\x41\x56\x43\x56\x44\x57\x44\x58\x42\x5a'\
b'\x41\x5c\x41\x5d\x41\x5f\x41\x61\x43\x61\x45\x2b\x47\x5d\x5b'\
b'\x45\x5b\x45\x5b\x46\x5b\x47\x5b\x48\x5b\x48\x59\x52\x54\x52'\
b'\x56\x48\x56\x48\x56\x47\x56\x46\x56\x45\x55\x45\x54\x45\x54'\
b'\x45\x52\x45\x51\x47\x50\x49\x50\x4a\x4e\x52\x49\x52\x4b\x46'\
b'\x4b\x46\x4c\x44\x4c\x43\x4c\x41\x4c\x41\x51\x41\x51\x41\x51'\
b'\x42\x51\x43\x51\x44\x51\x44\x51\x44\x51\x43\x53\x42\x55\x41'\
b'\x56\x41\x57\x41\x59\x41\x5b\x43\x5b\x45\x2d\x47\x5d\x5b\x48'\
b'\x5b\x49\x5a\x4b\x59\x4e\x58\x50\x55\x51\x53\x52\x51\x52\x4f'\
b'\x52\x4c\x51\x4a\x4f\x49\x4d\x49\x4b\x49\x4a\x4a\x47\x4b\x45'\
b'\x4c\x43\x4f\x41\x52\x41\x53\x41\x55\x41\x58\x42\x5a\x43\x5b'\
b'\x46\x5b\x48\x20\x52\x55\x48\x55\x47\x55\x46\x54\x45\x54\x45'\
b'\x53\x45\x52\x45\x50\x46\x4f\x48\x4f\x4a\x4f\x4b\x4f\x4d\x50'\
b'\x4e\x51\x4e\x52\x4e\x54\x4d\x55\x4b\x55\x49\x55\x48\x3b\x46'\
b'\x5e\x5c\x47\x5c\x48\x5c\x4b\x5b\x4e\x59\x50\x56\x51\x53\x52'\
b'\x52\x52\x51\x52\x4f\x52\x4f\x52\x4d\x5a\x48\x5a\x4c\x47\x4c'\
b'\x46\x4c\x45\x4c\x43\x4d\x41\x4d\x41\x52\x41\x52\x41\x52\x42'\
b'\x52\x43\x51\x44\x51\x44\x52\x44\x52\x43\x53\x42\x55\x41\x56'\
b'\x41\x57\x41\x58\x41\x5a\x41\x5c\x43\x5c\x45\x5c\x47\x20\x52'\
b'\x57\x47\x57\x47\x57\x46\x56\x45\x55\x45\x55\x45\x54\x45\x52'\
b'\x46\x51\x47\x50\x49\x50\x4b\x4f\x4e\x50\x4e\x50\x4f\x51\x4f'\
b'\x51\x4f\x51\x4f\x53\x4f\x55\x4d\x56\x4b\x57\x49\x57\x47\x39'\
b'\x47\x5d\x56\x5a\x51\x5a\x52\x53\x52\x52\x53\x51\x53\x50\x53'\
b'\x50\x53\x4f\x53\x4f\x53\x50\x52\x51\x50\x52\x4f\x52\x4e\x52'\
b'\x4d\x52\x4b\x52\x49\x50\x49\x4d\x49\x4c\x49\x4b\x49\x48\x4a'\
b'\x46\x4c\x43\x4e\x42\x52\x41\x54\x41\x55\x41\x57\x41\x59\x41'\
b'\x5b\x41\x5b\x42\x56\x5a\x20\x52\x55\x44\x54\x44\x54\x44\x53'\
b'\x44\x51\x45\x50\x46\x4f\x48\x4e\x49\x4e\x4b\x4e\x4b\x4e\x4c'\
b'\x4e\x4d\x4f\x4e\x50\x4e\x50\x4e\x51\x4e\x52\x4e\x53\x4d\x53'\
b'\x4c\x54\x4b\x54\x49\x55\x49\x55\x44\x55\x44\x20\x49\x5b\x58'\
b'\x46\x58\x46\x58\x46\x57\x45\x56\x45\x55\x45\x54\x46\x53\x48'\
b'\x52\x4a\x52\x4b\x50\x52\x4b\x52\x4d\x47\x4d\x46\x4d\x45\x4e'\
b'\x43\x4e\x42\x4e\x41\x53\x41\x53\x41\x53\x42\x53\x43\x53\x44'\
b'\x53\x44\x53\x44\x54\x42\x56\x41\x58\x41\x58\x41\x59\x41\x59'\
b'\x41\x58\x46\x37\x49\x5b\x58\x45\x58\x45\x57\x45\x56\x44\x55'\
b'\x44\x54\x44\x53\x44\x52\x45\x52\x46\x52\x46\x53\x47\x54\x48'\
b'\x55\x48\x57\x49\x58\x4a\x58\x4c\x58\x4d\x58\x4e\x57\x50\x55'\
b'\x51\x52\x52\x50\x52\x4f\x52\x4e\x52\x4d\x52\x4b\x52\x4b\x52'\
b'\x4c\x4d\x4c\x4e\x4d\x4e\x4e\x4f\x50\x4f\x50\x4f\x52\x4f\x53'\
b'\x4e\x53\x4d\x53\x4d\x52\x4c\x51\x4b\x50\x4b\x4e\x4a\x4d\x49'\
b'\x4d\x47\x4d\x46\x4d\x45\x4e\x43\x4f\x42\x52\x41\x54\x41\x55'\
b'\x41\x56\x41\x58\x41\x59\x41\x59\x41\x58\x45\x29\x4a\x5a\x57'\
b'\x45\x54\x45\x52\x4b\x52\x4b\x52\x4c\x52\x4c\x52\x4d\x52\x4d'\
b'\x52\x4e\x53\x4e\x53\x4e\x53\x4e\x54\x4e\x55\x4e\x55\x4e\x56'\
b'\x4e\x55\x52\x54\x52\x54\x52\x53\x52\x51\x52\x51\x52\x50\x52'\
b'\x4e\x52\x4d\x51\x4c\x4f\x4c\x4e\x4c\x4e\x4d\x4d\x4d\x4c\x4d'\
b'\x4c\x4d\x4b\x4e\x45\x4c\x45\x4d\x41\x4f\x41\x50\x3d\x55\x3c'\
b'\x54\x41\x58\x41\x57\x45\x2d\x47\x5d\x59\x4c\x59\x4d\x59\x4f'\
b'\x58\x50\x58\x52\x58\x52\x53\x52\x53\x52\x53\x51\x53\x50\x53'\
b'\x4f\x53\x4f\x53\x4f\x53\x50\x51\x51\x4f\x52\x4e\x52\x4d\x52'\
b'\x4b\x52\x49\x50\x49\x4e\x49\x4e\x49\x4d\x49\x4c\x49\x4b\x49'\
b'\x4b\x4b\x41\x50\x41\x4e\x4b\x4e\x4b\x4e\x4b\x4e\x4c\x4e\x4c'\
b'\x4e\x4d\x4e\x4d\x4f\x4e\x50\x4e\x50\x4e\x52\x4d\x53\x4c\x54'\
b'\x4a\x54\x49\x56\x41\x5b\x41\x59\x4c\x13\x47\x5d\x51\x52\x4b'\
b'\x52\x49\x41\x4e\x41\x4f\x4a\x4f\x4b\x4f\x4c\x4f\x4d\x4f\x4e'\
b'\x4f\x4e\x4f\x4e\x4f\x4e\x50\x4d\x50\x4c\x50\x4b\x51\x4a\x55'\
b'\x41\x5b\x41\x51\x52\x2b\x43\x61\x57\x52\x51\x52\x51\x48\x51'\
b'\x47\x51\x46\x51\x46\x51\x46\x51\x46\x51\x47\x51\x47\x50\x48'\
b'\x50\x48\x4b\x52\x46\x52\x45\x41\x4a\x41\x4a\x4c\x4a\x4c\x4a'\
b'\x4e\x4a\x4e\x4a\x4e\x4a\x4e\x4a\x4d\x4a\x4d\x4a\x4c\x4a\x4c'\
b'\x50\x41\x55\x41\x55\x4c\x55\x4c\x55\x4d\x55\x4d\x55\x4e\x55'\
b'\x4e\x55\x4e\x55\x4e\x55\x4d\x55\x4d\x56\x4c\x56\x4c\x5a\x41'\
b'\x5f\x41\x57\x52\x1b\x45\x5f\x56\x49\x59\x52\x54\x52\x52\x4e'\
b'\x52\x4d\x52\x4c\x52\x4c\x52\x4c\x51\x4c\x51\x4d\x50\x4d\x4d'\
b'\x52\x47\x52\x4f\x49\x4b\x41\x51\x41\x52\x45\x52\x46\x53\x47'\
b'\x53\x47\x53\x47\x53\x47\x54\x46\x54\x45\x57\x41\x5d\x41\x56'\
b'\x49\x1e\x45\x5f\x53\x54\x52\x55\x50\x57\x4e\x59\x4b\x5a\x49'\
b'\x5a\x49\x5a\x47\x5a\x47\x5a\x48\x55\x48\x56\x49\x56\x49\x56'\
b'\x4a\x56\x4c\x55\x4d\x54\x4e\x52\x4b\x41\x50\x41\x52\x4b\x52'\
b'\x4c\x52\x4d\x52\x4e\x52\x4e\x52\x4d\x52\x4c\x53\x4b\x58\x41'\
b'\x5d\x41\x53\x54\x0b\x46\x5e\x5b\x44\x51\x4e\x59\x4e\x58\x52'\
b'\x48\x52\x49\x50\x54\x45\x4c\x45\x4d\x41\x5c\x41\x5b\x44\x33'\
b'\x4a\x5a\x58\x3d\x57\x3d\x56\x3e\x55\x3e\x55\x3f\x55\x40\x54'\
b'\x44\x53\x46\x51\x49\x50\x49\x50\x49\x51\x4a\x52\x4b\x52\x4d'\
b'\x52\x4d\x52\x4e\x51\x52\x51\x52\x51\x53\x51\x53\x51\x55\x53'\
b'\x55\x52\x58\x50\x58\x4e\x57\x4d\x56\x4c\x55\x4c\x54\x4c\x53'\
b'\x4c\x52\x4d\x52\x4d\x4e\x4e\x4d\x4e\x4d\x4e\x4d\x4e\x4c\x4c'\
b'\x4b\x4c\x4b\x4c\x47\x4d\x47\x4f\x46\x4f\x45\x50\x40\x50\x3f'\
b'\x51\x3d\x53\x3c\x54\x3b\x56\x3a\x58\x3a\x58\x3a\x58\x3d\x05'\
b'\x4e\x56\x50\x5a\x50\x38\x54\x38\x54\x5a\x50\x5a\x34\x4a\x5a'\
b'\x58\x4b\x56\x4b\x55\x4c\x55\x4e\x54\x52\x54\x53\x53\x55\x51'\
b'\x57\x50\x58\x4e\x58\x4c\x58\x4c\x58\x4c\x55\x4d\x55\x4e\x55'\
b'\x4f\x54\x4f\x53\x4f\x52\x50\x4e\x51\x4c\x53\x49\x54\x49\x54'\
b'\x49\x53\x48\x52\x47\x52\x46\x52\x45\x52\x44\x53\x44\x53\x40'\
b'\x53\x40\x53\x3f\x53\x3f\x53\x3d\x51\x3d\x52\x3a\x54\x3a\x56'\
b'\x3b\x57\x3c\x58\x3e\x58\x3f\x58\x3f\x58\x40\x57\x41\x57\x44'\
b'\x56\x45\x56\x45\x56\x46\x56\x47\x58\x48\x58\x48\x58\x4b\x29'\
b'\x47\x5d\x5b\x46\x5a\x49\x59\x4a\x57\x4b\x56\x4b\x55\x4b\x54'\
b'\x4b\x53\x4b\x52\x4a\x51\x4a\x51\x49\x4f\x49\x4f\x49\x4e\x49'\
b'\x4d\x49\x4d\x4a\x4d\x4b\x4d\x4b\x49\x4b\x49\x4a\x4a\x48\x4b'\
b'\x46\x4d\x45\x4e\x45\x4f\x45\x50\x45\x51\x46\x52\x46\x52\x47'\
b'\x53\x47\x54\x47\x54\x48\x55\x48\x55\x48\x56\x48\x57\x47\x57'\
b'\x47\x57\x46\x57\x45\x5b\x45\x5b\x46\x0b\x48\x5c\x4a\x52\x4a'\
b'\x3b\x5a\x3b\x5a\x52\x4a\x52\x20\x52\x4c\x50\x58\x50\x58\x3d'\
b'\x4c\x3d\x4c\x50'

_index =\
b'\x00\x00\x03\x00\x3c\x00\x55\x00\x9e\x00\x2f\x01\xf8\x01\xd7'\
b'\x02\xe4\x02\x15\x03\x46\x03\x69\x03\x86\x03\x93\x03\xa0\x03'\
b'\xcd\x03\xda\x03\x1d\x04\x2e\x04\x71\x04\xc4\x04\xef\x04\x30'\
b'\x05\x87\x05\xa4\x05\x13\x06\x6c\x06\xc5\x06\xfe\x06\x13\x07'\
b'\x2c\x07\x41\x07\xc2\x07\xb3\x08\xe8\x08\x55\x09\xae\x09\xef'\
b'\x09\x0c\x0a\x25\x0a\x86\x0a\xa3\x0a\xb0\x0a\xe1\x0a\x3c\x0b'\
b'\x4d\x0b\xa2\x0b\xe3\x0b\x5c\x0c\x99\x0c\xe2\x0c\x33\x0d\xb8'\
b'\x0d\xcd\x0d\x12\x0e\x33\x0e\x94\x0e\xd9\x0e\xfe\x0e\x17\x0f'\
b'\x2c\x0f\x39\x0f\x4e\x0f\x63\x0f\x70\x0f\x7d\x0f\xf6\x0f\x63'\
b'\x10\xb4\x10\x29\x11\x96\x11\xcb\x11\x52\x12\x99\x12\x12\x13'\
b'\x6b\x13\x8a\x13\xdb\x13\x60\x14\xb9\x14\x16\x15\x8f\x15\x04'\
b'\x16\x47\x16\xb8\x16\x0d\x17\x6a\x17\x93\x17\xec\x17\x25\x18'\
b'\x64\x18\x7d\x18\xe6\x18\xf3\x18\x5e\x19\xb3\x19'

FONT = memoryview(_font)
INDEX = memoryview(_index)
