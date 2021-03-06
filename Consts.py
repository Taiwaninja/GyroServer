from bunch import Bunch

PORT = 15170
LISTEN_ADDRESS = "0.0.0.0"
MAX_PACKET_SIZE = 6 * 4

VELOCITY_THRESHOLD = 1
JUMP_THRESHOLD = 5

# Usage: Movement_State.LEFT
MOVEMENT_STATE = Bunch.fromDict({"LEFT": "Left", "STILL": "Still", "RIGHT": "Right"})