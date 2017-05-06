import os
import subprocess
import socket
import Consts
import struct
import time

LEFT_PACKET = struct.pack("!ffffff", 0, 0, 0, -1, 0, 0)
RIGHT_PACKET = struct.pack("!ffffff", 0, 0, 0, 1, 0, 0)
STILL_PACKET = struct.pack("!ffffff", 0, 0, 0, 0, 0, 0)
STILL2_PACKET = struct.pack("!ffffff", 0, 0, 0, 0.01, 0, 0)


SLEEP_TIME=1
def test_call_process():
    path = os.path.join(os.getcwd(), r"..\icy_ahk\right.ahk")
    print path
    subprocess.call([Consts.AHK_PATH, path])


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect(("localhost", Consts.PORT))

    time.sleep(SLEEP_TIME*10)
    sock.send(LEFT_PACKET)
    print "Sent left"
    time.sleep(SLEEP_TIME)

    sock.send(STILL_PACKET)
    print "Sent still"
    time.sleep(SLEEP_TIME)

    sock.send(RIGHT_PACKET)
    print "Sent right"
    time.sleep(SLEEP_TIME)

    sock.send(STILL2_PACKET)
    print "Sent still 2"


if __name__ == "__main__":
    main()
    # test_call_process()