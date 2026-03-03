import sock_pipe.uart_socket as sery
import packet_deframe.deframe as defr
import packet_deframe.packet as pkt
import gui_interface.window as wdw


def main():
    Serial = sery.init_pipe("COM1")
    if Serial is None:
        print("Serial failed to initialize.")
        return

    # Create GUI
    gui_window = wdw.GPSWindow()

    # Create initial packets
    pkt_base_gps = pkt.base_gps()
    pkt_team_gps = pkt.team_gps()
    pkt_unknown = pkt.unknown()

    def read_serial_loop():
        """Read serial in GUI mainloop using after()"""
        bytey = sery.one_shot_read(Serial)
        if bytey and bytey[0:1] == b"$":
            defr.deframe_packet(
                bytey, pkt_team_gps, pkt_base_gps, pkt_unknown, gui_window
            )
        gui_window.root.after(100, read_serial_loop)  # call again after 100ms

    # Start loop
    gui_window.root.after(100, read_serial_loop)
    gui_window.run()


if __name__ == "__main__":
    main()
