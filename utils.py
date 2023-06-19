distance_units = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
}

time_units = {
    "sec": 1,
    "min": 60,
    "hour": 3600,
    "day": 86400,
}

area_units = {
    "m\u00b2": 1,
    "ha": 10000,
    "km\u00b2": 1000000,
}

intensity_units = {"%s/%s" % (dist,time): distance_units[dist] / time_units[time] for dist in distance_units.keys() for time in time_units.keys()}
