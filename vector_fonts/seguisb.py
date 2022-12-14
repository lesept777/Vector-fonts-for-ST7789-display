FIRST = 32
LAST = 127
WIDTH = 25
HEIGHT = 26

_font =\
b'\x01\x4f\x55\x13\x4e\x56\x53\x3f\x53\x4d\x51\x4d\x50\x3f\x53'\
b'\x3f\x20\x52\x52\x52\x51\x52\x50\x51\x50\x51\x50\x50\x51\x4f'\
b'\x52\x4f\x53\x4f\x54\x50\x54\x51\x54\x51\x53\x52\x52\x52\x0b'\
b'\x4c\x58\x51\x3f\x51\x45\x4e\x45\x4e\x3f\x51\x3f\x20\x52\x56'\
b'\x3f\x56\x45\x53\x45\x53\x3f\x56\x3f\x23\x49\x5b\x59\x44\x59'\
b'\x46\x56\x46\x55\x4a\x58\x4a\x58\x4c\x55\x4c\x54\x50\x52\x50'\
b'\x53\x4c\x50\x4c\x4f\x50\x4d\x50\x4e\x4c\x4b\x4c\x4b\x4a\x4e'\
b'\x4a\x4f\x46\x4c\x46\x4c\x44\x4f\x44\x50\x3f\x52\x3f\x51\x44'\
b'\x54\x44\x55\x3f\x57\x3f\x56\x44\x59\x44\x20\x52\x54\x46\x51'\
b'\x46\x50\x4a\x53\x4a\x54\x46\x30\x4a\x5a\x53\x52\x53\x55\x51'\
b'\x55\x51\x52\x4e\x52\x4d\x51\x4d\x4e\x4d\x4f\x50\x50\x51\x50'\
b'\x51\x4a\x4e\x48\x4c\x46\x4c\x44\x4c\x43\x4f\x40\x51\x3f\x51'\
b'\x3d\x53\x3d\x53\x3f\x55\x3f\x56\x40\x56\x43\x55\x42\x53\x42'\
b'\x53\x48\x56\x49\x58\x4c\x58\x4d\x58\x4f\x55\x52\x53\x52\x20'\
b'\x52\x51\x47\x51\x42\x50\x42\x4f\x43\x4f\x44\x4f\x45\x50\x46'\
b'\x51\x47\x20\x52\x53\x4b\x53\x50\x55\x4f\x55\x4d\x55\x4c\x53'\
b'\x4b\x3d\x46\x5e\x4c\x49\x4a\x49\x48\x46\x48\x44\x48\x42\x4b'\
b'\x3f\x4d\x3f\x4f\x3f\x51\x42\x51\x44\x51\x46\x4e\x49\x4c\x49'\
b'\x20\x52\x4d\x41\x4c\x41\x4a\x43\x4a\x44\x4a\x45\x4c\x47\x4d'\
b'\x47\x4e\x47\x4f\x45\x4f\x44\x4f\x43\x4e\x41\x4d\x41\x20\x52'\
b'\x59\x3f\x4d\x52\x4b\x52\x57\x3f\x59\x3f\x20\x52\x57\x52\x55'\
b'\x52\x53\x50\x53\x4e\x53\x4b\x55\x49\x58\x49\x5a\x49\x5c\x4b'\
b'\x5c\x4d\x5c\x50\x59\x52\x57\x52\x20\x52\x57\x4b\x56\x4b\x55'\
b'\x4c\x55\x4e\x55\x4f\x56\x51\x57\x51\x59\x51\x5a\x4f\x5a\x4d'\
b'\x5a\x4c\x59\x4b\x57\x4b\x4c\x47\x5d\x57\x52\x55\x50\x55\x51'\
b'\x53\x51\x52\x52\x50\x52\x4f\x52\x4e\x52\x4c\x52\x4a\x50\x49'\
b'\x4e\x49\x4d\x49\x4a\x4e\x48\x4c\x45\x4c\x44\x4c\x43\x4c\x41'\
b'\x4e\x40\x50\x3f\x51\x3f\x52\x3f\x54\x40\x55\x41\x55\x42\x55'\
b'\x43\x55\x44\x55\x45\x54\x47\x53\x48\x51\x48\x52\x49\x55\x4b'\
b'\x56\x4d\x56\x4c\x56\x4b\x57\x4a\x57\x49\x57\x48\x59\x48\x59'\
b'\x4c\x57\x4e\x58\x4f\x5a\x51\x5b\x52\x57\x52\x20\x52\x53\x43'\
b'\x53\x43\x52\x42\x52\x42\x51\x41\x51\x41\x50\x41\x4f\x42\x4f'\
b'\x42\x4e\x43\x4e\x44\x4e\x45\x50\x47\x53\x45\x53\x43\x20\x52'\
b'\x54\x4f\x52\x4d\x4f\x4a\x4e\x4a\x4c\x4c\x4c\x4d\x4c\x4e\x4d'\
b'\x4f\x4e\x50\x4f\x50\x50\x50\x52\x50\x54\x4f\x05\x4f\x55\x53'\
b'\x3f\x53\x45\x51\x45\x51\x3f\x53\x3f\x0b\x4d\x57\x55\x56\x53'\
b'\x56\x4f\x52\x4f\x4b\x4f\x44\x53\x3f\x55\x3f\x51\x44\x51\x4b'\
b'\x51\x51\x55\x56\x0b\x4d\x57\x51\x56\x4f\x56\x53\x51\x53\x4b'\
b'\x53\x44\x4f\x3f\x51\x3f\x55\x44\x55\x4b\x55\x52\x51\x56\x10'\
b'\x4b\x59\x57\x44\x53\x45\x56\x48\x54\x49\x52\x46\x50\x49\x4e'\
b'\x48\x51\x45\x4d\x44\x4e\x42\x51\x43\x51\x3f\x53\x3f\x53\x43'\
b'\x56\x42\x57\x44\x0d\x4a\x5a\x58\x4b\x53\x4b\x53\x51\x51\x51'\
b'\x51\x4b\x4c\x4b\x4c\x49\x51\x49\x51\x44\x53\x44\x53\x49\x58'\
b'\x49\x58\x4b\x05\x4e\x56\x54\x4f\x52\x55\x50\x55\x51\x4f\x54'\
b'\x4f\x05\x4c\x58\x56\x4c\x4e\x4c\x4e\x4a\x56\x4a\x56\x4c\x0d'\
b'\x4e\x56\x52\x52\x51\x52\x50\x51\x50\x51\x50\x50\x51\x4f\x52'\
b'\x4f\x53\x4f\x54\x50\x54\x51\x54\x51\x53\x52\x52\x52\x05\x4a'\
b'\x5a\x58\x3f\x4f\x55\x4c\x55\x55\x3f\x58\x3f\x16\x4a\x5a\x52'\
b'\x52\x4f\x52\x4c\x4e\x4c\x49\x4c\x44\x4f\x3f\x52\x3f\x58\x3f'\
b'\x58\x49\x58\x4d\x55\x52\x52\x52\x20\x52\x52\x42\x4f\x42\x4f'\
b'\x49\x4f\x50\x52\x50\x55\x50\x55\x49\x55\x42\x52\x42\x0e\x4d'\
b'\x57\x55\x3f\x55\x52\x52\x52\x52\x43\x52\x43\x50\x44\x4f\x44'\
b'\x4f\x42\x4f\x42\x51\x41\x52\x40\x53\x40\x54\x3f\x55\x3f\x2f'\
b'\x4a\x5a\x58\x52\x4c\x52\x4c\x51\x4c\x50\x4d\x4e\x4e\x4d\x4f'\
b'\x4c\x50\x4a\x51\x49\x52\x49\x52\x48\x53\x47\x54\x46\x54\x45'\
b'\x54\x45\x54\x44\x54\x43\x53\x42\x52\x42\x51\x42\x50\x42\x4e'\
b'\x43\x4d\x44\x4d\x41\x4d\x40\x4f\x40\x50\x3f\x51\x3f\x52\x3f'\
b'\x53\x3f\x55\x40\x57\x41\x58\x43\x58\x44\x58\x45\x57\x47\x56'\
b'\x49\x55\x4a\x54\x4b\x53\x4b\x51\x4d\x50\x4e\x4f\x4f\x4f\x4f'\
b'\x4f\x4f\x58\x4f\x58\x52\x23\x4a\x5a\x4c\x51\x4c\x4f\x4e\x50'\
b'\x50\x50\x52\x50\x55\x4e\x55\x4d\x55\x4a\x50\x4a\x4e\x4a\x4e'\
b'\x47\x50\x47\x54\x47\x54\x44\x54\x42\x51\x42\x4f\x42\x4d\x43'\
b'\x4d\x40\x4f\x3f\x52\x3f\x54\x3f\x57\x42\x57\x44\x57\x47\x53'\
b'\x48\x53\x48\x55\x49\x58\x4b\x58\x4d\x58\x4f\x54\x52\x51\x52'\
b'\x4e\x52\x4c\x51\x17\x49\x5b\x56\x3f\x56\x4b\x59\x4b\x59\x4e'\
b'\x56\x4e\x56\x52\x53\x52\x53\x4e\x4b\x4e\x4b\x4b\x4c\x4a\x4f'\
b'\x47\x51\x44\x53\x41\x53\x3f\x56\x3f\x20\x52\x53\x4b\x53\x44'\
b'\x52\x46\x4f\x4a\x4e\x4b\x53\x4b\x1b\x4b\x59\x4d\x52\x4d\x4f'\
b'\x4e\x50\x50\x50\x52\x50\x54\x4e\x54\x4c\x54\x4b\x52\x49\x50'\
b'\x49\x4f\x49\x4d\x49\x4e\x3f\x57\x3f\x57\x42\x50\x42\x50\x47'\
b'\x51\x47\x51\x47\x54\x47\x57\x4a\x57\x4c\x57\x4f\x54\x52\x51'\
b'\x52\x4e\x52\x4d\x52\x3b\x4a\x5a\x58\x4c\x58\x4d\x57\x50\x56'\
b'\x51\x53\x52\x52\x52\x51\x52\x4e\x51\x4d\x4f\x4c\x4c\x4c\x4a'\
b'\x4c\x47\x4d\x43\x4f\x41\x52\x3f\x54\x3f\x55\x3f\x56\x3f\x57'\
b'\x40\x57\x42\x56\x42\x55\x42\x54\x42\x53\x42\x51\x42\x50\x44'\
b'\x4f\x47\x4f\x48\x4f\x48\x50\x47\x52\x46\x53\x46\x54\x46\x56'\
b'\x47\x57\x49\x58\x4b\x58\x4c\x20\x52\x55\x4c\x55\x4b\x55\x4a'\
b'\x54\x49\x53\x49\x52\x49\x51\x49\x50\x49\x4f\x4a\x4f\x4b\x4f'\
b'\x4c\x4f\x4d\x4f\x4e\x50\x4f\x51\x50\x52\x50\x53\x50\x54\x4f'\
b'\x55\x4e\x55\x4d\x55\x4c\x10\x4a\x5a\x58\x41\x57\x43\x55\x47'\
b'\x53\x4b\x52\x50\x52\x52\x4f\x52\x4f\x50\x50\x4c\x52\x48\x53'\
b'\x44\x55\x42\x4c\x42\x4c\x3f\x58\x3f\x58\x41\x51\x4a\x5a\x4c'\
b'\x4d\x4c\x4c\x4c\x4b\x4d\x49\x4e\x48\x4f\x48\x4e\x47\x4c\x45'\
b'\x4c\x44\x4c\x43\x4d\x41\x4f\x40\x51\x3f\x52\x3f\x53\x3f\x55'\
b'\x40\x57\x41\x57\x43\x57\x44\x57\x45\x56\x47\x55\x48\x56\x48'\
b'\x57\x49\x58\x4b\x58\x4c\x58\x4d\x58\x4e\x57\x50\x56\x51\x53'\
b'\x52\x52\x52\x51\x52\x4e\x51\x4d\x50\x4c\x4e\x4c\x4d\x20\x52'\
b'\x4f\x4d\x4f\x4d\x4f\x4f\x50\x50\x51\x50\x52\x50\x53\x50\x54'\
b'\x4f\x55\x4f\x55\x4d\x55\x4d\x55\x4c\x55\x4b\x54\x4a\x53\x49'\
b'\x52\x49\x51\x49\x50\x4a\x4f\x4b\x4f\x4c\x4f\x4d\x20\x52\x4f'\
b'\x44\x4f\x45\x50\x46\x50\x47\x51\x47\x52\x47\x53\x47\x53\x47'\
b'\x54\x46\x55\x45\x55\x44\x55\x44\x54\x43\x53\x42\x53\x41\x52'\
b'\x41\x51\x41\x50\x42\x50\x43\x4f\x44\x4f\x44\x41\x4a\x5a\x58'\
b'\x48\x58\x4b\x57\x4f\x55\x51\x52\x52\x50\x52\x50\x52\x4f\x52'\
b'\x4e\x52\x4d\x52\x4d\x52\x4d\x4f\x4d\x4f\x4e\x4f\x4f\x50\x50'\
b'\x50\x50\x50\x51\x50\x53\x4f\x54\x4d\x55\x4b\x55\x49\x55\x49'\
b'\x55\x4a\x54\x4a\x53\x4b\x52\x4b\x51\x4b\x50\x4b\x4e\x4a\x4d'\
b'\x49\x4c\x47\x4c\x45\x4c\x44\x4d\x42\x4e\x40\x51\x3f\x52\x3f'\
b'\x53\x3f\x56\x40\x57\x42\x58\x45\x58\x48\x20\x52\x55\x46\x55'\
b'\x45\x55\x43\x54\x42\x53\x42\x52\x42\x51\x42\x50\x42\x4f\x43'\
b'\x4f\x44\x4f\x45\x4f\x46\x4f\x47\x50\x48\x51\x49\x52\x49\x53'\
b'\x49\x54\x48\x55\x48\x55\x46\x55\x46\x1b\x4e\x56\x52\x52\x51'\
b'\x52\x50\x51\x50\x51\x50\x50\x51\x4f\x52\x4f\x53\x4f\x54\x50'\
b'\x54\x51\x54\x51\x53\x52\x52\x52\x20\x52\x52\x48\x51\x48\x50'\
b'\x47\x50\x46\x50\x46\x51\x45\x52\x45\x53\x45\x54\x46\x54\x46'\
b'\x54\x47\x53\x48\x52\x48\x13\x4e\x56\x52\x48\x52\x48\x51\x47'\
b'\x51\x46\x51\x46\x52\x45\x52\x45\x53\x45\x54\x46\x54\x46\x54'\
b'\x47\x53\x48\x52\x48\x20\x52\x54\x4f\x52\x55\x50\x55\x51\x4f'\
b'\x54\x4f\x09\x4a\x5a\x58\x51\x4c\x4b\x4c\x4a\x58\x44\x58\x46'\
b'\x4f\x4a\x4f\x4a\x58\x4e\x58\x51\x0b\x4a\x5a\x58\x49\x4c\x49'\
b'\x4c\x47\x58\x47\x58\x49\x20\x52\x58\x4e\x4c\x4e\x4c\x4c\x58'\
b'\x4c\x58\x4e\x09\x4a\x5a\x58\x4b\x4c\x51\x4c\x4e\x55\x4a\x55'\
b'\x4a\x4c\x46\x4c\x44\x58\x4a\x58\x4b\x37\x4b\x59\x50\x4d\x50'\
b'\x4c\x50\x4b\x50\x4b\x50\x4a\x50\x49\x51\x48\x52\x47\x53\x46'\
b'\x54\x45\x54\x44\x54\x43\x53\x43\x53\x42\x52\x42\x51\x42\x4f'\
b'\x42\x4d\x43\x4d\x40\x4f\x3f\x52\x3f\x53\x3f\x55\x40\x56\x41'\
b'\x57\x42\x57\x43\x57\x44\x56\x46\x55\x47\x54\x48\x53\x49\x52'\
b'\x4a\x52\x4b\x52\x4c\x52\x4c\x53\x4d\x50\x4d\x20\x52\x51\x52'\
b'\x51\x52\x50\x52\x50\x51\x50\x51\x50\x50\x50\x4f\x51\x4f\x51'\
b'\x4f\x52\x4f\x53\x4f\x53\x50\x53\x51\x53\x51\x53\x52\x52\x52'\
b'\x51\x52\x41\x45\x5f\x54\x4d\x54\x4d\x53\x50\x50\x50\x4f\x50'\
b'\x4d\x4d\x4d\x4b\x4d\x48\x50\x44\x52\x44\x53\x44\x54\x45\x54'\
b'\x46\x54\x46\x55\x45\x55\x44\x57\x44\x56\x4b\x56\x4b\x56\x4e'\
b'\x58\x4e\x59\x4e\x5a\x4b\x5a\x49\x5a\x45\x56\x41\x52\x41\x4f'\
b'\x41\x4a\x46\x4a\x4a\x4a\x4e\x4e\x53\x52\x53\x55\x53\x58\x52'\
b'\x58\x53\x55\x54\x52\x54\x4d\x54\x47\x4f\x47\x4a\x47\x45\x4e'\
b'\x3f\x52\x3f\x57\x3f\x5d\x44\x5d\x49\x5d\x4c\x59\x50\x57\x50'\
b'\x54\x50\x54\x4d\x20\x52\x52\x46\x51\x46\x4f\x49\x4f\x4b\x4f'\
b'\x4c\x50\x4e\x51\x4e\x53\x4e\x54\x4b\x54\x48\x54\x46\x52\x46'\
b'\x13\x47\x5d\x5b\x52\x57\x52\x56\x4d\x4e\x4d\x4d\x52\x49\x52'\
b'\x50\x3f\x54\x3f\x5b\x52\x20\x52\x55\x4b\x52\x43\x52\x43\x52'\
b'\x42\x52\x42\x52\x43\x52\x43\x4f\x4b\x55\x4b\x25\x4a\x5a\x4c'\
b'\x52\x4c\x3f\x52\x3f\x54\x3f\x57\x42\x57\x44\x57\x45\x56\x48'\
b'\x54\x48\x54\x48\x56\x48\x58\x4b\x58\x4d\x58\x4f\x55\x52\x52'\
b'\x52\x4c\x52\x20\x52\x4f\x42\x4f\x47\x51\x47\x52\x47\x54\x46'\
b'\x54\x44\x54\x42\x51\x42\x4f\x42\x20\x52\x4f\x4a\x4f\x50\x51'\
b'\x50\x53\x50\x55\x4e\x55\x4d\x55\x4a\x51\x4a\x4f\x4a\x17\x49'\
b'\x5b\x59\x51\x57\x52\x54\x52\x50\x52\x4b\x4d\x4b\x49\x4b\x45'\
b'\x50\x3f\x55\x3f\x57\x3f\x59\x40\x59\x43\x57\x42\x55\x42\x52'\
b'\x42\x4e\x46\x4e\x49\x4e\x4c\x52\x50\x54\x50\x57\x50\x59\x4e'\
b'\x59\x51\x13\x48\x5c\x4a\x52\x4a\x3f\x50\x3f\x5a\x3f\x5a\x49'\
b'\x5a\x4d\x54\x52\x4f\x52\x4a\x52\x20\x52\x4d\x42\x4d\x4f\x50'\
b'\x4f\x53\x4f\x57\x4c\x57\x49\x57\x42\x50\x42\x4d\x42\x0d\x4b'\
b'\x59\x57\x52\x4d\x52\x4d\x3f\x57\x3f\x57\x42\x50\x42\x50\x47'\
b'\x56\x47\x56\x4a\x50\x4a\x50\x4f\x57\x4f\x57\x52\x0b\x4b\x59'\
b'\x57\x42\x50\x42\x50\x48\x56\x48\x56\x4a\x50\x4a\x50\x52\x4d'\
b'\x52\x4d\x3f\x57\x3f\x57\x42\x1b\x48\x5c\x5a\x51\x57\x52\x53'\
b'\x52\x4f\x52\x4a\x4d\x4a\x49\x4a\x45\x50\x3f\x54\x3f\x57\x3f'\
b'\x59\x40\x59\x43\x57\x42\x54\x42\x51\x42\x4d\x46\x4d\x49\x4d'\
b'\x4c\x51\x50\x53\x50\x55\x50\x57\x4f\x57\x4b\x53\x4b\x53\x48'\
b'\x5a\x48\x5a\x51\x0d\x49\x5b\x59\x52\x56\x52\x56\x4a\x4e\x4a'\
b'\x4e\x52\x4b\x52\x4b\x3f\x4e\x3f\x4e\x47\x56\x47\x56\x3f\x59'\
b'\x3f\x59\x52\x05\x4e\x56\x54\x52\x50\x52\x50\x3f\x54\x3f\x54'\
b'\x52\x0e\x4c\x58\x56\x4b\x56\x4f\x53\x52\x50\x52\x4f\x52\x4e'\
b'\x52\x4e\x4f\x4f\x50\x50\x50\x53\x50\x53\x4b\x53\x3f\x56\x3f'\
b'\x56\x4b\x12\x49\x5b\x59\x52\x55\x52\x4f\x4a\x4e\x49\x4e\x49'\
b'\x4e\x49\x4e\x52\x4b\x52\x4b\x3f\x4e\x3f\x4e\x48\x4e\x48\x4e'\
b'\x48\x4f\x48\x55\x3f\x58\x3f\x51\x48\x59\x52\x07\x4b\x59\x57'\
b'\x52\x4d\x52\x4d\x3f\x50\x3f\x50\x4f\x57\x4f\x57\x52\x1d\x46'\
b'\x5e\x5c\x52\x59\x52\x59\x46\x59\x45\x59\x42\x59\x42\x59\x44'\
b'\x59\x44\x53\x52\x51\x52\x4b\x44\x4b\x44\x4b\x42\x4b\x42\x4b'\
b'\x44\x4b\x46\x4b\x52\x48\x52\x48\x3f\x4c\x3f\x51\x4c\x52\x4d'\
b'\x52\x4e\x52\x4e\x53\x4c\x53\x4c\x58\x3f\x5c\x3f\x5c\x52\x15'\
b'\x48\x5c\x5a\x52\x56\x52\x4e\x44\x4d\x44\x4d\x43\x4d\x43\x4d'\
b'\x44\x4d\x46\x4d\x52\x4a\x52\x4a\x3f\x4e\x3f\x56\x4d\x57\x4e'\
b'\x57\x4e\x57\x4e\x57\x4d\x57\x4b\x57\x3f\x5a\x3f\x5a\x52\x1b'\
b'\x47\x5d\x52\x52\x4e\x52\x49\x4d\x49\x49\x49\x44\x4e\x3f\x52'\
b'\x3f\x56\x3f\x5b\x44\x5b\x49\x5b\x4d\x56\x52\x52\x52\x20\x52'\
b'\x52\x42\x50\x42\x4c\x46\x4c\x49\x4c\x4c\x4f\x50\x52\x50\x55'\
b'\x50\x58\x4c\x58\x49\x58\x45\x55\x42\x52\x42\x16\x4a\x5a\x4f'\
b'\x4b\x4f\x52\x4c\x52\x4c\x3f\x51\x3f\x55\x3f\x58\x42\x58\x45'\
b'\x58\x48\x54\x4b\x51\x4b\x4f\x4b\x20\x52\x4f\x42\x4f\x49\x51'\
b'\x49\x53\x49\x55\x47\x55\x45\x55\x42\x51\x42\x4f\x42\x2f\x46'\
b'\x5e\x51\x52\x4f\x52\x4c\x51\x49\x4e\x48\x4b\x48\x49\x48\x47'\
b'\x49\x43\x4c\x41\x4f\x3f\x51\x3f\x53\x3f\x56\x41\x59\x43\x5a'\
b'\x46\x5a\x49\x5a\x4b\x58\x4f\x56\x51\x5c\x54\x57\x54\x54\x52'\
b'\x53\x52\x52\x52\x51\x52\x20\x52\x51\x42\x50\x42\x4e\x43\x4c'\
b'\x45\x4b\x47\x4b\x49\x4b\x4a\x4c\x4d\x4e\x4f\x50\x50\x51\x50'\
b'\x52\x50\x54\x4f\x56\x4d\x57\x4a\x57\x49\x57\x47\x56\x45\x55'\
b'\x43\x52\x42\x51\x42\x2b\x49\x5b\x59\x52\x56\x52\x53\x4d\x52'\
b'\x4c\x51\x4b\x51\x4b\x50\x4a\x4f\x4a\x4e\x4a\x4e\x52\x4b\x52'\
b'\x4b\x3f\x51\x3f\x52\x3f\x54\x40\x56\x41\x57\x43\x57\x44\x57'\
b'\x45\x56\x47\x55\x48\x54\x49\x53\x4a\x53\x4a\x53\x4a\x54\x4b'\
b'\x55\x4b\x55\x4c\x56\x4d\x59\x52\x20\x52\x4e\x42\x4e\x48\x50'\
b'\x48\x51\x48\x52\x48\x53\x47\x54\x46\x54\x45\x54\x43\x52\x42'\
b'\x50\x42\x4e\x42\x37\x4a\x5a\x4c\x51\x4c\x4e\x4d\x4e\x4e\x4f'\
b'\x4f\x50\x50\x50\x51\x50\x53\x50\x55\x4e\x55\x4d\x55\x4d\x54'\
b'\x4c\x53\x4b\x51\x4a\x51\x4a\x50\x49\x4e\x48\x4d\x47\x4c\x45'\
b'\x4c\x44\x4c\x43\x4d\x41\x4f\x40\x52\x3f\x53\x3f\x56\x3f\x57'\
b'\x40\x57\x43\x56\x42\x53\x42\x52\x42\x51\x42\x50\x43\x4f\x44'\
b'\x4f\x44\x4f\x45\x50\x46\x51\x46\x52\x47\x53\x48\x54\x48\x56'\
b'\x49\x57\x4b\x58\x4c\x58\x4d\x58\x4f\x57\x51\x55\x52\x52\x52'\
b'\x51\x52\x51\x52\x4f\x52\x4e\x52\x4c\x52\x4c\x51\x09\x49\x5b'\
b'\x59\x42\x54\x42\x54\x52\x50\x52\x50\x42\x4b\x42\x4b\x3f\x59'\
b'\x3f\x59\x42\x0f\x49\x5b\x59\x4b\x59\x52\x52\x52\x4b\x52\x4b'\
b'\x4b\x4b\x3f\x4e\x3f\x4e\x4a\x4e\x50\x52\x50\x56\x50\x56\x4a'\
b'\x56\x3f\x59\x3f\x59\x4b\x0d\x48\x5c\x5a\x3f\x54\x52\x50\x52'\
b'\x4a\x3f\x4d\x3f\x52\x4e\x52\x4e\x52\x4f\x52\x4f\x52\x4e\x52'\
b'\x4e\x57\x3f\x5a\x3f\x1d\x44\x60\x5e\x3f\x59\x52\x56\x52\x52'\
b'\x45\x52\x44\x52\x43\x52\x43\x52\x44\x52\x45\x4e\x52\x4b\x52'\
b'\x46\x3f\x49\x3f\x4c\x4d\x4c\x4e\x4d\x4f\x4d\x4f\x4d\x4e\x4d'\
b'\x4d\x51\x3f\x54\x3f\x57\x4d\x58\x4e\x58\x4f\x58\x4f\x58\x4e'\
b'\x58\x4d\x5b\x3f\x5e\x3f\x17\x48\x5c\x5a\x52\x56\x52\x52\x4b'\
b'\x52\x4b\x52\x4a\x52\x4a\x52\x4b\x52\x4b\x4e\x52\x4a\x52\x50'\
b'\x49\x4b\x3f\x4e\x3f\x52\x46\x52\x46\x52\x47\x52\x47\x53\x46'\
b'\x53\x46\x56\x3f\x5a\x3f\x54\x49\x5a\x52\x0f\x48\x5c\x5a\x3f'\
b'\x53\x4b\x53\x52\x50\x52\x50\x4b\x4a\x3f\x4e\x3f\x52\x47\x52'\
b'\x48\x52\x48\x52\x48\x52\x48\x52\x47\x56\x3f\x5a\x3f\x0b\x49'\
b'\x5b\x59\x41\x4f\x4f\x59\x4f\x59\x52\x4b\x52\x4b\x51\x55\x42'\
b'\x4c\x42\x4c\x3f\x59\x3f\x59\x41\x09\x4d\x57\x55\x56\x4f\x56'\
b'\x4f\x3f\x55\x3f\x55\x42\x52\x42\x52\x54\x55\x54\x55\x56\x05'\
b'\x4a\x5a\x58\x55\x55\x55\x4c\x3f\x4f\x3f\x58\x55\x09\x4d\x57'\
b'\x55\x56\x4f\x56\x4f\x54\x52\x54\x52\x42\x4f\x42\x4f\x3f\x55'\
b'\x3f\x55\x56\x09\x4a\x5a\x58\x4a\x56\x4a\x52\x42\x52\x42\x4e'\
b'\x4a\x4c\x4a\x51\x3f\x53\x3f\x58\x4a\x05\x4b\x59\x57\x56\x4d'\
b'\x56\x4d\x54\x57\x54\x57\x56\x05\x4d\x57\x55\x42\x53\x42\x4f'\
b'\x3e\x52\x3e\x55\x42\x23\x4a\x5a\x58\x52\x55\x52\x55\x50\x55'\
b'\x50\x53\x52\x51\x52\x4f\x52\x4c\x50\x4c\x4e\x4c\x4b\x51\x4a'\
b'\x55\x4a\x55\x47\x52\x47\x50\x47\x4e\x48\x4e\x46\x50\x44\x53'\
b'\x44\x58\x44\x58\x49\x58\x52\x20\x52\x55\x4c\x52\x4c\x51\x4c'\
b'\x4f\x4d\x4f\x4e\x4f\x4f\x51\x50\x52\x50\x53\x50\x55\x4e\x55'\
b'\x4d\x55\x4c\x21\x4a\x5a\x4f\x50\x4f\x50\x4f\x52\x4c\x52\x4c'\
b'\x3e\x4f\x3e\x4f\x47\x4f\x47\x50\x44\x53\x44\x56\x44\x58\x48'\
b'\x58\x4b\x58\x4e\x55\x52\x53\x52\x50\x52\x4f\x50\x20\x52\x4f'\
b'\x4b\x4f\x4c\x4f\x4e\x50\x50\x52\x50\x53\x50\x55\x4d\x55\x4b'\
b'\x55\x49\x54\x47\x52\x47\x50\x47\x4f\x49\x4f\x4b\x17\x4b\x59'\
b'\x57\x51\x56\x52\x53\x52\x50\x52\x4d\x4f\x4d\x4c\x4d\x48\x51'\
b'\x44\x54\x44\x56\x44\x57\x45\x57\x48\x56\x47\x54\x47\x52\x47'\
b'\x50\x49\x50\x4c\x50\x4e\x52\x50\x54\x50\x56\x50\x57\x4f\x57'\
b'\x51\x21\x4a\x5a\x58\x52\x55\x52\x55\x50\x55\x50\x54\x52\x51'\
b'\x52\x4e\x52\x4c\x4f\x4c\x4c\x4c\x48\x4f\x44\x52\x44\x54\x44'\
b'\x55\x47\x55\x47\x55\x3e\x58\x3e\x58\x52\x20\x52\x55\x4c\x55'\
b'\x4a\x55\x49\x54\x47\x52\x47\x51\x47\x4f\x49\x4f\x4c\x4f\x4e'\
b'\x50\x50\x52\x50\x54\x50\x55\x4e\x55\x4c\x1d\x4a\x5a\x58\x4c'\
b'\x4f\x4c\x4f\x4e\x51\x50\x53\x50\x55\x50\x57\x4f\x57\x51\x55'\
b'\x52\x52\x52\x4f\x52\x4c\x4f\x4c\x4b\x4c\x48\x50\x44\x52\x44'\
b'\x55\x44\x58\x48\x58\x4b\x58\x4c\x20\x52\x55\x4a\x55\x48\x54'\
b'\x47\x52\x47\x51\x47\x4f\x49\x4f\x4a\x55\x4a\x16\x4c\x58\x56'\
b'\x41\x56\x41\x55\x41\x53\x41\x53\x43\x53\x45\x56\x45\x56\x47'\
b'\x53\x47\x53\x52\x50\x52\x50\x47\x4e\x47\x4e\x45\x50\x45\x50'\
b'\x43\x50\x41\x53\x3e\x55\x3e\x56\x3e\x56\x3e\x56\x41\x29\x4a'\
b'\x5a\x58\x51\x58\x58\x51\x58\x4f\x58\x4d\x57\x4d\x55\x4f\x56'\
b'\x51\x56\x55\x56\x55\x51\x55\x50\x55\x50\x54\x52\x51\x52\x4f'\
b'\x52\x4c\x4f\x4c\x4c\x4c\x48\x4f\x44\x52\x44\x54\x44\x55\x47'\
b'\x55\x47\x55\x45\x58\x45\x58\x51\x20\x52\x55\x4c\x55\x4a\x55'\
b'\x49\x54\x47\x52\x47\x51\x47\x4f\x49\x4f\x4c\x4f\x4e\x50\x50'\
b'\x52\x50\x54\x50\x55\x4e\x55\x4c\x13\x4a\x5a\x58\x52\x55\x52'\
b'\x55\x4b\x55\x47\x52\x47\x51\x47\x4f\x49\x4f\x4b\x4f\x52\x4c'\
b'\x52\x4c\x3e\x4f\x3e\x4f\x47\x4f\x47\x51\x44\x53\x44\x58\x44'\
b'\x58\x4a\x58\x52\x13\x4e\x56\x52\x42\x51\x42\x50\x41\x50\x40'\
b'\x50\x40\x51\x3f\x52\x3f\x53\x3f\x54\x40\x54\x40\x54\x41\x53'\
b'\x42\x52\x42\x20\x52\x53\x52\x50\x52\x50\x45\x53\x45\x53\x52'\
b'\x1c\x4c\x58\x55\x51\x55\x55\x53\x58\x50\x58\x4f\x58\x4e\x58'\
b'\x4e\x55\x4f\x56\x50\x56\x52\x56\x52\x51\x52\x45\x55\x45\x55'\
b'\x51\x20\x52\x54\x42\x53\x42\x52\x41\x52\x40\x52\x40\x53\x3f'\
b'\x54\x3f\x55\x3f\x56\x40\x56\x40\x56\x41\x55\x42\x54\x42\x0e'\
b'\x4a\x5a\x58\x52\x54\x52\x4f\x4c\x4f\x4c\x4f\x52\x4c\x52\x4c'\
b'\x3e\x4f\x3e\x4f\x4b\x4f\x4b\x54\x45\x58\x45\x52\x4b\x58\x52'\
b'\x05\x4e\x56\x54\x52\x50\x52\x50\x3e\x54\x3e\x54\x52\x21\x46'\
b'\x5e\x5c\x52\x59\x52\x59\x4b\x59\x49\x58\x47\x56\x47\x55\x47'\
b'\x54\x49\x54\x4b\x54\x52\x50\x52\x50\x4b\x50\x47\x4e\x47\x4d'\
b'\x47\x4b\x49\x4b\x4b\x4b\x52\x48\x52\x48\x45\x4b\x45\x4b\x47'\
b'\x4b\x47\x4d\x44\x4f\x44\x51\x44\x53\x46\x53\x47\x55\x44\x58'\
b'\x44\x5c\x44\x5c\x4a\x5c\x52\x14\x4a\x5a\x58\x52\x55\x52\x55'\
b'\x4b\x55\x47\x52\x47\x51\x47\x4f\x49\x4f\x4a\x4f\x52\x4c\x52'\
b'\x4c\x45\x4f\x45\x4f\x47\x4f\x47\x51\x44\x53\x44\x56\x44\x58'\
b'\x47\x58\x4a\x58\x52\x1b\x49\x5b\x52\x52\x4f\x52\x4b\x4f\x4b'\
b'\x4c\x4b\x48\x4f\x44\x52\x44\x55\x44\x59\x48\x59\x4b\x59\x4f'\
b'\x55\x52\x52\x52\x20\x52\x52\x47\x50\x47\x4e\x49\x4e\x4b\x4e'\
b'\x4e\x50\x50\x52\x50\x54\x50\x56\x4e\x56\x4b\x56\x49\x54\x47'\
b'\x52\x47\x21\x4a\x5a\x4f\x50\x4f\x50\x4f\x58\x4c\x58\x4c\x45'\
b'\x4f\x45\x4f\x47\x4f\x47\x50\x44\x53\x44\x56\x44\x58\x48\x58'\
b'\x4b\x58\x4e\x55\x52\x53\x52\x50\x52\x4f\x50\x20\x52\x4f\x4b'\
b'\x4f\x4c\x4f\x4e\x50\x50\x52\x50\x53\x50\x55\x4d\x55\x4b\x55'\
b'\x49\x54\x47\x52\x47\x50\x47\x4f\x49\x4f\x4b\x21\x4a\x5a\x58'\
b'\x58\x55\x58\x55\x50\x55\x50\x54\x52\x51\x52\x4f\x52\x4c\x4f'\
b'\x4c\x4c\x4c\x48\x4f\x44\x52\x44\x54\x44\x55\x47\x55\x47\x55'\
b'\x45\x58\x45\x58\x58\x20\x52\x55\x4c\x55\x4a\x55\x49\x54\x47'\
b'\x52\x47\x51\x47\x4f\x49\x4f\x4c\x4f\x4e\x50\x50\x52\x50\x54'\
b'\x50\x55\x4e\x55\x4c\x12\x4c\x58\x56\x48\x55\x47\x54\x47\x53'\
b'\x47\x51\x4a\x51\x4c\x51\x52\x4e\x52\x4e\x45\x51\x45\x51\x48'\
b'\x51\x48\x52\x46\x53\x45\x55\x45\x55\x45\x56\x45\x56\x48\x30'\
b'\x4b\x59\x4d\x52\x4d\x4f\x4f\x50\x51\x50\x54\x50\x54\x4e\x54'\
b'\x4e\x53\x4d\x52\x4d\x51\x4d\x51\x4c\x50\x4c\x4f\x4b\x4e\x4a'\
b'\x4d\x49\x4d\x48\x4d\x47\x4e\x46\x50\x45\x52\x44\x53\x44\x55'\
b'\x44\x56\x45\x56\x48\x55\x47\x53\x47\x52\x47\x51\x47\x51\x47'\
b'\x50\x48\x50\x48\x50\x49\x51\x49\x51\x4a\x52\x4a\x53\x4a\x54'\
b'\x4b\x55\x4b\x56\x4c\x57\x4e\x57\x4e\x57\x4f\x56\x51\x54\x52'\
b'\x52\x52\x51\x52\x4f\x52\x4d\x52\x16\x4c\x58\x56\x52\x55\x52'\
b'\x54\x52\x50\x52\x50\x4f\x50\x47\x4e\x47\x4e\x45\x50\x45\x50'\
b'\x42\x53\x41\x53\x45\x56\x45\x56\x47\x53\x47\x53\x4e\x53\x4f'\
b'\x54\x50\x55\x50\x56\x50\x56\x4f\x56\x52\x13\x4a\x5a\x58\x52'\
b'\x55\x52\x55\x50\x55\x50\x54\x52\x51\x52\x4c\x52\x4c\x4d\x4c'\
b'\x45\x4f\x45\x4f\x4c\x4f\x50\x52\x50\x53\x50\x55\x4e\x55\x4c'\
b'\x55\x45\x58\x45\x58\x52\x0d\x49\x5b\x59\x45\x53\x52\x50\x52'\
b'\x4b\x45\x4f\x45\x52\x4e\x52\x4f\x52\x50\x52\x50\x52\x4f\x52'\
b'\x4e\x55\x45\x59\x45\x1d\x46\x5e\x5c\x45\x58\x52\x55\x52\x52'\
b'\x49\x52\x49\x52\x48\x52\x48\x52\x48\x52\x49\x4f\x52\x4c\x52'\
b'\x48\x45\x4b\x45\x4e\x4e\x4e\x4f\x4e\x4f\x4e\x4f\x4e\x4f\x4e'\
b'\x4e\x51\x45\x54\x45\x56\x4e\x56\x4f\x56\x4f\x56\x4f\x56\x4f'\
b'\x57\x4e\x59\x45\x5c\x45\x15\x4a\x5a\x58\x45\x54\x4b\x58\x52'\
b'\x55\x52\x53\x4e\x52\x4e\x52\x4d\x52\x4d\x52\x4d\x51\x4e\x4f'\
b'\x52\x4c\x52\x50\x4c\x4c\x45\x4f\x45\x52\x49\x52\x4a\x52\x4a'\
b'\x52\x4a\x55\x45\x58\x45\x16\x49\x5b\x59\x45\x53\x54\x51\x58'\
b'\x4d\x58\x4d\x58\x4c\x58\x4c\x56\x4d\x56\x4d\x56\x4f\x56\x50'\
b'\x54\x51\x52\x4b\x45\x4f\x45\x52\x4e\x52\x4f\x52\x4f\x52\x4f'\
b'\x52\x4f\x52\x4e\x56\x45\x59\x45\x0b\x4a\x5a\x58\x46\x51\x50'\
b'\x58\x50\x58\x52\x4c\x52\x4c\x51\x54\x47\x4d\x47\x4d\x45\x58'\
b'\x45\x58\x46\x1a\x4d\x57\x55\x56\x51\x56\x51\x52\x51\x4e\x51'\
b'\x4c\x4f\x4c\x4f\x4a\x51\x4a\x51\x47\x51\x43\x51\x40\x55\x3f'\
b'\x55\x41\x53\x42\x53\x44\x53\x48\x53\x4a\x51\x4b\x51\x4b\x53'\
b'\x4b\x53\x4e\x53\x52\x53\x53\x54\x54\x55\x54\x55\x56\x05\x4f'\
b'\x55\x53\x58\x51\x58\x51\x3e\x53\x3e\x53\x58\x1a\x4d\x57\x55'\
b'\x4c\x53\x4c\x53\x4e\x53\x52\x53\x56\x4f\x56\x4f\x54\x50\x54'\
b'\x51\x53\x51\x52\x51\x4e\x51\x4b\x53\x4b\x53\x4b\x51\x4a\x51'\
b'\x48\x51\x44\x51\x42\x4f\x41\x4f\x3f\x53\x40\x53\x43\x53\x47'\
b'\x53\x4a\x55\x4a\x55\x4c\x16\x49\x5b\x59\x48\x58\x4a\x57\x4d'\
b'\x55\x4d\x54\x4d\x52\x4b\x50\x4a\x4f\x4a\x4e\x4a\x4e\x4d\x4b'\
b'\x4d\x4b\x4b\x4d\x48\x4f\x48\x51\x48\x52\x49\x54\x4a\x55\x4a'\
b'\x55\x4a\x56\x49\x56\x48\x59\x48\x0b\x4a\x5a\x4c\x52\x4c\x40'\
b'\x58\x40\x58\x52\x4c\x52\x20\x52\x4e\x50\x56\x50\x56\x42\x4e'\
b'\x42\x4e\x50'

_index =\
b'\x00\x00\x03\x00\x2c\x00\x45\x00\x8e\x00\xf1\x00\x6e\x01\x09'\
b'\x02\x16\x02\x2f\x02\x48\x02\x6b\x02\x88\x02\x95\x02\xa2\x02'\
b'\xbf\x02\xcc\x02\xfb\x02\x1a\x03\x7b\x03\xc4\x03\xf5\x03\x2e'\
b'\x04\xa7\x04\xca\x04\x6f\x05\xf4\x05\x2d\x06\x56\x06\x6b\x06'\
b'\x84\x06\x99\x06\x0a\x07\x8f\x07\xb8\x07\x05\x08\x36\x08\x5f'\
b'\x08\x7c\x08\x95\x08\xce\x08\xeb\x08\xf8\x08\x17\x09\x3e\x09'\
b'\x4f\x09\x8c\x09\xb9\x09\xf2\x09\x21\x0a\x82\x0a\xdb\x0a\x4c'\
b'\x0b\x61\x0b\x82\x0b\x9f\x0b\xdc\x0b\x0d\x0c\x2e\x0c\x47\x0c'\
b'\x5c\x0c\x69\x0c\x7e\x0c\x93\x0c\xa0\x0c\xad\x0c\xf6\x0c\x3b'\
b'\x0d\x6c\x0d\xb1\x0d\xee\x0d\x1d\x0e\x72\x0e\x9b\x0e\xc4\x0e'\
b'\xff\x0e\x1e\x0f\x2b\x0f\x70\x0f\x9b\x0f\xd4\x0f\x19\x10\x5e'\
b'\x10\x85\x10\xe8\x10\x17\x11\x40\x11\x5d\x11\x9a\x11\xc7\x11'\
b'\xf6\x11\x0f\x12\x46\x12\x53\x12\x8a\x12\xb9\x12'

FONT = memoryview(_font)
INDEX = memoryview(_index)

