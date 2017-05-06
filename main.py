import GyroServer
import time
import KeyManager


def printing_move_change_callback(old_move, new_move):
    print "%(time)s changed from %(old)s to %(new)s" % {"time": time.ctime(), "old": old_move, "new": new_move}


def main():
    server = GyroServer.GyroServer(KeyManager.KeyManager.handle_callback)
    server.start()


if __name__ == "__main__":
    main()