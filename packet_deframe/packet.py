import abc


class packet(abc.ABC):
    def __init__(self):
        self.packet_type = None
        self.utc_timestamp = None

    def set_utc(self, utc):
        self.utc_timestamp = utc

    def get_utc(self):
        return self.utc_timestamp


class team_gps(packet):
    def __init__(self):
        super().__init__()
        self.team_id = None
        self.fix = None
        self.latitude = None
        self.longitude = None
        self.altitude = None
        self.num_sats = None

    def set_fix(self, fix):
        self.fix = fix

    def set_team_id(self, team_id):
        self.team_id = team_id

    def set_latitude(self, lat):
        self.latitude = lat

    def set_longitude(self, long):
        self.longtitude = long

    def set_altitude(self, alt):
        self.altitude = alt

    def set_num_sats(self, num_sats):
        self.num_sats = num_sats

    def get_fix(self):
        return self.fix

    def get_team_id(self):
        return self.team_id

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longtitude

    def get_altitude(self):
        return self.altitude

    def get_num_sats(self):
        return self.num_sats


class base_gps(packet):
    def __init__(self):
        super().__init__()
        self.fix = None
        self.latitude = None
        self.longitude = None
        self.altitude = None

    def set_fix(self, fix):
        self.fix = fix

    def set_latitude(self, lat):
        self.latitude = lat

    def set_longitude(self, long):
        self.longtitude = long

    def set_altitude(self, alt):
        self.altitude = alt

    def set_num_sats(self, num_sats):
        self.num_sats = num_sats

    def get_fix(self):
        return self.fix

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longtitude

    def get_altitude(self):
        return self.altitude

    def get_num_sats(self):
        return self.num_sats


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
