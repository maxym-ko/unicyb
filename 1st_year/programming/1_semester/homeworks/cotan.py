import math


def cotan_compare(x: float, y: float) -> float:
    """
    Check if one cotanges is bigger/less/equal to the other one
    Return 1 if cotan(x) > cotan(y), 0 if cotan(x) = cotan(y), -1 if cotan(x) < cotan(y)
    """
    # check if cos(x) -> 0 and cos(y) -> 0 or sin(x) -> 0 and sin(y) -> 0
    if (math.fabs(x - math.pi / 2) < 0.0000000001) and (math.fabs(y - math.pi / 2) < 0.0000000001) or \
            (math.fabs(x - math.pi) < 0.0000000001) and (math.fabs(y - math.pi) < 0.0000000001):
        return 0
    if math.cos(x) / math.sin(x) > math.cos(y) / math.sin(y):
        return 1
    else:
        return -1
