from bunch import Bunch
import os

PORT = 15170
LISTEN_ADDRESS = "0.0.0.0"
MAX_PACKET_SIZE = 6 * 4

VELOCITY_THRESHOLD = 0.1

# Usage: Movement_State.LEFT
MOVEMENT_STATE = Bunch.fromDict({"LEFT": "Left", "STILL": "Still", "RIGHT": "Right"})

PRESS_RIGHT_PATH = os.path.join(os.getcwd(), r"..\icy_ahk\right.ahk")
PRESS_LEFT_PATH = r"..\icy_ahk\left.ahk"
RELEASE_PATH = r"..\icy_ahk\release.ahk"