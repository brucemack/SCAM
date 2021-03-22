import math


def rotate(coords, degrees):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    The angle should be given in degrees.
    """
    angle = math.radians(degrees)
    origin = (0, 0)
    ox, oy = origin
    px, py = coords
    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def round_coords(coords):
    return round(coords[0], 2), round(coords[1], 2)


def calc_rect_path(top_left, bottom_right, tool_diam):
    """ Creates the milling path for the outline of the specified
        rectangle.  The tool center is inside of the rectangle by
        half the width. """
    result = []
    adj = tool_diam / 2
    # Top left
    result.append((top_left[0] + adj, top_left[1] - adj))
    # Top right
    result.append((bottom_right[0] - adj, top_left[1] - adj))
    # Bottom right
    result.append((bottom_right[0] - adj, bottom_right[1] + adj))
    # Bottom left
    result.append((top_left[0] + adj, bottom_right[1] + adj))
    # Top left
    result.append((top_left[0] + adj, top_left[1] - adj))
    return result


def mill_calc_h(top_left, bottom_right, tool_diam):
    """ Takes a rectangle (defined by corners) and a tool diameter and generates
        the points on the milling path to clear the area.  We scan from top
        left to bottom right in all cases.
    """
    dy = bottom_right[1] - top_left[1]
    dx = bottom_right[0] - top_left[0]
    # Adjusted for tool
    adx = dx - tool_diam
    # Number of passes
    passes = math.ceil(math.fabs(dy) / tool_diam)
    # Pass offset
    pass_offset = dy / passes
    # Generate passes
    origin_x = top_left[0] + tool_diam / 2
    # Start tool a bit below the top of the edge (remember, we are
    # milling from the top down
    y = top_left[1] - (tool_diam / 2)
    result = []
    for p in range(0, passes):
        # Even passes go left to right
        if p % 2 == 0:
            result.append((origin_x, y))
            result.append((origin_x + adx, y))
        # Odd passes to right to left
        elif p % 2 == 1:
            result.append((origin_x + adx, y))
            result.append((origin_x, y))
        # Move up
        y = y + pass_offset
    return result


def mill_calc_v(top_left, bottom_right, tool_diam):
    """ Takes a rectangle (defined by corners) and a tool diameter and generates
        the points on the milling path to clear the area.  We scan from top
        left to bottom right in all cases.
    """
    dy = bottom_right[1] - top_left[1]
    dx = bottom_right[0] - top_left[0]
    # Number of passes is based on the width (dx) of the area
    passes = math.ceil(math.fabs(dx) / tool_diam)
    # Pass offset
    pass_offset = dx / passes
    # Generate passes
    top_y = top_left[1] - (tool_diam / 2)
    bottom_y = bottom_right[1] + (tool_diam / 2)
    x = top_left[0] + (tool_diam / 2)
    result = []
    for p in range(0, passes):
        # Even passes go top to bottom
        if p % 2 == 0:
            result.append((x, top_y))
            result.append((x, bottom_y))
        # Odd passes to right to left
        elif p % 2 == 1:
            result.append((x, bottom_y))
            result.append((x, top_y))
        # Move right
        x = x + pass_offset
    return result
