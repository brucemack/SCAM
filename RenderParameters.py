# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ


class RenderParameters:
    # This class contains machine-specific constants
    scaling = 1.0
    pixelsPerMm = 0

    def __init__(self, ppmm, cam_parameters):
        # ppmm is pixels per millimeter (used for rendering)
        self.pixelsPerMm = ppmm
        self.height = cam_parameters.board_h * ppmm
        self.width = cam_parameters.board_w * ppmm

    def u2px(self, units):
        # Converts dimensional units (i.e. mm) to pixels
        return int(round(units * self.pixelsPerMm * self.scaling))

