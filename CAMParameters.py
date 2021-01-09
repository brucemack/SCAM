# SCAM G-Code Generator
# (c) 2020 Bruce MacKinnon KC1FSZ


class CAMParameters:
    # This class contains machine-specific constants
    travel_z = 1
    # Changed this from 20 on 8-Jan-2021
    feedrate_z = 40
    # This is the speed used to remove the tool from the work
    feedrate_z_out = 100
    # Changed this from 70 on 9-Nov-2020
    feedrate_xy = 100
    safe_z = 10
    board_w = 100
    board_h = 70
    passes = 3
    # The size (mm) of the corner area to avoid
    corner_sie = 8

