import struct
import GyroInformation
import GyroWithSpeedInformation
from Consts import PACKET_TYPE

class ParsingUtils(object):
    @classmethod
    def parse_command_packet(cls, packet):
        command = struct.unpack("!i", packet)
        return command[0]
    
    @classmethod
    def parse_acceleration_packet(cls, packet):
        (x, y, z) = struct.unpack("!fff", packet)
        return GyroInformation.GyroInformation(x, y, z)

    @classmethod
    def parse_velocity_packet(cls, packet):
        (x, y, z, speed_x, speed_y, speed_z) = struct.unpack("!ffffff", packet)
        return GyroWithSpeedInformation.GyroWithSpeedInformation(x, y, z, speed_x, speed_y, speed_z)
    
    @classmethod
    def parse_packet(cls, packet):
        if len(packet) == 4:
            return PACKET_TYPE.COMMAND, cls.parse_command_packet(packet)
        elif len(packet) == 12:
            return PACKET_TYPE.ACCELERATION, cls.parse_acceleration_packet(packet)
        elif len(packet) == 24:
            return PACKET_TYPE.VELOCITY, cls.parse_velocity_packet(packet)
        else:
            print(len(packet))
            return None
