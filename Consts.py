# THINGS TO CONFIG: Paths here
# Config the scores.properties path!





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
RESET_PROFILE_PATH = os.path.join(os.getcwd(), r"..\icy_ahk\reset_profile.ahk")
PRESS_RIGHT_PATH = os.path.join(os.getcwd(), r"..\icy_ahk\right.ahk")
PRESS_LEFT_PATH = os.path.join(os.getcwd(), r"..\icy_ahk\left.ahk")
RELEASE_PATH = os.path.join(os.getcwd(), r"..\icy_ahk\release.ahk")
JUMP_PATH = os.path.join(os.getcwd(), r"..\icy_ahk\up.ahk")

# END_GAME
MODE_REGOCNITION_JAR_PATH = r"C:\Users\Crispy\PycharmProjects\icy_tower\GyroServer\mode_recognition.jar"
JAVA_PATH = r"C:\Program Files (x86)\Java\jre1.8.0_131\bin\java.exe"

END_GAME_DETECTOR_COMMAND = [JAVA_PATH, "-jar", MODE_REGOCNITION_JAR_PATH]

IMAGE_LIST = ["high_score.jpg", "game_over.jpg"]


# SCORE

SCORE_EXTRACTOR = r"C:\Users\Crispy\PycharmProjects\tower\icy_tower\runnables\extract_score.jar"
ICY_STATS_FILE_PATH = r"C:\\games\\icytower1.5\\profiles\\icy\\icy_stats.txt"
SCORE_PROPERTIES_FILE = r"C:\Users\Crispy\PycharmProjects\icy_tower\runnables\scores.properties"
SLEEP_TIME = "15000"
PROCESS_TO_KILL = "WLXPhotoGallery"
SCORE_EXTRACTOR_COMMAND = [JAVA_PATH, "-jar", SCORE_EXTRACTOR, ICY_STATS_FILE_PATH, SCORE_PROPERTIES_FILE, SLEEP_TIME,
                           PROCESS_TO_KILL]