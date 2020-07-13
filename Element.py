# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

class Element:
    # The base class for all elements

    pixelsPerMm = 2.83

    @classmethod
    def set_pixels_per_mm(cls, p):
        # Call this method to establish the conversion between millimeters
        # and pixels on the display output.
        cls.pixelsPerMm = p

    def __init__(self):
        pass

    def render(self, canvas, origin_x_mm, origin_y_mm, height, color, scaling):
        # The standard interface for drawing this element on the canvas
        pass

    def u2px(self, units, scaling):
        # Converts dimensional units (i.e. mm) to pixels
        return int(round(units * self.pixelsPerMm * scaling))

    def mill(self, gcode_stream, origin_x_mm, origin_y_mm, depth_mm, params):
        # The standard interface for emitting g-code for this element
        pass


