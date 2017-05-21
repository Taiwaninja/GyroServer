from Consts import MOVEMENT_STATE
import Consts
import subprocess
import thread

class KeyManager(object):
    is_jump = False
    current_state = MOVEMENT_STATE.STILL
    
    @classmethod
    def handle_callback(cls, old_state, new_state):
        cls.current_state = new_state

    @classmethod
    def handle_jump(cls):
        cls.is_jump = True

    @classmethod
    def start_game(cls):
        cls.run_script(Consts.START_GAME_PATH)

    @classmethod
    def handle_callback_script(cls, old_state, new_state):
        if new_state == MOVEMENT_STATE.RIGHT:
            cls.run_script(Consts.PRESS_RIGHT_PATH)
        elif new_state == MOVEMENT_STATE.LEFT:
            cls.run_script(Consts.PRESS_LEFT_PATH)
        else:
            cls.run_script(Consts.RELEASE_PATH)

    @classmethod
    def handle_jump_script(cls):
        cls.run_script(Consts.JUMP_PATH)

    @classmethod
    def run_script(cls, script_path):
        subprocess.call([Consts.AHK_PATH, script_path])
        
    @classmethod
    def init(cls):
        thread.start_new_thread(cls.run_script_movement, ())
        thread.start_new_thread(cls.run_script_jump, ())
    
    @classmethod
    def run_script_movement(cls):
        last_state = MOVEMENT_STATE.STILL
        while(True):
            current_state_local = cls.current_state
            if current_state_local != last_state:
                print "! changed from %(old)s to %(new)s" % {"old": last_state, "new": cls.current_state}
                cls.handle_callback_script(last_state, current_state_local)
                last_state = current_state_local

    @classmethod
    def run_script_jump(cls):
        while(True):
            is_jump_local = cls.is_jump
            if is_jump_local:
                cls.handle_jump_script()
                cls.is_jump = False
