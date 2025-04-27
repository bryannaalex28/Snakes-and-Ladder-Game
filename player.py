class Player:
    def __init__(self, color, name):
        self.position = 0
        self.color = color
        self.name = name

    def move(self, steps):
        self.position += steps
        if self.position > 99:  # 10x10 board
            self.position = 99

    def teleport(self, new_pos):
        self.position = new_pos
