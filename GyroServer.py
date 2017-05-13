import Consts
import socket
import ParsingUtils
from GyroWithSpeedInformation import GyroWithSpeedInformation
from Consts import MOVEMENT_STATE


class GyroServer(object):
    """
    A server that listens to reports about movement.

    Calls given callbacks upon changing directions.
    callback is formated (old_state,new_state)
    """

    def __init__(self, change_movement_callback, port=Consts.PORT, velocity_threshold=Consts.VELOCITY_THRESHOLD):
        self.change_movement_callback = change_movement_callback
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
        location_movement_info = GyroWithSpeedInformation(0,0,0,0,0,0)
        while self.is_running:
            pack = self.socket.recv(Consts.MAX_PACKET_SIZE)
            location_movement_info.set_data(ParsingUtils.ParsingUtils.parse_packet(pack))
            new_state = self.get_current_movement_state(location_movement_info)
            if not new_state == self.current_state:
                self.change_movement_callback(self.current_state, new_state)
                self.current_state = new_state

    def get_current_movement_state(self, gyro_with_speed_info):
        # TODO: We might need to reverse this!
        x_movement = MOVEMENT_STATE.STILL
        is_jump = False
        if gyro_with_speed_info.speed_x >= Consts.VELOCITY_THRESHOLD:
            x_movement = MOVEMENT_STATE.LEFT
        if gyro_with_speed_info.speed_x <= -1 * Consts.VELOCITY_THRESHOLD:
            x_movement = MOVEMENT_STATE.RIGHT
        if gyro_with_speed_info.speed_z >= Consts.JUMP_THRESHOLD:
            is_jump = True
        return x_movement, is_jump
