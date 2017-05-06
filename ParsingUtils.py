import struct
import GyroInformation
import GyroWithSpeedInformation


class ParsingUtils(object):
    @classmethod
    def parse_acceleration_packet(cls, packet):
        (x, y, z) = struct.unpack("!fff", packet)
        return GyroInformation.GyroInformation(x, y, z)

    @classmethod
    def parse_velocity_packet(cls, packet):
        (x, y, z, speed_x, speed_y, speed_z) = struct.unpack("!ffffff", packet)
        return GyroWithSpeedInformation.GyroWithSpeedInformation(x, y, z, speed_x, speed_y, speed_z)

