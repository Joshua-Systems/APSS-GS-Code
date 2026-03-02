import abc


@abc.ABC
class packet(abc.ABC):
    def __init__(self):
        self.packet_type = None
        self.utc_timestamp = None


class team_gps(packet):
    def __init__(self):
        super.__init__()
        self.team_id = None
        self.latitude = None
        self.longitude = None
        self.altitude = None

    def set_team_id(self, team_id):
        self.team_id = team_id

    def set_latitude(self, lat):
        self.latitude = lat

    def set_longitude(self, long):
        self.longtitude = long

    def set_altitude(self, alt):
        self.altitude = alt

    def get_team_id(self):
        return self.team_id

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longtitude

    def get_altitude(self):
        return self.altitude


class base_gps(packet):
    def __init__(self):
        super.__init__()
        self.latitude = None
        self.longitude = None
        self.altitude = None

    def set_latitude(self, lat):
        self.latitude = lat

    def set_longitude(self, long):
        self.longtitude = long

    def set_altitude(self, alt):
        self.altitude = alt

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longtitude

    def get_altitude(self):
        return self.altitude


class unknown:
    def __init__(self):
        self.length = None
        self.data = None

    def set_length(self, length):
        self.length = length

    def set_data(self, data):
        self.data = data

    def get_length(self):
        return self.length

    def get_data(self):
        return self.data
