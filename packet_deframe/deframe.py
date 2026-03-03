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
    team_gps.set_altitude(fields[5])
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
    data: bytes, team_gps: pkt.team_gps, base_gps: pkt.base_gps, unknown: pkt.unknown
) -> None:
    """Deframe bytes into deserialised protocols with most recent relevant packet data stored within class instances"""
    if data.startswith(b"$") and data.endswith(b"\n") and not (data[1:3] == b"?"):
        clean_data = data[1:-1]  # remove $ at start and \n at end
    else:
        clean_data = data
    fields = clean_data.split(b";")
    print(fields)
    type = enm.message_type(data[1:2])
    match type:
        case enm.message_type.BASE_GPS:
            base_gps_deframe(fields, base_gps)
        case enm.message_type.GPS:
            team_gps_deframe(fields, team_gps)
        case enm.message_type.UNKNOWN:
            unknown_gps_deframe(clean_data, unknown)
        case _:
            print("ERROR WITH PAcKET TYPE, UNEXPECTED RETURNED")
            return None
