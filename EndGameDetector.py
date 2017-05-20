import subprocess
import Consts


class EndGameDetector(object):
    def __init__(self, ):
        self.images = Consts.IMAGE_LIST
        self.found_game_over = False
        self.processes = []

    def detect_game_over(self):
        for image in self.images:
            self.processes.append(self.create_new_process(image))

        while not self.found_game_over:
            for process in self.processes:
                if process.poll() is not None:
                    self.found_game_over = True
        for process in self.processes:
            process.kill()
        return

    def create_new_process(self, image):
        # Concat params so we can run as a process
        args = Consts.END_GAME_DETECTOR_COMMAND + [image]
        return subprocess.Popen(args)


if __name__ == "__main__":
    detector = EndGameDetector()
    detector.detect_game_over()
    print "Done!"