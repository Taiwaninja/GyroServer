import Consts
import socket
import ParsingUtils
from Consts import MOVEMENT_STATE, X_INVERSION


class GyroServer(object):
    """
    A server that listens to reports about movement.

    Calls given callbacks upon changing directions.
    callback is formated (old_state,new_state)
    """

    # TODO: Consider changing jump to stateful aswell.
    def __init__(self, change_movement_callback, jump_callback, port=Consts.PORT,
                 velocity_threshold=Consts.VELOCITY_THRESHOLD):
        self.change_movement_callback = change_movement_callback
        self.jump_callback = jump_callback
        self.port = port
        self.socket = None
        self.current_state = MOVEMENT_STATE.STILL
        self.velocity_threshold = velocity_threshold
        self.is_running = False

    def start(self):
        """
        Starts the server, This function is blocking.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((Consts.LISTEN_ADDRESS, Consts.PORT))
        self.is_running = True
        while self.is_running:
            pack = self.socket.recv(Consts.MAX_PACKET_SIZE)
            location_movement_info = ParsingUtils.ParsingUtils.parse_velocity_packet(pack)
            self.handle_horizontal(location_movement_info)
            self.handle_up_axis(location_movement_info)

    def handle_horizontal(self, location_movement_info):
        new_state = self.get_current_movement_state(location_movement_info)
        if not new_state == self.current_state:
            self.change_movement_callback(self.current_state, new_state, location_movement_info.speed_x)
            self.current_state = new_state

    def handle_up_axis(self, gyro_with_speed_info):
        if self.is_jumping(gyro_with_speed_info):
            self.jump_callback(gyro_with_speed_info.speed_z)

    def is_jumping(self, gyro_with_speed_info):
        if gyro_with_speed_info.speed_z >= Consts.JUMP_THRESHOLD:
            return True

    def get_current_movement_state(self, gyro_with_speed_info):
        # TODO: We might need to reverse this!
        if gyro_with_speed_info.speed_x >= Consts.VELOCITY_THRESHOLD:
            return self.get_movement_state_with_inversion(MOVEMENT_STATE.RIGHT)
        if gyro_with_speed_info.speed_x <= -1 * Consts.VELOCITY_THRESHOLD:
            return self.get_movement_state_with_inversion(MOVEMENT_STATE.LEFT)
        return MOVEMENT_STATE.STILL
        
    def get_movement_state_with_inversion(self, movement_state):
        if not X_INVERSION:
            if movement_state == MOVEMENT_STATE.RIGHT:
                return MOVEMENT_STATE.RIGHT
            if movement_state == MOVEMENT_STATE.LEFT:
                return MOVEMENT_STATE.LEFT
        else:
            if movement_state == MOVEMENT_STATE.RIGHT:
                return MOVEMENT_STATE.LEFT
            if movement_state == MOVEMENT_STATE.LEFT:
                return MOVEMENT_STATE.RIGHT
        return MOVEMENT_STATE.STILL


