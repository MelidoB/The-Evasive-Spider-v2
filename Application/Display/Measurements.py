class DisplayMeasurements:
    def __init__(self):
        self.gameDisplay = None
        self.display_width = None
        self.display_height = None

    def set_display_measurements(self, width, height):
        """
        param width & param height needs to be bigger than 0.
        """
        if width > 0 and height > 0:
            self.display_width = width
            self.display_height = height