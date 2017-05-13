import GyroInformation


class GyroWithSpeedInformation(GyroInformation.GyroInformation):
    def __init__(self, accel_x, accel_y, accel_z, speed_x, speed_y, speed_z):
        super(GyroWithSpeedInformation, self).__init__(accel_x, accel_y, accel_z)
        self.speed_input = True
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.speed_z = speed_z
        
    def set_data(self, other):
        super(GyroWithSpeedInformation, self).set_data(other)
        if (other.speed_input):
            self.speed_x = other.speed_x
            self.speed_y = other.speed_y
            self.speed_z = other.speed_z
