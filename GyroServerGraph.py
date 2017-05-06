import socket
import struct
import GyroInformation
import time
import matplotlib.pyplot as plt
import threading
import traceback


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


def listening_function(results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", 15170))
    velocity_info = GyroInformation.GyroInformation(0,0,0)
    # last_time = time.ctime()
    curr_delay = 0.1
    while True:
        pack = sock.recv(10000)
        # curr_delay = time.ctime() - last_time
        location_info, location_info_velocity = parse_packet(pack)
        if curr_delay < 100:
            velocity_info.conditional_add(location_info, 1)
        else:
            velocity_info.x = 0
            velocity_info.y = 0
            velocity_info.z = 0
            
        show_info = velocity_info 
        print "(%s: %s,%s,%s)" % (time.ctime(), show_info.x, show_info.y, show_info.z)
        results.append(show_info)


def parse_packet(packet):
    (x, y, z, v_x, v_y, v_z) = struct.unpack("!ffffff", packet)
    # (x, y, z) = struct.unpack("!fff", packet); v_x = 0; v_y = 0; v_z = 0
    return GyroInformation.GyroInformation(x, y, z), GyroInformation.GyroInformation(v_x, v_y, v_z)


if __name__ == "__main__":
    main()
