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


def one_shot_write_test(Serial: serial.Serial) -> None:
    RAW_BYTES = "\xfa\x03\x8c\x99"
    RAW_BYTES = RAW_BYTES.upper
    print(f"{RAW_BYTES}")
    Serial.write(RAW_BYTES)


def gps_test_data(Serial: serial.Serial) -> None:
    GPS_MSG = "$G2;g;23:59:59 UTC;174.768807;-36.853628;61.5m;2\n"
    print(f"GPS: {GPS_MSG}")
    Serial.write(GPS_MSG.encode())


def gps_test_real_data(Serial: serial.Serial) -> None:
    GPS_MSG = "$G4;g;23:59:59 UTC;179.000000;1.999999;5200.0m;5\n"
    print(f"GPS: {GPS_MSG}")
    Serial.write(GPS_MSG.encode())
