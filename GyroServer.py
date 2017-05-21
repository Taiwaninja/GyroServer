import Consts
import socket
import ParsingUtils
import threading
from Consts import MOVEMENT_STATE, X_INVERSION, PACKET_TYPE


class GyroServer(object):
    """
    A server that listens to reports about movement.

    Calls given callbacks upon changing directions.
    callback is formated (old_state,new_state)
    """

    # TODO: Consider changing jump to stateful aswell.
    def __init__(self, change_movement_callback, jump_callback, start_callback, port=Consts.PORT,
                 velocity_threshold=Consts.VELOCITY_THRESHOLD):
        self.change_movement_callback = change_movement_callback
        self.jump_callback = jump_callback
        self.start_callback = start_callback
        self.port = port
        self.socket = None
        self.current_state = MOVEMENT_STATE.STILL
        self.velocity_threshold = velocity_threshold
        self.is_running = False
        self.running_thread = None

    def start(self):
        """
        Starts the server, This function is blocking.
        """
        self.running_thread = threading.Thread(target=self.start_game_thread)
        self.running_thread.start()


    def start_game_thread(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((Consts.LISTEN_ADDRESS, Consts.PORT))
        # TODO: Value to consts
        self.socket.settimeout(3)
        self.is_running = True

        while self.is_running:
            try:
                pack = self.socket.recv(Consts.MAX_PACKET_SIZE)
            except socket.error:
                continue

            packet_type, packet_data = ParsingUtils.ParsingUtils.parse_packet(pack)
            if packet_type == PACKET_TYPE.COMMAND:
                self.handle_command(packet_data)
            else:
                location_movement_info = packet_data
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

    def stop(self):
        self.is_running = False
        self.running_thread.join()
        self.change_movement_callback(self.current_state, MOVEMENT_STATE.STILL)
        self.socket.close()

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

    def handle_command(self, command):
        if command == 2:
            self.start_callback()
            print("Started Game")
        else:
            print(command)



