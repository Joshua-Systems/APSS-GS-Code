import sock_pipe.uart_socket as sery


def main():
    ##Use Either JTAG COM PORT or VCP From com0com
    Serial = sery.init_pipe("COM1")

    if Serial is None:
        print("Serial failed to initialize.")
        return
    while True:
        bytey = sery.one_shot_read(Serial)
        print(f"recieved: {bytey}")


if __name__ == "__main__":
    main()
