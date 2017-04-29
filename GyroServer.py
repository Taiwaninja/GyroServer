import socket
import struct
import LocationInformation
import time


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 15170))
    print "Listening"
    while True:
        pack = sock.recv(10000)
        location_info = parse_packet(pack)
        print "(%s: %s,%s,%s)" % (time.ctime(), location_info.x, location_info.y, location_info.z)


def parse_packet(packet):
    (x, y, z) = struct.unpack("!fff", packet)
    return LocationInformation.LocationInformation(x, y, z)


if __name__ == "__main__":
    main()