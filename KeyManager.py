from Consts import MOVEMENT_STATE
import Consts
import subprocess


class KeyManager(object):
    @classmethod
    def handle_callback(cls, old_state, new_state):
        cls.run_process(Consts.RELEASE_PATH)
        if new_state == MOVEMENT_STATE.RIGHT:
            cls.run_process(Consts.PRESS_RIGHT_PATH)
        elif new_state == MOVEMENT_STATE.LEFTT:
            cls.run_process(Consts.PRESS_LEFT_PATH)

    @classmethod
    def run_process(cls, process_name):
        subprocess.call(process_name)