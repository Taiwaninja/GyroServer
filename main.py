import GyroServer
import time
import KeyManager
import EndGameDetector
import Consts


def printing_move_change_callback(old_move, new_move):
    print "%(time)s changed from %(old)s to %(new)s" % {"time": time.ctime(), "old": old_move, "new": new_move}


def print_then_move(old_move, new_move):
    printing_move_change_callback(old_move, new_move)
    KeyManager.KeyManager.handle_callback(old_move, new_move)


def print_then_jump():
    KeyManager.KeyManager.handle_jump()
    print "%s Jumped" % time.ctime()


def main():
    # server = GyroServer.GyroServer(KeyManager.KeyManager.handle_callback)
    while True:
        # Start game
        server = GyroServer.GyroServer(print_then_move, print_then_jump)
        server.start()

        # SLeep untill game over
        detector = EndGameDetector.EndGameDetector()
        detector.detect_game_over()
        print "Game Over"

        server.stop()
        # Showing score
        detector.show_score()

        # Reset profile
        KeyManager.KeyManager.run_script(Consts.RESET_PROFILE_PATH)

if __name__ == "__main__":
    main()