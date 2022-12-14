FIRST = 32
LAST = 127
WIDTH = 20
HEIGHT = 22

_font =\
b'\x01\x50\x54\x13\x4f\x55\x53\x43\x53\x4e\x51\x4e\x51\x43\x53'\
b'\x43\x20\x52\x52\x52\x52\x52\x51\x52\x51\x51\x51\x51\x52\x50'\
b'\x52\x50\x52\x50\x53\x51\x53\x51\x53\x52\x52\x52\x52\x52\x0b'\
b'\x4d\x57\x51\x43\x51\x47\x50\x47\x4f\x43\x51\x43\x20\x52\x55'\
b'\x43\x54\x47\x53\x47\x53\x43\x55\x43\x23\x4a\x5a\x58\x47\x58'\
b'\x48\x55\x48\x54\x4b\x57\x4b\x57\x4c\x54\x4c\x53\x51\x52\x51'\
b'\x53\x4c\x50\x4c\x4f\x51\x4e\x51\x4f\x4c\x4c\x4c\x4c\x4b\x4f'\
b'\x4b\x50\x48\x4d\x48\x4d\x47\x50\x47\x51\x43\x52\x43\x51\x47'\
b'\x54\x47\x55\x43\x56\x43\x55\x47\x58\x47\x20\x52\x54\x48\x51'\
b'\x48\x50\x4b\x53\x4b\x54\x48\x30\x4c\x58\x53\x52\x53\x54\x51'\
b'\x54\x51\x52\x4f\x52\x4e\x51\x4e\x4f\x4e\x50\x50\x50\x51\x50'\
b'\x51\x4b\x4f\x4a\x4e\x48\x4e\x47\x4e\x45\x50\x43\x51\x43\x51'\
b'\x41\x53\x41\x53\x42\x55\x43\x55\x43\x55\x45\x54\x44\x53\x44'\
b'\x53\x4a\x55\x4b\x56\x4d\x56\x4e\x56\x50\x54\x52\x53\x52\x20'\
b'\x52\x51\x49\x51\x44\x50\x44\x4f\x45\x4f\x46\x4f\x47\x50\x48'\
b'\x51\x49\x20\x52\x53\x4c\x53\x50\x55\x50\x55\x4e\x55\x4d\x53'\
b'\x4c\x3d\x48\x5c\x4d\x4a\x4c\x4a\x4a\x48\x4a\x46\x4a\x45\x4c'\
b'\x42\x4e\x42\x4f\x42\x51\x44\x51\x46\x51\x48\x4f\x4a\x4d\x4a'\
b'\x20\x52\x4d\x44\x4c\x44\x4b\x45\x4b\x46\x4b\x48\x4c\x49\x4d'\
b'\x49\x4e\x49\x50\x48\x50\x46\x50\x45\x4e\x44\x4d\x44\x20\x52'\
b'\x58\x43\x4e\x52\x4c\x52\x56\x43\x58\x43\x20\x52\x57\x52\x55'\
b'\x52\x53\x50\x53\x4e\x53\x4c\x55\x4a\x57\x4a\x58\x4a\x5a\x4c'\
b'\x5a\x4e\x5a\x50\x58\x52\x57\x52\x20\x52\x57\x4b\x56\x4b\x54'\
b'\x4d\x54\x4e\x54\x50\x56\x51\x57\x51\x58\x51\x59\x50\x59\x4e'\
b'\x59\x4d\x58\x4b\x57\x4b\x6d\x48\x5c\x58\x52\x58\x52\x57\x52'\
b'\x56\x51\x55\x50\x55\x50\x54\x50\x53\x51\x52\x52\x50\x52\x4f'\
b'\x52\x4e\x52\x4c\x52\x4b\x51\x4a\x4f\x4a\x4e\x4a\x4c\x4c\x4a'\
b'\x4e\x49\x4d\x49\x4d\x48\x4c\x47\x4c\x46\x4c\x46\x4c\x45\x4c'\
b'\x44\x4e\x43\x4f\x42\x50\x42\x51\x42\x52\x43\x53\x44\x54\x45'\
b'\x54\x46\x54\x47\x52\x49\x51\x49\x51\x49\x53\x4a\x54\x4b\x55'\
b'\x4d\x55\x4d\x56\x4c\x57\x49\x57\x47\x57\x47\x57\x46\x57\x46'\
b'\x58\x46\x58\x46\x58\x47\x58\x47\x58\x48\x58\x4a\x57\x4c\x56'\
b'\x4e\x56\x4f\x56\x4f\x57\x50\x58\x50\x58\x51\x59\x51\x59\x51'\
b'\x5a\x50\x5a\x50\x5a\x52\x5a\x52\x59\x52\x58\x52\x20\x52\x4f'\
b'\x51\x50\x51\x51\x50\x53\x50\x54\x4f\x54\x4f\x53\x4e\x52\x4c'\
b'\x51\x4b\x50\x4a\x4f\x4a\x4e\x4a\x4d\x4b\x4c\x4c\x4c\x4d\x4c'\
b'\x4e\x4c\x4e\x4c\x50\x4d\x50\x4f\x51\x4f\x51\x20\x52\x52\x46'\
b'\x52\x45\x52\x44\x51\x44\x50\x44\x50\x44\x4f\x44\x4e\x45\x4e'\
b'\x46\x4e\x46\x4e\x47\x4e\x48\x4f\x48\x4f\x48\x51\x48\x52\x47'\
b'\x52\x46\x05\x4f\x55\x53\x43\x53\x47\x51\x47\x51\x43\x53\x43'\
b'\x0b\x4e\x56\x54\x56\x53\x56\x50\x52\x50\x4c\x50\x46\x53\x43'\
b'\x54\x43\x51\x47\x51\x4c\x51\x51\x54\x56\x0b\x4e\x56\x51\x56'\
b'\x50\x56\x53\x51\x53\x4c\x53\x47\x50\x43\x51\x43\x54\x46\x54'\
b'\x4c\x54\x52\x51\x56\x10\x4c\x58\x56\x46\x53\x47\x55\x49\x54'\
b'\x4a\x52\x47\x50\x4a\x4f\x49\x51\x47\x4e\x46\x4f\x45\x52\x46'\
b'\x51\x43\x53\x43\x53\x46\x55\x45\x56\x46\x0d\x4b\x59\x57\x4c'\
b'\x53\x4c\x53\x51\x51\x51\x51\x4c\x4d\x4c\x4d\x4b\x51\x4b\x51'\
b'\x47\x53\x47\x53\x4b\x57\x4b\x57\x4c\x05\x4f\x55\x53\x50\x52'\
b'\x55\x51\x55\x52\x50\x53\x50\x05\x4d\x57\x55\x4d\x4f\x4d\x4f'\
b'\x4b\x55\x4b\x55\x4d\x0d\x4f\x55\x52\x52\x51\x52\x51\x52\x51'\
b'\x51\x51\x51\x51\x50\x52\x50\x52\x50\x53\x51\x53\x51\x53\x52'\
b'\x52\x52\x52\x52\x05\x4b\x59\x57\x43\x4f\x55\x4d\x55\x55\x43'\
b'\x57\x43\x16\x4b\x59\x52\x52\x50\x52\x4d\x4e\x4d\x4b\x4d\x46'\
b'\x50\x42\x52\x42\x57\x42\x57\x4a\x57\x4e\x54\x52\x52\x52\x20'\
b'\x52\x52\x44\x4f\x44\x4f\x4b\x4f\x51\x52\x51\x55\x51\x55\x4a'\
b'\x55\x44\x52\x44\x0b\x4c\x58\x56\x52\x4e\x52\x4e\x50\x51\x50'\
b'\x51\x44\x4e\x46\x4e\x44\x53\x42\x53\x50\x56\x50\x56\x52\x19'\
b'\x4b\x59\x57\x52\x4d\x52\x4d\x50\x52\x4c\x54\x4a\x55\x48\x55'\
b'\x47\x55\x45\x53\x44\x52\x44\x50\x44\x4e\x46\x4e\x44\x50\x42'\
b'\x52\x42\x54\x42\x57\x45\x57\x46\x57\x48\x55\x4b\x53\x4d\x4f'\
b'\x50\x4f\x50\x57\x50\x57\x52\x23\x4c\x58\x4e\x51\x4e\x50\x4f'\
b'\x51\x51\x51\x53\x51\x55\x4f\x55\x4e\x55\x4b\x50\x4b\x4f\x4b'\
b'\x4f\x49\x50\x49\x54\x49\x54\x46\x54\x44\x51\x44\x50\x44\x4e'\
b'\x45\x4e\x43\x50\x42\x52\x42\x54\x42\x56\x44\x56\x46\x56\x49'\
b'\x53\x4a\x53\x4a\x54\x4a\x56\x4c\x56\x4e\x56\x50\x53\x52\x51'\
b'\x52\x4f\x52\x4e\x51\x16\x4b\x59\x57\x4e\x56\x4e\x56\x52\x54'\
b'\x52\x54\x4e\x4d\x4e\x4d\x4d\x53\x43\x56\x43\x56\x4c\x57\x4c'\
b'\x57\x4e\x20\x52\x54\x4c\x54\x46\x54\x45\x54\x44\x54\x44\x54'\
b'\x45\x53\x45\x4e\x4c\x54\x4c\x1b\x4c\x58\x4e\x52\x4e\x50\x4f'\
b'\x51\x51\x51\x53\x51\x55\x4f\x55\x4d\x55\x4c\x52\x4a\x51\x4a'\
b'\x50\x4a\x4e\x4a\x4e\x43\x56\x43\x56\x44\x50\x44\x50\x49\x51'\
b'\x49\x51\x49\x54\x49\x56\x4b\x56\x4d\x56\x50\x53\x52\x51\x52'\
b'\x4f\x52\x4e\x52\x26\x4b\x59\x56\x43\x56\x44\x55\x44\x53\x44'\
b'\x51\x44\x4f\x47\x4f\x4b\x4f\x4b\x50\x48\x52\x48\x55\x48\x57'\
b'\x4b\x57\x4d\x57\x4f\x54\x52\x52\x52\x50\x52\x4d\x4f\x4d\x4b'\
b'\x4d\x47\x51\x42\x53\x42\x55\x42\x56\x43\x20\x52\x52\x4a\x51'\
b'\x4a\x4f\x4c\x4f\x4d\x4f\x4f\x51\x51\x52\x51\x53\x51\x55\x4f'\
b'\x55\x4d\x55\x4c\x54\x4a\x52\x4a\x08\x4b\x59\x57\x43\x51\x52'\
b'\x4f\x52\x55\x44\x4d\x44\x4d\x43\x57\x43\x57\x43\x2f\x4b\x59'\
b'\x50\x4a\x50\x4a\x4e\x49\x4e\x46\x4e\x44\x50\x42\x52\x42\x54'\
b'\x42\x56\x44\x56\x46\x56\x48\x53\x4a\x53\x4a\x57\x4b\x57\x4e'\
b'\x57\x50\x54\x52\x52\x52\x50\x52\x4d\x50\x4d\x4e\x4d\x4b\x50'\
b'\x4a\x20\x52\x55\x46\x55\x45\x53\x44\x52\x44\x51\x44\x4f\x45'\
b'\x4f\x46\x4f\x48\x52\x49\x55\x48\x55\x46\x20\x52\x52\x4b\x4f'\
b'\x4c\x4f\x4e\x4f\x4f\x51\x51\x52\x51\x53\x51\x55\x4f\x55\x4e'\
b'\x55\x4c\x52\x4b\x27\x4b\x59\x4e\x52\x4e\x50\x4f\x51\x51\x51'\
b'\x53\x51\x55\x4d\x55\x4a\x55\x4a\x55\x4a\x54\x4c\x52\x4c\x50'\
b'\x4c\x4d\x4a\x4d\x47\x4d\x45\x50\x42\x52\x42\x54\x42\x57\x46'\
b'\x57\x49\x57\x4e\x54\x52\x51\x52\x4f\x52\x4e\x52\x20\x52\x52'\
b'\x44\x51\x44\x4f\x46\x4f\x47\x4f\x49\x51\x4b\x52\x4b\x53\x4b'\
b'\x55\x49\x55\x48\x55\x46\x53\x44\x52\x44\x1b\x4f\x55\x52\x49'\
b'\x51\x49\x51\x48\x51\x48\x51\x47\x51\x47\x52\x47\x52\x47\x53'\
b'\x47\x53\x48\x53\x48\x52\x49\x52\x49\x20\x52\x52\x52\x51\x52'\
b'\x51\x52\x51\x51\x51\x51\x51\x50\x52\x50\x52\x50\x53\x51\x53'\
b'\x51\x53\x52\x52\x52\x52\x52\x13\x4e\x56\x52\x49\x52\x49\x51'\
b'\x48\x51\x48\x51\x47\x52\x47\x52\x47\x53\x47\x54\x47\x54\x48'\
b'\x54\x48\x53\x49\x52\x49\x20\x52\x53\x50\x52\x55\x50\x55\x52'\
b'\x50\x53\x50\x09\x4b\x59\x57\x51\x4d\x4c\x4d\x4b\x57\x46\x57'\
b'\x48\x50\x4c\x50\x4c\x57\x4f\x57\x51\x0b\x4b\x59\x57\x4a\x4d'\
b'\x4a\x4d\x49\x57\x49\x57\x4a\x20\x52\x57\x4f\x4d\x4f\x4d\x4d'\
b'\x57\x4d\x57\x4f\x09\x4b\x59\x57\x4c\x4d\x51\x4d\x4f\x54\x4c'\
b'\x54\x4c\x4d\x48\x4d\x46\x57\x4b\x57\x4c\x37\x4c\x58\x51\x4e'\
b'\x50\x4d\x50\x4d\x50\x4c\x50\x4b\x51\x4a\x52\x49\x53\x48\x53'\
b'\x48\x54\x47\x54\x46\x54\x45\x54\x45\x53\x44\x52\x44\x51\x44'\
b'\x50\x44\x4e\x45\x4e\x43\x50\x42\x52\x42\x53\x42\x54\x43\x55'\
b'\x44\x56\x45\x56\x46\x56\x46\x55\x48\x54\x49\x53\x4a\x52\x4b'\
b'\x52\x4c\x52\x4c\x52\x4d\x52\x4d\x52\x4e\x51\x4e\x20\x52\x51'\
b'\x52\x51\x52\x51\x52\x50\x52\x50\x51\x50\x51\x51\x50\x51\x50'\
b'\x51\x50\x52\x50\x52\x50\x53\x51\x53\x51\x53\x52\x52\x52\x52'\
b'\x52\x51\x52\x41\x47\x5d\x54\x4d\x54\x4d\x53\x50\x51\x50\x4f'\
b'\x50\x4e\x4e\x4e\x4c\x4e\x4a\x50\x46\x52\x46\x53\x46\x54\x47'\
b'\x54\x48\x54\x48\x54\x47\x54\x47\x56\x47\x55\x4c\x55\x4d\x55'\
b'\x4f\x57\x4f\x58\x4f\x59\x4c\x59\x4a\x59\x47\x55\x44\x52\x44'\
b'\x4f\x44\x4b\x48\x4b\x4b\x4b\x4f\x4f\x53\x52\x53\x55\x53\x57'\
b'\x52\x57\x53\x55\x54\x52\x54\x4e\x54\x49\x4f\x49\x4b\x49\x48'\
b'\x4e\x42\x52\x42\x56\x42\x5b\x47\x5b\x4a\x5b\x4d\x58\x50\x56'\
b'\x50\x54\x50\x54\x4d\x20\x52\x52\x48\x51\x48\x4f\x4a\x4f\x4c'\
b'\x4f\x4d\x50\x4f\x51\x4f\x52\x4f\x54\x4c\x54\x4a\x54\x48\x52'\
b'\x48\x13\x49\x5b\x59\x52\x57\x52\x55\x4e\x4f\x4e\x4d\x52\x4b'\
b'\x52\x51\x43\x53\x43\x59\x52\x20\x52\x55\x4c\x52\x45\x52\x45'\
b'\x52\x44\x52\x44\x52\x45\x52\x45\x4f\x4c\x55\x4c\x25\x4b\x59'\
b'\x4d\x52\x4d\x43\x52\x43\x54\x43\x56\x45\x56\x46\x56\x47\x55'\
b'\x49\x53\x4a\x53\x4a\x55\x4a\x57\x4c\x57\x4e\x57\x50\x54\x52'\
b'\x52\x52\x4d\x52\x20\x52\x4f\x44\x4f\x49\x51\x49\x52\x49\x54'\
b'\x48\x54\x46\x54\x44\x51\x44\x4f\x44\x20\x52\x4f\x4b\x4f\x50'\
b'\x52\x50\x53\x50\x55\x4f\x55\x4e\x55\x4b\x51\x4b\x4f\x4b\x17'\
b'\x4a\x5a\x58\x51\x56\x52\x53\x52\x50\x52\x4c\x4e\x4c\x4b\x4c'\
b'\x47\x51\x42\x54\x42\x56\x42\x58\x43\x58\x45\x56\x44\x54\x44'\
b'\x51\x44\x4e\x47\x4e\x4a\x4e\x4d\x51\x51\x54\x51\x56\x51\x58'\
b'\x50\x58\x51\x13\x4a\x5a\x4c\x52\x4c\x43\x50\x43\x58\x43\x58'\
b'\x4a\x58\x4e\x54\x52\x50\x52\x4c\x52\x20\x52\x4e\x44\x4e\x50'\
b'\x50\x50\x53\x50\x56\x4d\x56\x4a\x56\x44\x50\x44\x4e\x44\x0d'\
b'\x4c\x58\x56\x52\x4e\x52\x4e\x43\x56\x43\x56\x44\x50\x44\x50'\
b'\x49\x55\x49\x55\x4b\x50\x4b\x50\x50\x56\x50\x56\x52\x0b\x4c'\
b'\x58\x56\x44\x50\x44\x50\x4a\x55\x4a\x55\x4b\x50\x4b\x50\x52'\
b'\x4e\x52\x4e\x43\x56\x43\x56\x44\x1b\x4a\x5a\x58\x51\x56\x52'\
b'\x53\x52\x50\x52\x4c\x4e\x4c\x4a\x4c\x47\x50\x42\x54\x42\x56'\
b'\x42\x58\x43\x58\x45\x56\x44\x54\x44\x51\x44\x4e\x48\x4e\x4a'\
b'\x4e\x4d\x51\x51\x53\x51\x55\x51\x56\x50\x56\x4c\x53\x4c\x53'\
b'\x4a\x58\x4a\x58\x51\x0d\x4a\x5a\x58\x52\x56\x52\x56\x4b\x4e'\
b'\x4b\x4e\x52\x4c\x52\x4c\x43\x4e\x43\x4e\x49\x56\x49\x56\x43'\
b'\x58\x43\x58\x52\x0d\x4e\x56\x54\x43\x54\x44\x53\x44\x53\x50'\
b'\x54\x50\x54\x52\x50\x52\x50\x50\x51\x50\x51\x44\x50\x44\x50'\
b'\x43\x54\x43\x0e\x4d\x57\x55\x4c\x55\x4f\x53\x52\x51\x52\x50'\
b'\x52\x4f\x52\x4f\x50\x50\x51\x51\x51\x53\x51\x53\x4c\x53\x43'\
b'\x55\x43\x55\x4c\x12\x4b\x59\x57\x52\x55\x52\x4f\x4b\x4f\x4b'\
b'\x4e\x4a\x4e\x4a\x4e\x52\x4d\x52\x4d\x43\x4e\x43\x4e\x4a\x4e'\
b'\x4a\x4f\x4a\x4f\x49\x55\x43\x57\x43\x50\x4a\x57\x52\x07\x4c'\
b'\x58\x56\x52\x4e\x52\x4e\x43\x50\x43\x50\x50\x56\x50\x56\x52'\
b'\x1d\x48\x5c\x5a\x52\x58\x52\x58\x48\x58\x46\x58\x45\x58\x45'\
b'\x58\x46\x58\x46\x52\x52\x52\x52\x4c\x46\x4c\x46\x4c\x45\x4c'\
b'\x45\x4c\x46\x4c\x48\x4c\x52\x4a\x52\x4a\x43\x4d\x43\x51\x4d'\
b'\x52\x4f\x52\x4f\x52\x4f\x52\x4e\x53\x4d\x58\x43\x5a\x43\x5a'\
b'\x52\x15\x4a\x5a\x58\x52\x56\x52\x4e\x46\x4e\x45\x4e\x45\x4d'\
b'\x45\x4e\x45\x4e\x47\x4e\x52\x4c\x52\x4c\x43\x4e\x43\x56\x4f'\
b'\x56\x4f\x56\x50\x57\x50\x56\x4f\x56\x4d\x56\x43\x58\x43\x58'\
b'\x52\x1b\x49\x5b\x52\x52\x4f\x52\x4b\x4e\x4b\x4a\x4b\x47\x4f'\
b'\x42\x52\x42\x55\x42\x59\x47\x59\x4a\x59\x4e\x55\x52\x52\x52'\
b'\x20\x52\x52\x44\x50\x44\x4d\x47\x4d\x4a\x4d\x4d\x50\x51\x52'\
b'\x51\x54\x51\x57\x4d\x57\x4a\x57\x47\x55\x44\x52\x44\x16\x4b'\
b'\x59\x4f\x4c\x4f\x52\x4d\x52\x4d\x43\x52\x43\x54\x43\x57\x45'\
b'\x57\x47\x57\x49\x54\x4c\x51\x4c\x4f\x4c\x20\x52\x4f\x44\x4f'\
b'\x4b\x51\x4b\x53\x4b\x55\x49\x55\x47\x55\x44\x51\x44\x4f\x44'\
b'\x3c\x49\x5b\x52\x52\x51\x52\x50\x52\x4e\x51\x4d\x51\x4c\x50'\
b'\x4b\x4e\x4b\x4a\x4b\x47\x4d\x45\x4f\x42\x52\x42\x55\x42\x57'\
b'\x44\x59\x47\x59\x4a\x59\x4c\x58\x4e\x57\x50\x55\x52\x54\x52'\
b'\x54\x53\x55\x54\x56\x54\x57\x54\x58\x54\x58\x54\x59\x54\x59'\
b'\x54\x59\x54\x59\x54\x59\x56\x59\x56\x59\x56\x58\x56\x58\x56'\
b'\x58\x56\x57\x56\x55\x56\x54\x54\x52\x53\x52\x52\x20\x52\x52'\
b'\x44\x4f\x44\x4e\x46\x4c\x47\x4c\x4a\x4c\x4d\x4e\x4f\x4f\x51'\
b'\x52\x51\x54\x51\x56\x4f\x57\x4d\x57\x4a\x57\x47\x56\x46\x54'\
b'\x44\x52\x44\x2b\x4a\x5a\x58\x52\x55\x52\x53\x4e\x52\x4d\x52'\
b'\x4c\x51\x4c\x50\x4b\x50\x4b\x4e\x4b\x4e\x52\x4c\x52\x4c\x43'\
b'\x51\x43\x52\x43\x54\x43\x55\x44\x56\x46\x56\x47\x56\x47\x55'\
b'\x49\x54\x4a\x53\x4b\x52\x4b\x52\x4b\x53\x4b\x53\x4b\x54\x4c'\
b'\x54\x4d\x55\x4d\x58\x52\x20\x52\x4e\x44\x4e\x4a\x51\x4a\x51'\
b'\x4a\x53\x49\x53\x49\x54\x48\x54\x47\x54\x46\x52\x44\x51\x44'\
b'\x4e\x44\x37\x4b\x59\x4d\x51\x4d\x4f\x4e\x50\x4f\x50\x50\x50'\
b'\x51\x51\x51\x51\x53\x51\x55\x4f\x55\x4e\x55\x4e\x54\x4d\x53'\
b'\x4c\x52\x4b\x51\x4b\x50\x4a\x4f\x4a\x4e\x49\x4d\x47\x4d\x46'\
b'\x4d\x45\x4e\x44\x50\x43\x52\x42\x53\x42\x55\x42\x56\x43\x56'\
b'\x45\x55\x44\x53\x44\x52\x44\x51\x44\x50\x45\x4f\x46\x4f\x46'\
b'\x4f\x47\x50\x48\x51\x48\x52\x49\x53\x49\x53\x4a\x55\x4b\x56'\
b'\x4c\x57\x4d\x57\x4e\x57\x4f\x56\x51\x54\x52\x52\x52\x51\x52'\
b'\x51\x52\x50\x52\x4f\x52\x4e\x52\x4d\x51\x09\x4b\x59\x57\x44'\
b'\x53\x44\x53\x52\x51\x52\x51\x44\x4d\x44\x4d\x43\x57\x43\x57'\
b'\x44\x0f\x4a\x5a\x58\x4c\x58\x52\x52\x52\x4c\x52\x4c\x4c\x4c'\
b'\x43\x4e\x43\x4e\x4c\x4e\x51\x52\x51\x56\x51\x56\x4c\x56\x43'\
b'\x58\x43\x58\x4c\x0d\x49\x5b\x59\x43\x53\x52\x51\x52\x4b\x43'\
b'\x4d\x43\x52\x4f\x52\x4f\x52\x50\x52\x50\x52\x50\x52\x4f\x57'\
b'\x43\x59\x43\x1d\x46\x5e\x5c\x43\x58\x52\x56\x52\x52\x47\x52'\
b'\x46\x52\x45\x52\x45\x52\x46\x52\x47\x4f\x52\x4c\x52\x48\x43'\
b'\x4a\x43\x4d\x4e\x4d\x4f\x4e\x50\x4e\x50\x4e\x4f\x4e\x4e\x51'\
b'\x43\x53\x43\x56\x4e\x56\x4f\x57\x50\x57\x50\x57\x4f\x57\x4e'\
b'\x5a\x43\x5c\x43\x17\x4a\x5a\x58\x52\x56\x52\x52\x4c\x52\x4c'\
b'\x52\x4b\x52\x4b\x52\x4c\x52\x4c\x4e\x52\x4c\x52\x51\x4a\x4c'\
b'\x43\x4e\x43\x52\x48\x52\x49\x52\x49\x52\x49\x53\x48\x53\x48'\
b'\x56\x43\x58\x43\x53\x4a\x58\x52\x0f\x4a\x5a\x58\x43\x53\x4c'\
b'\x53\x52\x51\x52\x51\x4c\x4c\x43\x4e\x43\x52\x4a\x52\x4a\x52'\
b'\x4a\x52\x4a\x52\x4a\x52\x4a\x56\x43\x58\x43\x0b\x4a\x5a\x58'\
b'\x43\x4f\x50\x58\x50\x58\x52\x4c\x52\x4c\x51\x55\x44\x4d\x44'\
b'\x4d\x43\x58\x43\x58\x43\x09\x4e\x56\x54\x56\x50\x56\x50\x43'\
b'\x54\x43\x54\x44\x52\x44\x52\x54\x54\x54\x54\x56\x05\x4c\x58'\
b'\x56\x55\x55\x55\x4e\x43\x4f\x43\x56\x55\x09\x4e\x56\x54\x56'\
b'\x50\x56\x50\x54\x52\x54\x52\x44\x50\x44\x50\x43\x54\x43\x54'\
b'\x56\x09\x4b\x59\x57\x4b\x55\x4b\x52\x45\x52\x45\x4f\x4b\x4d'\
b'\x4b\x51\x42\x52\x42\x57\x4b\x05\x4b\x59\x57\x55\x4d\x55\x4d'\
b'\x54\x57\x54\x57\x55\x05\x4e\x56\x54\x45\x53\x45\x50\x41\x52'\
b'\x41\x54\x45\x23\x4c\x58\x56\x52\x55\x52\x55\x50\x55\x50\x53'\
b'\x52\x51\x52\x50\x52\x4e\x51\x4e\x4f\x4e\x4c\x51\x4b\x55\x4b'\
b'\x55\x48\x52\x48\x50\x48\x4f\x4a\x4f\x48\x50\x47\x52\x47\x56'\
b'\x47\x56\x4b\x56\x52\x20\x52\x55\x4c\x52\x4d\x51\x4d\x4f\x4e'\
b'\x4f\x4f\x4f\x50\x51\x51\x52\x51\x53\x51\x55\x4f\x55\x4e\x55'\
b'\x4c\x21\x4b\x59\x4f\x50\x4f\x50\x4f\x52\x4d\x52\x4d\x42\x4f'\
b'\x42\x4f\x49\x4f\x49\x50\x47\x53\x47\x55\x47\x57\x4a\x57\x4c'\
b'\x57\x4f\x54\x52\x52\x52\x50\x52\x4f\x50\x20\x52\x4f\x4c\x4f'\
b'\x4d\x4f\x4f\x50\x51\x52\x51\x53\x51\x55\x4e\x55\x4c\x55\x4a'\
b'\x54\x48\x52\x48\x51\x48\x4f\x4a\x4f\x4c\x17\x4c\x58\x56\x51'\
b'\x55\x52\x53\x52\x51\x52\x4e\x4f\x4e\x4d\x4e\x4a\x51\x47\x54'\
b'\x47\x55\x47\x56\x47\x56\x49\x55\x48\x54\x48\x52\x48\x50\x4b'\
b'\x50\x4d\x50\x4f\x52\x51\x53\x51\x55\x51\x56\x50\x56\x51\x21'\
b'\x4b\x59\x57\x52\x55\x52\x55\x50\x55\x50\x54\x52\x51\x52\x4f'\
b'\x52\x4d\x4f\x4d\x4d\x4d\x4a\x50\x47\x52\x47\x54\x47\x55\x49'\
b'\x55\x49\x55\x42\x57\x42\x57\x52\x20\x52\x55\x4d\x55\x4b\x55'\
b'\x4a\x54\x48\x52\x48\x51\x48\x4f\x4b\x4f\x4d\x4f\x4f\x51\x51'\
b'\x52\x51\x53\x51\x55\x4f\x55\x4d\x1d\x4b\x59\x57\x4d\x4f\x4d'\
b'\x4f\x4f\x51\x51\x53\x51\x54\x51\x56\x50\x56\x51\x55\x52\x52'\
b'\x52\x50\x52\x4d\x4f\x4d\x4d\x4d\x4a\x50\x47\x52\x47\x54\x47'\
b'\x57\x4a\x57\x4c\x57\x4d\x20\x52\x55\x4b\x55\x4a\x54\x48\x52'\
b'\x48\x51\x48\x4f\x4a\x4f\x4b\x55\x4b\x16\x4d\x57\x55\x43\x55'\
b'\x43\x54\x43\x52\x43\x52\x45\x52\x47\x55\x47\x55\x48\x52\x48'\
b'\x52\x52\x51\x52\x51\x48\x4f\x48\x4f\x47\x51\x47\x51\x45\x51'\
b'\x43\x53\x41\x54\x41\x55\x41\x55\x42\x55\x43\x29\x4b\x59\x57'\
b'\x51\x57\x57\x51\x57\x4f\x57\x4e\x56\x4e\x55\x50\x56\x51\x56'\
b'\x55\x56\x55\x51\x55\x50\x55\x50\x54\x52\x51\x52\x4f\x52\x4d'\
b'\x4f\x4d\x4d\x4d\x4a\x50\x47\x52\x47\x54\x47\x55\x49\x55\x49'\
b'\x55\x47\x57\x47\x57\x51\x20\x52\x55\x4d\x55\x4b\x55\x4a\x54'\
b'\x48\x52\x48\x51\x48\x4f\x4b\x4f\x4d\x4f\x4f\x51\x51\x52\x51'\
b'\x53\x51\x55\x4f\x55\x4d\x13\x4b\x59\x57\x52\x55\x52\x55\x4c'\
b'\x55\x48\x52\x48\x51\x48\x4f\x4a\x4f\x4c\x4f\x52\x4d\x52\x4d'\
b'\x42\x4f\x42\x4f\x49\x4f\x49\x51\x47\x53\x47\x57\x47\x57\x4b'\
b'\x57\x52\x13\x4f\x55\x52\x44\x52\x44\x51\x44\x51\x43\x51\x43'\
b'\x52\x42\x52\x42\x52\x42\x53\x43\x53\x43\x53\x44\x52\x44\x52'\
b'\x44\x20\x52\x53\x52\x51\x52\x51\x47\x53\x47\x53\x52\x1c\x4d'\
b'\x57\x55\x52\x55\x54\x53\x57\x50\x57\x50\x57\x4f\x57\x4f\x55'\
b'\x50\x56\x51\x56\x53\x56\x53\x52\x53\x47\x55\x47\x55\x52\x20'\
b'\x52\x54\x44\x53\x44\x53\x44\x53\x43\x53\x43\x53\x42\x54\x42'\
b'\x54\x42\x55\x43\x55\x43\x55\x44\x54\x44\x54\x44\x0e\x4b\x59'\
b'\x57\x52\x54\x52\x4f\x4d\x4f\x4d\x4f\x52\x4d\x52\x4d\x42\x4f'\
b'\x42\x4f\x4c\x4f\x4c\x54\x47\x56\x47\x51\x4c\x57\x52\x05\x4f'\
b'\x55\x53\x52\x51\x52\x51\x42\x53\x42\x53\x52\x21\x48\x5c\x5a'\
b'\x52\x58\x52\x58\x4c\x58\x4a\x57\x48\x56\x48\x54\x48\x53\x4a'\
b'\x53\x4c\x53\x52\x51\x52\x51\x4b\x51\x48\x4f\x48\x4d\x48\x4c'\
b'\x4a\x4c\x4c\x4c\x52\x4a\x52\x4a\x47\x4c\x47\x4c\x49\x4c\x49'\
b'\x4d\x47\x4f\x47\x51\x47\x52\x48\x53\x49\x54\x47\x56\x47\x5a'\
b'\x47\x5a\x4b\x5a\x52\x14\x4b\x59\x57\x52\x55\x52\x55\x4c\x55'\
b'\x48\x52\x48\x51\x48\x4f\x4a\x4f\x4c\x4f\x52\x4d\x52\x4d\x47'\
b'\x4f\x47\x4f\x49\x4f\x49\x50\x47\x53\x47\x55\x47\x57\x49\x57'\
b'\x4b\x57\x52\x1b\x4b\x59\x52\x52\x4f\x52\x4d\x4f\x4d\x4d\x4d'\
b'\x4a\x50\x47\x52\x47\x55\x47\x57\x4a\x57\x4c\x57\x4f\x54\x52'\
b'\x52\x52\x20\x52\x52\x48\x50\x48\x4e\x4b\x4e\x4d\x4e\x4f\x50'\
b'\x51\x52\x51\x54\x51\x56\x4f\x56\x4d\x56\x4a\x54\x48\x52\x48'\
b'\x21\x4b\x59\x4f\x50\x4f\x50\x4f\x57\x4d\x57\x4d\x47\x4f\x47'\
b'\x4f\x49\x4f\x49\x50\x47\x53\x47\x55\x47\x57\x4a\x57\x4c\x57'\
b'\x4f\x54\x52\x52\x52\x50\x52\x4f\x50\x20\x52\x4f\x4c\x4f\x4d'\
b'\x4f\x4f\x50\x51\x52\x51\x53\x51\x55\x4e\x55\x4c\x55\x4a\x54'\
b'\x48\x52\x48\x51\x48\x4f\x4a\x4f\x4c\x21\x4b\x59\x57\x57\x55'\
b'\x57\x55\x50\x55\x50\x54\x52\x52\x52\x4f\x52\x4d\x4f\x4d\x4d'\
b'\x4d\x4a\x50\x47\x52\x47\x54\x47\x55\x49\x55\x49\x55\x47\x57'\
b'\x47\x57\x57\x20\x52\x55\x4d\x55\x4b\x55\x4a\x54\x48\x52\x48'\
b'\x51\x48\x4f\x4b\x4f\x4d\x4f\x4f\x51\x51\x52\x51\x53\x51\x55'\
b'\x4f\x55\x4d\x12\x4d\x57\x55\x49\x54\x48\x54\x48\x52\x48\x51'\
b'\x4b\x51\x4c\x51\x52\x4f\x52\x4f\x47\x51\x47\x51\x49\x51\x49'\
b'\x51\x48\x53\x47\x54\x47\x55\x47\x55\x47\x55\x49\x30\x4c\x58'\
b'\x4e\x52\x4e\x50\x50\x51\x52\x51\x54\x51\x54\x4f\x54\x4f\x53'\
b'\x4e\x53\x4e\x52\x4d\x51\x4d\x51\x4d\x4f\x4c\x4f\x4b\x4e\x4b'\
b'\x4e\x4a\x4e\x49\x4f\x48\x50\x47\x52\x47\x53\x47\x54\x47\x55'\
b'\x47\x55\x49\x54\x48\x52\x48\x52\x48\x51\x48\x50\x49\x50\x49'\
b'\x50\x4a\x50\x4a\x50\x4b\x51\x4b\x52\x4c\x53\x4c\x53\x4c\x54'\
b'\x4d\x55\x4d\x56\x4e\x56\x4f\x56\x50\x55\x51\x54\x52\x52\x52'\
b'\x51\x52\x50\x52\x4e\x52\x16\x4d\x57\x55\x52\x55\x52\x54\x52'\
b'\x51\x52\x51\x4f\x51\x48\x4f\x48\x4f\x47\x51\x47\x51\x44\x52'\
b'\x44\x52\x47\x55\x47\x55\x48\x52\x48\x52\x4f\x52\x50\x53\x51'\
b'\x54\x51\x55\x51\x55\x50\x55\x52\x13\x4b\x59\x57\x52\x55\x52'\
b'\x55\x50\x55\x50\x54\x52\x51\x52\x4d\x52\x4d\x4e\x4d\x47\x4f'\
b'\x47\x4f\x4d\x4f\x51\x52\x51\x53\x51\x55\x4f\x55\x4d\x55\x47'\
b'\x57\x47\x57\x52\x0d\x4b\x59\x57\x47\x53\x52\x51\x52\x4d\x47'\
b'\x4f\x47\x52\x4f\x52\x50\x52\x51\x52\x51\x52\x50\x52\x4f\x55'\
b'\x47\x57\x47\x1d\x48\x5c\x5a\x47\x56\x52\x55\x52\x52\x4a\x52'\
b'\x4a\x52\x49\x52\x49\x52\x49\x52\x4a\x4f\x52\x4e\x52\x4a\x47'\
b'\x4c\x47\x4e\x4f\x4f\x50\x4f\x50\x4f\x50\x4f\x50\x4f\x4f\x51'\
b'\x47\x53\x47\x55\x4f\x55\x50\x55\x50\x56\x50\x56\x50\x56\x4f'\
b'\x58\x47\x5a\x47\x15\x4b\x59\x57\x47\x53\x4d\x57\x52\x55\x52'\
b'\x52\x4e\x52\x4e\x52\x4e\x52\x4e\x52\x4e\x51\x4e\x4f\x52\x4d'\
b'\x52\x51\x4d\x4d\x47\x4f\x47\x52\x4b\x52\x4b\x52\x4c\x52\x4c'\
b'\x55\x47\x57\x47\x16\x4b\x59\x57\x47\x52\x54\x51\x57\x4e\x57'\
b'\x4e\x57\x4d\x57\x4d\x55\x4e\x56\x4e\x56\x50\x56\x50\x54\x51'\
b'\x52\x4d\x47\x4f\x47\x52\x4f\x52\x50\x52\x50\x52\x50\x52\x50'\
b'\x52\x4f\x55\x47\x57\x47\x0b\x4b\x59\x57\x47\x50\x50\x56\x50'\
b'\x56\x52\x4d\x52\x4d\x51\x54\x48\x4e\x48\x4e\x47\x57\x47\x57'\
b'\x47\x1a\x4e\x56\x54\x56\x51\x55\x51\x52\x51\x4f\x51\x4d\x50'\
b'\x4d\x50\x4b\x51\x4b\x51\x49\x51\x46\x51\x43\x54\x43\x54\x44'\
b'\x53\x44\x53\x46\x53\x49\x53\x4b\x51\x4c\x51\x4c\x53\x4d\x53'\
b'\x4f\x53\x52\x53\x53\x54\x54\x54\x54\x54\x56\x05\x4f\x55\x53'\
b'\x57\x51\x57\x51\x41\x53\x41\x53\x57\x1a\x4e\x56\x54\x4d\x53'\
b'\x4d\x53\x4f\x53\x52\x53\x55\x50\x56\x50\x54\x50\x54\x51\x53'\
b'\x51\x52\x51\x4f\x51\x4d\x53\x4c\x53\x4c\x51\x4b\x51\x49\x51'\
b'\x46\x51\x44\x50\x44\x50\x43\x53\x43\x53\x46\x53\x49\x53\x4b'\
b'\x54\x4b\x54\x4d\x16\x4b\x59\x57\x4a\x57\x4c\x56\x4d\x54\x4d'\
b'\x53\x4d\x51\x4c\x50\x4b\x50\x4b\x4e\x4b\x4e\x4d\x4d\x4d\x4d'\
b'\x4c\x4e\x4a\x50\x4a\x51\x4a\x52\x4b\x54\x4c\x54\x4c\x55\x4c'\
b'\x56\x4b\x56\x4a\x57\x4a\x0b\x4b\x59\x4d\x52\x4d\x43\x57\x43'\
b'\x57\x52\x4d\x52\x20\x52\x4e\x50\x56\x50\x56\x45\x4e\x45\x4e'\
b'\x50'

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

