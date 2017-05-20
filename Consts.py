from bunch import Bunch
import os

PORT = 15170
LISTEN_ADDRESS = "0.0.0.0"
MAX_PACKET_SIZE = 6 * 4

JUMP_THRESHOLD = 0.5
VELOCITY_THRESHOLD = 0.1

# Usage: Movement_State.LEFT
MOVEMENT_STATE = Bunch.fromDict({"LEFT": "Left", "STILL": "Still", "RIGHT": "Right"})

AHK_PATH = "C:\Program Files\AutoHotkey\AutoHotkey.exe"
PRESS_RIGHT_PATH = os.path.join(os.getcwd(), r"..\icy_ahk\right.ahk")
PRESS_LEFT_PATH = os.path.join(os.getcwd(), r"..\icy_ahk\left.ahk")
RELEASE_PATH = os.path.join(os.getcwd(), r"..\icy_ahk\release.ahk")
JUMP_PATH = os.path.join(os.getcwd(), r"..\icy_ahk\up.ahk")

MODE_REGOCNITION_JAR_PATH = "C:\Users\Crispy\PycharmProjects\icy_tower\GyroServer\mode_recognition.jar"
JAVA_PATH = r"C:\Program Files (x86)\Java\jre1.8.0_131\bin\java.exe"
END_GAME_DETECTOR_COMMAND = [JAVA_PATH, "-jar", MODE_REGOCNITION_JAR_PATH]
IMAGE_LIST = ["high_score.jpg", "game_over.jpg"]