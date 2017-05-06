import GyroInformation


class GyroWithSpeedInformation(GyroInformation.GyroInformation):
    def __init__(self, accel_x, accel_y, accel_z, speed_x, speed_y, speed_z):
        super(GyroWithSpeedInformation, self).__init__(accel_x, accel_y, accel_z)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_z = speed_z