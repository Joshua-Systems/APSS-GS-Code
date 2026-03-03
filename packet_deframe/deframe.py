import packet_deframe.enums as enm
import packet_deframe.packet as pkt


def team_gps_deframe(fields, team_gps: pkt.team_gps):
    # team_gps fields[0][:1]  # b'G' implement packet checking inside class?
    team_gps.set_team_id(fields[0][1:])
    team_gps.set_fix(fields[1])
    team_gps.set_utc(fields[2].decode())
    print(team_gps.get_utc())
    team_gps.set_longitude(float(fields[3]))
    team_gps.set_latitude(float(fields[4]))
    team_gps.set_altitude(float((fields[5])[:-1]))
    print(team_gps.get_altitude())
    team_gps.set_num_sats(int(fields[6]))


def base_gps_deframe(fields, team_gps: pkt.base_gps):
    team_gps.set_fix(fields[1])
    team_gps.set_utc(fields[2].decode())
    team_gps.set_longitude(float(fields[3]))
    team_gps.set_latitude(float(fields[4]))
    team_gps.set_altitude(fields[5])
    team_gps.set_num_sats(int(fields[6]))


def unknown_gps_deframe(data, team_gps: pkt.unknown):
    length = int(data[1:2].decode())  # assumes length is a single ASCII digit
    team_gps.set_length(length)

    byte_data = data[2:].replace(b";", b"").replace(b"\n", b"")
    team_gps.set_data(byte_data)


def deframe_packet(
    data: bytes,
    team_gps: pkt.team_gps,
    base_gps: pkt.base_gps,
    unknown: pkt.unknown,
    gui_window=None,  # Optional GUI object
) -> None:
    """Deframe bytes and optionally print to GUI"""
    if data.startswith(b"$") and data.endswith(b"\n") and not (data[1:3] == b"?"):
        clean_data = data[1:-1]
    else:
        clean_data = data

    fields = clean_data.split(b";")
    packet_type = enm.message_type(data[1:2])

    match packet_type:
        case enm.message_type.BASE_GPS:
            base_gps_deframe(fields, base_gps)
            output = (
                f"BASE_GPS -> Lat: {base_gps.get_latitude()}, "
                f"Lon: {base_gps.get_longitude()}, Alt: {base_gps.get_altitude()}"
            )
        case enm.message_type.GPS:
            team_gps_deframe(fields, team_gps)
            output = (
                f"TEAM_GPS -> Team: {enm.team_id(int(team_gps.get_team_id()))}, "
                f"Lat: {team_gps.get_latitude()}, Lon: {team_gps.get_longitude()}, "
                f"Alt: {team_gps.get_altitude()}"
            )
        case enm.message_type.UNKNOWN:
            unknown_gps_deframe(clean_data, unknown)
            output = f"UNKNOWN -> Data: {unknown.get_data()}"
        case _:
            output = "ERROR: Unexpected packet type"

    # Print to console
    print(output)

    # Update GUI if provided
    if gui_window is not None:
        gui_window.update_display(output)
