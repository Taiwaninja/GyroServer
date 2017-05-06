class GyroInformation(object):
    def __init__(self, x, y, z):
        self.x = x
        self.x_delay = 0
        self.y = y
        self.y_delay = 0
        self.z = z
        self.z_delay = 0

    def add(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        
    def zeroize(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def conditional_add(self, other, threshold):
        if abs(other.x) > threshold:
            self.x += other.x
        else:
            self.x_delay += 1
            if self.x_delay >= 10:
                self.x = 0
                self.x_delay = 0
        if abs(other.y) > threshold:
            self.y += other.y
        else:
            self.y_delay += 1
            if self.y_delay >= 10:
                self.y = 0
                self.y_delay = 0
        if abs(other.z) > threshold:
            self.z += other.z
        else:
            self.z_delay += 1
            if self.z_delay >= 10:
                self.z = 0
                self.z_delay = 0
