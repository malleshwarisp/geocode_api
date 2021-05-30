import os

import requests

# from simplexlm import dumps

GEOCODE_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
API_KEY = os.getenv("API_KEY")


def cal_geocode(address: str, repeat_time=0):
    """
    Takes in address and returns latitude and longitude of the given address.
    Parameters
    address(str) : Address of any location

    Returns
    coordinates(dict): lat and lng of the given location
    """
    params = {"key": API_KEY, "address": address}
    status = False
    err_msg = ""
    try:
        output = requests.get(GEOCODE_BASE_URL, params=params).json()
        if output["status"] == "ZERO_RESULTS":
            err_msg = "Unable to geocode the address"

        elif output["status"] == "UNKNOWN_ERROR":
            if repeat_time < 3:
                return cal_geocode(address, repeat_time + 1)
            err_msg = "Some Geocode service error"

        elif output["status"] == "INVALID_REQUEST":
            err_msg = "Invalid Address"

        elif output["status"] == "OK":
            geometry = output["results"][0]["geometry"]
            lat = geometry["location"]["lat"]
            lng = geometry["location"]["lng"]

            response = {"coordinates": {"lat": lat, "lng": lng}, "address": address}
            return (True, response)
        else:
            err_msg = "Some Unknown Error"
    except requests.exceptions.Timeout:
        if repeat_time < 3:
            return cal_geocode(address, repeat_time + 1)
        err_msg = "Geocoding API Failed"

    return (status, err_msg)
