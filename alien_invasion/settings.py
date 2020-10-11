class Settings:
    """A class to store all alien invasion settings"""

    def __init__(self):
        """"Initialise the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230,230,230)
        self.ship_speed = 1.5