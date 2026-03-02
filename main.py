import sock_pipe.uart_socket as sery
import packet_deframe.deframe as defr
import packet_deframe.packet as pkt


def main():
    ##Use Either JTAG COM PORT or VCP From com0com
    Serial = sery.init_pipe("COM1")

    if Serial is None:
        print("Serial failed to initialize.")
        return
    while True:
        bytey = sery.one_shot_read(Serial)
        pkt_base_gps = pkt.base_gps()
        pkt_team_gps = pkt.team_gps()
        pkt_unknown = pkt.unknown()
        print(f"recieved: {bytey}, with bytey 0 {bytey[0:1]}")
        if bytey[0:1] == b"$":
            defr.deframe_packet(bytey, pkt_team_gps, pkt_base_gps, pkt_unknown)


if __name__ == "__main__":
    main()
