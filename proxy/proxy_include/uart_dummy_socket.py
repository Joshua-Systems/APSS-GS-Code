import time

import serial


def init_pipe(
    port: str = "/dev/ttyUSB0",
    baud: int = 9600,
    data_bits: int = 8,
    stop_bits: int = 1,
    parity: str = serial.PARITY_NONE,
    timeout: float = 10,
) -> serial.Serial | None:
    try:
        Serial = serial.Serial(port, baud, data_bits, parity, stop_bits, timeout)
        time.sleep(1)
    except ValueError as e:
        print(f"Value Error, problem here: {e} ")
        return 0
    except serial.SerialException as e:
        print(f"Serial Exception!: {e}")
        return 0
    return Serial


def one_shot_write(Serial: serial.Serial) -> bytes:
    RAW_BYTES = b"\xfa\x03\x8c\x99\x0a"  # <-- bytes, not string
    print(RAW_BYTES)
    Serial.write(RAW_BYTES)
