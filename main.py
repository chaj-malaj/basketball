class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0

    def get_pos(self, t):
        return self.x + self.vx * t, self.y + self.vy * t - 4.9 * t * t


