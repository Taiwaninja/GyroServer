import GyroServer
import time
import KeyManager


def printing_move_change_callback(old_move, new_move, value):
    if value is None:
        print "%(time)s changed from %(old)s to %(new)s" % \
              {"time": time.ctime(), "old": old_move, "new": new_move}
    else:
        print "%(time)s changed from %(old)s to %(new)s with value %(value)f" % \
              {"time": time.ctime(), "old": old_move, "new": new_move, "value": value}


def print_then_move(old_move, new_move, value=None):
    printing_move_change_callback(old_move, new_move, value)
    KeyManager.KeyManager.handle_callback(old_move, new_move)


def print_then_jump(value=None):
    KeyManager.KeyManager.handle_jump()
    if value is None:
        print "%s Jumped" % time.ctime()
    else:
        print "%s Jumped with value %f" % (time.ctime(), value)


def main():
    KeyManager.KeyManager.init()
    # server = GyroServer.GyroServer(KeyManager.KeyManager.handle_callback)
    server = GyroServer.GyroServer(print_then_move, print_then_jump)
    server.start()


if __name__ == "__main__":
    main()