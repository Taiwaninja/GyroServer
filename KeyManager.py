from Consts import MOVEMENT_STATE
import Consts
import subprocess


class KeyManager(object):
    @classmethod
    def handle_callback(cls, old_state, new_state):
        cls.run_script(Consts.RELEASE_PATH)
        if new_state == MOVEMENT_STATE.RIGHT:
            cls.run_script(Consts.PRESS_RIGHT_PATH)
        elif new_state == MOVEMENT_STATE.LEFT:
            cls.run_script(Consts.PRESS_LEFT_PATH)

    @classmethod
    def handle_jump(cls):
        cls.run_script(Consts.JUMP_PATH)

    @classmethod
    def run_script(cls, script_path):
        subprocess.call([Consts.AHK_PATH, script_path])