import socket
import Consts
import struct
import time

LEFT_PACKET = struct.pack("!ffffff", 0, 0, 0, -1, 0, 0)
RIGHT_PACKET = struct.pack("!ffffff", 0, 0, 0, 1, 0, 0)
STILL_PACKET = struct.pack("!ffffff", 0, 0, 0, 0, 0, 0)
STILL2_PACKET = struct.pack("!ffffff", 0, 0, 0, 0.01, 0, 0)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("localhost", Consts.PORT))

    sock.send(LEFT_PACKET)
    print "Sent left"
    time.sleep(5)

    sock.send(STILL_PACKET)
    print "Sent still"
    time.sleep(5)

    sock.send(RIGHT_PACKET)
    print "Sent right"
    time.sleep(5)

    sock.send(STILL2_PACKET)
    print "Sent still 2"


if __name__ == "__main__":
    main()