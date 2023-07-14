import math


def angle_to_sexigesimal(angle_in_degrees, decimals=3):
    """
    Convert the given angle to a sexigesimal string of hours of RA.

    Parameters
    ----------
    angle_in_degrees : float
        A scalar angle, expressed in degrees

    Returns
    -------
    hms_str : str
        The sexigesimal string giving the hours, minutes, and seconds of RA for
        the given `angle_in_degrees`

    """
    if math.floor(decimals) != decimals:
        raise OSError('decimals should be an integer!')

    hours_num = angle_in_degrees * 24 / 180
    hours = math.floor(hours_num)

    min_num = (hours_num - hours) * 60
    minutes = math.floor(min_num)

    seconds = (min_num - minutes) * 60
    frac = math.floor((seconds % 1) * 10 ** decimals)
    
    seconds = math.floor(seconds)
    format_string = '{:02d}:{:02d}:{:02d}.{:0' + str(decimals) + 'd}'
    return format_string.format(hours, minutes, seconds, frac)

def angle_test():
    sex = angle_to_sexigesimal(32.231515, decimals=3)
    assert sex == '04:17:51.127'

angle_test()
