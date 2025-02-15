def get_spn(lower_corner, upper_corner):
    spn_longitude = str(float(upper_corner[0]) - float(lower_corner[0]))
    spn_latitude = str(float(upper_corner[1]) - float(lower_corner[1]))
    return spn_longitude, spn_latitude
