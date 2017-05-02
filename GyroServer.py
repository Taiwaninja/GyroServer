import socket
import struct
import GyroInformation
import time
import matplotlib.pyplot as plt
import threading
import traceback


def main():
    results = []
    gui_thread = threading.Thread(target=listeing_function, args=(results,))
    gui_thread.start()
    i = 0

    plt.axis([0, 80, -5, 5])
    plt.ion()
    last_scat = None
    print "Listening"
    while True:

        i += 1
        # TODO: Remove non relevant results
        if last_scat:
            last_scat.remove()
        last_scat = plt.scatter(range(len(results[-80:])), [result.x for result in results[-80:]])
        plt.pause(0.001)


def listeing_function(results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 15170))
    while True:
        pack = sock.recv(10000)
        location_info = parse_packet(pack)
        print "(%s: %s,%s,%s)" % (time.ctime(), location_info.z, location_info.y, location_info.z)
        results.append(location_info)


def parse_packet(packet):
    (x, y, z) = struct.unpack("!fff", packet)
    return GyroInformation.GyroInformation(x, y, z)


if __name__ == "__main__":
    main()