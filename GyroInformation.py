class GyroInformation(object):
    def __init__(self, x, y, z):
        self.speed_input = False
        self.x = x
        self.x_delay = 0
        self.speed_x = 0
        self.y = y
        self.y_delay = 0
        self.speed_y = 0
        self.z = z
        self.z_delay = 0
        self.speed_z = 0
        self.calculate_speed(1)

    def set_data(self, other):
        self.x = other.x
        self.y = other.y
        self.z = other.z
        self.calculate_speed(1)

        
    def calculate_speed(self, threshold):
        if abs(self.x) > threshold:
            self.speed_x += self.x
        else:
            self.x_delay += 1
            if self.x_delay >= 5:
                self.speed_x = 0
                self.x_delay = 0
        if abs(self.y) > threshold:
            self.speed_y += self.y
        else:
            self.y_delay += 1
            if self.y_delay >= 5:
                self.speed_y = 0
                self.y_delay = 0
        if abs(self.z) > threshold:
            self.speed_z += self.z
        else:
            self.z_delay += 1
            if self.z_delay >= 5:
                self.speed_z = 0
                self.z_delay = 0