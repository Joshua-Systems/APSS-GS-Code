import enum


class message_type(enum.Enum):
    GPS = b"G"
    BASE_GPS = b"B"
    UNKNOWN = b"?"


class team_id(enum.Enum):
    probably_stable = 0
    the_retrievers = 1
    kessel_runners = 2
    team_plonk = 3
    ctrl_freaks = 4
    the_eigenvectors = 5
    djk = 6
    brain_exe = 7


class fix_type(enum.Enum):
    no_fix = "n"
    GPS = "g"
    DGPS = "d"
