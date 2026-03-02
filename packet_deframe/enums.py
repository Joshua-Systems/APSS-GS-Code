import enum


class message_type(enum):
    GPS = "G"
    BASE_GPS = "B"
    UNKNOWN = "?"


class team_id(enum):
    probably_stable = b"00000"
    the_retrievers = b"00001"
    kessel_runners = b"00010"
    team_plonk = b"00011"
    ctrl_freaks = b"00100"
    the_eigenvectors = b"00101"
    djk = b"00110"
    brain_exe = b"00111"


class fix_type(enum):
    no_fix = "n"
    GPS = "g"
    DGPS = "d"
