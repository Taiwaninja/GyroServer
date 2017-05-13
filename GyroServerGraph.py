import socket
import struct
import GyroWithSpeedInformation
import time
import matplotlib.pyplot as plt
import threading
import traceback
import ParsingUtils
import copy


def main():
    results = []
    gui_thread = threading.Thread(target=listening_function, args=(results,))
    gui_thread.start()
    i = 0

    plt.axis([0, 80, -50, 50])
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
                            [result.speed_x + 1 for result in display_results],
                            c='b',
                            label="x")
        last_y_scat = plt.scatter(
                            range(len(display_results)),
                            [result.x for result in display_results],
                            c='g',
                            label="x")
        #last_y_scat = plt.scatter(
        #                    range(len(display_results)),
        #                    [result.speed_y for result in display_results],
        #                    c='g',
        #                    label="y")
        last_z_scat = plt.scatter(
                            range(len(display_results)),
                            [result.speed_z for result in display_results],
                            c='y',
                            label="z")
        plt.pause(0.001)
        if last_x_scat:
            should_clear_scats = True


def listening_function(results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 15170))
    velocity_info = GyroWithSpeedInformation.GyroWithSpeedInformation(0,0,0,0,0,0)
    print("Listening")
    while True:
        pack = sock.recv(10000)
        location_info = ParsingUtils.ParsingUtils.parse_packet(pack)
        velocity_info.set_data(location_info)
            
        show_info = copy.copy(velocity_info)
        print "(%s: %s,%s,%s)" % (time.ctime(), show_info.speed_x, show_info.speed_y, show_info.speed_z)
        results.append(show_info)

if __name__ == "__main__":
    main()
