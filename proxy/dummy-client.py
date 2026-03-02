import proxy_include.uart_dummy_socket as sery


def main():
    Serial = sery.init_pipe("COM1")
    while True:
        # sery.one_shot_write_test(Serial)
        sery.gps_test_data(Serial)


if __name__ == "__main__":
    main()
