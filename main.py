import GyroServer
import time
import KeyManager


def printing_move_change_callback(old_move, new_move):
    print "%(time)s changed from %(old)s to %(new)s" % {"time": time.ctime(), "old": old_move, "new": new_move}


def print_then_move(old_move, new_move):
    printing_move_change_callback(old_move, new_move)
    KeyManager.KeyManager.handle_callback(old_move, new_move)


def main():
    # server = GyroServer.GyroServer(KeyManager.KeyManager.handle_callback)
    server = GyroServer.GyroServer(print_then_move)
    server.start()


if __name__ == "__main__":
    main()