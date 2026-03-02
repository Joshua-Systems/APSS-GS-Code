import packet_deframe.enums as enm
import packet_deframe.packet as pkt


def deframe_packet(
    data: bytes, team_gps: pkt.team_gps, base_gps: pkt.base_gps, unknown: pkt.unknown
) -> None:
    """Deframe bytes into deserialised protocols with most recent relevant packet data stored within class instances"""
