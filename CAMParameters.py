# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ


class CAMParameters:
    # This class contains machine-specific constants
    travel_z = 1
    feedrate_z = 20
    # Changed this from 70 on 9-Nov-2020
    feedrate_xy = 90
    safe_z = 10
    board_w = 100
    board_h = 40
    passes = 3
    # The size (mm) of the corner area to avoid
    corner_sie = 5

