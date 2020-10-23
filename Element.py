# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ

class Element:
    # The base class for all elements

    def __init__(self):
        pass

    def render(self, canvas, origin_x_mm, origin_y_mm, color, render_params):
        # The standard interface for drawing this element on the canvas.
        # The origin of the coordinate system is the bottom left of the
        # window.
        pass

    def mill(self, gcode_stream, origin_x_mm, origin_y_mm, depth_mm, cam_params):
        # The standard interface for emitting g-code for this element
        pass

    @staticmethod
    def u2px(units, render_params):
        # Converts dimensional units (i.e. mm) to pixels
        return int(round(units * render_params.pixelsPerMm * render_params.scaling))

    @staticmethod
    def u2px_2d(point_mm, render_params):
        # Converts dimensional units (i.e. mm) to pixels
        return int(round(point_mm[0] * render_params.pixelsPerMm * render_params.scaling)), \
               int(round(point_mm[1] * render_params.pixelsPerMm * render_params.scaling))



