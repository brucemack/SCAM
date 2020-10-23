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
