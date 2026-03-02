from sklearn import base

import packet_deframe.enums as enm
import packet_deframe.packet as pkt


def return_packet_type(
    type, team_gps: pkt.team_gps, base_gps: pkt.base_gps, unknown: pkt.unknown
):
    match type:
        case enm.message_type.BASE_GPS:
            return base_gps
        case enm.message_type.GPS:
            return team_gps
        case enm.message_type.UNKNOWN:
            return unknown
        case _:
            print("ERROR WITH PAcKET TYPE, UNEXPECTED RETURNED")
            return None


def deframe_packet(
    data: bytes, team_gps: pkt.team_gps, base_gps: pkt.base_gps, unknown: pkt.unknown
) -> None:
    """Deframe bytes into deserialised protocols with most recent relevant packet data stored within class instances"""

    type = enm.message_type(data[1:2])
    return_packet_type(type, team_gps, base_gps, unknown)
