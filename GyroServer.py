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
    should_clear_scats = False
    last_x_scat = None
    last_y_scat = None
    last_z_scat = None

    print "Listening"
    while True:

        i += 1
        # TODO: Remove non relevant results
        if should_clear_scats:
            should_clear_scats = False
            last_x_scat.remove()
            last_y_scat.remove()
            last_z_scat.remove()
        display_results = results[-80:]
        
        last_x_scat = plt.scatter(
                            range(len(display_results)),
                            [result.x for result in display_results],
                            c='b',
                            label="x")
        last_y_scat = plt.scatter(
                            range(len(display_results)),
                            [result.y for result in display_results],
                            c='g',
                            label="y")
        last_z_scat = plt.scatter(
                            range(len(display_results)),
                            [result.z for result in display_results],
                            c='y',
                            label="z")
        plt.pause(0.001)
        if last_x_scat or last_y_scat or last_z_scat:
            should_clear_scats = True


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
